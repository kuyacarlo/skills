# Skills

Installable agent skills for Cursor / Claude / Gemini / Kiro / Codex and other
local harnesses.

```bash
./apply -y        # enable all, deploy
./apply           # interactive
FORCE_ALL=1 ./scripts/package_skills.sh   # rebuild dist/*.skill
```

Symlinks land under `~/.agents`, `~/.gemini/config`, `~/.cursor`, `~/.copilot`,
`~/.kiro`, … when present. `apply` never touches `~/.claude` (Claude Code is out
of scope for this pack).
Pack defaults: technical prose rules always apply; focus guidance auto-triggers when the user is stuck or low-energy.

---

## Live skills

| Skill | Role |
|-------|------|
| `agent-fleet` | Multi-agent claims, trees, file work queue |
| `engineering-rulebook` | Action boundaries, branch closeout, YAGNI, proof, durable lessons |
| `personal-context` | Load `~/.config/karlo`; focus, report, and prose guides (data stays outside skills) |
| `ef-starter` | Executive-function system (submodule) |
| `specification-pipeline` | specify → clarify → plan → implement |
| `idea-generator` | Generate, compare, and evaluate ideas |

Detailed guides load only for matching tasks, keeping the default skill context small.

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
