# Skills collection

Working set of agent skills used across local engineering agents. Each skill is a directory with a `SKILL.md` file, plus optional `references/`, `agents/`, and `scripts/` files.

This repository is a public snapshot of the live tree at `~/.agents/skills` (also linked from `~/.claude/skills`). `lee-engineering` is the default router for software work. It loads the other skills only when they apply.

## Use a skill

1. Clone this repository.
2. Copy or symlink the skill directory into your agent's skills folder.
3. Invoke the skill by name.

Typical install locations:

- `~/.agents/skills/<skill-name>`
- `~/.claude/skills/<skill-name>`

A skill is available as soon as its folder is present. You do not register it in a separate manifest.

```bash
git clone https://github.com/korallis/skills-collection.git
cp -R skills-collection/lee-engineering ~/.agents/skills/
```

To install every skill:

```bash
git clone https://github.com/korallis/skills-collection.git
mkdir -p ~/.agents/skills
for skill in skills-collection/*/; do
  name=$(basename "$skill")
  case "$name" in
    .git) continue ;;
  esac
  cp -R "$skill" ~/.agents/skills/
done
```

Skip directories that are not skills. `LICENSE`, `README.md`, and `.gitignore` are not skills.

## Catalog

| Skill | Role |
| --- | --- |
| [lee-engineering](lee-engineering/) | Router for software work. Selects specialist skills, local multi-model routing, verification, and GitHub delivery. |
| [architect](architect/) | Architecture-first design for changes that cross modules, contracts, or domain concepts. |
| [codebase-design](codebase-design/) | Vocabulary and method for deep modules, seams, and testable interfaces. |
| [improve-codebase-architecture](improve-codebase-architecture/) | Scan for deepening opportunities, present an HTML report, then grill the chosen one. |
| [domain-modeling](domain-modeling/) | Sharpen domain language. Write or edit `CONTEXT.md` and architecture decision records. |
| [prototype](prototype/) | Throwaway prototype to test a state model, logic, or UI before committing to it. |
| [grilling](grilling/) | Relentless interview that stress-tests a plan, decision, or idea. |
| [grill-with-docs](grill-with-docs/) | Same interview, and it writes ADRs and glossary entries as you go. |
| [typescript-best-practices](typescript-best-practices/) | TypeScript and TSX conventions used when reading or editing `.ts` / `.tsx` files. |
| [tdd](tdd/) | Test-driven development. Red, green, refactor, including integration tests. |
| [diagnosing-bugs](diagnosing-bugs/) | Diagnosis loop for hard bugs and performance regressions. |
| [bootstrap-ios](bootstrap-ios/) | Bootstrap agents for Apple platforms: Swift, SwiftUI, Xcode, Simulator, App Intents. |
| [swiftui-animation-match](swiftui-animation-match/) | Match a UI interaction to proven SwiftUI animation patterns. |
| [code-review](code-review/) | Two-axis review of a diff: standards versus the originating spec. |
| [blast-radius](blast-radius/) | Change-impact and completion audit before declaring wide or risky work done. |
| [interrogate](interrogate/) | Independent local multi-model review for contested, security-sensitive, or merge-critical work. |
| [running-bug-review-board](running-bug-review-board/) | Real-user QA, bug filing, phase sign-off, and an HTML dashboard. |
| [technical-writing](technical-writing/) | Diátaxis, Google developer style, STE, and Global English for docs and PR text. |
| [writing-for-agents](writing-for-agents/) | How to write skills, `AGENTS.md`, and other documents that agents consume. |
| [github-delivery](github-delivery/) | GitHub-only branches, issues, pull requests, checks, and merges. No Graphite. |
| [resolving-merge-conflicts](resolving-merge-conflicts/) | Resolve an in-progress git merge or rebase conflict. |
| [to-tickets](to-tickets/) | Break a plan into tracer-bullet tickets with blocking edges. |
| [handoff](handoff/) | Compact the current conversation into a handoff for the next agent. |
| [arena](arena/) | Isolated competing candidates, judged against shared criteria. |
| [waves-codex](waves-codex/) | Bounded wave orchestration for Codex: workers, aggregate, verify, extend. |
| [research](research/) | Investigate a question against primary sources and write findings into the repo. |

## Router

### lee-engineering

Default entry point for planning, design, implementation, refactoring, debugging, review, and documentation. It reads the repository's own rules first, prefers TypeScript for new code when no language is already chosen, and loads only the specialist skills that help the current task.

For non-trivial work it follows the local multi-model contract in `lee-engineering/references/model-routing.md`: coordinator, supervisor, specialist, worker, writer lease, route admission, receipts, and independent review. Cloud coding agents are out of scope. Skill activation never grants permission to push, open a pull request, deploy, or mutate unrelated external state.

## Architecture and design

### architect

Use for non-trivial or high-risk software changes. Ground the design in callers, data structures, signatures, and repository evidence, produce genuine alternatives, then implement against the chosen shape.

### codebase-design

Shared vocabulary for deep modules: where a seam goes, how an interface should look, how to make a module testable and navigable by an agent.

### improve-codebase-architecture

Scan a codebase for deepening opportunities, render them as a visual HTML report, then grill through the one you pick.

### domain-modeling

Build and sharpen the project's domain model. Use when discussing terminology, writing `CONTEXT.md`, or recording an ADR. Includes `CONTEXT-FORMAT.md` and `ADR-FORMAT.md`.

### prototype

Build a disposable prototype to answer a design question. Use it to sanity-check a state model, a logic path, or a UI, not to ship the prototype.

### grilling

Interview the user until the plan, decision, or idea is stress-tested. Triggered by "grill" phrasing and by under-specified product or architecture decisions.

### grill-with-docs

Runs `grilling` and `domain-modeling` together so the interview also leaves ADRs and glossary entries.

## Implementation

### typescript-best-practices

Conventions for TypeScript and TSX. Load whenever reading or editing `.ts` or `.tsx` files. Detailed patterns live in `references/patterns.md`.

### tdd

Test-driven development. Use when building features or fixing bugs test-first, when the user mentions red-green-refactor, or when writing integration tests. Companion notes: `tests.md`, `mocking.md`.

### diagnosing-bugs

Diagnosis loop for failures and performance regressions. Use when the user says "diagnose" or "debug this", or reports something broken, throwing, failing, or slow.

### bootstrap-ios

Bootstrap agents for iOS, iPadOS, macOS, Swift, SwiftUI, SwiftData / Core Data, Swift Testing, Xcode, Simulator, App Intents, and XcodeBuildMCP. Use before Apple-platform work, or when asked to load Ray's iOS skills.

### swiftui-animation-match

Match a UI/UX interaction to proven SwiftUI animation patterns from curated open-source catalogs. Prefers system-first restraint before custom motion. Covers loaders, likes, toggles, card decks, reveals, and shaders.

## Review and quality

### code-review

Review changes since a fixed point (commit, branch, tag, or merge-base) on two axes, in parallel:

- **Standards:** does the code follow this repository's documented coding standards?
- **Spec:** does the code match the originating issue or spec?

### blast-radius

Change-impact and completion audit. Use before declaring wide, risky, cross-cutting, or merge-critical work complete. Inspects callers and contracts beyond the diff, identifies safety facts, exercises the real artifact, and reports what is cleared versus still risky.

### interrogate

Independent local multi-model review. Use when one reviewer is not enough: contested, security-sensitive, high-risk, or merge-critical plans and changes. Reviewers get the same intent and rubric. The lead aggregates consensus and disagreement without pretending that two runs of the same family are independent.

### running-bug-review-board

Real-user QA for web or iOS/iPadOS apps. Runs manual test plans, UX bug hunts, build sign-off, bug filing, and triage. Produces P0/P1/P2 reports, a YES/NO phase verdict, tracker sync guidance, and an HTML dashboard. Interactive Bug Review Board triage stays in a separate session.

### technical-writing

Layered writing standard for docs, RFCs, READMEs, PR descriptions, and commit messages: Diátaxis structure, Google developer style, STE instruction rules, and Global English syntax.

### writing-for-agents

How to write documents that agents consume: skills, `AGENTS.md`, `CLAUDE.md`, and context pointers. Companion: `SKILL-MECHANICS.md` for frontmatter, invocation, and router skills.

## Delivery

### github-delivery

GitHub-only delivery for branches, worktrees, issues, pull requests, checks, reviews, and merges. Uses `git`, `gh`, GitHub Actions, and GitHub Projects. Graphite and `gt` are disabled.

### resolving-merge-conflicts

Resolve an in-progress git merge or rebase conflict. Preserve both intents where possible, run the project's checks, and finish the merge or rebase. Do not abort.

### to-tickets

Break a plan, spec, or conversation into tracer-bullet tickets. Each ticket declares its blocking edges. Edges are text in one file per ticket locally, or native blocking links on a real tracker.

### handoff

Compact the current conversation into a handoff document so another agent can continue. Redacts secrets and personal data. Saves outside the workspace.

## Orchestration and research

### arena

Local multi-agent design or implementation competition. Use when several materially different solutions are plausible and selection quality matters. Creates isolated candidates, judges them against shared criteria, and lets the lead synthesize and verify the strongest result. No cloud agents.

### waves-codex

WAVES: Workers, Aggregate, Verify, Extend. Wave-based orchestration for Codex. Decompose a large goal into independent slices, spawn a bounded parallel wave, collect evidence-backed handoffs, verify important claims, synthesize one deliverable, and start another wave only when warranted.

### research

Investigate a question against high-trust primary sources and write the findings as a Markdown file in the repository. Use for docs, API facts, or reading work that can run in a background agent.

## Layout of a skill

```
skill-name/
  SKILL.md           # required: name, description, and instructions
  agents/            # optional: harness display metadata
  references/        # optional: material loaded only when needed
  scripts/           # optional: helper scripts
```

The YAML `description` on `SKILL.md` is the trigger. Agents decide whether to load the skill from that text.

## What this snapshot does not include

Grok Build TUI also ships product skills under `~/.grok/bundled/skills`. Those files belong to the TUI and are not copied here. They cover image and video generation, Office documents, Grok workflows, and session-resume helpers:

| Bundled skill | Role |
| --- | --- |
| `build-with-ai` | Default to SpaceXAI when adding LLM features to an app. |
| `code-review` | Strict maintainability audit (separate from this repo's `code-review`). |
| `create-skill` | Scaffold a new Grok skill. |
| `create-workflow` | Author a Grok Build Rhai workflow. |
| `design` | Design-doc writer and reviewer loop. |
| `docx` | Create, read, and edit Word documents. |
| `execute-plan` | Execute a PR-plan DAG from a design document. |
| `game-animation-frames` | Animation sheets from a video-first pipeline. |
| `game-asset-core` | Shared rules for game-asset generation. |
| `game-character-consistency` | Character identity across images. |
| `game-tilesets` | Tileable textures and terrain tilesets. |
| `game-ui-icons` | Game UI, HUD, and icon sets. |
| `imagine` | How to use Grok image generation and editing. |
| `implement` | Implement-review-fix loop with scaled reviewers. |
| `pdf` | Read, create, and transform PDF files. |
| `pptx` | Read, create, and edit PowerPoint files. |
| `pr-babysit` | Watch a pull request, fix CI, and address review comments. |
| `resume-claude` | Continue a Claude Code session. |
| `resume-codex` | Continue a Codex session. |
| `resume-cursor` | Continue a Cursor session. |
| `review` | Reviewer subagent for local changes, a branch, or a GitHub pull request. |
| `skill-design-principles` | Principles for writing and editing skills. |

An older public collection lives at [korallis/skills](https://github.com/korallis/skills). That repository is not this working set.

## License

MIT. See [LICENSE](LICENSE). Some skills were adapted from public skill libraries. Keep their provenance notes inside the skill files when those notes exist.
