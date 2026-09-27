# Durable lessons

Read this guide only when its workflow applies.

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
blackboard, `.agents/LEARNINGS.md`. The failure loop in
[Proof and CI](proof-and-ci.md) reads that file at startup and writes back at
closure. Typical: "this linter fails when React is imported but unused",
"the fixture needs the env var set before import".

**Question 2 (if it survives the task): would it still be true in a different
repository?**

| | Goes to | And you must |
|---|---|---|
| **No — tied to one codebase** | That repo's **org** skills (`claude-skills/`, `.claude/skills/`, or wherever it keeps them) | Be concrete. Paths, commands, schema, version numbers, PR numbers and incident dates all belong here — that is the entire point. |
| **Yes — portable** | **This repo**, as a skill | **Generalize it.** Strip the repo, the paths, the PR numbers, the ticket IDs. Keep the *shape* of the lesson and the *test* for recognising it next time. |

```
lesson
 ├── dies with the task ......... .agents/LEARNINGS.md   (failure loop)
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
