# Smell IDs

Cite these on review. Fix a smell only if it is in the diff, blocks the task, or is a risk you
introduced. Otherwise report it.

| ID | Smell | Fix |
| --- | --- | --- |
| N1 | Name hides what the value is | Rename to the domain concept |
| N7 | Name hides a side effect | Put persist, delete, send, mutate in the name, or split command from query |
| F1 | Too many arguments | Bundle a missing type |
| F3 | Flag argument | Split into two functions |
| G5 | Duplicated knowledge | One home, if both copies must always change together |
| G14 | Feature envy | Move the behavior onto the data it uses |
| G16 | Obscured intent | Extract a named predicate or type |
| G17 | Misplaced responsibility | Put it in the unit that owns that job |
| G30 | Function does more than one thing | Split until the one-sentence test passes |
| G36 | Train wreck `a.b.c.d` | Ask the first object for the decision |
| C3 | Comment restates the code | Delete the comment or rename the code |
| C5 | Commented-out code | Delete it. Version control keeps it |
| T1 | Untested reachable behavior | Add a test at a public seam |
| T5 | Missing boundary case | Test the edge, not only the happy path |
