# Engineering principles

- Start from the caller and the user-visible outcome. A component is useful only through the path
  that consumes it.
- Make boundaries earn their existence. Prefer cohesive modules and domain-shaped data over
  pass-through layers, temporal decomposition, and scattered primitive parameters.
- Use the type system to make invalid states difficult to represent. At boundaries, parse and
  validate untrusted data rather than asserting it into shape.
- Diagnose causes before treating symptoms. Encode durable lessons in types, tests, schemas,
  linters, or repository instructions when the recurring cost justifies it.
- Choose the smallest architectural lever that simplifies several downstream decisions. Avoid
  speculative abstraction and generality without a real second use.
- Keep shared state explicit, ownership singular, and operations idempotent where retries or
  concurrency are possible.
- Sequence work into independently verifiable units. One writer owns a branch or worktree; readers
  and reviewers may work concurrently.
- Protect context: give each agent a bounded objective and the evidence it needs, then aggregate at
  clear checkpoints.
- Optimize explanations and APIs for reader load. Names, contracts, and examples should let a new
  maintainer understand the normal path without reconstructing hidden assumptions.
- Prove the real artifact. Generated output, UI, migrations, integrations, and workflows need the
  checks that exercise what users will actually run.
