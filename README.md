# beeirl skills

Agent skills for bee-mode: Paseo as harness, Claude Fable 5 as coordinator, Grok 4.6 as worker model. Each skill is a directory with a `SKILL.md` file, plus optional `references/`, `scripts/`, and `tests/` files. The same files load in Claude Code and in Grok.

This repository is a snapshot of the live tree at `~/.agents/skills` (also linked from `~/.claude/skills`). `bee-mode` is the default router for software work. It loads the other skills only when they apply.

This collection started as a copy of [korallis/skills-collection](https://github.com/korallis/skills-collection) and is maintained independently; see [NOTICE.md](NOTICE.md).

Most skills here come from these sources. Use the linked repositories for upstream copies where they exist:

- [mattpocock/skills](https://github.com/mattpocock/skills) — Skills For Real Engineers. Matt Pocock. MIT.
- [RayFernando1337/rayfernando-skills](https://github.com/RayFernando1337/rayfernando-skills) — waves, QA, iOS bootstrap, and SwiftUI animation matching. Ray Fernando. Apache License 2.0.
- Robert C. Martin, *Clean Code* (2008) and *Clean Architecture* (2017).
- Lauren Tan's Dune method: capability folders, public module contracts, one data owner, and mechanical boundaries. Supporting principles: [pstack](https://github.com/cursor/plugins/tree/main/pstack/skills). Workshop chapter: [Implementing Strict CI Constraints and the Dune Architecture](https://maven.com/p/e23d9c/how-cursor-turned-ai-agents-into-better-engineers#t=2460).

The catalog below links each copied skill to its folder in those repos. Original skills written for this collection are marked Original. Full notices are in [NOTICE.md](NOTICE.md).

## Use a skill

1. Clone this repository.
2. Copy or symlink the skill directory into your agent's skills folder.
3. Invoke the skill by name.

Typical install locations:

- `~/.agents/skills/<skill-name>`
- `~/.claude/skills/<skill-name>`

A skill is available as soon as its folder is present. You do not register it in a separate manifest.

```bash
git clone https://github.com/beeirl/skills.git
python3 skills/bee-mode/scripts/install.py install --json   # bee-mode, bee-grok wrappers, Grok approve mode
```

To install every skill:

```bash
git clone https://github.com/beeirl/skills.git
python3 skills/bee-mode/scripts/install.py install --json
for skill in skills/*/; do
  name=$(basename "$skill")
  case "$name" in
    .git|licenses|bee-mode) continue ;;
  esac
  rm -rf ~/.agents/skills/"$name" && cp -R "$skill" ~/.agents/skills/
done
```

Skip directories that are not skills. `LICENSE`, `NOTICE.md`, `README.md`, `.gitignore`, and `licenses/` are not skills.

## Catalog

| Skill | Role | Source |
| --- | --- | --- |
| [bee-mode](bee-mode/) | Router for software work in bee-mode. Selects specialist skills, dispatches Grok workers through Paseo, verification, and GitHub delivery. | Adapted from [korallis/skills-collection](https://github.com/korallis/skills-collection) `lee-engineering` |
| [architect](architect/) | Architecture-first design for changes that cross modules, contracts, or domain concepts. | Original |
| [codebase-design](codebase-design/) | Vocabulary and method for deep modules, seams, and testable interfaces. | [mattpocock/skills](https://github.com/mattpocock/skills) · [codebase-design](https://github.com/mattpocock/skills/tree/main/skills/engineering/codebase-design) |
| [improve-codebase-architecture](improve-codebase-architecture/) | Scan for deepening opportunities, present an HTML report, then grill the chosen one. | [mattpocock/skills](https://github.com/mattpocock/skills) · [improve-codebase-architecture](https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture) |
| [domain-modeling](domain-modeling/) | Sharpen domain language. Write or edit `CONTEXT.md` and architecture decision records. | [mattpocock/skills](https://github.com/mattpocock/skills) · [domain-modeling](https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling) |
| [prototype](prototype/) | Throwaway prototype to test a state model, logic, or UI before committing to it. | [mattpocock/skills](https://github.com/mattpocock/skills) · [prototype](https://github.com/mattpocock/skills/tree/main/skills/engineering/prototype) |
| [grilling](grilling/) | Relentless interview that stress-tests a plan, decision, or idea. | [mattpocock/skills](https://github.com/mattpocock/skills) · [grilling](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling) |
| [grill-with-docs](grill-with-docs/) | Same interview, and it writes ADRs and glossary entries as you go. | [mattpocock/skills](https://github.com/mattpocock/skills) · [grill-with-docs](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs) |
| [typescript-best-practices](typescript-best-practices/) | TypeScript and TSX conventions used when reading or editing `.ts` / `.tsx` files. | Original |
| [clean-code](clean-code/) | Enforce Clean Code on every source change: names, small functions, comments, errors, tests. | Robert C. Martin, *Clean Code* (2008) |
| [clean-architecture](clean-architecture/) | Enforce the Dependency Rule when adding a file, import, module, or vendor. | Robert C. Martin, *Clean Architecture* (2017) |
| [scaffolding](scaffolding/) | Enforce Dune-style capability folders, public module contracts, one data owner, and mechanical boundaries when creating an app or module. | Original · [Lauren Tan, Dune](https://maven.com/p/e23d9c/how-cursor-turned-ai-agents-into-better-engineers#t=2460) · [pstack](https://github.com/cursor/plugins/tree/main/pstack/skills) |
| [tdd](tdd/) | Test-driven development. Red, green, refactor, including integration tests. | [mattpocock/skills](https://github.com/mattpocock/skills) · [tdd](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd) |
| [diagnosing-bugs](diagnosing-bugs/) | Diagnosis loop for hard bugs and performance regressions. | [mattpocock/skills](https://github.com/mattpocock/skills) · [diagnosing-bugs](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs) |
| [bootstrap-ios](bootstrap-ios/) | Bootstrap agents for Apple platforms: Swift, SwiftUI, Xcode, Simulator, App Intents. | [RayFernando1337/rayfernando-skills](https://github.com/RayFernando1337/rayfernando-skills) · [bootstrap-ios](https://github.com/RayFernando1337/rayfernando-skills/tree/main/plugins/bootstrap-ios/skills/bootstrap-ios) |
| [swiftui-animation-match](swiftui-animation-match/) | Match a UI interaction to proven SwiftUI animation patterns. | [RayFernando1337/rayfernando-skills](https://github.com/RayFernando1337/rayfernando-skills) · [swiftui-animation-match](https://github.com/RayFernando1337/rayfernando-skills/tree/main/plugins/swiftui-animation-match/skills/swiftui-animation-match) |
| [code-review](code-review/) | Two-axis review of a diff: standards versus the originating spec. | [mattpocock/skills](https://github.com/mattpocock/skills) · [code-review](https://github.com/mattpocock/skills/tree/main/skills/engineering/code-review) (adapted) |
| [blast-radius](blast-radius/) | Change-impact and completion audit before declaring wide or risky work done. | Original |
| [interrogate](interrogate/) | Independent local multi-model review for contested, security-sensitive, or merge-critical work. | Original |
| [running-bug-review-board](running-bug-review-board/) | Real-user QA, bug filing, phase sign-off, and an HTML dashboard. | [RayFernando1337/rayfernando-skills](https://github.com/RayFernando1337/rayfernando-skills) · [running-bug-review-board](https://github.com/RayFernando1337/rayfernando-skills/tree/main/plugins/running-bug-review-board/skills/running-bug-review-board) |
| [technical-writing](technical-writing/) | Diátaxis, Google developer style, STE, and Global English for docs and PR text. | Original (cites public style guides) |
| [writing-for-agents](writing-for-agents/) | How to write skills, `AGENTS.md`, and other documents that agents consume. | [mattpocock/skills](https://github.com/mattpocock/skills) · [writing-for-agents](https://github.com/mattpocock/skills/tree/main/skills/productivity/writing-for-agents) |
| [github-delivery](github-delivery/) | GitHub-only branches, issues, pull requests, checks, and merges. No Graphite. | Original |
| [resolving-merge-conflicts](resolving-merge-conflicts/) | Resolve an in-progress git merge or rebase conflict. | [mattpocock/skills](https://github.com/mattpocock/skills) · [resolving-merge-conflicts](https://github.com/mattpocock/skills/tree/main/skills/engineering/resolving-merge-conflicts) |
| [to-tickets](to-tickets/) | Break a plan into tracer-bullet tickets with blocking edges. | [mattpocock/skills](https://github.com/mattpocock/skills) · [to-tickets](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-tickets) (adapted) |
| [handoff](handoff/) | Compact the current conversation into a handoff for the next agent. | [mattpocock/skills](https://github.com/mattpocock/skills) · [handoff](https://github.com/mattpocock/skills/tree/main/skills/productivity/handoff) |
| [arena](arena/) | Isolated competing candidates, judged against shared criteria. | Original |
| [waves](waves/) | Bounded wave orchestration for bee-mode: Fable plans, Grok workers run under Paseo. | [RayFernando1337/rayfernando-skills](https://github.com/RayFernando1337/rayfernando-skills) · [waves](https://github.com/RayFernando1337/rayfernando-skills/tree/main/plugins/waves-codex/skills/waves-codex) |
| [research](research/) | Investigate a question against primary sources and write findings into the repo. | [mattpocock/skills](https://github.com/mattpocock/skills) · [research](https://github.com/mattpocock/skills/tree/main/skills/engineering/research) |

## Sources

Original skill repositories:

- **[mattpocock/skills](https://github.com/mattpocock/skills)** — https://github.com/mattpocock/skills
- **[RayFernando1337/rayfernando-skills](https://github.com/RayFernando1337/rayfernando-skills)** — https://github.com/RayFernando1337/rayfernando-skills

Full notices are in [NOTICE.md](NOTICE.md).

### [mattpocock/skills](https://github.com/mattpocock/skills)

Skills For Real Engineers. MIT. Copyright (c) 2026 Matt Pocock.

Copied here: `codebase-design`, `code-review`, `diagnosing-bugs`, `domain-modeling`, `grill-with-docs`, `grilling`, `handoff`, `improve-codebase-architecture`, `prototype`, `research`, `resolving-merge-conflicts`, `tdd`, `to-tickets`, and `writing-for-agents`.

`code-review` and `to-tickets` keep Matt's method and drop the requirement to run his setup skill. They use the repository's own GitHub tracker instead.

Docs for several of these skills also live on [aihero.dev](https://www.aihero.dev/posts).

### [RayFernando1337/rayfernando-skills](https://github.com/RayFernando1337/rayfernando-skills)

Apache License 2.0. Copyright 2026 Ray Fernando. License text: [licenses/APACHE-2.0.txt](licenses/APACHE-2.0.txt).

Copied here: `bootstrap-ios`, `running-bug-review-board`, `swiftui-animation-match`, and `waves` (from `waves-codex`, re-targeted to Paseo and Grok).

`waves` also credits [Phillip Chaffee's public `deep-research` Cursor skill](https://github.com/PhillipChaffee/.cursor) for run-shape triage and dependency-aware dispatch. `swiftui-animation-match` catalogs [Shubham Kumar Singh's SwiftUI-Animations](https://github.com/Shubham0812/SwiftUI-Animations). `bootstrap-ios` routes to community packs listed in [bootstrap-ios/references/sources.md](bootstrap-ios/references/sources.md), including [Paul Hudson / Hacking with Swift](https://github.com/twostraws/swift-agent-skills), [Antoine van der Lee](https://github.com/AvdLee), [OpenAI plugins](https://github.com/openai/plugins), [Krzysztof Zablocki](https://merowing.info/posts/stop-getting-average-code-from-your-llm/), and [XcodeBuildMCP](https://github.com/getsentry/XcodeBuildMCP).

### Robert C. Martin — *Clean Code* and *Clean Architecture*

- *Clean Code: A Handbook of Agile Software Craftsmanship* (Prentice Hall, 2008) → [`clean-code`](clean-code/).
- *Clean Architecture: A Craftsman's Guide to Software Structure and Design* (Prentice Hall, 2017) → [`clean-architecture`](clean-architecture/).

These folders are not a reprint of either book.

### Lauren Tan — Dune method and pstack

[`scaffolding`](scaffolding/) packages Lauren Tan's Dune method. Dune is an in-house, agent-friendly React framework. There is no public Dune package. This collection does not contain Dune source.

- [How Cursor Turned AI Agents Into Better Engineers](https://maven.com/p/e23d9c/how-cursor-turned-ai-agents-into-better-engineers#t=2460) — Maven workshop, 12 August 2026, chapter "Implementing Strict CI Constraints and the Dune Architecture" at 00:41:00.
- [Lauren Tan's speaking history](https://www.no.lol/speaking/) — first-party background.
- [pstack public principle skills](https://github.com/cursor/plugins/tree/main/pstack/skills) — model the domain, boundary discipline, minimise reader load, type-system discipline, idempotent operations.
- Matilda OS `docs/audit/typescript-refactor-plan.md` §8 is the worked application of that method (capability folders, public module contracts, one data owner, mechanical dependency rules). Matilda product source is not copied here.

Sources recorded in [`scaffolding/SOURCE.md`](scaffolding/SOURCE.md). Full notices are in [NOTICE.md](NOTICE.md).

### Original to this collection

`architect`, `arena`, `blast-radius`, `github-delivery`, `interrogate`, `scaffolding`, and `typescript-best-practices` were written by Lee for korallis/skills-collection; `bee-mode` is this collection's adaptation of his `lee-engineering`. No earlier public skill matching these files was found.

`technical-writing` is also original. Its rules cite [Diátaxis](https://diataxis.fr) (Daniele Procida), the [Google developer documentation style guide](https://developers.google.com/style), [ASD-STE100](https://asd-ste100.org), and John R. Kohl, *The Global English Style Guide*.

## Router

### bee-mode

Adapted from Lee's `lee-engineering` in [korallis/skills-collection](https://github.com/korallis/skills-collection).

Default entry point for planning, design, implementation, refactoring, debugging, review, and documentation. It reads the repository's own rules first, prefers TypeScript for new code when no language is already chosen, and loads only the specialist skills that help the current task. Creating an app, module, package, workspace, or folder tree loads `scaffolding`. Adding a dependency, layer, or import that crosses a boundary loads `clean-architecture`. Writing or reviewing source loads `clean-code`.

For non-trivial work it follows the multi-model contract in `bee-mode/references/model-routing.md`: the Paseo `claude` agent on Claude Fable 5 is the coordinator, Paseo (`paseo wait`, `paseo logs`, `paseo permit`) is the supervisor, Grok 4.6 workers are dispatched with `paseo run --provider grok/grok-4.6`, and `bee-grok-review` provides different-family review. Install and verification: `bee-mode/references/grok-harness.md`. Cloud coding agents are out of scope. Skill activation never grants permission to push, open a pull request, deploy, or mutate unrelated external state.

## Architecture and design

### architect

Original to this collection.

Use for non-trivial or high-risk software changes. Ground the design in callers, data structures, signatures, and repository evidence, produce genuine alternatives, then implement against the chosen shape.

### scaffolding

Original to this collection. Enforces Lauren Tan's Dune **method**, not a Dune install. Dune is in-house and has no public package.

Use when creating an app, module, package, workspace, monorepo, or folder tree, or when deciding where a new capability lives. A model should load this skill for those tasks without being asked by name.

It makes the safe path the default:

- **Capability folders.** Domain knowledge lives in `modules/<noun>/`. One noun, one body of knowledge. Apps live in `apps/<name>/` as composition roots. Tooling stays in `tooling/`.
- **Public module contract.** Callers import the package root only. `package.json` `exports` expose `"."`. The public file is `src/index.ts` or `public.ts`.
- **One data owner.** One module writes each durable kind. Other modules call a public command or consume a versioned event. They do not query another module's tables.
- **Thin apps.** Route handlers, CLIs, and workers authenticate, parse, invoke a module, and render. They do not own domain rules, SQL, or provider SDKs.
- **Mechanical boundaries.** Forbidden imports fail CI. If the repo has an architecture check, run it. Otherwise run [`scaffolding/scripts/check_capability_folders.py`](scaffolding/scripts/check_capability_folders.py).
- **Slice, not inventory.** Scaffold only the modules the current vertical slice uses. Empty packages and unused layer folders fail.

Repository layout wins where it is already declared. The skill does not rewrite a healthy non-modular tree.

Pair with `architect` for a new shape, `clean-architecture` for the Dependency Rule on imports, and `codebase-design` for the module's interface.

Layout and ownership questions: [`scaffolding/references/layout.md`](scaffolding/references/layout.md). Sources: [`scaffolding/SOURCE.md`](scaffolding/SOURCE.md). Supporting principles: [pstack](https://github.com/cursor/plugins/tree/main/pstack/skills). Worked example: Matilda OS `docs/audit/typescript-refactor-plan.md` §8.

### codebase-design

From [Matt Pocock's `codebase-design`](https://github.com/mattpocock/skills/tree/main/skills/engineering/codebase-design).

Shared vocabulary for deep modules: where a seam goes, how an interface should look, how to make a module testable and navigable by an agent.

### improve-codebase-architecture

From [Matt Pocock's `improve-codebase-architecture`](https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture).

Scan a codebase for deepening opportunities, render them as a visual HTML report, then grill through the one you pick.

### domain-modeling

From [Matt Pocock's `domain-modeling`](https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling).

Build and sharpen the project's domain model. Use when discussing terminology, writing `CONTEXT.md`, or recording an ADR. Includes `CONTEXT-FORMAT.md` and `ADR-FORMAT.md`.

### prototype

From [Matt Pocock's `prototype`](https://github.com/mattpocock/skills/tree/main/skills/engineering/prototype).

Build a disposable prototype to answer a design question. Use it to sanity-check a state model, a logic path, or a UI, not to ship the prototype.

### grilling

From [Matt Pocock's `grilling`](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling). The user-invoked wrapper in his repo is [`grill-me`](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me).

Interview the user until the plan, decision, or idea is stress-tested. Triggered by "grill" phrasing and by under-specified product or architecture decisions.

### grill-with-docs

From [Matt Pocock's `grill-with-docs`](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs).

Runs `grilling` and `domain-modeling` together so the interview also leaves ADRs and glossary entries.

## Implementation

### typescript-best-practices

Original to this collection. No earlier public skill matching this file was found.

Conventions for TypeScript and TSX. Load whenever reading or editing `.ts` or `.tsx` files. Detailed patterns live in `references/patterns.md`.

### clean-code

Enforce Robert C. Martin's *Clean Code* (2008) on every source change. Model-invoked when writing, editing, reviewing, or refactoring any source file. Smell IDs: [`clean-code/references/smells.md`](clean-code/references/smells.md).

### clean-architecture

Enforce the Dependency Rule from *Clean Architecture* (2017) when adding a file, import, module, or vendor. Circles: [`clean-architecture/references/circles.md`](clean-architecture/references/circles.md).

### tdd

From [Matt Pocock's `tdd`](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd).

Test-driven development. Use when building features or fixing bugs test-first, when the user mentions red-green-refactor, or when writing integration tests. Companion notes: `tests.md`, `mocking.md`.

### diagnosing-bugs

From [Matt Pocock's `diagnosing-bugs`](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs).

Diagnosis loop for failures and performance regressions. Use when the user says "diagnose" or "debug this", or reports something broken, throwing, failing, or slow.

### bootstrap-ios

From [Ray Fernando's `bootstrap-ios`](https://github.com/RayFernando1337/rayfernando-skills/tree/main/plugins/bootstrap-ios/skills/bootstrap-ios). It loads community packs listed in [sources.md](bootstrap-ios/references/sources.md).

Bootstrap agents for iOS, iPadOS, macOS, Swift, SwiftUI, SwiftData / Core Data, Swift Testing, Xcode, Simulator, App Intents, and XcodeBuildMCP. Use before Apple-platform work, or when asked to load Ray's iOS skills.

### swiftui-animation-match

From [Ray Fernando's `swiftui-animation-match`](https://github.com/RayFernando1337/rayfernando-skills/tree/main/plugins/swiftui-animation-match/skills/swiftui-animation-match). First catalog: [Shubham0812/SwiftUI-Animations](https://github.com/Shubham0812/SwiftUI-Animations).

Match a UI/UX interaction to proven SwiftUI animation patterns from curated open-source catalogs. Prefers system-first restraint before custom motion. Covers loaders, likes, toggles, card decks, reveals, and shaders.

## Review and quality

### code-review

From [Matt Pocock's `code-review`](https://github.com/mattpocock/skills/tree/main/skills/engineering/code-review). This copy uses the repository's GitHub tracker and does not require his setup skill.

Review changes since a fixed point (commit, branch, tag, or merge-base) on two axes, in parallel:

- **Standards:** does the code follow this repository's documented coding standards?
- **Spec:** does the code match the originating issue or spec?

### blast-radius

Original to this collection.

Change-impact and completion audit. Use before declaring wide, risky, cross-cutting, or merge-critical work complete. Inspects callers and contracts beyond the diff, identifies safety facts, exercises the real artifact, and reports what is cleared versus still risky.

### interrogate

Original to this collection.

Independent local multi-model review. Use when one reviewer is not enough: contested, security-sensitive, high-risk, or merge-critical plans and changes. Reviewers get the same intent and rubric. The lead aggregates consensus and disagreement without pretending that two runs of the same family are independent.

### running-bug-review-board

From [Ray Fernando's `running-bug-review-board`](https://github.com/RayFernando1337/rayfernando-skills/tree/main/plugins/running-bug-review-board/skills/running-bug-review-board). iOS simulator companions are credited in [ios-simulator-playbook.md](running-bug-review-board/references/ios-simulator-playbook.md).

Real-user QA for web or iOS/iPadOS apps. Runs manual test plans, UX bug hunts, build sign-off, bug filing, and triage. Produces P0/P1/P2 reports, a YES/NO phase verdict, tracker sync guidance, and an HTML dashboard. Interactive Bug Review Board triage stays in a separate session.

### technical-writing

Original to this collection. Rules cite [Diátaxis](https://diataxis.fr), the [Google developer documentation style guide](https://developers.google.com/style), [ASD-STE100](https://asd-ste100.org), and Kohl's *The Global English Style Guide*.

Layered writing standard for docs, RFCs, READMEs, PR descriptions, and commit messages: Diátaxis structure, Google developer style, STE instruction rules, and Global English syntax.

### writing-for-agents

From [Matt Pocock's `writing-for-agents`](https://github.com/mattpocock/skills/tree/main/skills/productivity/writing-for-agents).

How to write documents that agents consume: skills, `AGENTS.md`, `CLAUDE.md`, and context pointers. Companion: `SKILL-MECHANICS.md` for frontmatter, invocation, and router skills.

## Delivery

### github-delivery

Original to this collection.

GitHub-only delivery for branches, worktrees, issues, pull requests, checks, reviews, and merges. Uses `git`, `gh`, GitHub Actions, and GitHub Projects. Graphite and `gt` are disabled.

### resolving-merge-conflicts

From [Matt Pocock's `resolving-merge-conflicts`](https://github.com/mattpocock/skills/tree/main/skills/engineering/resolving-merge-conflicts).

Resolve an in-progress git merge or rebase conflict. Preserve both intents where possible, run the project's checks, and finish the merge or rebase. Do not abort.

### to-tickets

From [Matt Pocock's `to-tickets`](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-tickets). This copy keeps the repository's own tracker authoritative.

Break a plan, spec, or conversation into tracer-bullet tickets. Each ticket declares its blocking edges. Edges are text in one file per ticket locally, or native blocking links on a real tracker.

### handoff

From [Matt Pocock's `handoff`](https://github.com/mattpocock/skills/tree/main/skills/productivity/handoff).

Compact the current conversation into a handoff document so another agent can continue. Redacts secrets and personal data. Saves outside the workspace.

## Orchestration and research

### arena

Original to this collection.

Local multi-agent design or implementation competition. Use when several materially different solutions are plausible and selection quality matters. Creates isolated candidates, judges them against shared criteria, and lets the lead synthesize and verify the strongest result. No cloud agents.

### waves

From [Ray Fernando's `waves-codex`](https://github.com/RayFernando1337/rayfernando-skills/tree/main/plugins/waves-codex/skills/waves-codex). Run-shape triage and dependency-aware dispatch also credit [Phillip Chaffee's `deep-research` Cursor skill](https://github.com/PhillipChaffee/.cursor).

WAVES: Workers, Aggregate, Verify, Extend. Wave-based orchestration for bee-mode: the Fable manager decomposes and Grok workers run under Paseo. Decompose a large goal into independent slices, spawn a bounded parallel wave, collect evidence-backed handoffs, verify important claims, synthesize one deliverable, and start another wave only when warranted.

### research

From [Matt Pocock's `research`](https://github.com/mattpocock/skills/tree/main/skills/engineering/research).

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

Upstream: [korallis/skills-collection](https://github.com/korallis/skills-collection). This repository does not track it; changes are cherry-picked by hand.

## License

Original files and the Matt Pocock copies are MIT. See [LICENSE](LICENSE). Ray Fernando skills stay Apache License 2.0. See [licenses/APACHE-2.0.txt](licenses/APACHE-2.0.txt). Authors, URLs, and which license applies to each skill are in [NOTICE.md](NOTICE.md).
