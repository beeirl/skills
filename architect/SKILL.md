---
name: architect
description: Architecture-first workflow for non-trivial or high-risk software changes. Use when a plan or implementation crosses modules, introduces domain concepts, changes contracts, or risks shallow layering. Grounds designs in callers, data structures, signatures, and repository evidence before implementation.
---

# Architect

Design from the real system, then implement against the chosen shape.

## Ground the design

1. Read the entry points, callers, contracts, tests, persistence boundaries, and adjacent modules.
2. State the user-visible outcome, invariants, constraints, and facts still unknown.
3. Map the existing data flow before proposing new abstractions.

## Produce candidates

For non-trivial or high-risk work, produce at least two genuinely different designs when local
concurrency is available. Otherwise produce one design and one explicit alternative. Each candidate
must show:

- the caller-facing usage;
- types and primary data structures;
- important function or method signatures;
- module ownership and dependencies;
- state transitions, errors, and boundary validation;
- migration and verification strategy;
- tradeoffs and rejected complexity.

Screen out pass-through modules, information leakage, temporal decomposition, hidden shared state,
and abstractions with no real second use.

## Decide and implement

Compare candidates against repository constraints and the simplest complete user path. Select a
design explicitly, then implement in coherent vertical slices. If repeated implementation deviations
are needed, treat that as evidence that the design is wrong and redesign instead of accumulating
exceptions.

End with the chosen contracts, module map, implementation sequence, verification evidence, and
remaining risks.
