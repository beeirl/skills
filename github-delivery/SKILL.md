---
name: github-delivery
description: GitHub-only delivery workflow for planning branches, worktrees, issues, pull requests, checks, reviews, and merges. Use whenever software work may affect Git or GitHub. Replaces Graphite and other stack managers with plain git, gh, GitHub Actions, Projects, and repository merge policy.
---

# Github Delivery

GitHub is the source of truth for issues, pull requests, checks, project state, and merges. Use plain
`git`, `gh`, GitHub Actions, and GitHub Projects. Do not use Graphite, `gt`, Graphite metadata,
Graphite bases, or Graphite merge queues.

## Plan branches and worktrees

1. Inspect repository instructions, status, remotes, default branch, existing worktrees, and open PRs.
2. Preserve user changes. Create a separate worktree when current work overlaps or must remain
   untouched.
3. Prefer one small, independently verifiable unit per branch and PR.
4. Prefer independent PRs based on the default branch. If a true dependency requires a stack, use
   ordinary GitHub base branches, document the dependency, and keep one writer per branch/worktree.
5. After a parent merges, retarget and rebase or update every child against the new default branch;
   verify each child independently.

## Deliver through GitHub

1. Link the issue or project item required by repository policy.
2. Before pushing, run relevant tests, formatting, type checks, builds, and artifact verification.
3. Create or update the PR with `gh`. Record acceptance criteria, observed validation, dependencies,
   and closing keywords required by the repository.
4. Treat required GitHub checks and review policy as hard gates. Never merge a conflicted, stale, or
   failing head.
5. When the user has explicitly authorized shipping, merge using the repository's GitHub-native
   merge method or auto-merge. Otherwise stop at a verified, reviewable state.
6. Remove obsolete dependency bases after migration, but never force-push the default branch.

Activation of this skill authorizes no external write by itself. Read-only inspection is safe;
pushing, creating or editing issues/PRs, merging, or deleting branches must already be within the
user's request.
