# HANDOFF — <agent-name>

- **Lane:** <what you own>
- **Worktree:** `<absolute path>` — `<branch>`
- **Written:** <ISO timestamp> by <who wrote it>

**Read `../decisions.md` from the top first.** It is append-only, newest first.
This file is a snapshot; that file is the law.

Written so that a replacement agent — or you after a blackout — can resume
without redoing anything. Assume the reader knows nothing and can see only git.

## Current truth about the environment

State anything that changed recently and contradicts older notes. Put it first,
because a stale "X is broken, hold your work" line stops a fresh agent cold.

## What I am doing right now

The specific ticket, the specific branch, the specific files. If work is
uncommitted, say exactly where it is and what state it is in.

## Done and pushed

| Branch | PR | State |
|---|---|---|

Distinguish **complete and verified** from **pushed but unproven**. Say which
test lanes you actually ran, and which could not run here.

## Problems you inherit

Numbered, most dangerous first. For each: what is wrong, what it blocks, and what
would clear it. Name the owner if it belongs to someone else.

## Next, in order

1. …
2. …

Order matters more than the list. Say why the first is first.

## Landmines

Traps that cost real time. Tooling quirks, misleading exit codes, files that must
not be touched, tests that look broken and are not. **Include the incident, not
just the rule** — "X is dangerous" is forgettable; "X destroyed 50 commits on
2026-07-28 because the worktree was nested inside another checkout" is not.

## Corrections to carry forward

Where the ticket, the spec, or an earlier document is wrong. Say what the shipped
code actually does and why it diverges. Without this, the next agent "fixes" your
deliberate decision back into a bug.
