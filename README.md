# Skills

Installable agent skills for Cursor / Claude / Gemini / Kiro / Codex and other
local harnesses.

```bash
./apply -y        # enable all, deploy
./apply           # interactive
FORCE_ALL=1 ./scripts/package_skills.sh   # rebuild dist/*.skill
```

Symlinks land under `~/.agents`, `~/.gemini/config`, `~/.cursor`, `~/.copilot`,
… when present. `apply` never touches `~/.claude` (Claude Code is out of scope
for this pack) or `~/.kiro`.
Pack default: **`simplified-technical-english`** always deploys.

---

## Live skills

| Skill | Role |
|-------|------|
| `agent-fleet` | Multi-agent claims, trees, file work queue |
| `context-handoff` | HANDOFF.md across agent/tool switches |
| `branch-lifecycle` | Start → PR → merge → delete/prune WIP |
| `verification-before-completion` | Done-gate: your lane + local hooks, not all-CI |
| `engineering-rulebook` | When to act alone; proof; silent failure |
| `operations` | Commits, signing, session start/end |
| `personal-context` | Load `~/.config/karlo` (data stays outside skills) |
| `developer-profile` | Generate portable profile artifacts (setup) |
| `ef-starter` | Executive-function system (submodule) |
| `focus-management` | Energy / demotivation / reconnect logs |
| `specification-pipeline` | specify → clarify → plan → implement |
| `specification-compliance` | SPEC.md drift checks |
| `architectural-planning` | Mermaid plans, milestones |
| `thorough-code-review` | Citation-style review |
| `code-simplification` | YAGNI prune |
| `continuous-improvement` | `.agents/LEARNINGS.md` loop |
| `idea-generator` | Hackathon ideation only |
| `idea-evaluation` | Go / No-Go / Pivot |
| `numbers-first-report` | Blunt gap / research reports (counts → P0–P3 → skip → GO wave) |
| `free-tier-deploy` | CF / Vercel / Fly / Railway / Render |
| `git-signed-commit` | GPG / profiles / SSH host aliases |
| `simplified-technical-english` | Default dense prose (always on) |

\* Auto: STE always on; `focus-management` on stuck/low-energy language.

Credits / submodule policy: [ORIGINS.md](ORIGINS.md).

---

## Scope

| Scope | Where |
|-------|--------|
| Agent-wide | `./apply` → home skill dirs |
| Project | `.agents/skills`, repo `AGENTS.md` |

If it would be wrong in another repo, keep it project-local.

## License

See [LICENSE](LICENSE). Submodules keep their own licenses.
