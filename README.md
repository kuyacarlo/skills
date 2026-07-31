# Skills

Personal + installable agent skills for Antigravity / Gemini / Cursor / Copilot / Claude / Codex / and other local harnesses when present.

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
| Agents | `~/.agents/skills/` |
| Gemini / Antigravity | `~/.gemini/config/skills/` |
| Cursor | `~/.cursor/skills/` |
| Copilot | `~/.copilot/skills/` |
| Claude Code | `~/.claude/skills/` |
| Codex | `~/.codex/skills/` |
| Qwen | `~/.qwen/skills/` |
| Kiro | `~/.kiro/skills/` |
| Agent | `~/.agent/skills/` |

Also links `AGENTS.md` into those roots. Pack default `simplified-technical-english` always deploys.

---

## Skill packages (`.skill`)

Each skill can be shipped as a zip renamed to `.skill` (SKILL.md at archive root).

```bash
FORCE_ALL=1 ./scripts/package_skills.sh   # rebuild all → dist/*.skill
./scripts/package_skills.sh               # only changed skills, or missing packages
```

CI (`.github/workflows/package-skills.yml`) runs on every push:

1. Detect changes under `skills/<name>/`
2. Rebuild `dist/<name>.skill` when that skill changed
3. If unchanged, skip — unless `dist/<name>.skill` is missing
4. Upload built packages as workflow artifacts

Manual full rebuild: Actions → **Package skills** → Run workflow → `force_all=true`.

---

## Live skills

| Skill | Role | Invoke |
|-------|------|--------|
| `architectural-planning` | Mermaid plans, milestones, task matrices | user |
| `code-simplification` | YAGNI / decision-ladder prune (ponytail-inspired) | model |
| `simplified-technical-english` | Default technical prose (ASD-STE100 Issue 9 practice) | model* |
| `developer-profile` | Generate portable profile artifacts for agents | user / setup |
| `ef-starter` | Executive-function system builder (submodule) | user |
| `focus-management` | Energy diagnosis, reconnect logs, low-activation defaults | model* |
| `idea-evaluation` | Go / No-Go / Pivot grill | model |
| `idea-generator` | Hackathon **ideation only** (not a full product factory) | user |
| `specification-compliance` | SPEC.md drift / contract checks | model |
| `specification-pipeline` | specify → clarify → plan → implement chain | user |
| `free-tier-deploy` | Cloudflare / Vercel / Fly / Railway free-tier deploy patterns | model |
| `personal-context` | Load systems/background context; keep data out of skill bodies | model |
| `thorough-code-review` | Exhaustive citation-style review (generalized) | user |

\* Auto-reach / always-on: `simplified-technical-english` is the pack default (always deployed by `./apply`). `focus-management` triggers on demotivation / stuck language.

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
