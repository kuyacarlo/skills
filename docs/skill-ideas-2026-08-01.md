# Skill Ideas — Brainstorm 2026-08-01

Sources:
- **From context**: Gaps identified by analyzing your personal profile, homelab, student life, ADHD systems, and existing skills
- **From ecosystem**: Inspired by popular skills on skills.sh (mattpocock, obra/superpowers, vercel-labs, juliusbrussee/caveman) adapted to your setup
- **From wild**: Creative/unusual ideas unique to your situation (Philippines, hardware+software, multi-agent, power/internet constraints)

---

## Tier 1: High-value, fills real gaps

| # | Skill | What it does | Why | Source |
|---|-------|-------------|-----|--------|
| 1 | ~~`context-handoff`~~ | **Shipped** — `skills/context-handoff` (+ fleet work-queue) | — | context |
| 2 | `homelab-watchdog` | Monitoring / health / alert loop for Podman fleet | Still open (not decided) | context |
| 3 | `backup-rotation` | **Deferred** — no budget for backup infra yet | — | context |
| 4 | `container-lifecycle` | Track image freshness, generate update diffs, flag CVEs | Unsure — park | context |
| 5 | ~~`branch-lifecycle`~~ | **Shipped** — `skills/branch-lifecycle` | — | ecosystem |
| 6 | ~~`verification-before-completion`~~ | **Shipped** — scoped done-gate (not all-CI) | — | ecosystem |

## Tier 2: Strong fit, solves recurring annoyances

| # | Skill | What it does | Why | Source |
|---|-------|-------------|-----|--------|
| 7 | `systematic-debugging` | Reproduce → isolate → fix → verify loop with structured logging | Cross-container bugs where printf-debugging wastes time. | ecosystem |
| 8 | `academic-scheduler` | Syllabi → deadline-aware task streams with exam-prep blocks | Student + CTO + intern = competing deadlines. | context |
| 9 | `secrets-audit` | Scan for leaked creds, expired tokens, rotation-due secrets | Infisical manages secrets but nothing catches drift. | context |
| 10 | `dependency-changelog` | Summarize breaking changes when bumping deps | "Read 12 changelogs" → one actionable diff. | context |
| 11 | `tdd-fastapi` | Test-first workflow for FastAPI with pytest fixtures | Spec-pipeline gets to "what" but not "prove it works first." | ecosystem |
| 12 | `incident-postmortem` | Guided blameless timeline → root cause → action items | Homelab outages and work bugs need structured learning. | context |

## Tier 3: Creative / unique to your situation

| # | Skill | What it does | Why | Source |
|---|-------|-------------|-----|--------|
| 13 | `brownout-continuity` | Power-interruption checkpointing + resume packets | MERALCO brownouts destroy flow state weekly. | wild |
| 14 | `bandwidth-shepherd` | Adapts agent behavior to connection quality (batch, cache, smaller models) | Philippine internet reality. 200kbps is normal sometimes. | wild |
| 15 | `barangay-deploy` | Offline-first PWA, Filipino i18n, prepaid-data-sized assets, GCash hooks | Ship tools to communities where cloud = ₱50 load burned. | wild |
| 16 | `hyperfocus-arbitrage` | Detects high-focus via commit velocity, feeds deep work; on drop, surfaces dopamine tasks | Exploits ADHD superpower instead of only managing downsides. | wild |
| 17 | `socratic-datasheet` | Interactive Q&A replacing datasheet reading for registers/timing/gotchas | ADHD + embedded work = glazing at 400-page PDFs. Socratic > reading. | wild |
| 18 | `dopamine-menu` | Curated low-friction starter tasks by energy level | Defeats the blank-screen activation problem. | wild |
| 19 | `pcb-to-container` | KiCad schematics → emulated firmware environments on homelab | Bridge hardware projects with container compute. | wild |

## Tier 4: Ecosystem-inspired, good but less urgent

| # | Skill | What it does | Why | Source |
|---|-------|-------------|-----|--------|
| 20 | `context-compression` | Auto-summarize long sessions into compact working memory | Prevents re-explaining across long sessions. | ecosystem |
| 21 | `parallel-agent-dispatch` | Fan-out/fan-in protocol for multi-agent concurrent work | Formalize what you already do ad-hoc. | ecosystem |
| 22 | `domain-modeling-civic` | Ubiquitous language + bounded contexts for gov/civic domains | Civic tech domain language drifts between legal/bureaucratic/user. | ecosystem |
| 23 | `container-topology` | Visualize Podman compose graphs, detect port conflicts, orphans | "Why is X unreachable" → read graph, not 12 compose files. | ecosystem |
| 24 | `worktree-workflow` | Git worktree management for parallel features without stashing | Physical separation > mental overhead of stash/pop. | ecosystem |
| 25 | `portfolio-builder` | Git history + READMEs → case studies + portfolio pages | Y3 = job hunt soon. | context |
| 26 | `meeting-distiller` | Transcripts → decisions + action items + follow-ups | CTO + intern = many meetings. ADHD recall unreliable. | context |
| 27 | `group-project-scaffold` | Multi-contributor repos with role-based tasks, PR templates for student teams | University group projects fail from coordination. | context |
| 28 | `migration-guide` | Step-by-step migration plans for stack transitions | Docker→Podman done, but Nebius cloud, Quadlet adoption coming. | context |
| 29 | `mesh-canary` | Inject synthetic tasks across agents + homelab to detect degradation | Cross-agent + cross-container observability. | wild |

---

## Sources detail

**From context** — Analyzed `~/.config/karlo/CONTEXT.md`, `INVENTORY.md`, `AGENTS.md`,
`SKILLS.md`, existing skill bodies, and the gaps between them (what exists vs what breaks).
Key signals: 51 containers with no lifecycle automation, multi-agent daily use with no
handoff protocol, student+CTO+intern competing deadlines, ADHD completion dropout at 90%.

**From ecosystem** — Top skills on skills.sh adapted to this profile:
- `obra/superpowers`: systematic-debugging, verification-before-completion, dispatching-parallel-agents, worktrees
- `mattpocock/skills`: tdd, branch lifecycle, domain-modeling, handoff, caveman (compression)
- `juliusbrussee/caveman`: context compression, commit discipline
- `vercel-labs/agent-skills`: find-skills pattern, progressive disclosure

**From wild** — Creative riffs on unique situation intersection:
- Philippines (MERALCO brownouts, prepaid data, barangay-level civic deployment)
- Hardware+software (ESP32, KiCad, cylindrical PCBs meeting container infrastructure)
- Multi-agent constellation (4+ daily agents as a system, not isolated tools)
- ADHD as leverage (hyperfocus detection, Socratic learning, dopamine-aware task routing)

---

## Your call

**Started 2026-08-01:** `1` context-handoff — skill at `skills/context-handoff/`.

Reply with numbers. Examples:
- "1, 5, 6, 13 — hit" 
- "8, 19 — not so much"
- "16 — merge with focus-management?"
