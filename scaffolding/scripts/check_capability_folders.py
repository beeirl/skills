#!/usr/bin/env python3
"""Check Dune-style capability-folder rules in apps/ and modules/.

Fitness function, not a linter. Reads files; never writes. Standard library
only. Exits non-zero on a violation. If apps/ and modules/ are both missing,
exits 0: the tree is not a capability-folder repo yet.

Usage:
    python check_capability_folders.py
    python check_capability_folders.py --root ../app
    python check_capability_folders.py --json
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Iterable

SKIP_DIRS = frozenset(
    {
        ".git",
        ".hg",
        ".svn",
        ".idea",
        ".vscode",
        ".next",
        ".nuxt",
        ".turbo",
        ".venv",
        "venv",
        "node_modules",
        "dist",
        "build",
        "coverage",
        "out",
        "target",
    }
)

SOURCE_SUFFIXES = (
    ".ts",
    ".tsx",
    ".mts",
    ".cts",
    ".js",
    ".jsx",
    ".mjs",
    ".cjs",
)

IMPORT_RE = re.compile(
    r"""(?:(?:import|export)\s+(?:type\s+)?(?:[^'"\n]+from\s*)?|import\s*\(|require\s*\()\s*['"]([^'"]+)['"]"""
)

ALLOWED_EXPORT_KEYS = frozenset({".", "./package.json"})


class Finding(dict):
    pass


def is_source(path: Path) -> bool:
    name = path.name
    if name.endswith((".d.ts", ".d.mts", ".d.cts")):
        return False
    return name.endswith(SOURCE_SUFFIXES)


def walk_sources(root: Path) -> Iterable[Path]:
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [name for name in dirnames if name not in SKIP_DIRS]
        for filename in filenames:
            path = Path(dirpath) / filename
            if is_source(path):
                yield path


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf8"))


def discover_packages(kind_root: Path) -> dict[str, Path]:
    packages: dict[str, Path] = {}
    if not kind_root.is_dir():
        return packages
    for child in sorted(kind_root.iterdir()):
        manifest = child / "package.json"
        if not child.is_dir() or not manifest.is_file():
            continue
        parsed = load_json(manifest)
        name = parsed.get("name")
        if isinstance(name, str) and name:
            packages[name] = child
    return packages


def export_keys(manifest: dict[str, object]) -> set[str]:
    exports = manifest.get("exports")
    if exports is None:
        return set()
    if isinstance(exports, str):
        return {"."}
    if isinstance(exports, dict):
        return {str(key) for key in exports}
    return set()


def package_root_for(file: Path, apps: dict[str, Path], modules: dict[str, Path]) -> Path | None:
    for root in list(apps.values()) + list(modules.values()):
        try:
            file.relative_to(root)
            return root
        except ValueError:
            continue
    return None


def resolve_relative(file: Path, specifier: str) -> Path:
    return (file.parent / specifier).resolve()


def is_deep_workspace_import(specifier: str, packages: dict[str, Path]) -> bool:
    for name in packages:
        if specifier.startswith(f"{name}/"):
            return True
    return False


def check_manifests(repo: Path, modules: dict[str, Path]) -> list[Finding]:
    findings: list[Finding] = []
    for name, root in modules.items():
        manifest_path = root / "package.json"
        parsed = load_json(manifest_path)
        keys = export_keys(parsed)
        extra = keys - ALLOWED_EXPORT_KEYS
        rel = str(manifest_path.relative_to(repo))
        if "." not in keys:
            findings.append(
                Finding(
                    file=rel,
                    line=1,
                    rule="public-export-only",
                    specifier=name,
                    detail="package.json exports must include '.'",
                )
            )
        if extra:
            findings.append(
                Finding(
                    file=rel,
                    line=1,
                    rule="public-export-only",
                    specifier=",".join(sorted(extra)),
                    detail="package.json exports must not expose internals",
                )
            )
    return findings


def check_file(
    file: Path,
    repo: Path,
    apps: dict[str, Path],
    modules: dict[str, Path],
) -> list[Finding]:
    findings: list[Finding] = []
    packages = {**apps, **modules}
    package_root = package_root_for(file, apps, modules)
    if package_root is None:
        return findings

    relative_file = str(file.relative_to(repo))
    in_module = any(str(file).startswith(str(root) + os.sep) for root in modules.values())
    app_names = set(apps)

    text = file.read_text(encoding="utf8")
    for index, line in enumerate(text.splitlines(), start=1):
        for specifier in IMPORT_RE.findall(line):
            if is_deep_workspace_import(specifier, packages):
                findings.append(
                    Finding(
                        file=relative_file,
                        line=index,
                        rule="no-deep-package-import",
                        specifier=specifier,
                    )
                )
            if in_module and (
                specifier in app_names
                or any(specifier.startswith(f"{name}/") for name in app_names)
            ):
                findings.append(
                    Finding(
                        file=relative_file,
                        line=index,
                        rule="no-modules-import-apps",
                        specifier=specifier,
                    )
                )
            if specifier.startswith("."):
                resolved = resolve_relative(file, specifier)
                try:
                    resolved.relative_to(package_root.resolve())
                except ValueError:
                    findings.append(
                        Finding(
                            file=relative_file,
                            line=index,
                            rule="no-relative-across-packages",
                            specifier=specifier,
                        )
                    )
                else:
                    continue
                if in_module:
                    apps_root = (repo / "apps").resolve()
                    try:
                        resolved.relative_to(apps_root)
                    except ValueError:
                        pass
                    else:
                        findings.append(
                            Finding(
                                file=relative_file,
                                line=index,
                                rule="no-modules-import-apps",
                                specifier=specifier,
                            )
                        )
    return findings


def check_repo(repo: Path) -> list[Finding]:
    apps = discover_packages(repo / "apps")
    modules = discover_packages(repo / "modules")
    if not apps and not modules:
        return []

    findings = check_manifests(repo, modules)
    for root in (repo / "apps", repo / "modules"):
        if not root.is_dir():
            continue
        for file in walk_sources(root):
            findings.extend(check_file(file, repo, apps, modules))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="repository root")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    repo = Path(args.root).resolve()
    findings = check_repo(repo)
    if args.json:
        json.dump(findings, sys.stdout, indent=2)
        sys.stdout.write("\n")
    else:
        for finding in findings:
            print(
                f"{finding['file']}:{finding['line']}:{finding['rule']}:{finding['specifier']}",
                file=sys.stderr,
            )
        if not findings:
            if not (repo / "apps").is_dir() and not (repo / "modules").is_dir():
                print("no apps/ or modules/; nothing to check", file=sys.stderr)
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
