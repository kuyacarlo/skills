# Cross-agent work queue (file-first)

Portable coordination for **agy / Cursor / Kiro / Claude / any CLI agent** without a
separate Taskboard server. Complements claim files and trees in the parent skill.

**Mental model:** restaurant ticket rail. One job per claim. Cooks do not grab the
same ticket. Pass with a note when done or blocked.

This is **not** personal life todos, internship trackers, or a SaaS kanban.

## When to use which layer

| Need | Use |
|------|-----|
| Who owns which paths / branches in one repo | Claim files + reconcile (`SKILL.md`) |
| Survive agent switch / brownout | `context-handoff` (+ per-agent `HANDOFF.md`) |
| Shared backlog of jobs across tools/sessions | **Work queue** (this file) |
| Live DAG, blocking ask/reply, supervise workers **inside Orca** | Orca orchestration skill (`orca skills get orchestration`) |
| Full ownership move to another worktree/agent without supervising a DAG | `orca-cli` handoff — not this queue |

Default: **file queue + claims**. Escalate to Orca only when you need runtime
waits, threaded ask/reply, or a coordinator loop that Orca already runs.

## Queue location

Prefer a **sibling** of the repo (same reason as `.coordination/`):

```
<workspace>/
├── <repo>/                 ← git project
└── .coordination/
    ├── …claim files…
    └── queue/
        ├── inbox/          ← unclaimed jobs (one .md per job)
        ├── claimed/        ← held by an agent (lease in frontmatter)
        ├── blocked/        ← waiting on human / external
        └── done/           ← finished (or delete after PR lands)
```

If a sibling path is impossible, `docs/agent-queue/` inside the repo is acceptable
for a solo project — accept the git noise.

## Job file shape

Filename: `YYYYMMDD-<short-slug>.md` or `<issue-or-id>-<short-slug>.md`.

```markdown
---
id: 20260810-fix-auth
status: inbox          # inbox | claimed | blocked | done
owner: null            # null | agy | cursor | kiro | claude | human | <name>
claim_token: null      # random string set on claim; required to mutate
lease_until: null      # ISO timestamp; expired → reclaimable as inbox
blocked_reason: null
---

# Title

## Goal
One sentence.

## Paths
Globs this job may edit. Claim these in the agent claim file too.

## Done when
- [ ] …

## Notes / artifacts
- …
```

## Protocol (every agent)

1. **Next** — pick oldest `inbox/` job whose `paths` do not collide with an active
   claim (or take the human-assigned owner hint).
2. **Claim** — move to `claimed/`, set `owner`, `claim_token`, `lease_until`
   (default 2–4h). Refuse if already claimed with a live lease.
3. **Work** — edit only claimed paths; measure git (parent skill), do not trust
   the job file alone.
4. **Comment** — append under Notes (what changed, PR URL, blockers).
5. **Done** — move to `done/` (or delete) when Done-when is true **and** git/PR
   evidence exists.
6. **Block / release / handoff** — `blocked/` + reason; or clear owner → `inbox/`
   with notes for the next agent; or set `owner` to the next tool and leave in
   `claimed/` / `inbox/` per human preference.

**Atomicity without a DB:** one agent updates one file; do not rewrite another
agent's claim_token. If `lease_until` is past, any agent may reclaim after
appending a "reclaimed expired lease" note.

## Optional CLI shim

If you want muscle memory later, wrap the same files:

```text
tb next [--owner agy]
tb claim <id> --owner agy
tb done <id> --token …
tb comment <id> --token … "…"
tb block <id> --token … --reason "…"
```

Implementation can stay a shell script over `queue/`. A HTTP board is optional
and out of scope for this skill.

## Orca supplement (short)

When the human is in Orca and asks to **supervise a multi-agent DAG**, use the
Orca orchestration skill — threaded messages, task dispatch, `worker_done` /
escalation waits, decision gates. Do **not** invent a fake Orca DAG in markdown.

When they only need "give this branch to another agent" without supervision, use
`orca-cli` handoff (see that skill), and leave a `context-handoff` / queue note so
non-Orca agents can still see state.

File queue and Orca can coexist: Orca runs the live turn; the queue/HANDOFF
files are what survive after Orca closes.

## Non-goals

- Replacing Linear / Todoist / ZenNotes / Google Tasks
- Multi-tenant SaaS, budgets, Paperclip org charts
- Running agents *inside* the queue (agents stay external CLIs/IDEs)
