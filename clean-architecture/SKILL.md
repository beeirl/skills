---
name: clean-architecture
description: Use when adding a dependency, creating or crossing a layer or module boundary, deciding where a file belongs across layers, adopting a framework or database, starting a new project structure, or auditing architectural drift. Covers the Dependency Rule, policy versus detail, SOLID as dependency rules, component cohesion and coupling, Humble Object, and packaging.
license: MIT
metadata:
  source: "https://github.com/btseee/clean-code-skills"
---

# Clean Architecture

Source: [btseee/clean-code-skills](https://github.com/btseee/clean-code-skills) v3.0.0. MIT.
Copyright (c) 2026 Battseren Badral. Code-level rules live in `clean-code`.

Architecture is the lines *between* units: which way dependencies cross, and what a change costs.

Read [`references/architecture.md`](references/architecture.md) before adding a dependency, a
layer, a framework, or a database. Use [`references/architecture-map.md`](references/architecture-map.md)
when you know the question and need the governing rule.

## Load project context

1. Read `.clean/architecture.md` if it exists. Declared layers win over instinct.
2. Read `.clean/decisions.md` and `.clean/ledger.md` if they exist. Do not re-open a recorded decision.
3. Read the project's own architecture docs. Project instructions outrank this skill.
4. If no layer declaration exists, work from the code and offer to write one from
   [`references/architecture-template.md`](references/architecture-template.md).

## The Dependency Rule

Source-code dependencies point only inward, toward higher-level policies. Nothing in an inner
circle may name anything in an outer circle: not a class, function, variable, annotation, or
data format.

Before every new import, ask: which direction does this line cross, and why?

- **Level is distance from I/O**, not call order. Business rules are highest level. Database,
  web, UI, and framework are details.
- **Policy must not name a detail.** When policy needs a detail, declare the interface on the
  policy side and implement it outside.
- **Confine details.** SQL, ORM types, HTTP objects, and framework base classes stay in the
  outer layer. Copy fields into inner-shaped structures at the boundary.
- **`main` is the dirtiest component.** Wiring, config, and framework binding live there.
- **Keep the component graph acyclic.** Break a cycle by inverting a dependency or extracting a
  shared component.

If `.clean/architecture.md` exists, check it with
`scripts/check_boundaries.py --root .`. If Python is unavailable, read the imports of every
changed file and ask which layer each name belongs to.

## Placement

1. Find two or three similar artifacts and mirror their directory, naming, and registration.
2. Put domain rules in domain modules, I/O in adapters, orchestration in use cases.
3. Wire the file completely: imports, exports, routes, DI, build config. An unreferenced file
   is dead code.
4. Do not grow `utils`, `helpers`, `common`, or `misc` without naming the domain concept.
5. Never create `_v2`, `_new`, `_final`, or date-suffixed siblings. Edit the original.

## One job per unit

Describe the unit's job in one sentence without "and", "also", or "then". If you cannot, extract
a collaborator. Route new behavior to the owner of that responsibility, not the file that is open.

SRP at module scale: ask which *actor* can demand this change. Code answering to different actors
belongs in different modules even when it looks identical today.

## When to add a boundary

Do not add a boundary you cannot justify now. Implement one at the inflection point where the
cost of building it drops below the cost of going without it. Prefer compile-time enforcement
over discipline.

## Workflows

| Situation | Follow |
| --- | --- |
| New project or major module | [`references/new-project.md`](references/new-project.md) |
| Whole-project or module-wide cleanup | [`references/project-refactor.md`](references/project-refactor.md) |
| Ordinary feature or fix | `clean-code` surgical mode, then this skill for any new dependency |

## Failure modes

- Shortest-path wiring: a controller calling a repository and skipping the layer that owns
  authorization.
- Detail leaking inward: an ORM type or HTTP object in a business rule.
- Framework as architecture: directories named after the stack, not the domain.
- Eager deduplication across actor boundaries.
- A process split (microservices) treated as an architectural boundary.

## Done

- Every new dependency points inward.
- No outer-circle name appears in inner-circle code.
- New files sit in the conventional layer and are fully wired.
- Boundary checks ran, or you named exactly what was not run.
