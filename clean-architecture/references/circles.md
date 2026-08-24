# Circles and SOLID

Innermost to outermost. Dependencies point inward.

1. **Entities** — enterprise rules. Would exist with no software.
2. **Use cases** — application rules. Orchestrate entities. Do not know delivery.
3. **Interface adapters** — controllers, presenters, gateways. All SQL stays here.
4. **Frameworks and drivers** — web, UI, database, devices, vendor SDKs.

## SOLID as import checks

| Principle | Fail if |
| --- | --- |
| SRP | One module changes for two different actors |
| OCP | A small new requirement edits many existing files |
| LSP | A caller must know which implementation it has |
| ISP | A use case depends on methods it never calls |
| DIP | Policy names a volatile concrete class |

## Adapter

Policy calls an interface it owns. The outer circle implements it. Control flow can run outward.
The source import still points inward.
