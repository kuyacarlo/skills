# Skills

Personal + installable agent skills for Antigravity / Gemini / Cursor (and Copilot if present).

**Claude Code is not managed by this repo.** Do not run installers that touch `~/.claude`.

---

## Quick start

```bash
./apply -y        # enable all skills, deploy
./apply           # interactive toggle (default: all on)
./apply -y -v     # verbose
```

Deploys symlinks into (when present):

| Target | Path |
|--------|------|
| Agents / Codex-style | `~/.agents/skills/` |
| Gemini / Antigravity | `~/.gemini/config/skills/` |
| Cursor | `~/.cursor/skills/` |
| Copilot | `~/.copilot/skills/` |

Also links `AGENTS.md` into those roots.

---

## Live skills

| Skill | Role | Invoke |
|-------|------|--------|
| `architectural-planning` | Mermaid plans, milestones, task matrices | user |
| `code-simplification` | YAGNI / decision-ladder prune (ponytail-inspired) | model |
| `continuous-improvement` | Capture learnings from test/lint loops | model |
| `developer-profile` | Generate portable profile artifacts for agents | user / setup |
| `ef-starter` | Executive-function system builder (submodule) | user |
| `email-management` | Classify / route mail + filter configs | user |
| `focus-management` | Energy diagnosis, reconnect logs, low-activation defaults | model* |
| `git-signed-commit` | Git identity, GPG/SSH signing, custom hosts | user / setup |
| `idea-evaluation` | Go / No-Go / Pivot grill | model |
| `idea-generator` | Hackathon **ideation only** (not a full product factory) | user |
| `output-compression` | Dense replies, less waffle (caveman-inspired) | model |
| `specification-compliance` | SPEC.md drift / contract checks | model |
| `specification-pipeline` | specify → clarify → plan → implement chain | user |
| `free-tier-deploy` | Cloudflare / Vercel / Fly / Railway free-tier deploy patterns | model |
| `personal-context` | Load systems/background context; keep data out of skill bodies | model |
| `thorough-code-review` | Exhaustive citation-style review (generalized) | user |
| `parallel-work-planning` | Multi-engineer interface contracts (generalized) | user |

\* `focus-management` descriptions include demotivation / stuck triggers so agents can auto-reach for it.

See [ORIGINS.md](ORIGINS.md) for upstream credits and submodule vs reframe policy.

---

## Naming

- **Reframes (this repo):** objective `name:` + upstream mentioned in description.
- **Submodules:** keep **upstream** titles (e.g. `ef-starter`).
- **Private workflows** (e.g. full hackathon factories) stay in their own repos and may **link to** this pack — they are never vendored here.

---

## Project vs workspace vs agent-wide

| Scope | Where | When |
|-------|--------|------|
| **Agent / tool-wide** | `~/.agents/skills`, `~/.gemini/config/skills`, `~/.cursor/skills` via `./apply` | Defaults, guardrails, EF, personal context — every project |
| **Workspace / multi-repo** | Shared rules in this repo’s `AGENTS.md` linked home-wide | Homelab + coding conventions that span projects |
| **Project** | `.agents/skills/`, `.cursor/skills/`, or project `AGENTS.md` | Repo-specific SOPs, contest rules, private product domain |

Rule of thumb: if it would be wrong in another repo, keep it **project-local**. If it prevents breakage everywhere, keep it **agent-wide**.

---

## License

See [LICENSE](LICENSE). Submodules keep their own licenses.
