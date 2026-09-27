# Skills

Installable agent skills for local harnesses (Agents, Gemini/Antigravity, Cursor,
Copilot). Personal data stays in `~/.config/karlo`, not in this repository.

- `./apply -y` enables all skills and deploys them. It also installs `karlo-sync`.
- `./apply` opens the interactive setup.
- `FORCE_ALL=1 ./scripts/package_skills.sh` rebuilds skill packages.
- `./scripts/check_readme_skills.sh` checks this table against the skill folders.

## Personal context sync

`./apply` installs `karlo-sync`, a personal-context pull and push helper.

| Install | Path |
|---------|------|
| PATH | `~/.local/bin/karlo-sync` → `scripts/karlo-sync` |
| Cursor hook | `~/.cursor/hooks/karlo-sync-session.sh` |
| systemd | `~/.config/systemd/user/karlo-context-pull.{service,timer}` |

Pull runs when the tree is clean. Push stays explicit. See private `SYNC.md` in
`karlo-context` before wiring Cursor session hooks.

## What `./apply` deploys

Symlinks land only under supported roots that already exist:

| Target | Path |
|--------|------|
| Agents | `~/.agents/skills/` |
| Gemini / Antigravity | `~/.gemini/config/skills/` |
| Cursor | `~/.cursor/skills/` |
| Copilot | `~/.copilot/skills/` |

The installer also links this repository's `AGENTS.md` into each target root.
It does not manage Claude, Codex, Kiro, Qwen, or Cursor product skills.

Technical prose follows the pack's short-sentence defaults. Detailed prose and
focus guidance load from personal-context only when the task calls for them.

Cursor agents that load `~/.agents/skills` pick up this pack after `./apply`.

---

## Live skills

| Skill | Role |
|-------|------|
| `agent-fleet` | Multi-agent claims, trees, queues, and worktree reconciliation |
| `engineering-rulebook` | Engineering safety, branches, YAGNI, proof, live operations, lessons |
| `personal-context` | Personal settings, focus support, report structure, technical prose |
| `ef-starter` | Executive-function system builder (upstream submodule) |
| `idea-generator` | Generate, compare, and evaluate ideas |
| `specification-pipeline` | Requirements, specifications, plans, tasks, implementation, drift audits |

Detailed guides load only for matching tasks, keeping default skill context small.

Credits and submodule policy: [ORIGINS.md](ORIGINS.md).

---

## Scope

| Scope | Where |
|-------|--------|
| Agent-wide | `./apply` → supported home skill directories |
| Personal context | Private `~/.config/karlo` (Forgejo `karlo-context`) |
| Project | `.agents/skills`, repository `AGENTS.md` |

If a rule would be wrong in another repository, keep it project-local.

## License

See [LICENSE](LICENSE). Submodules keep their own licenses.
