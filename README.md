# Skills

Installable agent skills for local harnesses (Agents, Gemini/Antigravity, Cursor,
Copilot). Personal data stays in `~/.config/karlo` — not in this repo.

```bash
./apply -y        # enable all, deploy (+ install karlo-sync)
./apply           # interactive
FORCE_ALL=1 ./scripts/package_skills.sh   # rebuild dist/*.skill
./scripts/check_readme_skills.sh          # README table vs skills/ must match
```

`./apply` also installs **`karlo-sync`** (personal-context git pull/push helper):

| Install | Path |
|---------|------|
| PATH | `~/.local/bin/karlo-sync` → `scripts/karlo-sync` |
| Cursor hook | `~/.cursor/hooks/karlo-sync-session.sh` |
| systemd | `~/.config/systemd/user/karlo-context-pull.{service,timer}` (enabled when possible) |

Wire `sessionStart` / `sessionEnd` in `~/.cursor/hooks.json` to `./hooks/karlo-sync-session.sh` once (see private `SYNC.md` in karlo-context). Pull is automatic when the tree is clean; push stays explicit.

## What `./apply` actually deploys

Symlinks land only under these roots **when the directory already exists**:

| Target | Path |
|--------|------|
| Agents | `~/.agents/skills/` |
| Gemini / Antigravity | `~/.gemini/config/skills/` |
| Cursor | `~/.cursor/skills/` |
| Copilot | `~/.copilot/skills/` |

Also links this repo's `AGENTS.md` into each target root.

**Not managed by `./apply`:** `~/.claude`, `~/.codex`, `~/.kiro`, `~/.qwen`,
`~/.agent`, and Cursor's product dir `~/.cursor/skills-cursor`. Those are
vendor/manual. Claude Code skills stay out of this installer on purpose — do not
edit vendor symlinks in place; point lessons at a skill you own or at
`~/.config/karlo`.

Pack default: **`simplified-technical-english`** always deploys when enabled (default).

Cursor agents that load `~/.agents/skills` pick up this pack after `./apply`.

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
| `code-simplification` | YAGNI prune |
| `context-handoff` | HANDOFF.md across agent/tool switches |
| `continuous-improvement` | `.agents/LEARNINGS.md` loop |
| `idea-generator` | Hackathon ideation only |
| `idea-evaluation` | Go / No-Go / Pivot |
| `numbers-first-report` | Blunt gap / research reports (counts → P0–P3 → skip → GO wave) |
| `free-tier-deploy` | CF / Vercel / Fly / Railway / Render |
| `git-signed-commit` | GPG / profiles / SSH host aliases |
| `idea-evaluation` | Go / No-Go / Pivot |
| `idea-generator` | Hackathon ideation only |
| `operations` | Commits, signing, session start/end, loop closure |
| `personal-context` | Load `~/.config/karlo` (data stays outside skills) |
| `simplified-technical-english` | Default dense prose (always on) |
| `specification-compliance` | SPEC.md drift checks |
| `specification-pipeline` | specify → clarify → plan → implement |
| `thorough-code-review` | Citation-style review |

\* Auto: STE always on; `focus-management` on stuck/low-energy language.

Credits / submodule policy: [ORIGINS.md](ORIGINS.md).

---

## Scope

| Scope | Where |
|-------|--------|
| Agent-wide | `./apply` → home skill dirs above |
| Personal context | Private `~/.config/karlo` (Forgejo `karlo-context`) |
| Project | `.agents/skills`, repo `AGENTS.md` |

If it would be wrong in another repo, keep it project-local.

## License

See [LICENSE](LICENSE). Submodules keep their own licenses.
