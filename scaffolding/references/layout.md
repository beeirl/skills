# Capability-folder layout

## New repository

```text
repo/
├── apps/
│   └── staff-web/          # composition root: authenticate, parse, invoke, render
├── modules/
│   ├── auth/               # one durable kind per folder
│   ├── matters/
│   └── work/
├── tooling/                # architecture checks, generators
└── pnpm-workspace.yaml     # or the repo's existing workspace file
```

This is a modular monolith. Do not split processes until a network boundary is
forced. Follow the repo's existing names if it already uses this shape.

## Public surface

```text
modules/work/
├── package.json            # name, exports: { ".": "./src/index.ts" }
├── src/index.ts            # the only external import surface
├── test/work.test.ts       # asserting contract tests through that surface
└── tsconfig.json
```

`public.ts` at the module root is the same contract under another name. Pick the
name the repo already uses.

Inside the module, relative imports are fine. Across modules, use the package
name.

## Internals to create only when the slice uses them

| Folder | When it exists |
| --- | --- |
| `src/model/` | Types, invariants, state machines that do not belong on the public file yet |
| `src/commands/` | State-changing use cases that have outgrown `src/index.ts` |
| `src/queries/` | Read use cases that have outgrown `src/index.ts` |
| `src/ui/` | UI this domain owns |
| `src/jobs/` | Retryable handlers this domain owns |
| `src/db/` | Owned tables, SQL, mapping |
| `evals/` | Task evals this domain owns |

Do not create a folder to hold a future file.

## Ownership questions

Answer these before `mkdir`:

1. What durable value is this the writer for?
2. Which existing module already writes that value?
3. Can this slice be one new file in that module?
4. What is the public command or query a caller will type?
5. Which files will a test import in this slice?

If (2) has an answer, do not create a package. If (5) is empty, you are
scaffolding inventory.

## Apps

A route, CLI, or worker may:

- resolve the caller
- parse untrusted input into a domain type
- call one module command or query
- map the result into view-model copy and render it

It may not:

- query another module's tables
- import a provider SDK
- duplicate a domain rule that already lives in a module
