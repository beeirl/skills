---
name: scaffolding
description: Scaffolding. Enforce Dune-style capability folders, public module contracts, one data owner, and mechanical boundaries. Use when creating an app, module, package, workspace, monorepo, or folder tree, or when deciding where a new capability lives.
---

# Scaffolding

Mandatory when the change creates an app, module, package, or folder tree.
Repository layout wins where it is already declared. On a greenfield app or a
Dune-shaped monorepo, apply this layout. Do not rewrite a healthy tree merely
to match it. Do not explain Dune. Place the files. Pair with `architect` for a
new shape, `clean-architecture` for inward imports, and `codebase-design` for
the module's interface.

Layout and ownership questions: [`references/layout.md`](references/layout.md).

## Before you add a package or folder

1. Name the capability in one domain noun (`work`, `matter`, `billing`). If the
   name needs "and", it is two modules. Stop until the noun is one body of
   knowledge.
2. Name the durable value this folder would write, and find who already writes
   it. If an owner exists, add an isolated file there. Do not start a sibling
   writer.
3. List the files this slice will actually import. Create those. Leave every
   unused layer uncreated.

## Enforce these rules

| Rule | You must |
| --- | --- |
| Capability folder | Domain knowledge lives in `modules/<noun>/`. Apps live in `apps/<name>/` as composition roots. Tooling stays in `tooling/`. Register the package the way this repo already registers packages. |
| Public contract | Callers import the package root only (`@scope/work`). `package.json` `exports` expose `"."` and nothing internal. The public file is `src/index.ts` or `public.ts`. |
| One data owner | One module writes each durable kind. Other modules call a public command or consume a versioned event. Cross-ownership work is one application command or an outbox, never another module's tables. |
| Thin app | Route handlers, CLI, and worker entrypoints authenticate, parse, invoke a module, and render. They do not own domain rules, SQL, or provider SDKs. |
| Isolated files | New product work is a new file in the owning module. Do not grow a shared root with another branch, flag, or `kind`. |
| Vendor wrap | A third-party SDK is imported only inside the module that owns that adapter. |
| Mechanical fail | Forbidden imports fail CI. If the repo has an architecture check, run it. Otherwise run `scripts/check_capability_folders.py --root .`. |
| Correction ladder | When the same agent mistake repeats: make it unrepresentable, then encode it in CI, then a narrow instruction, then human review. Do not start at review. |
| Slice, not inventory | Scaffold the modules this vertical slice uses. Empty packages, placeholder APIs, and unused `model/` `commands/` `queries/` folders fail. |

## Forbidden in the diff

- A `utils`, `helpers`, `common`, or `misc` package used as a capability.
- A deep import (`@scope/work/src/...`, or a relative path into another
  package's internals).
- A module importing an app.
- A second ledger for work, tasks, reminders, or notifications beside the
  owning module.
- A vendor client constructed in a route handler or in a module that does not
  own that adapter.
- An exception with no ADR and no allowlist entry.

## Done

Do not claim the change is finished until:

- [ ] The new folder is a single capability, or you extended the existing owner.
- [ ] Callers import the package root. `exports` expose only `"."`.
- [ ] One module writes the durable data this slice introduces.
- [ ] App files only compose; domain rules sit in the module.
- [ ] No unused layer or empty package was added.
- [ ] You ran the repo architecture check or
      `scripts/check_capability_folders.py --root .`, or you named exactly what
      was not run.
