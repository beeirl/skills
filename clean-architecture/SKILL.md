---
name: clean-architecture
description: Clean Architecture. Enforce the Dependency Rule. Use when adding a file, import, module, package, layer, dependency, framework, database, HTTP client, or use case, or when deciding where code belongs.
---

# Clean Architecture

Mandatory when the change adds a dependency or crosses a module boundary. Repository layering
wins where it is declared. Do not explain the book. Apply the rule. Pair with `architect` for
a new shape and with `clean-code` for the lines inside a unit.

Circles and SOLID checks: [`references/circles.md`](references/circles.md).

## Before you add a file or import

1. Name which circle the change belongs to: entity, use case, interface adapter, or
   framework/driver.
2. Find two similar artifacts and put the new file next to them, with the same registration.
3. For every new import, ask: does this name something in an outer circle? If yes, invert it.
   Declare the interface on the inner side. Implement it outside.

## Enforce these rules

| Rule | You must |
| --- | --- |
| Dependency Rule | Source dependencies point only inward, toward policy. Inner code never names an outer type, function, annotation, or data format. |
| Policy vs detail | Database, HTTP, UI, and frameworks are details. Business rules do not import them. |
| Entities vs use cases | Entities hold rules that would exist on paper. Use cases hold automated application rules. Use cases depend on entities, never the reverse. |
| Data across a boundary | Pass inner-shaped values. No request objects, ORM rows, result sets, or framework types inward. Copy fields even when they overlap. |
| Vendor wrap | Import a third-party library only inside an adapter you own. |
| Screaming architecture | Top-level names say the domain (billing, matter, intake), not the framework (Next, Rails, Spring). |
| Accidental duplication | Do not merge two use cases because they look the same today. Merge only if they must always change together. |
| `main` | Construction, config, and framework binding live in `main` or an equivalent composition root. Policy does not `new` volatile concretions. |
| Services | A process split is not a boundary. Shared records still couple services. Keep components isolated in one address space until a service is forced. |

## Forbidden in the diff

- A controller or route handler importing a repository, ORM, or SQL helper when a use case
  should sit between them.
- A domain module importing a web framework, database driver, or mailer.
- A new `utils` / `helpers` package used as a home for mixed layers.
- A `_v2` module beside the original.

If the project has a layer map, run `scripts/check_boundaries.py --root .` when Python is
available. Otherwise read every import you added and name its circle.

## Done

Do not claim the change is finished until:

- [ ] Every new file sits in the circle that owns that job and is fully wired in.
- [ ] Every new import points inward, or you named the inversion you used.
- [ ] No outer-circle type appears in inner-circle code.
- [ ] Vendor types are confined to an adapter.
- [ ] You ran the boundary check, or you named exactly what was not run.
