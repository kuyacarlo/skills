---
name: context-handoff
author: kaoru
version: "1.0.0"
description: "Structured handoff when switching agents (agy, Cursor, Kiro) or pausing a branch. First file on a new feature branch is HANDOFF.md. Use when starting a branch, mid-task agent switch, brownout/restart risk, or \"hand this off\". Triggers on handoff, HANDOFF.md, switch agent, continue this branch, context loss."
---

# Context Handoff

Stops context evaporating across agy / Cursor / Kiro / session restarts.

## When

1. **First commit on a new feature branch** — write `HANDOFF.md` (or `docs/handoff/<branch>.md`) before code.
2. **Agent switch** — update the same file before the other agent starts.
3. **Pause / brownout / token limit** — refresh Status + Next before exit.

## File location

Prefer repo root `HANDOFF.md` on the feature branch (branch-local; do not merge to main unless asked). Alternate: `docs/handoffs/<short-name>.md` if the repo already uses `docs/`.

## Template (copy)

```markdown
# Handoff — <short-name>

## Goal
One sentence. Link issue/SPEC if any.

## Branch
`<feat/...>` from `<base>` @ `<sha-or-date>`

## Status
- Done:
- In progress:
- Not started:

## Constraints
Stack, non-goals, “do not touch” paths.

## Next (≤3 micro-steps)
1.
2.
3.

## Artifacts
Paths, PR URL, commands to run.

## Agent notes
Owner last session: agy | cursor | kiro | human
Model/effort if relevant. Open questions.
```

## Rules

1. Handoff **before** implementation commits on a fresh branch.
2. Keep Next to **≤3** steps (ADHD-friendly).
3. Do not paste secrets. Point to Infisical / env names only.
4. Incoming agent: read HANDOFF.md + `git status` + last commit; do not re-litigate Goal.
5. On PR merge: delete branch-local HANDOFF with the branch (or move a summary into the PR body).

## Related skills

- `agent-fleet` — multi-agent claims, trees, and file work queue
  (`references/work-queue.md`); use handoff *inside* a claimed job or branch
- `branch-lifecycle` — start → PR → merge → cleanup (handoff dies with branch)
- `verification-before-completion` — scoped done-gate before “ready”
- `operations` — session start/end, commit discipline
- `specification-pipeline` — SPEC before big features
- `personal-context` — identity / stack defaults (local context files)
- Orca orchestration — live DAG / supervise only when inside Orca; otherwise
  prefer agent-fleet files + this handoff
