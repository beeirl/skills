# Local model evidence — 2026-08-24

This dated evidence register informs, but does not override,
[`model-routing.md`](model-routing.md). Recheck live model IDs, account controls, and representative
repository performance before changing a route default.

## Evidence method

The research used three evidence streams for their separate purposes:

1. concrete community reports that identify a task, artifact, failure, correction, latency, or cost;
2. the same bounded self-assessment prompt run through each installed CLI; and
3. first-party documentation and actual account/CLI state for hard route facts such as model
   identity, tool support, retention, and account controls.

Only the first two form subjective task-fit hypotheses. Community feedback and self-assessment never
establish a provider, model ID, context limit, retention term, or zero-data-retention status. Only current authoritative
documentation and the actual account configuration establish those facts.

## Shared observed failure modes

Across the installed routes, community reports and self-assessments repeatedly identified:

- invented or stale APIs without primary documentation;
- scope creep and overengineering on broad prompts;
- premature completion claims without running the real artifact;
- instruction and context drift in long sessions;
- shallow self-review and agreement bias; and
- weak concurrency, operations, or UI conclusions without a reproducible runtime path.

## Community-informed hypotheses

These are not permanent rankings or dispatch rules.

| Family or route | Strengths worth testing | Recurring weaknesses to guard against |
| --- | --- | --- |
| GPT/Codex, especially GPT-5.6 Sol | Complete implementation, edge cases, difficult debugging, long tool-driven tasks, and orchestration. | Latency, token use, overengineering, prioritization drift, and weaker visual judgment without a browser artifact. |
| Claude Code, especially Opus | Architecture critique, repository comprehension, technical prose, and thoughtful implementation. | Scope creep, blocking questions, invented infrastructure, false completion, high usage, and inconsistent self-review. |
| Grok Build 4.6 | Fast implementation scrutiny, tool use, debugging, value, and an adversarial perspective. | False assumptions, lost instructions, uneven edge-case correctness, and variable latency or token use. |
| Cursor Composer | Fast edit-run-fix loops, routine implementation, and low-cost exploration. | Persistent-rule drift, tangents, context sensitivity, and accidental duplication of the primary writer. |
| Gemini | Multimodal or UI work, large-context exploration, and fast implementation. | Incomplete runs, rabbit holes, awkward prose, semantic drift, and weaker pure architecture or logic without corroboration. |
| Kimi | Long-context exploration and bounded frontend, backend, or implementation candidates. | Shallow verification, style/context drift, overloaded service behavior, expense, and hype that exceeds reproducible evidence. |
| GLM | Literal bounded implementation, long-context comparison, and inexpensive research candidates. | Lower trust for critical judgment, slower runs, API invention, and weaker runtime verification. |

Lower-cost models and reasoning levels are preferred when a bounded repository evaluation shows that
they meet the same evidence bar. Reasoning level is not an independent model family.

## Installed CLI self-assessments

The same bounded prompt was run through the locally installed Codex, Claude Code, Grok Build, and
Cursor routes for Composer, Gemini, Kimi, and GLM. The common self-reported best case was bounded
implementation or debugging with a real tool loop and executable acceptance criteria. The common
self-reported weak cases were invented APIs, scope drift, false completion, long-context drift, and
sole reliance on self-review.

Treat these statements as admissions about likely failure modes, not proof of capability. Exact
checkpoint identity was not always knowable from model text; use CLI/catalog output and provider
documentation instead.

## Contract forward test

The coordinator/supervisor/specialist/worker contract was tested against Matilda issue #5, a
high-risk native release and rollback proof. Reviewers received fixed file hashes, read-only scope,
and distinct lenses. Initial reviews found real defects in route authority, writer leases, complete
untracked-file snapshots, lifecycle states, context handoffs, and fail-closed independent review.
Those findings changed the normative contract.

On the corrected packet, GPT harness reviewers, Claude Opus, Gemini 3.7 Flash, Kimi K3, and GLM-5.2
returned usable passing receipts for their assigned lenses. Grok 4.6 twice returned setup/progress
text without a review receipt, and Composer 2.5 produced no final receipt before termination on the
last run. These results describe this policy-review task only; they are negative routing evidence,
not a general model ranking.

## Community sources

- GPT/Codex: [GPT-5.6 impressions](https://www.reddit.com/r/codex/comments/1uue8ad/so_what_do_we_think_of_gpt_56/),
  [overengineering discussion](https://www.reddit.com/r/codex/comments/1uuo6x4/how_to_keep_gpt56_sol_high_from_overengineering/),
  and [coding-task comparison](https://www.reddit.com/r/ClaudeCode/comments/1t0xrad/gpt55_vs_gpt54_vs_opus_47_on_56_real_coding_tasks/)
- Claude: [Opus 5 feedback thread](https://www.reddit.com/r/ClaudeCode/comments/1va445h/opus_5_feedback_megathread/)
  and [mixed coding experience](https://www.reddit.com/r/ClaudeAI/comments/1v7b1u1/opus_5_is_an_incredible_coder_and_really_painful/)
- Grok and Cursor: [Grok 4.6 versus GPT-5.6 Sol](https://www.reddit.com/r/cursor/comments/1vo8ogp/i_compared_grok_46_and_gpt_56_sol/),
  [Grok 4.6 experience](https://www.reddit.com/r/cursor/comments/1vmibtf/grok_46_amazing/),
  [Composer praise](https://forum.cursor.com/t/praise-for-cursor-composer-2-5/162448), and
  [Composer failure report](https://forum.cursor.com/t/omg-these-agents-are-like-children-running-with-scissors/162552)
- Gemini: [Gemini 3.7 Flash feedback](https://www.reddit.com/r/GeminiAI/comments/1vr8fja/so_do_you_like_37_flash_would_love_to_know_your/)
- Kimi and GLM: [Kimi K3 field reports](https://www.reddit.com/r/LocalLLaMA/comments/1uymonq/does_k3_really_live_up_to_the_hype_real_world/),
  [GLM comparison](https://www.reddit.com/r/LocalLLM/comments/1ur67j3/is_glm_52_worth_using_instead_of_opus_48gpt55/),
  and [GLM community release discussion](https://www.reddit.com/r/LocalLLaMA/comments/1u7kcwf/zaiorgglm52_is_here/)

## Provider sources for hard constraints

- [OpenAI model catalog](https://developers.openai.com/api/docs/models) and
  [latest-model guidance](https://developers.openai.com/api/docs/guides/latest-model)
- [Anthropic model overview](https://platform.claude.com/docs/en/about-claude/models/overview) and
  [model selection](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)
- [xAI Grok 4.6](https://docs.x.ai/developers/grok-4-6) and
  [Grok Build instruction discovery](https://docs.x.ai/build/features/skills-plugins-marketplaces)
- [Google Gemini model guidance](https://ai.google.dev/gemini-api/docs/latest-model)
- [Cursor CLI rules](https://prod.cursor.com/docs/cli/using) and
  [Cursor model catalog](https://cursor.com/docs/models-and-pricing)
- [Kimi model catalog](https://platform.kimi.ai/) and
  [Kimi K3 announcement](https://forum.moonshot.ai/t/kimi-k3-is-here-our-most-capable-model/480)
- [Z.ai GLM-5.2 announcement](https://z.ai/blog/glm-5.2)
