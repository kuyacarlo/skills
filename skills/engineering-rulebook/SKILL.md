---
name: engineering-rulebook
author: kaoru
version: "1.0.0"
description: >-
  Use before changing infrastructure, CI/CD, a deploy, a live system, or anything
  whose blast radius you have not measured — and before reporting that a change
  works. Answers "am I allowed to just do this, or does a human have to decide?",
  "what counts as proof?", "this check is red, is that mine?", "is this safe to
  run against prod?". Also use when a session teaches you something durable, to
  route the lesson to the right home and write it in the same change. Triggers on
  "can I just try it", "do I need approval", "is it safe to", "CI is red", "the
  check failed", "did that actually work", "tested it", "ready or draft",
  "deploy", "promote to prod", "rollback", "migration", "spin up a VM", "change
  it on the box", "hotfix", "update the skill", "we should remember this",
  "lesson learned", "that cost me an hour". Covers the three red lines,
  experiment→document→script→PR, skill upkeep and routing, proof discipline,
  red-CI baselines, silent failure modes, live-change and promotion order.
---

# Engineering Rulebook

The rules that hold whatever you are touching — a cloud project, a CI pipeline, a
deploy, a database migration, a running box. Domain rulebooks live in each repo
and carry the local detail. This file carries the part that does not change when
the repo changes.

Read the spine. Then find the repo's own rulebook for the plumbing.

## The default is: try it

**You are allowed to mess up.** Experiment. Break a VM. Get the firewall rule
wrong. Delete the thing and make it again.

This is not a formality. Infrastructure nobody is willing to touch rots, and
asking permission for every change costs more than the mistakes do. Most cloud
and CI mistakes are recoverable in minutes and cost less than the meeting that
would have prevented them.

Three exceptions. They are narrow on purpose.

## The three red lines

A change needs a human decision before you make it if any of these is true.

### 🔴 1. It notifies people

Anything that can send a page, a chat message, an email, a push notification, or
a customer-facing message.

**Test: if this misbehaves, does a human's phone buzz? If yes, it is not an
experiment.**

Rolling back does not un-send a message. Waking the on-call at 3am, or messaging
a real customer from a test system, has already happened by the time you notice.

Alert rules count. An alerting rule that fires on missing data will page forever
if you ship it before the thing it watches exists — or if that thing is later
removed while the rule stays live. Land the target first, the alert second. This
gets violated repeatedly because the rule *looks* inert.

### 🔴 2. It bills without a ceiling

Expensive cloud mistakes are almost always **unbounded** or **invisible**, not
big. A single large VM is a cheap mistake. A loop that creates VMs, a log sink
with no retention, a job that retries forever — those are the ones.

**Test: if I forget about this for a month, what is the bill? If you cannot
answer, put a ceiling on it before you create it.**

### 🔴 3. It can put a person at risk

The rarest, and the one that matters most. It applies whenever the system
touches the physical world, personal safety, or personal data: locks, doors,
vehicles, medical anything, location data, identity.

**Test: could this let the wrong person in, or lock the right person out, or tell
a stranger where someone is? If maybe, stop.**

**Everything outside these three: go.** You do not need permission, and you do
not need to ask twice.

## The loop

```
1. Experiment.               Scratch resource. By hand. Fast and messy is fine.
2. Document what happened.   What worked AND what did not. The failures are the
                             valuable half — they are what stops the next person
                             re-deriving the same dead end.
3. Turn it into a script.    The thing you did by hand becomes runnable.
4. Commit the script. PR it. The repo is the record, not your shell history.
```

**Steps 3 and 4 are not optional.** A change that exists only as commands
someone once ran is a change that will be lost, and then re-derived wrong. The
script is the deliverable. The working machine is only evidence that the script
is right.

Corollary, worth stating as its own rule: **if a human has to do something
repetitively, that is a bug.** Not a chore, not a runbook step to be executed
more carefully next time. A bug.

## Skills update themselves, in the change that taught them

Step 2 of the loop has a second half. A script captures what you *did*. A skill
captures what you *learned*. Both land in the same change.

**When you learn something durable, write it into a skill now — not "later".**
Later does not arrive. The lesson decays into a PR description nobody reads
again, and the next agent pays for it a second time.

### What counts as durable

- A **trap that cost time.** If it cost you an hour, it will cost the next person
  an hour.
- An **assumption that turned out false.** Especially one that looked safe.
- A **command that does not work the obvious way** — the flag you needed, the
  wrapper that lies, the mode that silently differs from the mode you tested.
- A **failure mode that looked like something else.** These are the highest value
  of all, because the wrong diagnosis is the expensive part.

### What does not

- A one-off fact with no next time.
- Anything **already recorded** — check first. A second copy is worse than none,
  because the copies drift and the reader cannot tell which is current.
- Anything **you have not verified.** A skill is load-bearing. Writing a guess
  into one launders it into an established fact for everyone downstream. If you
  must record an unverified thing, mark it unverified in the same sentence.

### Where it goes — three destinations, two questions

Never guess between them. Ask the two questions in order.

**Question 1: will this outlive the task I am on?**
If no → it is a working constraint, not a lesson. It goes in the project
blackboard, `.agents/LEARNINGS.md`. **`continuous-improvement` already owns this**
— its loop reads that file at startup and writes back at closure. Use it; do not
reinvent it here. Typical: "this linter fails when React is imported but unused",
"the fixture needs the env var set before import".

**Question 2 (if it survives the task): would it still be true in a different
repository?**

| | Goes to | And you must |
|---|---|---|
| **No — tied to one codebase** | That repo's **org** skills (`claude-skills/`, `.claude/skills/`, or wherever it keeps them) | Be concrete. Paths, commands, schema, version numbers, PR numbers and incident dates all belong here — that is the entire point. |
| **Yes — portable** | **This repo**, as a skill | **Generalize it.** Strip the repo, the paths, the PR numbers, the ticket IDs. Keep the *shape* of the lesson and the *test* for recognising it next time. |

```
lesson
 ├── dies with the task ......... .agents/LEARNINGS.md   (continuous-improvement)
 ├── outlives it, one repo ...... that repo's org skill
 └── outlives it, any repo ...... a skill here, generalized
```

**The generalize step is the one that gets skipped.** A personal skill full of one
repo's paths is just a worse copy of that repo's documentation, and it is wrong
the moment you switch projects. If you cannot state the lesson without naming the
repo, it was never portable — put it in the org skill instead.

The inverse matters as much: **when a portable rule already exists, the org skill
points at it and does not restate it.** One rule, one home, or the copies drift
and the reader cannot tell which is current.

Most portable rules have a repo-local *instance*. "Quote a CI baseline" is
portable; "this tree has 4,655 pre-existing lint errors as of today" is a
measurement. Keep the rule here and the number there. A stale number is then a
one-line fix in that repo, not a rewrite of a rule.

### 🔴 Only write to skills you own

`~/.claude/skills/` and its siblings are a **flat namespace shared with every
tool that installs skills.** Some entries are symlinks into a vendor-managed
directory that a separate tool owns and updates. Editing one in place is worse
than not writing the lesson at all: the change looks saved, and the next update
silently overwrites it.

The same applies in reverse — a skill you hand-write directly into
`~/.claude/skills/` is unversioned, invisible to every other harness, and lost on
the next machine. **Write it in this repo and let `./apply` deploy it.**

**Check before you write:**

```bash
ls -la ~/.claude/skills/            # arrow → symlink; where does it point?
readlink -f ~/.claude/skills/<name> # inside this repo → yours. Elsewhere → not.
```

### The precedent

Several mature skills already make this binding for their own domain, and the
wording is worth copying. A well-known example: an ops-domain skill in a large
internal repo opens with **"MANDATORY: This Skill Is The Contract"** and requires
the skill be updated *first* — before the code — on **every** change including bug
fixes:

> "If you find an undocumented trap or capability while working on this domain,
> **add it to the skill before you ship the fix.** Not after."

A harness-adjacent skill carries the same clause: "If your intended change isn't
described in a runbook below, **add the runbook first**."

Skill-first is stronger than skill-eventually, and it is the model. Writing the
skill first forces you to state what you think is true before the code can
quietly redefine it.

## Proof

**Never claim something works that you did not observe working.**

"Unverified, here is the risk" is a complete and acceptable answer. Silence is
not. Saying "tested" about a lane you could not run is a lie in the same way
silence is — it just reads better.

Four rules that decide whether you have proof.

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

### Taking the baseline without disturbing the working tree

"Run the check at the branch point" is easy to say and easy to skip, because the
obvious moves — `git stash`, `git checkout <ref> -- .` — destroy uncommitted
work. Two ways that touch nothing:

- **Lint, per file.** Pipe the old version into the linter and keep the filename
  so per-path config still applies:

      git show HEAD:path/to/file.py | ruff check --stdin-filename path/to/file.py -

- **Tests, temporarily.** Copy your version aside, drop the old one in with
  `git show`, run, restore. Never `git checkout --` / `git restore`:

      cp src/mod.py "$SCRATCH/mod.mine.py"
      git show HEAD:src/mod.py > src/mod.py
      <run the failing tests>
      cp "$SCRATCH/mod.mine.py" src/mod.py

  Confirm with `git diff --stat` that your change is back before moving on.

Both take under a minute and turn "those failures look pre-existing" into "those
failures **are** pre-existing, measured". The second is what a reviewer can act
on. Do it before writing a word about someone else's red, and quote the result.

**A caller can break on a field you added, not just a line you changed.** Adding
a read of `settings.some_field` to a shared dependency broke twenty-nine tests
whose fake settings object modelled only the fields its own subject touched.
When you widen what a shared function reads, run the suites of everything that
injects a double — nothing warns you, because a duck-typed double has no
contract to violate until runtime.

## Cost is a constraint, and it is the one nobody writes into the ticket

Correctness, blast radius and effort get weighed by default. **Money does not**,
because it rarely appears in the diff. Before moving work onto any metered
service — CI minutes, managed runners, a hosted database, an API tier — say
which resource is scarce and what the marginal cost of the move is.

- **"We pay for it now" is not a licence to relocate work onto it.** A paid plan
  usually buys a *different* thing than the one blocking you — concurrency,
  seats, support — while the metered resource stays metered. Name what you
  bought.
- **Never move a job onto a more expensive machine class than it needs.** A
  Linux build on a macOS instance is money spent for nothing, every run, forever.
- **Check standing directives before proposing spend.** An operator who has
  refused to pay one vendor has stated a policy about money, not about that
  vendor. Read it as the general rule it is.

**The meta-rule underneath: if you write "X doesn't need Y" and then select Y,
stop.** That sentence is a finding, not an aside. Rationalising past a smell to
keep moving is how the expensive mistakes happen — they are rarely knowledge
failures, they are failures to act on something already noticed. "It's the
proven shape" is not a defence for a path that has never once executed.

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

## Changing something that is live

1. **Read-only discovery first.** Look at the running state. Do not design from
   documentation — it goes stale, and the box is the truth.
2. **Back the file up, dated.** `foo.yaml.bak-20260731`.
3. **Change one thing.** Never run the full deployment path for a small edit.
4. **Verify by diffing, not by looking.** "It looked fine" is not verification.
5. **Guarantee nothing notified anyone, or do not ship it.** Red line 1.
6. **Record the drift, then close it.** A live change is not finished until the
   repo matches it. Everything else is step 3 and 4 of the loop, deferred.

One config file can wedge a whole service's boot, not just the feature it
configures. Validate before you restart, and know your rollback before you need
it.

## Promoting between environments

Portable rules. The names change; the ordering does not.

- **Development deploys from the trunk. Production deploys from a tagged,
  released commit.** Never the reverse, and never a direct push to production.
- **A second human approves the promotion.** Not the person who cut the release.
- **Migrations go first, alone, and verified — then the code.** They must be
  backward-compatible with the code currently running, because there is always a
  window where the old code meets the new schema. Expand, then contract.
- **Every gate must query the environment it is actually gating.** A gate reading
  the wrong environment's config is worse than no gate: it answers with
  authority.
- **Promote the artifact, not the source.** Two builds from one commit are not
  the same thing. Dependency resolution drifts between them.
- **Secrets are never promoted, copied, or cloned between environments.**
- **Rollback is a promotion.** It goes through the same gates.
- **When the artifact bakes its environment in at build time** (mobile apps,
  compiled binaries, container images with embedded config), promotion cannot
  mean re-pointing a running instance. The release cadence sets the clock, and
  the backend must stay compatible with versions already in the field.

## One rule about other people

**Never probe a shared interactive resource to find out whether it works.**
Signing agents, browser logins, passphrase prompts, a device, a lock. The probe
costs you a timeout and costs the human their prompt. **A failed real command is
already the answer** — do not confirm it a second time. Read stored state instead
of triggering a new interaction.

This one is here rather than in `agent-fleet` because it binds when you are
working alone too. Everything else about working alongside other agents is
`agent-fleet`'s.

## What this skill deliberately does not cover

These are owned elsewhere in this pack. Go to them; do not restate them here.

| For | Use |
|---|---|
| Commit discipline, GPG signing, session start/end, destructive-op guardrails, branch naming, "test before push" | **`operations`** — always active, and it owns all of this |
| Git profiles, signing keys, sign-offs, SSH host aliases | **`git-signed-commit`** |
| The build/test/lint iteration loop, and project-scoped lessons in `.agents/LEARNINGS.md` | **`continuous-improvement`** |
| Many agents on one repository: claim files, worktree reconciliation, measuring what an agent actually pushed, PR grain, why a merged PR failed to close its issue | **`agent-fleet`** |
| Splitting work across agents / worktrees / queues | **`agent-fleet`** (+ `context-handoff`) |
| Reviewing someone else's diff with file:line citations and severity ranking | **`thorough-code-review`** |
| Drift between code and `SPEC.md`, scope creep, contract audits | **`specification-compliance`** |
| Pruning bloat, YAGNI ladder, delete lists | **`code-simplification`** |
| The exact commands, schema, paths and traps of one codebase | That repo's `AGENTS.md` / `CLAUDE.md` / org skills |

This skill is the layer none of those cover: **deciding whether a change is yours
to make, and proving it worked.**

## Finding the repo's own rulebook

Before searching a codebase, look for the index. In order:

1. `CLAUDE.md` or `AGENTS.md` at the root — usually names the docs that matter,
   and sometimes the docs that are known wrong.
2. A router or map document, often `docs/ROUTER.md`.
3. `docs/runbooks/` for procedures with a blast radius; `docs/reference/` for
   living subsystem docs; `docs/handoffs/` and `docs/adr/` for the historical
   record.
4. Repo-local skills, commonly `.claude/skills/` or a `*-skills/` directory.

**Handoffs and ADRs are history. Do not edit them to make them current** — they
record what someone knew at a point in time, and rewriting one destroys the only
copy of that. Runbooks and reference docs are living, and should be corrected.

**Do not copy a repo's index into this skill.** That was the first draft of this
file and it was wrong: a table of one project's doc paths goes stale on someone
else's commit, and it is exactly the "would this be wrong in another repo?" test
failing. The repo's own `AGENTS.md` is the index. This file is the spine.
