---
name: verification-before-completion
author: kaoru
version: "1.0.0"
description: "Final gate before saying work is done or a PR is ready. Proof is scoped to what this change owns — not \"all CI green.\" Use when finishing a task, marking ready for review, or ADHD completion dropout. Triggers on done, finished, ready for review, ship it, verify before complete, is this done."
---

# Verification before completion

Blocks the \"mark done at 90%\" habit. Also blocks the opposite failure: waiting
forever for a red check that is not yours.

Aligns with `engineering-rulebook` Proof + \"A red check is not a signal until you
measure it.\" This skill is the short interrupt at the end of a task.

## Default gate (usually enough)

Before you say **done** or mark a PR **ready**:

1. **Local hooks** — pre-commit / pre-push for this repo ran clean on the
   commits you are shipping (or you have an explicit user waiver).
2. **Your lane** — targeted tests or checks for files you touched are green.
3. **User-visible proof** — if the change has a runtime surface, you observed it
   (or stated \"unverified, risk: …\").
4. **Scope honesty** — Known whole-repo failures, fixes-in-flight elsewhere, or
   baseline-red CI are named, not treated as your exit blocker.

You do **not** need every remote workflow green as the baseline for \"done.\"

## What is *not* required

| Noise | Why it is not your gate |
|-------|-------------------------|
| Pre-existing red CI at branch point | Quote baseline; your job is not to inherit the world |
| Fix already owned on another branch/PR | Point at it; do not block on it |
| Jobs that cannot pass (dead runner, billing freeze) | Noise — name and move (`engineering-rulebook`) |
| Unrelated suites you did not affect | Prefer affected / targeted runs |
| \"All checks\" when path filters skip half the matrix | Verify what should have run |

## Checklist (copy into PR or handoff)

```markdown
## Verification
- [ ] Pre-commit / local gate: pass (or waived: …)
- [ ] Targeted proof for this change: …
- [ ] Observed user-visible result / or unverified risk: …
- [ ] Baseline red (not mine): … @ <sha> — matching?
- [ ] In-flight fixes elsewhere (do not block): …
```

Tick only what applies. Empty \"baseline red\" is fine when CI is clean.

## How to decide \"done\"

| Situation | Verdict |
|-----------|---------|
| Local gate + your lane green; remote has known baseline red | **Done / ready** — document baseline |
| Local gate fails on your files | **Not done** |
| Fix for the red is already on the way (other PR/issue) | **Done** for *this* change; link the tracker |
| You cannot run the real surface | **Done with risk** — say unverified, do not claim tested |
| Only unit tests, consumer path untested | Prefer end-of-chain assert; else flag gap |

## Anti-patterns

- Holding a PR in draft until the entire org CI matrix is green.
- Claiming \"tested\" on a lane you did not run.
- Weakening a guard so a test passes.
- Treating equal failure *counts* as equal failure *sets* — diff names.

## Related

- `engineering-rulebook` — proof rules, baseline quoting, silent failure
- `branch-lifecycle` — done includes merge + branch cleanup
- `specification-compliance` — SPEC drift when behavior changed
- `continuous-improvement` — record what the gate taught you
