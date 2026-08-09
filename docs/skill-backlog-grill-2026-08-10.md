# Skill backlog — primer + grill

Captured 2026-08-10. Answer in this file or another thread later; do not fan out
new skills until the grill section has answers.

Ideas inventory: [skill-ideas-2026-08-01.md](./skill-ideas-2026-08-01.md).

---

## Already decided (Tier 1)

| # | Skill | Status |
|---|--------|--------|
| 1 | `context-handoff` | Shipped |
| 2 | `homelab-watchdog` | **Open** — not decided (see grill Q1) |
| 3 | `backup-rotation` | **Deferred** — no budget for backup infra yet |
| 4 | `container-lifecycle` | **Park** — unsure (see grill Q2) |
| 5 | `branch-lifecycle` | Shipped (PR #9 / pack) |
| 6 | `verification-before-completion` | Shipped — scoped done-gate: local hooks + owned proof; not “all CI green”; baseline red and in-flight whole-repo fixes get named, not used as blockers |

Numbering note from the chat: “hate 2 + no budget for backups” was read as
**backups** (this table’s #3). If “hate 2” meant **watchdog**, correct Q1.

---

## Fan-out rule (until grill answered)

- No Tier 2–4 skill PRs until grill answers land.
- Default proposal after that: **one** Tier 2 skill next (candidates in Q3), not a batch.

---

## Tier 2 primer — recurring annoyances

| # | Skill | In one line | Lean | Overlap / alternative |
|---|--------|-------------|------|------------------------|
| 7 | `systematic-debugging` | Reproduce → isolate → fix → verify | Weak GO if kept thin | Rulebook + CI already half-do this; obra/superpowers exists upstream |
| 8 | `academic-scheduler` | Syllabi → deadline streams | PIVOT or NO-GO as pack skill | Calendar / Notion / ef-starter; a skill will not beat a real planner |
| 9 | `secrets-audit` | Drift / leak / expiry scan | Conditional GO | Infisical + gitleaks/trufflehog; skill = *when* to run + what to do |
| 10 | `dependency-changelog` | Breaking-change digest on bumps | Weak GO | `pnpm why`, Dependabot, release notes; thin-skill risk |
| 11 | `tdd-fastapi` | Test-first FastAPI recipe | PIVOT → project `AGENTS.md` | Repo-local; pack-wide TDD ages badly |
| 12 | `incident-postmortem` | Blameless timeline → actions | Weak GO | One markdown template may be enough (no skill) |

Chat lean: T2 “sure” in principle; evaluator default would pick **9 + 7**, kill **8 / 11** as pack skills.

---

## Tier 3 primer — niche (PH / ADHD / hardware)

| # | Skill | In one line | Lean | Reality check |
|---|--------|-------------|------|----------------|
| 13 | `brownout-continuity` | Checkpoint + resume on power loss | Interesting PIVOT | Handoff + ops already cover “pause”; only worth it if brownout steps differ |
| 14 | `bandwidth-shepherd` | Degrade agent behavior on bad net | NO-GO / later | Hard to detect cleanly; model choice is often manual |
| 15 | `barangay-deploy` | Offline-first civic PWA patterns | NO-GO as pack skill | Build when there is a real barangay user |
| 16 | `hyperfocus-arbitrage` | Route tasks by focus signal | NO-GO | Overlaps `focus-management`; commit-velocity “detection” is folklore |
| 17 | `socratic-datasheet` | Q&A over datasheets | PIVOT | Useful in an ESP32 week; else unused |
| 18 | `dopamine-menu` | Low-friction starters by energy | PIVOT → fold into EF | Home is `focus-management` / ef-starter |
| 19 | `pcb-to-container` | KiCad → emulated firmware lab | NO-GO now | Science project until a board is in flight |

---

## Tier 4 primer — ecosystem / lower urgency

| # | Skill | In one line | Lean |
|---|--------|-------------|------|
| 20 | `context-compression` | Session → compact memory | NO-GO — STE + continuous-improvement cover enough |
| 21 | `parallel-agent-dispatch` | Fan-out protocol | NO-GO — `agent-fleet` owns this |
| 22 | `domain-modeling-civic` | Ubiquitous language for gov | Park until a civic project |
| 23 | `container-topology` | Compose graph / port orphans | Maybe merge with container-lifecycle — one skill, not two |
| 24 | `worktree-workflow` | Parallel worktrees | Fold into `branch-lifecycle` / fleet later |
| 25 | `portfolio-builder` | Git → case studies | Park until job-hunt crunch |
| 26 | `meeting-distiller` | Transcript → decisions | Thin; one prompt/template |
| 27 | `group-project-scaffold` | Student team repo kit | Park until next group class |
| 28 | `migration-guide` | Stack migration plans | Park until Nebius/Quadlet is real |
| 29 | `mesh-canary` | Synthetic probes across agents/lab | NO-GO — needs watchdog first |

---

## Grill — answer here when ready

Copy answers under each question (short is fine).

### Q1 — Watchdog (#2)

Hate it, park, or “only a dead-simple health script skill later”?

**Answer:**

### Q2 — Container lifecycle (#4)

Do you actually pull/update images on a cadence, or is this aspirational guilt?

**Answer:**

### Q3 — Tier 2 pick (at most two)

Choose from 7 / 9 / 10 / 12. (Evaluator default: **9 + 7**.)

**Answer:**

### Q4 — Academic scheduler (#8)

Do deadlines fail because *no list*, or because *you ignore the list*?
(If ignore → pack skill will not help.)

**Answer:**

### Q5 — Brownout (#13)

When power dies mid-agent, what do you wish existed that `HANDOFF.md` + commit WIP does *not* already do?

**Answer:**

### Q6 — Hard no list

Which of 14–19 / 20–29 should be marked `[X]` in the ideas doc so they stop resurfacing?

**Answer:**

### Q7 — Fan-out rule

OK to ship **one** Tier 2 skill next, only after branch-lifecycle PR merges — yes/no?

**Answer:**

---

## Related

- [skill-ideas-2026-08-01.md](./skill-ideas-2026-08-01.md) — full brainstorm tables
- Skills: `branch-lifecycle`, `verification-before-completion`, `idea-evaluation`
