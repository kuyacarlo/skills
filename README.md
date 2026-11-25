# Skills

This repository owns portable skills and the scripts that install them.
Personal identity, host details, and work preferences live in the private
`personal-context` repository. Its companion `personal-context` skill reads
those files only when a task needs them.

## Install

- Run `./apply` to choose skills interactively.
- Run `./apply -y` to enable every skill and refresh its links.
- Run `SKIP_KARLO_SYNC=1 ./apply -y` to refresh skill links without installing
  the optional sync helper and timer.

`apply` creates harness-specific symlinks. It always creates `~/.agents/skills`
for shared skill discovery, then links skills under each installed harness.
It links `AGENTS.md` and `harness-context.md` where those files apply. It links
`GEMINI.md` for Gemini and Antigravity. It links the context-health helper into
Cursor's `agents/` directory. Claude gets skill links only; the script does not
add global Claude instructions.

The private context folder remains a separate downstream working area. The
installer does not replace or synchronize `~/.config/karlo`.

## Maintain

- Run `FORCE_ALL=1 ./scripts/package_skills.sh` to rebuild every skill package.
- Run `./scripts/check_readme_skills.sh` to compare the list below with skill
  folders.
- Run `./scripts/check_slop_examples.sh` after changing `anti-slop-design/examples`.
  Slop pages must fail impeccable; clean regions must pass the browser probe
  (set `PUPPETEER_MODULE` and `PUPPETEER_EXECUTABLE_PATH`).
- Keep examples synthetic. Never include private context or secrets.
- Keep source and retirement notes in [ORIGINS.md](ORIGINS.md).

## Simulate and evaluate

Use [the evaluation handbook](docs/skill-evaluation.md) to compare matched runs
with and without a skill. It includes a rubric and synthetic starter cases for
`personal-context`. Keep fixtures generic and do not include private profile
data or conversation logs.

## Live skills

| Skill | Role |
|-------|------|
| `agent-fleet` | Multi-agent claims, trees, queues, and worktree reconciliation |
| `engineering-rulebook` | Engineering safety, branches, proof, operations, and lessons |
| `personal-context` | Personal settings, focus support, report structure, technical prose |
| `saas-readiness-audit` | Evidence-backed SaaS launch-readiness audit with runner and evals |
| `ef-starter` | Executive-function system builder (upstream submodule) |
| `feature-plan` | Feature planning and handoff documentation |
| `idea-generator` | Generate, compare, and evaluate ideas |
| `anti-slop-design` | Anti-slop UI rules, replacements, and a pre-ship checklist |
| `specification-pipeline` | Requirements, specifications, plans, tasks, and drift audits |
| `ui-design` | Grill, redesign, and prove UI (process; taste in personal context) |

Detailed guides load only for matching tasks. Credits and submodule policy:
[ORIGINS.md](ORIGINS.md).

## Boundaries

| Scope | Source |
|-------|--------|
| Portable skills and adapters | This repository |
| Personal context | Private `~/.config/karlo` checkout |
| Project rules | The project's own `AGENTS.md` and skill links |

If a rule is only valid for one repository, keep it with that project.

## License

See [LICENSE](LICENSE). Submodules keep their own licenses.
