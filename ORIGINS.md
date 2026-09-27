# Origins

Policy:

- **Works well as-is and not heavy** → git submodule (keep upstream title).
- **Can be smaller / renamed for clarity** → local reframe + credit here.
- **Private end-to-end factories** → stay in their own repos; never vendor into `skills/`.

| Local skill | Kind | Upstream / source |
|-------------|------|-------------------|
| `ef-starter` | submodule | [DoxxedDoxie/ef-skill](https://github.com/DoxxedDoxie/ef-skill) |
| `specification-pipeline` | reframe | [github/spec-kit](https://github.com/github/spec-kit); includes compliance guidance from [JuliusBrussee/cavekit](https://github.com/JuliusBrussee/cavekit) |
| `idea-generator` | reframe | Personal ideation and evaluation workflow |
| `personal-context` | original | `~/.config/karlo/` |
| `agent-fleet` | original | — |
| `engineering-rulebook` | original | — |

## Retired (2026-08-10)

| Skill | Why removed |
|-------|-------------|
| `output-compression` | Overlaps STE; thin caveman reframe |
| `email-management` | Niche, unused |
| `parallel-work-planning` | Superseded by `agent-fleet` + engineering-rulebook handoff guide |

## Consolidated (2026-09-27)

| Skill | Kept in |
|-------|---------|
| `idea-generator`, `idea-evaluation` | `idea-generator` |
| `specification-compliance` | `specification-pipeline` |
| `operations`, `verification-before-completion` | `engineering-rulebook` |
| `context-handoff` | engineering-rulebook handoff guide |
| `developer-profile` setup flow | `personal-context` |
| `continuous-improvement` | `engineering-rulebook` proof and lesson guides |
| `branch-lifecycle` | `engineering-rulebook` reference; original workflow |
| `code-simplification` | `engineering-rulebook` reference; reframe of [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) |
| `focus-management` | `personal-context` reference; original workflow |
| `numbers-first-report` | `personal-context` reference; original Freestack report pattern |
| `simplified-technical-english` | `personal-context` reference; ASD-STE100 practice |

## Retired (2026-09-27)

| Skill | Why removed |
|-------|-------------|
| `architectural-planning` | General planning is covered by native plan modes; use the specification pipeline for durable artifacts. |
| `thorough-code-review` | Generic review wrapper duplicates host review tools and baseline agent capability. |
| `free-tier-deploy` | Hosting offers and limits change; use current provider docs and live research. |
| `git-signed-commit` | Signing policy and profile setup are personal and repo-local. |

Optional external: [mattpocock/skills](https://github.com/mattpocock/skills).
