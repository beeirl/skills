# Grok harness installation and verification

The GitHub repository `beeirl/skills` is the canonical bee-mode source. Install the skill once per
machine; repositories consume that shared installation and must not carry private copies.

## Install or update

From a clean, current clone of `beeirl/skills`, run:

```bash
python3 bee-mode/scripts/install.py install --json
```

The command atomically replaces `~/.agents/skills/bee-mode` and `~/.claude/skills/bee-mode` (the same
directory when `~/.claude/skills` is a symlink to `~/.agents/skills`), installs `~/.local/bin/bee-grok`
and `~/.local/bin/bee-grok-review`, and changes only `ui.permission_mode` in `~/.grok/config.toml`. It
is safe to run repeatedly. Repeat `--skills-root` for any additional skill root.

The other skills in the collection need no installer: copy each skill directory into
`~/.agents/skills/`.

## Routes

- `paseo run --provider grok/grok-4.6 ...` dispatches a Grok worker under the Paseo daemon, which
  launches `grok agent stdio`. The `always-approve` setting in `~/.grok/config.toml` governs it.
- `bee-grok` launches Grok directly in the current checkout with tools. Do not invoke `grok`
  directly from an engineering workflow and do not supply a permission-mode flag.
- `bee-grok-review` runs a tool-free immutable review slice: Grok 4.6 at low reasoning, approve mode,
  memory off, streaming Messages JSON, one turn, planning, subagents, web access, and built-in tools
  disabled.

Do not copy credentials or the rest of `~/.grok`. Authentication remains machine-local.

## Verify

```bash
python3 ~/.agents/skills/bee-mode/scripts/install.py verify --json
paseo provider diagnostic grok --json
```

`verify` exits nonzero unless the installed skill digest matches the canonical source, every skill
root matches, each wrapper is executable and byte-identical to its counterpart in the skill tree, and
Grok has exactly one `always-approve` UI setting. The Paseo diagnostic must report `Status: Ready`.

## Verify more than one machine

Each remote target must be reachable through non-interactive SSH and must already contain the
installed verifier:

```bash
python3 bee-mode/scripts/verify_grok_fleet.py local user@other-host
```

It exits nonzero for unreachable targets, configuration drift, wrapper drift, or skill digest
differences, and prints JSON suitable for a CI artifact.
