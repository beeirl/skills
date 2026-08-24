# Source

This skill enforces the **method** Lauren Tan describes as Dune architecture,
not a Dune package. No public Dune repository or specification was found.

Primary sources:

- Lauren Tan, Maven workshop (12 August 2026), chapter "Implementing Strict CI
  Constraints and the Dune Architecture" at 00:41:00.
  https://maven.com/p/e23d9c/how-cursor-turned-ai-agents-into-better-engineers#t=2460
- Lauren Tan, public posts on Dune as an in-house agent-friendly React
  framework, mechanical CI, and the architecture-then-CI-then-skills correction
  ladder (`poteto`).
- [pstack public principles](https://github.com/cursor/plugins/tree/main/pstack/skills):
  model the domain, boundary discipline, minimise reader load, type-system
  discipline, idempotent operations.
- Matilda OS `docs/audit/typescript-refactor-plan.md` §8, the worked
  application of that method: capability folders, explicit public module
  contracts, one data owner, and mechanically enforced boundaries.

The skill is original packaging. It is not Dune source, a pstack copy, or a
Matilda module dump.
