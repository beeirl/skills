---
name: bee-mode
description: bee-mode, the TypeScript-first engineering router for beeirl's projects, run on Paseo with Claude Fable 5 coordinating and Grok 4.6 workers. Use for /bee-mode or whenever planning, designing, building, implementing, refactoring, debugging, reviewing, or documenting software. Selects the smallest relevant specialist skills, Paseo-managed Grok workers, verification, and GitHub-native delivery while respecting repository-specific guidance.
---

# Bee mode

Use this skill as the default entry point for software work. Read
[`references/principles.md`](references/principles.md) for non-trivial planning, architecture,
implementation, or review.

## Establish scope

1. Read the repository's instructions, manifests, relevant source, tests, and current Git state.
2. Treat repository-local product, language, and verification rules as authoritative.
3. Prefer TypeScript for new applications, services, packages, scripts, and developer tooling when
   the repository and user have not selected another language. Do not rewrite a healthy non-TypeScript
   codebase merely to satisfy this preference.
4. Keep planning and implementation inside the user's authorization. Skill activation never grants
   permission to push, open or merge a PR, deploy, message people, or mutate unrelated external state.
5. Use local harness agents and locally launched coding CLIs only. Do not route work to cloud coding
   agents.
6. Launch Grok workers through Paseo: `paseo run --provider grok/grok-4.6 --cwd <repo>
   --new-workspace worktree --env GROK_MEMORY=0 -d --json "<task packet>"`, then `paseo wait <id>` and
   `paseo logs <id> --json`. For a direct tool-bearing worker in the current checkout use `bee-grok`;
   for fixed-artifact read-only review use `bee-grok-review`. Before admitting any Grok route, run
   `install.py verify --json` and `paseo provider diagnostic grok`, and apply the approve-mode
   invariant defined in `references/model-routing.md`; a repository-local command must not override it.

## Route the work

Read-heavy delegated work never runs in the coordinator or in a coordinator sub-agent. Research,
scouting, codebase exploration, doc or API fact-gathering, and reading legwork run as a Grok worker:
`paseo run --provider grok/grok-4.6 --cwd <repo> --env GROK_MEMORY=0 --env GROK_SUBAGENTS=0 -d --json
"<self-contained packet>"`, then `paseo wait <id>` and `paseo logs <id> --json`. When a skill says
"sub-agent" or "background agent" for such work, that means this route. Implementation, review, and
risk-gated dispatch follow `references/model-routing.md` unchanged.

For every non-trivial software task, read and follow the normative
[`references/model-routing.md`](references/model-routing.md) contract before dispatch. It defines the
coordinator, supervisor, specialist-lead, worker, writer-lease, route-admission, lifecycle, receipt, and
independent-review requirements. Do not replace its definitions with a CLI or vendor's terminology.

Before the first provider-backed dispatch and before each later dispatch wave, read
[`references/capacity-routing.md`](references/capacity-routing.md). Inventory every installed
engineering harness, group routes by shared capacity pool, and schedule only from a current usage and
reset snapshot.

Use repository evaluations and concrete community evidence to form task-fit hypotheses, while using
authoritative provider/tool documentation for route identity and data controls. The dated evidence
register is non-normative. When broad multi-model coverage is explicitly requested, inventory all
installed routes, admit only eligible ones, and give each distinct family a non-duplicative lens.

Load only the skills that materially help the current task:

- A new system or high-risk cross-cutting plan: `architect`. A focused API, module boundary, or
  component design: `codebase-design`. Existing structural debt or architecture refactoring:
  `improve-codebase-architecture`. Use one of these by default, not all three; add `domain-modeling`
  when domain concepts or state transitions are central.
- An under-specified product or architecture decision: `grilling`; use `grill-with-docs` when the
  outcome should also update a glossary or architecture decision record.
- A settled plan that needs independently verifiable GitHub work units: `to-tickets`, while keeping
  the repository's existing tracker and source-of-work rules authoritative.
- TypeScript or TSX implementation and review: `typescript-best-practices`.
- Writing, placing, or reviewing code in any language: `clean-code`. Adding a
  dependency, layer, or module boundary: `clean-architecture`. Creating an app,
  module, package, workspace, or folder tree: `scaffolding`.
- New behavior or a defect fix: `tdd`; for an unknown failure, start with `diagnosing-bugs`.
- Merge conflicts: `resolving-merge-conflicts`.
- Large work with independent slices: `waves`.
- Competing viable designs or implementations: `arena`.
- Wide or risky changes: `blast-radius` before declaring completion.
- Contested, security-sensitive, or merge-critical review: `interrogate`.
- Ordinary code review: `code-review`.
- Agent instructions and technical prose: `writing-for-agents` and `technical-writing`.
- Branch, pull-request, check, or merge work: `github-delivery`.

Do not invoke every skill mechanically. Prefer the smallest combination that improves the result.

## Build and verify

1. Make data structures, contracts, and module boundaries explicit before adding orchestration.
2. Implement the smallest coherent slice that proves the design through a real caller or workflow.
3. Test at the closest useful layer, then run the repository's required checks.
4. Inspect the changed artifact and its callers, not just command exit codes.
5. For firm-visible behavior, verify the real user path when the repository supports it.
6. Before handoff, state what changed, what was verified, remaining risk, and any action requiring
   separate authorization.
