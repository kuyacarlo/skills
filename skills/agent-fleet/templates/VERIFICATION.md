# Verification contract

Fill this in ONCE per repository, before the first agent starts. Every agent
obeys it. Without it, each agent invents its own idea of "tested" and the fleet
reports green work that is broken.

Keep it in `.coordination/` beside the claim files.

---

## Lanes: what can and cannot run here

Be exact. "Probably works" is worse than "not runnable" — it produces false
green.

| Lane | Command | Runs here? |
|---|---|---|
| unit | `<exact command, incl. any env prefix>` | yes |
| integration | `<command>` | **no — needs <what>** |
| frontend | `<command>` | yes |
| mobile | `<command>` | **no — no toolchain** |
| lint | `<command>` | yes |
| types | `<command>` | yes |

**Structurally unavailable — do not plan around these:**

- <e.g. no database; the only credentials point at production>
- <e.g. no cloud CLI session>
- <e.g. no physical hardware>

State *why* for each. An agent that knows the reason will not waste a pass
rediscovering it.

## Exit-code traps

Tooling that lies about success. Add every one you find.

- `<cmd> | tail` reports `tail`'s exit code, not the command's. Never pipe when
  you need the status.
- `<coverage threshold in config>` makes every targeted run report failure even
  when the tests pass.
- `<import-time init in conftest>` causes whole files to be silently skipped
  without dummy env vars — a skipped file looks like a passing one.

## The rules every agent follows

**1. Red before green.** Prove the test fails against the unfixed code, then
passes with the fix. A test that never failed proves nothing. When the fix has a
self-correcting sibling branch, pin the branch that does NOT self-correct —
otherwise the test passes against broken code.

**2. Run the FULL affected suite, not just your own file.** The single most
common cause of a blocked review: N passing in a new file while N more break
elsewhere. Report before/after counts for every suite you touched, and diff the
failure NAME sets, not just the totals — equal counts can hide a swap.

**3. Distinguish pre-existing from introduced.** Run at the branch point too. If
failures are identical either side, say so and leave them alone. Do not fold
unrelated repairs into the fix; if you must repair one, put it in its own commit.

**4. Never claim "tested" for a lane that cannot run here.** Say exactly what you
could not verify and why: *"unit lane green; integration and mobile not runnable
in this environment — risk: X."* Silence and "tested" are both lies.

**5. Never weaken a guard to make a test pass.** If a new check breaks tests, fix
the tests' setup. Choose the option that leaves the guard armed for everything
you did not explicitly name.

**6. The orchestrator re-runs, it does not trust.** Self-reported results are a
claim like any other. Reproduce them independently before reporting them onward.

## Human gates

Things no agent can clear. List them explicitly so nobody burns a pass trying.

- <e.g. applying a migration to the live database>
- <e.g. confirming a production secret exists>
- <e.g. verifying behaviour on physical hardware>

When a change depends on one, put the exact query or command in the PR body and
hand it over. **Do not file tickets whose acceptance criteria require an agent to
do something structurally impossible here** — they can never be satisfied.
