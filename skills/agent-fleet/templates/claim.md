# <agent-name>

- **Status:** active | idle | stopped
- **Updated:** <ISO timestamp — and keep it honest, it is how others judge staleness>
- **Lane:** <the slice of work you own, in one sentence>
- **Worktree:** `<absolute path>` — `<branch>`

Read `decisions.md` from the top before acting. It is append-only, newest first,
and it overrides anything in this file.

## Claims

One row per path glob you are editing. **Claim before you edit, not after.**

| Path glob | Branch | Note |
|---|---|---|
| `src/foo/**` | `fix/123-thing` | Active. |
| `tests/foo/**` | `fix/123-thing` | New file. |

## Released — take these

| Path glob | Why |
|---|---|
| `src/bar/**` | Finished. <name>, it is yours. |

## Issues owned

Parent and children. Say which are done, which are in flight, which are not
started. **"Not started" is a valid and useful status — say it plainly.**

## Branches pushed

| Branch | PR | Commits beyond base | State |
|---|---|---|---|

**Measure this before writing it:**
`git rev-list --count origin/main..HEAD` — do not copy the last value forward.
A claim file that says "2 commits" while a subagent has 16 is how work gets
reassigned and lost.

## Subagents

If you run a sub-fleet, list it. Others do not need to coordinate with them, but
the orchestrator needs to know the work exists.

| Subagent worktree | Branch | Ticket |
|---|---|---|

## Blocked

What you cannot proceed on, and **who or what would unblock it**. Silence reads
as stalled; a named blocker reads as waiting.

## Notes for other agents

Landmines you found. Traps in the code or the machine. Corrections to specs.
This section is the highest-value part of the file — it is what survives you.

## Open questions

Things you need answered by a named agent or by the human. Say who.
