# Recommended configuration

`waves` in bee-mode needs no orchestration config: the Fable manager dispatches
each worker with `paseo run`, and Grok reads its own settings.

## `~/.grok/config.toml`

```toml
[ui]
permission_mode = "always-approve"   # required; enforced by bee-mode/scripts/install.py

[subagents]
enabled = false                      # workers do not spawn workers; the manager runs every wave
```

Grok's reasoning effort is a model default (`high` for grok-4.6). It cannot be
set per `paseo run`; use `bee-grok --reasoning-effort low` for a direct
scouting launch when the cheaper setting matters.

## `~/.paseo/config.json`

The `grok` provider must be enabled with `"command": ["grok", "agent", "stdio"]`
(the default). Check with `paseo provider diagnostic grok --json`; it must report
`Status: Ready`.

## Per-dispatch flags

| Purpose | Flags |
| --- | --- |
| Any worker | `--provider grok/grok-4.6 --cwd <repo> --env GROK_MEMORY=0 -d --json --title "wave-N/<slice>"` |
| Read-only worker | add `--env GROK_SUBAGENTS=0`; no worktree |
| Implementation worker | add `--new-workspace worktree --new-branch wave/<slice>` |
| Machine-readable result | add `--output-schema <file-or-json>` |
| Bounded wait | `paseo wait <id> --wait-timeout 20m` |

## Related skills

- `bee-mode/references/model-routing.md`: writer lease, receipts, independent review.
- `bee-mode/references/capacity-routing.md`: one Grok pool shared by all routes.
- `arena` for competing candidates, `interrogate` for review panels.
