# Notes distilled from gbkel's Clean Architecture notes

Source notes:
[guilhermebkel/gbkel-notes — Clean Architecture](https://github.com/guilhermebkel/gbkel-notes/blob/main/books/clean-architecture-a-craftsmans-guide-to-software-structure-and-design.md).
Those notes are a reader's summary of Robert C. Martin's *Clean Architecture* (2017). This file
turns them into agent rules. It is not a reprint of the book.

Load this file for architecture work. Load [`architecture.md`](architecture.md) for the full
Dependency Rule, SOLID as dependency rules, and component metrics.

## Goal

Minimize the human effort required to build and maintain the system. If that effort stays low
across releases, the design is good. If each release costs more than the last, the design is bad.

Leave as many decisions unmade as you can, for as long as you can. Architecture is shape-agnostic
where that keeps options open. Language paradigm is not required; wrap what you use.

## What a good architecture supports

1. **Use cases.** A shopping-cart system looks like a shopping-cart system. Names at the top
   of the tree say what the system does, not which framework it uses.
2. **Operation.** Isolation of components must survive a later split into threads, processes,
   or services. Do not hard-code the communication mechanism.
3. **Maintenance.** A small requirement produces a small diff.
4. **Development.** Independent teams can work without colliding. Conway's law: the design
   copies the org chart unless you draw boundaries on purpose.
5. **Deployment.** Prefer one action to ship, not a pile of scripts.

## Circles (Dependency Rule)

Source dependencies point only inward, toward higher-level policy.

```
Entities                 # enterprise business rules
Use cases                # application business rules
Interface adapters       # controllers, gateways, presenters
Frameworks and drivers   # devices, web, UI, database, vendors
```

Five properties of this shape:

- Independent of frameworks. Frameworks are tools, not a way of life.
- Testable without UI, database, or web server.
- Independent of the UI.
- Independent of the database.
- Independent of any external agency.

## Entities and use cases

- An **entity** holds critical business rules and the data they operate on. Those rules would
  exist if the business ran on paper. Example: a loan with principal, rate, period, and
  `makePayment` / `applyInterest` / `chargeLateFee`.
- A **use case** holds application-specific rules that only exist because the work is automated.
  Example: create-customer requires a unique email. Use cases orchestrate entities. Entities
  do not know about use cases.

Use cases and entities accept and return data they understand. Do not pass a framework request
object, a database row, or an ORM type inward.

## SOLID, as operating checks

- **SRP.** A module answers to one actor. Split Picture vs User vs Plan at the large scale,
  PictureUpload vs UserAccount at the small scale.
- **OCP.** A simple new requirement should add code, not rewrite old code. If it forces a
  massive change, the hierarchy is wrong. Protect higher-level components from lower-level
  change.
- **LSP.** Callers must not know which implementation they have. Swap Dropbox vs S3 behind
  one upload interface. Do not grow if/else on vendor names.
- **ISP.** Depend only on the methods you use. A create-customer use case sees Create, not
  Update and Delete.
- **DIP.** Source dependencies refer to abstractions, not volatile concretions.
  1. Do not refer to volatile concrete classes.
  2. Do not derive from them.
  3. Do not override concrete functions; add a new implementation.
  4. Do not mention the name of anything concrete and volatile; wrap it.

## Components

A component is the smallest independently deployable unit. Classes in a component belong
together. Version a reused component.

**Cohesion**

- **CCP.** Gather classes that change for the same reasons at the same times.
- **CRP.** Do not force users to depend on things they do not need. Classes reused together
  live together.

**Coupling**

- **ADP.** No cycles in the component graph. Dependencies run from higher-level policy toward
  lower-level details, never the reverse.
- **SDP.** Depend in the direction of stability.
- **SAP.** A component is as abstract as it is stable. Dependencies run toward abstraction.

## Boundaries

Draw a boundary where one side must not know the other: GUI vs business rules, database vs
business rules. Early boundaries exist to keep deferred decisions out of the core. Communication
across a boundary uses interfaces. That is plugin architecture: GUI and database plug into
business rules, not the reverse.

A full boundary is expensive. A partial boundary (interfaces in one deployable, or a facade)
holds a place when the cost of a full split is not yet justified. Know that a partial boundary
erodes without enforcement.

`main` constructs and starts the system. Treat `main` as a plugin. Prefer a separate `main` per
configuration rather than config branches inside policy.

## Services

A service is a function call across a process or platform boundary. It does not automatically
decouple you.

- **Decoupling fallacy.** Shared records still couple services. Add a field and every service
  that touches the record changes.
- **Independent-deploy fallacy.** Large systems have been built as monoliths and as component
  systems. Services are not the only path to independent teams.

Keep components isolated in one address space until a service boundary is forced. Do not treat
a process split as an architectural boundary.

## Checks before you edit

- Wrap a vendor library in an adapter. Do not import it into policy.
- Do not merge two similar use cases because they look the same today. Wait until they must
  always change together.
- Do not pass a row structure, request object, or ORM type inward.
- Name packages after the domain (screaming architecture).
- If a new import points outward, invert it: interface on the inner side, implementation outside.
