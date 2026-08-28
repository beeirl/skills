---
name: waves
description: WAVES - Workers, Aggregate, Verify, Extend - wave-based orchestration for bee-mode. Fable plans; Grok workers run under Paseo. Decompose a big goal into independent slices, verify coverage, dispatch Grok workers in parallel as a bounded wave, collect evidence-backed handoffs, verify important claims, synthesize one deliverable, and extend into another wave only when warranted. Bounded by design to avoid runaway token loops; invoke deliberately. Formerly waves-codex; also fan out, parallelize, spin up multiple agents, orchestrate workers, multi-stream research, audit a repo, split disjoint implementation work.
---

# WAVES — Workers · Aggregate · Verify · Extend (bee-mode)

Run **wave-based orchestration** with Grok workers dispatched through Paseo. A **wave** is a bounded
round of isolated workers in parallel, then a round that verifies what came back,
then a deliberate decision to build on it — not an open-ended loop. Use this skill
when a task is too broad for one clean linear pass but can be split into
independent slices. You are the manager: discover the problem shape, stage and
verify coverage, decompose it, dispatch bounded Grok workers, collect one structured
handoff from each worker, verify important claims, and synthesize the final
deliverable.

**The shape of every wave — WAVE:** Workers fan out across disjoint slices ->
Aggregate their handoffs -> Verify the evidence (the moat) -> Extend into another
wave only when warranted. A loop doesn't know when to stop; a wave does, because
verification is the stop function. (Invoke deliberately - a run spawns more agents
than usual.)

Dispatch surface (bee-mode, checked 2026-08-28 against Paseo 0.6.1 and Grok CLI 1.0.5): the
manager is the Paseo `claude` agent on `claude-fable-5`. Each worker is one Paseo agent:

```bash
paseo run --provider grok/grok-4.6 --cwd <repo> --new-workspace worktree \
  --env GROK_MEMORY=0 -d --json --title "wave-1/<slice>" "<self-contained worker prompt>"
paseo wait <id>                # block only when synthesis needs it
paseo logs <id> --json         # collect the handoff
paseo stop <id>                # budget or scope breach
```

Read-only slices add `--env GROK_SUBAGENTS=0` and may drop `--new-workspace`. A fixed-artifact
verifier slice can instead use `bee-grok-review` (one turn, no tools, Grok 4.6 low effort). Workers
never spawn their own workers; the manager runs every wave. The concurrency bound is the number of
Paseo agents you can verify at once (default 4 per wave). Grok's effort is not settable per
`paseo run`; the default in `~/.grok/config.toml` applies, and `bee-grok --reasoning-effort` sets it
for a direct launch. Every Paseo-dispatched Grok agent, `bee-grok`, and `bee-grok-review` draw from
one Grok capacity pool; read `bee-mode/references/capacity-routing.md` before each wave.

Read these references when using the skill:

- `references/handoff-format.md` for the exact worker handoff contract.
- `references/verification.md` for verification gates and verifier-worker
  playbooks.
- `references/examples.md` for decomposition recipes.
- `references/recommended-config.md` for Grok and Paseo configuration.
- `references/adaptation-notes.md` for the Cursor-to-Codex and Codex-to-Paseo translation notes.

## When to Use

- The user explicitly asks to use multiple agents, subagents, parallel workers,
  fan-out, or orchestration.
- The task splits into independent slices: data ranges, research streams,
  repo modules, audit dimensions, verification rows, or disjoint code ownership.
- The main value is speed, context hygiene, and verification discipline: keep
  noisy exploration out of the manager thread, then check the claims that matter.
- A second or third wave may be useful after first-wave handoffs expose gaps,
  conflicts, narrowed scope, or high-stakes claims needing verification.

## When to Skip

- The task is small, linear, or easy to do locally.
- The slices require constant cross-talk or shared mutable decisions.
- The next action is blocked on one immediate investigation; do that locally.
- Parallel code edits would overlap heavily and no worktree/isolation strategy is
  available.

## Core Principles

1. The manager plans, verifies, and synthesizes. Workers do heavy reading,
   research, tests, audits, bounded edits, or focused claim checks.
2. Worker prompts are self-contained. Do not assume workers can infer the user's
   original request, your scratch reasoning, or sibling work unless you
   intentionally pass that context. A Paseo-dispatched Grok worker starts with an
   empty context: it sees only its prompt, the checkout, and the skills on disk.
3. One worker owns one slice and returns one handoff.
4. Verify before you trust. A worker's `Status: success` is a claim, not
   evidence.
5. Parallel reads are the default safe case.
6. Parallel writes require disjoint ownership or isolated worktrees. Use
   `--new-workspace worktree` for every writing worker; one writer per checkout
   (the writer lease in `bee-mode/references/model-routing.md`). Write conflicts
   are still a coordination problem at merge time.
7. Continuous motion (within the stated budget). Handoffs reveal new work; treat
   each open question or suggested follow-up as a candidate second-wave task and
   spawn it. Keep going until every slice is terminal and the synthesis is
   complete -- stopping early while genuine follow-ups remain is the failure
   mode this skill guards against. (The manifest plus the stated budget is the
   stop function; see "Bounded Waves.")
8. Decomposition is entropy reduction. A vague goal is high-entropy: many
   plausible plans still fit. Shrink that space -- dig locally, then pull from
   attached resources, then ask the user only if it pays -- before you slice it.
   See "Entropy-First Decomposition."

## Bounded Waves - Size, Budget, and the Stop Function

A wave is bounded on purpose - but bounded by **completion and budget, not by a
wave count**. Unbounded "loop-until-done" burns tokens for little gain:
candidate generation is cheap, selection plateaus, and extra rounds are
non-monotonic (more iterations can lower quality, not just cost). Equally real
is the opposite failure: stopping while the manifest still has open slices.
Keep the exploration, drop the runaway, never abandon un-terminal work.

- Width: 3-8 workers per wave, and no more Paseo agents than you can fully
  verify (default 4; batch wider waves). Go wider only with a cheap automatic
  check (tests, `paseo run --output-schema`, schema/exec) gating results.
  (Grounding: homogeneous-agent teams plateau around N~4-8 - added workers
  contribute redundant evidence, and diversity, not head count, escapes the
  ceiling - arXiv 2606.02646, 2602.03794.)
- Depth: the manifest is the stop function. Keep extending while any manifest
  slice is non-terminal AND the last wave added verified progress. Stop only on
  one of three conditions: completion (every slice terminal, synthesis done),
  stagnation (nothing new + outputs near-duplicate the last wave, or a quality
  drop), or budget exhaustion. State the budget up front in the run-shape line
  - a worker or token budget, not a wave count (e.g. `budget: ~20 workers`). A
  realistic run is often `12 + 3 + 1` workers across three waves, and a
  decomposition cascade on a vague goal legitimately runs more. (Grounding:
  verification-driven replan loops stop on completeness thresholds, diminishing
  returns, and token budgets, not fixed iteration caps - VMAO, arXiv
  2603.11445; convergence-based stopping beats fixed `max_iterations` at parity
  quality - arXiv 2606.27009.)
- Scouting is cheap - don't let it eat the budget. Entropy-reduction waves
  (scouting, decomposition) run on cheap models/low effort and count separately
  from the execution budget. Never end a run "out of waves" when the budget was
  consumed by discovery before execution started.
- Budget ~60% generation / 40% verification; selection is the scarce resource.
- Match width to difficulty: easy -> 1 + light refine; medium -> 3-5;
  hard/open-ended -> 5-8 for diversity; hardest/novel -> escalate reasoning/model,
  don't loop.
- Anti-poisoning: carry only a distilled, verified handoff (winner + short
  critique) into the next wave, never raw transcripts or losing candidates.
  Exception: constraints are pinned, never summarized - the manifest, stop
  conditions/budget, and safety/scope rules travel verbatim through every
  synthesis and compaction (compaction measurably drops in-context constraints;
  arXiv 2606.22528).

Loop-until-done is justified only when ALL hold: a cheap reliable ~ground-truth
verifier exists; the signal is crisp/actionable (a failing test, not "try
harder"); each iteration shows measurable progress; easy-medium difficulty; still
hard-capped. Fits code-with-tests/exec-feedback; misfits open-ended
research/writing/design.

## Entropy-First Decomposition

Before you fan out, treat the goal as an entropy-reduction problem: shrink how
many plausible interpretations and plans still fit what you know. A vague,
high-entropy request ("build a Flappy Bird game", "make my app faster") does not
slice cleanly yet -- reduce the uncertainty first, then decompose the
low-entropy version. Name what is uncertain, because the two kinds resolve
differently:

- Specification uncertainty -- what the user wants (ambiguous goal, missing
  acceptance criteria, unstated constraints). Resolve by stating an explicit
  assumption and proceeding, or -- only when a wrong guess is expensive -- by
  asking.
- Environment / knowledge uncertainty -- facts you do not have yet but can get
  (repo shape, schema, API behavior, current docs, data size). Resolve by
  gathering, not by asking.

Spend the cheapest action that buys the most certainty first -- an
information-gain ladder -- and aim each probe at the unknown whose answer
eliminates the most plans (the highest-information question splits the
surviving interpretations roughly in half):

1. Dig locally first (cheap): inspect local state in the manager thread (list,
   read schema/README, grep, sample data). This is Step 0; it often collapses
   most of the uncertainty for free.
2. Then pull from attached resources: if local state lacks the answer, spawn a
   small scouting wave of read-only Grok workers to fetch it (docs, MCP, web)
   at low or medium effort (see Step 2).
3. Ask the user last, and only when it pays: when residual specification
   uncertainty is high and a question's expected information gain beats its cost.
   Most requests carry enough to proceed on a stated assumption.

Then cascade: one request becomes a decomposition wave (understand -> locate
unknowns -> draft the plan) -> verify -> an execution wave that builds the
subtasks least-to-most (each verified result lowering uncertainty for the next),
with more scouting sub-waves wherever entropy stays high. Track the living plan
in the bee-mode task ledger; stop reducing when entropy is low enough to act -- the
verification gate doubles as "is the uncertainty low enough to commit?" (Worked
example: `references/examples.md`.)

## The Loop

Track the run in the bee-mode task ledger (the coordinator's durable plan surface)
whenever the workflow has more than a couple of moving parts, and give every Paseo
agent a `--title` that names its wave and slice.

### Step 0 - Discover Serially

Do not fan out blind. First inspect enough local state to learn the natural
shape of the work:

- List directories or data sources.
- Read schemas, manifests, READMEs, package boundaries, or route maps.
- Sample representative records/files.
- Count rows, files, modules, routes, messages, or scope size.
- Identify likely independent slices and risky overlap.

This manager-side discovery prevents duplicate worker scopes, blind spots, and
mis-sized chunks.

### Step 0.5 - Stage and Verify Coverage

Paseo-dispatched Grok workers get Grok's own tools, MCP servers, and skills, plus
the checkout, so remote or messy data does not always need to be staged first. Still stage
data when it reduces risk or repeated work:

- Export remote/database data once if credentials, rate limits, or query cost
  would make every worker redo the same setup.
- Normalize noisy inputs once: strip wrappers, binary blobs, boilerplate, and
  irrelevant logs.
- Pre-chunk huge corpora into exact per-worker files or ranges.
- Keep one scratch dir per run (e.g. `.waves/<run>/` with `staging/`,
  `handoffs/`, `synthesis-wave-N.md`) so prompts cite paths instead of
  pasting content and later waves re-read files, not chat history.

Then run a pre-fan-out gate:

- Total rows, files, messages, modules, routes, or records.
- One line per slice with ID/range/path/date bounds and item count.
- Partition-sum check: slice counts add back to the total.
- Duplicate/gap check: no overlapping ranges, missing IDs, bad sort, or empty
  chunks.
- Central fix-and-recheck if any anomaly appears.

This serial prep is often the largest phase. The parallel fan-out is fast once
inputs are clean and coverage is proven.

### Step 1 - Decompose into Independent Slices

Size the run itself first, out loud: weigh breadth (how many independent
slices), depth (reasoning per slice), ambiguity (see "Entropy-First
Decomposition"), and stakes (this sets verification tiers), then state the
chosen shape in one line before spawning -- e.g. `Run shape: one wave, 4
workers; second wave only if handoffs expose gaps.` On the fence between two
shapes, pick the smaller and say so. If no wave is needed, do the task in the
manager thread and say that -- never present inline work as wave coverage.

Choose the split axis that gives each worker clear ownership:

- Data chunks: disjoint ID ranges, date ranges, files, or CSV rows.
- Workstreams: separate technologies, product areas, research questions.
- Repo modules: non-overlapping path sets or package boundaries.
- Audit dimensions: security, performance, correctness, tests, maintainability.
- Verification rows: one claim, citation group, or metric per verifier task.
- Code edits: disjoint file/module ownership, preferably in worktrees for
  heavier changes.

For a large wave, usually 5 or more workers, state the decomposition plan and
the pre-fan-out coverage gate to the user before spawning so they can redirect
cheaply.

Respect the concurrency bound (default 4 Paseo agents per wave). If you need
more slices than that, batch them into waves.

Then triage each slice on three axes (classify-and-act): the **worker role**
(table in Step 2), its **dependencies** (which slices it needs verified output
from -- most have none; a real dependency edge is what separates waves), and a
**verification tier** - `auto-accept` (low-stakes, corroborated) ->
`single verifier` -> `multi-model/multi-pass panel` (high-stakes) -> `debate`
(contested, no ground truth). Spend verification where a wrong claim is expensive,
not uniformly.

Record the triage as a **wave manifest** - one row per slice (`slice | scope |
role | effort | depends_on | verification tier`), written to the plan or
`.waves/<run>/manifest.md` before spawning. `depends_on` defines the wave
boundaries: a wave is every not-yet-run slice whose dependencies are all met,
and a dependency is met only when its handoff has been **verified** (Step 3),
not merely returned. Launch wave 1 (no dependencies) in parallel; launch each
dependent slice with the distilled, verified findings (or their
`.waves/<run>/` path) folded into its self-contained prompt, and keep
unrelated slices parallel. The manifest doubles as the **completion gate**: N
rows spawned means N handoffs collected and checked off before synthesis
(Step 3). It is also the **spawn-plan audit**: review it before dispatch, and keep
each worker prompt in `.waves/<run>/prompts/<slice>.md` so it can be inspected later.

### Step 2 - Fan Out with Paseo-Dispatched Grok Workers

Dispatch all workers whose dependencies are met (handoffs verified, not just
returned) back to back with `paseo run ... -d --json`, record each returned
agent ID in the manifest, then continue manager-side work and `paseo wait` only
when synthesis is blocked.

Pick the smallest capable role and state it in the prompt:

| Slice | Worker shape | Notes |
| --- | --- | --- |
| Read-heavy code/data exploration | Grok 4.6, read-only packet, `--env GROK_SUBAGENTS=0`, no worktree | Low or medium effort. Ask for evidence and counts, not edits. |
| General research, docs, MCP/web work | Grok 4.6, read-only packet | Workers inherit Grok's MCP servers and web search. |
| Implementation or fixes | Grok 4.6, `--new-workspace worktree --new-branch wave/<slice>` | Explicit file/module ownership; one writer per worktree. |
| Review/security/test-risk audit | `bee-grok-review` on a fixed artifact, or a read-only Paseo worker | Different family from the Fable manager, so it also satisfies the independent-review gate. |
| Browser/UI investigation | Grok 4.6 with browser MCP configured | Ask for evidence, not broad edits. |
| Verification of important claims | `bee-grok-review` with claim + cited sources | No generator reasoning, no authorship labels. |
| Many row-shaped tasks | One `paseo run` per row, batched to the concurrency bound | Use `--output-schema` for machine-readable results. |

Inline the role's instructions in every worker prompt; there is no role registry
to fall back on, and a missing role is not permission to skip it.

Model and effort routing: `grok-4.6` is the only worker model (`grok-4.5` is a
same-pool fallback, not a cheaper tier). Effort comes from `~/.grok/config.toml`
for Paseo dispatches and from `--reasoning-effort` on `bee-grok`; use `low` or
`medium` for scouting and research, `high` for implementation and verification.
The Fable manager keeps orchestration, deep problem solving, and pre-fan-out
synthesis; do not delegate those. **Verify what actually ran**: read the model
and mode from `paseo inspect <id>` rather than trusting the requested settings.
Honor any model or effort the user named; if it is unavailable, say so rather
than substituting.

### Step 3 - Collect and Verify Handoffs

Paseo tracks every worker: `paseo ls` shows status, `paseo wait <id>` blocks
until idle, `paseo logs <id> --json` returns the transcript, and
`paseo send <id> "<message>"` re-tasks a worker in place.

**Completion gate first:** check every handoff off against the wave manifest -
N spawned means N accounted for. A worker that never returns, errors out, or
comes back `partial`/`blocked` is a hole in the wave. **Worker failure
ladder:** (1) re-task once, narrower -- `paseo send <id>` when the slice just
needs continuation, or re-spawn fresh with a narrower scope and a
note about what came back. Re-task the same worker only for continuation of
its own slice -- it keeps its prior context, which contaminates an unrelated
assignment; (2) if it fails again, do that slice in the manager thread; (3) if
it stays blocked, carry the slice into the synthesis explicitly as
`not-covered` - never average over a missing slice as if coverage were
complete.

Avoid manual polling loops. Continue non-overlapping local work while workers
run; wait only when synthesis is blocked on their results. For each handoff:

- Check `Status`.
- Check `Coverage` against the assigned slice.
- Extract `Key findings`, evidence, confidence tags, and source paths/URLs.
- Preserve `Sources` and `Confidence & verification`.
- Treat each `Open questions` and `Suggested follow-ups` bullet as a candidate
  second-wave task: accept, reject, or consolidate it. Spawning a focused
  follow-up wave for real gaps is the normal path, not an exception.
- Reconcile contradictions across workers before presenting claims as settled.

Run cheap checks on every important finding:

- Evidence is present.
- Cited path/URL/range resolves.
- Evidence actually supports the claim.
- Scope matches the assigned slice.
- Headline counts can be re-counted from source.
- Confidence labels are preserved.

Accept only evidence-backed, scope-correct, non-contradicted findings. Demote,
re-task, or verify the rest. Then **compress at the barrier**: write the
distilled synthesis to `.waves/<run>/synthesis-wave-N.md` and work from that
file - next-wave prompts cite paths, never re-paste raw handoffs. Pin the
constraints through the compression: the manifest, stop conditions/budget, and
safety/scope rules are copied verbatim into every synthesis file, never
paraphrased (see "Bounded Waves" anti-poisoning note).

### Step 3.5 - Spawn Verifier Passes When Needed

Verification is the manager's highest-leverage job: checking a claim is usually
cheaper than generating it, and unchecked errors compound across waves.

Use a dedicated verifier when a claim is high-stakes, contested, surprising,
citation-heavy, single-sourced, or low-confidence. Give the verifier:

- The atomic claim.
- The cited source paths/URLs/commands.
- The acceptance question.
- No generator reasoning, and no authorship labels (judges favor output marked
  as their own; blind them).

The verifier returns `supported`, `partly-supported`, `unsupported`, or
`source-not-found` per claim. For many claims, run one `bee-grok-review` or
`paseo run --output-schema` per claim, batched to the concurrency bound.

### Step 4 - Second Waves (continuous motion)

Multi-wave is the normal shape, not an exception: a realistic run is often
`12 + 3 + 1` workers across three waves rather than one giant burst. Spawn
another wave whenever first-wave handoffs expose:

- Missing coverage.
- Conflicting findings.
- A specialized follow-up that was out of scope.
- A verification task that can run while you synthesize.
- A dependent manifest slice whose `depends_on` handoffs just verified.
- A bounded implementation task after research converged.
- A new user request that narrows or redirects the scope.

Repeat until no slice is pending and nothing new surfaces, within the stated
budget (see "Bounded Waves" - the manifest is the stop function, not a wave
count). Skipping a follow-up wave is legitimate in exactly three cases -- name
which one applies when you decide: the remaining open items are
**primary-source-verified** (a verifier can't improve on the evidence),
**time-gated** (unresolvable until an external event; carry them as explicit
open items), or **genuinely contested** (independent quality sources disagree;
record the disagreement instead of sampling more).

Sequential second and third waves are dispatched by the manager and are
encouraged. Workers do not spawn workers: pass `--env GROK_SUBAGENTS=0` to
read-only packets and keep implementation workers to their own slice.

### Step 5 - Deliver One Synthesized Artifact

Do not forward raw handoffs as the final answer. Produce the user's requested
artifact: report, roadmap, code patch, audit, decision memo, or implementation
plan. Cite worker evidence when it helps, especially file paths, line numbers,
data ranges, URLs, and unresolved uncertainties. Carry confidence into the final
output: `verified`, `single-sourced`, or `unverified`. Never turn a
low-confidence handoff into a confident sentence.

If implementation is required after the research wave, either:

- Make the edits yourself in the manager thread after reading all handoffs.
- Spawn a bounded implementation wave with disjoint file ownership.
- Use one `paseo run --new-workspace worktree` per attempt for heavier parallel
  code work.

Verify the deliverable itself:

- Run tests, validators, `curl`, screenshots, parsers, or smoke checks as
  appropriate.
- Regression-check sibling routes/files touched by the work.
- Re-read or grep critical files you wrote before relying on them.
- For generated artifacts, prefer a deterministic validator script or schema.

## Worker Prompt Contract

Every worker prompt includes:

1. Overall goal as context only.
2. The worker's exact slice and ownership.
3. Where to look: paths, data ranges, URLs, MCP/docs sources, commands, or repo
   modules.
4. Coverage rule: read the assigned slice completely when feasible, report
   counts read such as `388/388`, and call out skipped files/ranges.
5. Evidence rule: cite-or-drop every important claim, tag confidence
   (`high|med|low`), and say what would change the conclusion.
6. What not to do: avoid owning the whole task, avoid sibling scopes, avoid
   editing unless explicitly assigned.
7. The required handoff format from `references/handoff-format.md` - and keep
   it a digest: roughly 15 findings max with one-line evidence each; large
   artifacts (tables, logs, full lists) go to a file, cite the path.

End every worker prompt with the copy-paste ending for its worker type
(generic, research, implementation, or verifier) from
`references/handoff-format.md` § "Prompt endings per worker type".

## Row-Shaped Fan-Out

When the work is naturally one row per worker (files, incidents, packages, PRs,
migration targets, messages, customer records, or claims to verify):

- Write `rows.csv` with a stable `id` column and enough per-row context for a
  self-contained prompt.
- Render one prompt per row from a template and dispatch one `paseo run` per
  row, batched to the concurrency bound; pass `--output-schema` when downstream
  synthesis needs machine-readable results.
- Collect each result with `paseo logs <id> --json` into `.waves/<run>/rows/`.

For a verifier pass, build `claims.csv` with `claim_id`, `claim`, `sources`,
`acceptance_question`, and optional `stakes`. Require JSON fields: `verdict`,
`evidence`, `source_status`, `correction`, `confidence`, and `gaps`.

## Generate-and-Filter and Tournaments

For open-ended ideation or "produce the single best X", generate several
candidates and filter rather than trusting one attempt:

- Cheap filter first: gate candidates through a near-ground-truth check (tests,
  `paseo run --output-schema`, schema/exec, dedup/clustering) before spending
  judge tokens. Generation is cheap; judging is not.
- Selection ladder, not all-pairs: dedup/cluster -> shortlist -> pairwise-judge
  only among finalists. A naive O(N^2) tournament wastes tokens on also-rans.
- Competing implementations: one `paseo run --new-workspace worktree` per
  attempt (see the `arena` skill), then inspect/test/merge the winner.
- Budget check: at equal cost, k independent attempts plus a majority vote or
  cheap filter usually beats critique/debate loops -- benchmark any iterative
  loop against that baseline before paying for it.

## Parallel Writes

Grok workers are a good fit for parallel write work when each one has its own
Paseo worktree or disjoint ownership. Still treat write coordination as a real
merge problem:

- Read/research/test/log analysis: safe default.
- Disjoint edits in one checkout: acceptable only when ownership is explicit,
  paths do not overlap, and the writer lease is recorded.
- Overlapping edits: avoid. Have workers propose handoffs, then implement
  serially.
- Competing implementations: one `paseo run --new-workspace worktree` per
  attempt.
- Always inspect and test the merged result in the manager thread.

## Verification Surfaces

Use these where they fit:

- Tests, validators, type checks, linters, browser checks, and direct source
  recounts are the strongest verification signals.
- `bee-grok-review` is the dedicated verifier: fixed artifact, one turn, no
  tools, different model family from the Fable manager.
- `paseo run --output-schema` gives machine-readable verification results.
- `interrogate` runs a multi-reviewer panel with consensus tagging for
  contested or high-stakes claims.

## Escalating Beyond One Interactive Session

Use this skill for interactive, bounded fan-out inside one bee-mode task. For
long-horizon work, Paseo agents are durable: workers survive the manager's
session, `paseo ls` lists them, `paseo attach <id>` reopens one, and
`paseo schedule` runs recurring waves. Keep the same handoff discipline: never
pull a full worker transcript into the manager; collect the structured handoff.
Title workers consistently and track them in the manifest, archive them
(`paseo archive <id>`) when merged.

## Checklist

- [ ] Tracked multi-wave work in the task ledger and titled every Paseo agent.
- [ ] Discovered the shape of the problem before decomposing.
- [ ] Reduced entropy before slicing (dug locally -> pulled from attached
      resources -> asked the user only if it paid); sliced the low-entropy goal.
- [ ] Stated the run shape AND the budget (workers/tokens, not a wave count)
      in one line before spawning (on the fence -> the smaller shape); never
      presented inline work as wave coverage.
- [ ] Staged or normalized inputs when it materially helps.
- [ ] Verified coverage before spawning: counts, bounds, partition-sum,
      gaps/duplicates.
- [ ] Slices are independent (or their `depends_on` edges recorded) and sized
      to the concurrency bound.
- [ ] Wrote the wave manifest (slice / role / effort / depends_on /
      verification tier) before spawning; launched dependent slices only after
      their dependencies' handoffs were verified; checked every row off at
      collection (completion gate); ran the failure ladder on missing/blocked
      slices.
- [ ] Each worker prompt is self-contained and ends with the handoff contract.
- [ ] Picked read-only worker, implementation worker in a worktree,
      `bee-grok-review`, or row-shaped fan-out deliberately.
- [ ] Ran scouting / read-heavy waves at low or medium effort; used high effort
      for implementation and verification; kept orchestration and synthesis in
      the Fable manager.
- [ ] Avoided manual polling loops; waited only when synthesis was blocked.
- [ ] Read every handoff and resolved conflicts.
- [ ] Preserved per-finding confidence labels.
- [ ] Carried only distilled, verified syntheses between waves (no raw
      transcripts or losing candidates); pinned the manifest, stop conditions,
      and budget verbatim through every synthesis/compaction.
- [ ] Treated each open question / follow-up bullet as a candidate second-wave
      task; spawned waves for the ones that change the deliverable, coverage,
      or confidence; stopped only on completion, stagnation, or budget -- and
      named which of the three no-second-wave cases applied when skipping a
      follow-up.
- [ ] Verified high-stakes, conflicting, low-confidence, or uncited findings
      before synthesizing.
- [ ] Verified the final deliverable: re-ran/validated and re-read critical
      writes.
- [ ] Produced one synthesized deliverable.
- [ ] For edits, verified disjoint ownership or used worktrees.
