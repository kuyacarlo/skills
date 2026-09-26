---
name: agent-fleet
author: kaoru
version: "1.1.0"
description: "Use when several AI coding agents work one repository in parallel git worktrees and someone must answer \"what is the true state?\" — who holds which branch, what is actually pushed, which claims are stale, what work is invisible. Also covers running a TREE of agents, where each worker spawns its own sub-fleet, and a file-based cross-agent work queue (claim/lease/handoff) for agy, Cursor, Kiro, and similar CLIs. Triggers on \"who is working on what\", \"reconcile the claims\", \"is that branch done\", \"what is blocked\", \"did that agent push anything\", \"coordination folder\", \"orchestrator\", \"fan out subagents\", \"prune merged worktrees\", \"why is the issue still open after we merged\", \"agent work queue\", \"taskboard\", \"claim the next job\", \"ticket rail\". Covers the file-based coordination protocol, recursive delegation, the measurement bugs that silently under-report work, shared-resource hazards, PR grain and linking, and when to escalate to Orca orchestration vs file claims."
---

# Agent Fleet Coordination

Running N agents against one repository without collision, duplication, or
silently lost work — and running them as a **tree**, not a flat list.

## The core rule

**Claim files are assertions. Git is the fact.** Never relay a claim without
measuring it. A claim file is a snapshot written at a moment, and subagents move
faster than their parent updates it.

**A branch with a claim and zero commits beyond its base is not in progress. It
is not started.** Say exactly that — never a percentage you did not measure.

## The coordination directory

```
<workspace>/.coordination/
├── decisions.md          ← append-only, NEWEST FIRST. The law.
├── ORCHESTRATOR.md       ← the role definition
├── ENVIRONMENT-ISSUES.md ← machine faults every agent hits
├── <name>.md             ← one claim file per agent
└── <name>/HANDOFF.md     ← per-agent blackout-survival doc
```

**Keep it a SIBLING of the repo, not inside it.** It then never appears in
`git status`, never lands in a commit, and never collides with the work. The
cost: it does not survive a fresh clone, and people report it "missing" when they
look inside the repo. State the absolute path when handing over.

**Claim a path glob before editing it.** Two agents editing one file is the
failure this whole directory exists to prevent.

## Cross-agent work queue

When jobs must move between **different tools or sessions** (agy ↔ Cursor ↔
Kiro), keep a small file queue under `.coordination/queue/` — inbox → claimed →
blocked → done — with claim tokens and short leases. Same mental model as a
ticket rail; no server required.

Full protocol, job frontmatter, optional `tb` shim, and **when to use Orca
instead**: [references/work-queue.md](references/work-queue.md).  
Job stub: [templates/queue-job.md](templates/queue-job.md).  
Session/branch survival docs: skill `context-handoff`.

**Do not** stand up a Taskboard HTTP service unless the human asked for one.
Files first.

## Running a TREE, not a flat fleet

This is the highest-leverage structure, and it is under-used.

**Depth beats breadth.** One agent running ~11 subagents in parallel worktrees
out-produced two single-threaded agents combined — and added **zero** coordination
cost. More top-level agents cost collisions; subagents inside one lane cost none.

```
human
└── orchestrator            reconciles, edits no code
    ├── worker A            owns a lane, one claim file
    │   ├── sub A1          own worktree, own branch, own ticket
    │   ├── sub A2
    │   └── sub A3
    └── worker B
        ├── sub B1
        └── sub B2
```

**Why the tree is cheap:** everything below a worker shares one claim file, one
lane, one arbiter. Peers never need to know those subagents exist. The worker
resolves its own internal conflicts; only cross-lane contention reaches the
orchestrator.

**Rules for each level:**

- **A worker splits its own tickets** and gives each one its own worktree and
  subagent. It does not queue them.
- **A worker is responsible for what its subagents hold.** Measure them; do not
  trust your own notes. A claim file once said "not started, 2 commits" while a
  subagent had 16 and was still committing — the parent nearly reassigned work
  that already existed.
- **Subagents may go a level deeper** for genuinely separable pieces. Stop when a
  piece is no longer independently reviewable — depth is for parallelism, not
  decomposition theatre.
- **Only one node per subtree talks upward.** A subagent reporting straight to the
  orchestrator bypasses the arbiter and reintroduces the collisions the tree
  removed.
- **Cut every branch from the default branch**, whatever your depth. A stacked
  branch cannot auto-close its issue (below), and stacks multiply rebases.

### How many agents

**Count independent, well-scoped targets. That is your subagent count. Then ask
whether you need a second top-level agent at all — usually you do not.**

| Situation | Shape |
|---|---|
| Work is diagnosed and independent (N named fixes, no shared files) | **orchestrator + N subagents.** No peers. |
| Several distinct lanes needing different expertise, likely to touch each other | one worker per lane, each fanning out |
| Open-ended discovery, scope unknown | start with one worker; split only once the shape is known |

**Add a top-level agent only for a genuine lane boundary** — different subsystem,
different reviewer, different expertise. Never to "go faster": peers cost
arbitration, subagents do not.

**Sizing sanity check:** if merge or review authority sits with one human, adding
agents past that person's throughput just deepens a queue. Measure the queue
before adding capacity to fill it.

**Watch where subagent worktrees are created.** They frequently land *inside*
another agent's checkout (e.g. `<repo>/.<agent>/worktrees/`). A `git clean` in the
host tree then destroys the guest's work.

## Reconcile — the commands

```bash
git fetch -q origin --prune

# EVERY worktree. Do NOT filter — see blind spot 1.
git worktree list --porcelain | awk '/^worktree /{print $2}'

for d in $(git worktree list --porcelain | awk '/^worktree /{print $2}'); do
  br=$(git -C "$d" rev-parse --abbrev-ref HEAD 2>/dev/null); [ "$br" = HEAD ] && continue
  # CRITICAL: origin/$br does not resolve for a never-pushed branch
  if git rev-parse --verify -q "origin/$br" >/dev/null; then base="origin/$br"; else base="origin/main"; fi
  echo "$br dirty=$(git -C "$d" status --porcelain | wc -l) ahead=$(git -C "$d" rev-list --count "$base..HEAD")"
done

# Signatures — passive, opens no signing prompt.
git log --format='%h %G?' origin/main..origin/<branch> | grep -v ' G$'
```

## Seven blind spots that each produced a confident, wrong "nothing here"

1. **Filtered worktree lists.** Recipes that `grep -v '/tmp/'` or
   `grep -v '.<agent>/worktrees'` hide exactly where agents put worktrees. Eight
   commits stayed invisible across three passes because of one such filter.
2. **Branches with no origin counterpart** count `0` and get skipped entirely.
   Fall back to the default branch.
3. **First `fetch --prune`** reports every long-stale ref as newly deleted.
   Confirm against `git ls-remote` before reporting a deletion.
4. **Squash-merge ghosts.** After a merge, old branch tips read as "ahead" of a
   default branch that already contains their content. Check
   `gh pr list --head <branch> --state all` before calling it unpushed work.
5. **Paginated API results.** `gh pr list --limit 200` returning exactly 200 is a
   truncation, not a total. Raise the limit and re-check.
6. **A competing PR already owns your issue.** The fleet opened a PR for issue
   #12 while an external contributor's larger PR for the same issue was already
   open, overlapping 5 of the fleet's files. Before a lane claims an issue, check
   `gh pr list --state all --search "issue:<N>"` (or `gh pr list` and scan the
   body) — a claim file that says "ours" does not stop someone else's PR from
   landing first and making the lane's diff obsolete or conflicting.
7. **Draft PRs skip automated review.** CodeRabbit (and similar bots) report
   "Review skipped: draft pull request" and their check still reads **pass**.
   A green check on a draft is lint/build only — it is NOT a review signal. If
   review is the deliverable, the PR must be marked ready; do not report a draft
   as "reviewed" because its checks are green.

## Shared interactive resources — never probe

**If a resource prompts a human, an agent must never run it to test whether it
works.** Signing agents, browser auth, TTY password prompts. The agent gets a
timeout; **the human loses the prompt** to a process that cannot answer it.

**A failed real command is already the answer.** Do not verify it a second time.

Beware near-miss probes that lie: a signing tool's *clear-sign* mode may succeed
while its *detached* mode — the one commits actually use — fails. Read stored
state instead (`git log --format='%G?'`).

Note the failure mode of this rule: the agent that writes it will find a reason
its own case is exempt ("but I was told to fix it, so I should check first"). It
is not exempt. Write it so it binds the author.

## Definition of done, and why PRs fail to close issues

**Prefer "a PR exists and links its issue" over "merged"** when merge authority
sits with someone outside the fleet. Merge count then measures another person's
calendar, not the work.

Two silent faults break the link:

- **The keyword must stand alone.** `- Closes #818. Adds foo…` inside a list item
  registers nothing. A bare `Closes #818` paragraph works. Verify with
  `gh pr view <n> --json closingIssuesReferences` — never assume.
- **A stacked PR can never auto-close.** GitHub only creates closing references
  for PRs targeting the default branch. Re-targeting alone does **not** always fix
  it; the body must also be well-formed.

Landing the base of a stack is therefore often worth more than any new feature.

## PR grain

**Different namespace → SPLIT. Same or similar target → JOIN. Namespace wins.**

Namespace = the deployable and its reviewer (backend, web, mobile, infra,
migrations). Target = the thing changed. Two issues with a similar target in
different namespaces still split. Never join large refactors that merely share a
parent — if a reviewer cannot hold the diff in their head, it is two PRs.

Review capacity, not authoring, is usually the real bottleneck.

## Reporting discipline

- **Evidence, not summary:** counts, hashes, paths, the command you ran.
- **Distinguish authored from landed.** They diverge wildly.
- **Never publish an inference about another agent's intent as a finding.**
  "These commits are unsigned" is verified. "The author deliberately bypassed the
  rule" is a guess — and if the rule post-dates the commits, it is also wrong.
- **Re-measure when challenged.** Your instrument has bugs; the agent doing the
  work often finds them first.
- **Correct in writing.** Supersede in the append-only log; never silently edit an
  old entry.
- **Tune your monitors down, not up.** A watcher that reports every file save
  trains the reader to ignore it. Report state changes that need a decision.

## Verification — establish the contract once, then hold everyone to it

**The commands are per-project. The discipline is not.** Fill in
`templates/VERIFICATION.md` before the first agent starts, keep it in
`.coordination/`, and point every agent prompt at it. Without it each agent
invents its own definition of "tested" and the fleet reports green work that is
broken.

The contract records: which lanes actually run here and their exact commands,
what is structurally unavailable and why, the exit-code traps in this toolchain,
and the human gates no agent can clear.

**Six rules the contract enforces:**

1. **Red before green.** Prove the test fails against unfixed code first. A test
   that never failed proves nothing. Where a fix has a self-correcting sibling
   branch, pin the branch that does *not* self-correct — otherwise the test
   passes against broken code.
2. **Run the FULL affected suite, not just your own file.** This is the single
   most common cause of a blocked review: N passing in a new file while N more
   break elsewhere. Diff the failure **name sets**, not just totals — equal
   counts can hide a swap.
3. **Separate pre-existing from introduced.** Run at the branch point too. If the
   failing sets match either side, say so and leave them alone.
4. **Never claim "tested" for a lane that cannot run here.** Name what you could
   not verify and why. Silence and "tested" are both lies.
5. **Never weaken a guard to make a test pass.** Fix the test's setup instead,
   and prefer the option that leaves the guard armed for everything not
   explicitly named.
6. **The orchestrator re-runs; it does not trust.** A self-reported test count is
   a claim like any other.

**On rule 6:** in one batch of seven fixes, every agent's reported counts
reproduced exactly. That is only knowable because they were re-run — and the
reason the batch existed at all was a prior round where self-reported green hid
24 broken tests elsewhere.

**Check the repository's own rules first.** Most codebases already state a
testing standard, and a blocked review is usually that standard being ignored
rather than missing. Read `AGENTS.md`, `CONTRIBUTING.md` or equivalent before
writing a verification contract, and make the contract enforce what is already
there instead of competing with it.

## Bundled files

```
templates/ORCHESTRATOR.md       the role definition — drop into .coordination/
templates/decisions.md          the append-only log, with format and examples
templates/VERIFICATION.md       the testing contract — FILL THIS IN FIRST
templates/claim.md              one per agent
templates/HANDOFF.md            blackout-survival doc, one per agent
templates/queue-job.md          one job in .coordination/queue/{inbox,…}/
references/work-queue.md        cross-agent queue protocol + Orca boundary
scripts/fleet-monitor.sh        the watchdog described below
```

Copy the templates into `<workspace>/.coordination/` when standing up a
fleet (add `queue/inbox` etc. when using the work queue). They encode the
shape; the comments in them encode the mistakes.

**Fill in `VERIFICATION.md` before the first agent starts.** It is the only one
that must be complete up front — the others accumulate as work proceeds.

## Watch the coordination directory

Run a watchdog so the orchestrator learns about changes instead of polling.
`scripts/fleet-monitor.sh` emits one line per event; wire its stdout into
whatever background-monitor facility the harness provides.

```bash
bash scripts/fleet-monitor.sh /path/to/.coordination 120
```

**It reports only what needs a decision:**

| Event | Meaning |
|---|---|
| `CLAIM-EDIT <file>` | an agent updated its claim — or, if the fleet was down, came back alive |
| `OUR PUSH <branch>` | a branch we own reached origin |
| `*** OUR UNSIGNED COMMIT ON ORIGIN ***` | the one true alarm |
| `HELD-SET changed` | the **set** of branches holding unpushed, unmerged work changed |

**It is deliberately silent about** dirty-file churn, other people's pushes, and
counts changing on a branch already known to be holding work.

**Every one of those exclusions was added, found to be noise, and removed.** A
watcher that fires on every file save trains its reader to ignore it — at which
point it is worse than no watcher. Tune down, not up. If you find yourself
prefacing reports with "nothing really changed", fix the filter instead.

Two implementation traps the script already handles, both of which produced
wrong reports before they were fixed: `origin/<branch>` does not resolve for a
never-pushed branch (fall back to the default branch), and the merged-PR lookup
must not be truncated by its own `--limit`.

## Before destroying anything

1. `git status --porcelain` must be empty.
2. No open PR: `gh pr list --head <branch> --state all`.
3. Prefer `git worktree remove` while **keeping the branch** — frees the
   directory, leaves every commit recoverable.
4. **Never** `git clean`, `stash`, `checkout --` or `reset --hard` work you did
   not create. A merged branch with dirty files is not prunable; it is a question
   for the human.

## Recovering a dead agent's work

When an agent stops holding uncommitted work, and the human authorises recovery:

1. **Read every file before touching it.** You are committing someone else's work.
2. Commit exactly as found. Write no new code.
3. **State provenance** in the commit message and PR body — whose work it is, and
   that it was recovered.
4. Run its tests before pushing; report which lanes could not run.
5. Then push and open the PR.

## Environment facts to establish once, and record

Before planning any verification step, find out and write down: which test lanes
can actually run locally, which services are reachable, which credentials exist.
**Never plan a verification step around something unavailable, and never report
"tested" for a lane that cannot run.** Say what you could not verify and why.
