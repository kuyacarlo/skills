---
name: branch-lifecycle
author: kaoru
version: "1.0.0"
description: "Close the loop on a git branch: start → work → PR → merge → cleanup. Use when opening a feature branch, auditing stale WIP, finishing a PR, or after merge when local/remote branches and worktrees linger. Triggers on branch lifecycle, stale branch, delete branch, finish the PR, WIP audit, close the loop."
---

# Branch lifecycle

Stops ADHD WIP accumulation. A branch is not “in progress forever” — it ends in
merge + cleanup, or an explicit park/abandon note.

Pairs with `context-handoff` (first file on the branch) and `operations`
(commits, signing). Does not replace `agent-fleet` claims; those are assertions,
git is fact.

## Arc

```
1. Start     checkout -b from fresh base; HANDOFF.md first
2. Work      small commits; keep Next ≤3 in handoff
3. Open      push; PR with summary + test plan
4. Land      merge (squash/rebase per repo); never force-push main
5. Close     delete remote + local branch; prune worktree; drop HANDOFF
```

Skip a step only with a written reason in handoff or the PR body.

## Start

1. `git fetch` and branch from up-to-date base (`master` / `main`).
2. Name: `feat/`, `fix/`, or `chore/` + short slug.
3. Write `HANDOFF.md` before implementation commits (`context-handoff`).
4. If fleet/queue job: claim first, then branch (`agent-fleet`).

## Work → open

1. Commit in logical units (`operations`). Sign; never `--no-verify` unless asked.
2. Before push: run the **local** gate the repo actually uses (see
   `verification-before-completion`) — usually pre-commit / targeted tests, not
   “full remote CI must be imaginary-green.”
3. Open PR. Link issue. Say what is *your* proof vs known red baseline
   (`engineering-rulebook`).

## Land → close

After merge (or explicit abandon):

| Clean up | Command / action |
|----------|------------------|
| Remote branch | delete with merge (gh) or `git push origin --delete <branch>` |
| Local branch | checkout base; `git pull`; `git branch -d <branch>` |
| Worktree | `git worktree remove` if used |
| Handoff | delete branch-local `HANDOFF.md` with the branch |
| Claim / queue | mark done or release lease (`agent-fleet`) |
| Stale tracking | `git fetch --prune` |

Do not leave “merged but still checked out” as the default resting state.

## WIP audit (periodic)

When the user asks, or session start finds many local branches:

1. List local branches older than ~7 days (or never pushed).
2. For each: merged? open PR? zero commits past base? → say that plainly.
3. Propose ≤3 actions: merge/close PR, delete, or park with one-line reason in
   handoff. Do not mass-delete without confirmation.

A branch with a claim and **zero commits beyond base** is not started
(`agent-fleet`). Say that — do not invent a progress percentage.

## Done means closed

“Done” for branch work = merged (or abandoned) **and** cleanup above. Code on a
long-lived personal branch with no PR is not closed.
