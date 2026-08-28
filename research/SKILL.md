---
name: research
description: Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. Use when the user wants a topic researched, docs or API facts gathered, or reading legwork delegated to a background agent.
---

Dispatch a **Grok worker** through Paseo to do the research (bee-mode read-heavy route: `paseo run --provider grok/grok-4.6 --env GROK_MEMORY=0 --env GROK_SUBAGENTS=0 -d`, web search on), so you keep working while it reads. Do not use a coordinator sub-agent.

Its job:

1. Investigate the question against **primary sources** (official docs, source code, specs, first-party APIs), not a secondary write-up of them. Follow every claim back to the source that owns it.
2. Write the findings to a single Markdown file, citing each claim's source.
3. Save it where the repo already keeps such notes; match the existing convention, and if there is none, put it somewhere sensible and say where.
