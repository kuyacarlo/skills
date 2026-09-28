---
name: feature-plan
description: >-
  Turn a non-trivial feature request into a scoped project plan, branch, and
  durable handoff using the repository's own conventions. Use when starting
  implementation, creating a feature handoff, or continuing a planned workstream.
---

# Feature plan

Use the target repository's instructions and documentation as the source of truth.
Do not impose a branch, issue, or documentation scheme that conflicts with them.

## Workflow

1. Read the repository `AGENTS.md` and the project roadmap or equivalent overview.
   Check the current branch, worktree list, and `git status`; preserve unrelated work.
2. For planning-only requests, return a concise scope, milestones, risks, and done
   criteria. Do not create branches or files unless the user asked to start work.
3. For implementation requests, identify the smallest reviewable deliverable and
   its relevant issue or parent task when one already exists. Do not create or
   update external issues unless the user explicitly asks.
4. Create a branch from the repository's documented base branch. Use its naming
   convention; if none exists, use `feat/<short-slug>` for product work and
   `docs/<short-slug>` for documentation-only work.
5. Write or update the project's required handoff before implementation. Prefer
   its template and directory. If none exists, use `docs/handoffs/YYYY-MM-DD-
   <slug>.md` with the headings in [handoff-template.md](references/handoff-template.md).
   Update an index only when the repository maintains one.
6. Keep the work scoped to the agreed feature. Update the handoff as meaningful
   units ship; record open work and the actual verification performed.
7. Commit only when the user authorized commits or repository instructions
   authorize them. Never push, publish, merge, or message people unless explicitly
   authorized.

## Handoff quality

State the current behavior, intended outcome, changed paths, known limitations,
follow-up work, verification commands, and observable done criteria. Keep it
specific enough for another contributor to continue without repeating discovery.

Do not treat a handoff as a replacement for living product documentation. Keep
roadmaps, onboarding, architecture, and runbooks accurate at their source.
