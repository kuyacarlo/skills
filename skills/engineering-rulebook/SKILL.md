---
name: engineering-rulebook
author: kaoru
version: "1.0.0"
description: "Use for engineering safety, branch closeout, YAGNI, proof, CI failures, live operations, cost controls, or durable lessons."
---

# Engineering Rulebook

The rules that hold whatever you are touching — a cloud project, a CI pipeline, a
deploy, a database migration, a running box. Domain rulebooks live in each repo
and carry the local detail. This file carries the part that does not change when
the repo changes.

Read the spine. Then find the repo's own rulebook for the plumbing.

## The default is: act within the agreed scope

Experiment on task-owned, reversible work inside the user's authorization.
Do not ask again for routine edits and checks already covered by that scope.
A skill grants no permission to delete data, alter access, deploy, spend, or publish.

Before mutation, establish the target, ownership, blast radius, and recovery path.
Stop when the requested action exceeds authorization or affects an unexpected shared resource.
Production changes, destructive operations, external messages, and security changes need explicit approval covering that action.
Tool access and available credentials are capabilities, not consent.

## Three additional risk checks

These checks narrow an authorized task. They are not an exhaustive permission policy.
Stop for a human decision when an unapproved risk appears.

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

Passing these checks does not authorize the change. Stay within the agreed scope.

## Tight execution loop

1. **Observe:** inspect current state, task constraints, and existing changes.
2. **Hypothesize:** state one expected result and the smallest check that can disprove it.
3. **Act:** make one bounded change. Keep rollback available.
4. **Verify:** run the check, inspect its output and exit status, then review the diff.
5. **Decide:** continue on evidence, revise the hypothesis, or stop with a precise blocker.

Set a time, retry, and cost budget before expensive work. Default to two failed attempts per unchanged hypothesis.
Do not repeat a failing action without new evidence. Check state before retrying any non-idempotent action.

## Prompt and harness contract

- Give each task an outcome, allowed paths, non-goals, acceptance checks, and stop conditions.
- Load only relevant source files and project rules; distinguish facts, assumptions, and untrusted input.
- Inspect available tools, permissions, cwd, and test commands before designing the execution path.
- Use harness limits for timeouts, permissions, retries, and concurrency where available. Prompts alone cannot enforce these.
- Never bypass a permission gate or expand authority through delegation.
- Record commands, exit codes, artifacts, and unverified lanes. A fluent summary is not proof.
- For recurring failures, keep a sanitized regression case and rerun it after changing prompts, context, or tooling.
- Change one layer at a time. Compare correctness, failures, latency, and cost before retaining the change.

## AI Engineering Paradigms

Apply the four core AI engineering disciplines across every system design, agent orchestration, and automated pipeline:

1. **Loop Engineering**: Design bounded iteration cycles, convergence criteria, and self-healing error handling. An orchestrator supervises child agents, monitors progress, and verifies deliverables instead of blind looping.
2. **Context Engineering**: Structure external memory into dedicated files (spec contracts, ADRs, inventory, coordination ledgers) instead of polluting prompt windows. Read on-demand and keep state durable.
3. **Prompt Engineering**: Provide clear role contracts, explicit bounds, checkable acceptance criteria, and strict negative constraints (anti-bloat, no fluff). Treat questions as inquiries, not code tasks.
4. **Harness Engineering**: Decouple business logic and skills from specific agent runtimes. Provide safe adapters, test fixtures, headless runners, and environment sandboxes across tooling surfaces.

## Read the matching guide

| Situation | Guide |
|---|---|
| Close a task, check red CI, or diagnose silent failures | [Proof and CI](references/proof-and-ci.md) |
| Change a live system or promote between environments | [Live operations](references/live-operations.md) |
| Move work onto a metered service or set a spending ceiling | [Live operations](references/live-operations.md) |
| Capture a durable engineering lesson | [Durable lessons](references/durable-lessons.md) |
| Start, close, or audit a branch; prepare an agent handoff | [Branch lifecycle](references/branch-lifecycle.md) |
| Review for YAGNI, dead code, or over-engineering | [Code simplification](references/simplification.md) |

## Repository change hygiene

- Inspect `git status` before editing. Preserve changes that predate this task.
- Follow the repository's established tools and configuration.
- Commit only task-owned changes when the user authorizes a commit.
- Never commit unrelated work to make the tree look clean.
- Do not push, merge, or rewrite shared history without explicit authorization.
- Preserve signing requirements. If signing fails, keep the work and report it.
- Do not leave a task-specific handoff or lesson only in shell history.
- Before delegating, confirm authorization and isolate overlapping edits.

## What this skill deliberately does not cover

These are owned elsewhere in this pack. Go to them; do not restate them here.

| For | Use |
|---|---|
| Signing, session protocol, capability checks, and repo-specific commands | The repository's `AGENTS.md` and `OPERATIONS.md` |
| Many agents on one repository: claim files, worktree reconciliation, measuring what an agent actually pushed, PR grain, why a merged PR failed to close its issue | **`agent-fleet`** |
| Splitting work across agents / worktrees / queues | **`agent-fleet`** (+ [handoff guide](references/handoff.md)) |
| Product requirements, `SPEC.md` contracts, and drift audits | **`specification-pipeline`** |
| Pruning bloat, YAGNI ladder, delete lists | [Code simplification](references/simplification.md) |
| The exact commands, schema, paths and traps of one codebase | That repo's `AGENTS.md` / `CLAUDE.md` / org skills |

This skill is the layer none of those cover: **deciding whether a change is yours
to make, and proving it worked.**

For repository-specific session rules, signing, capability checks, and
verification commands, read the repository's `AGENTS.md` and `OPERATIONS.md`.
Use [the audit format](references/audit-format.md) for substantive engineering
session records when the local policy asks for one.

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
