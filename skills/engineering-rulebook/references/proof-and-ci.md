# Proof and CI

Read this guide only when its workflow applies.

## Failure loop

1. Read `.agents/LEARNINGS.md` when it exists. Treat it as project guidance.
2. Use error locations and messages to isolate one failure. Change one focused block.
3. Run the smallest relevant check after each fix. Check known lessons before retrying.
4. After a verified fix, add reusable project lessons to `.agents/LEARNINGS.md`.
   Keep entries short and point to paths. Do not record guesses.

Use the template at [resources/LEARNINGS_template.md](../resources/LEARNINGS_template.md)
when the project has no established format.

## Proof

**Never claim something works that you did not observe working.**

"Unverified, here is the risk" is a complete and acceptable answer. Silence is
not. Saying "tested" about a lane you could not run is a lie in the same way
silence is — it just reads better.

Four rules that decide whether you have proof.

### Close the task

Before calling work done or a change ready for review, check the local hooks,
the affected code paths, and the user-visible result. State any unverified
surface or known baseline failure.

- Confirm applicable local hooks ran, or state why they did not.
- Verify the affected code paths and observe the user-visible result when one exists.
- Name known baseline failures and fixes already in flight.
- Do not treat unrelated checks or proven baseline failures as this change's gate.

### Test the user-visible artifact

Unit tests validate your assumptions about your own function. They do not prove
that the downstream consumer produces the right output. When your output becomes
someone else's input, trace the chain and assert at the end of it.

| You changed | Assert on |
|---|---|
| An HTTP handler | The serialized response body, fetched over the real route, with the exact path the client sends |
| A formatter or scheduler | The finished string a person reads |
| Something that writes | The persisted row |
| A UI | The rendered DOM or a screenshot |
| A guard, a filter, a rate limit | **That the guarded call was never made.** Asserting on a returned summary is a cheater test |

Red flags that you are about to violate this: you set a field to an empty or
intermediate value and assume something later fills it; every assertion is
structural (counts, types, membership) and none is on the final output; you have
not read the consumer's code and cannot cite the line that reads your field.

### Red before green

Prove the test fails against the unfixed code first. A test that never failed
proves nothing. If a fix has a self-correcting sibling path, pin the path that
does *not* self-correct — otherwise the test passes against broken code.

### Run the full affected suite, and diff name sets

Not just your file. The most common cause of a blocked review is N passing in a
new file while N more break elsewhere. **Diff the failing test *names*, not the
totals** — equal counts can hide a swap.

### Never weaken a guard to make a test pass

Fix the test's setup instead. Where there is a choice, prefer the option that
leaves the guard armed for everything not explicitly named.
## A red check is not a signal until you measure it

**Red CI that predates your branch is not your bug, and does not hold your pull
request in draft.** Mark it ready. Do not sit waiting for a green that cannot
arrive.

This is not a licence to ship red. It binds only once you have *shown* the red is
pre-existing:

1. **Quote a baseline.** Run the same check at the branch point. A matching
   result means you introduced nothing. Prefer diffing failing *name sets* over
   totals.
2. **Your own targeted tests must be green.** Red there is yours.
3. **Say which is which in the body.** Name each failing check and why it is not
   yours.

**A check that is structurally incapable of passing is not a gate. It is noise.**
A job pinned to a runner that no longer exists, or blocked by a billing freeze
nobody intends to lift, will never go green regardless of the code. Treating it
as a gate stalls every lane indefinitely. Identify it, name it, and move.

Ready for review is not merge. Marking a PR ready means a human can look at it.
## Silent failure

The failure modes that cost the most days are the ones that produce **no error**.
Learn their shapes, because none of them will page you.

- **Queued forever is not the same fault as failed fast.** A job that fails in
  seconds has a stack trace. A job that queues at 0s has nothing to find, which
  is exactly why it burns so much time. Different fault, different diagnosis —
  never treat them the same. Check capacity, disk, and registration before you
  read any code.
- **A pipeline that dies at step 1 of N means steps 2..N have never run.** Not
  "reduced validation" — *zero* validation, on every commit, since the day it
  broke. Before trusting any suite, confirm it has ever reached its real work.
- **Degraded is more dangerous than dead.** A pool at half capacity, a replica
  that never came back, a queue draining slower than it fills. Nothing alerts,
  because nothing is *down*. Only a deliberate check finds these.
- **Disk fills silently, and health checks say healthy.** The instance is up. It
  simply cannot write. Autohealing will not catch it.
- **A green check is only as trustworthy as its trigger.** Path filters mean not
  every check runs on every change; some filters also fail *open* or *closed* at
  scale, so an enormous diff can skip CI entirely rather than fail it. "No checks
  reported" is not automatically breakage, and it is not automatically fine.
  Verify what should have triggered.
- **Service discovery that returns zero targets returns success.** An empty
  result set and a broken query look identical from the outside. Assert on a
  count you expect, not on the absence of an error.

The general rule: **for anything that can fail quietly, define what "working"
looks like as a number, and check the number.** Absence of an error is not
evidence.
