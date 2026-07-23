# Origins

Policy:

- **Works well as-is and not heavy** → git submodule (keep upstream title).
- **Can be smaller / renamed for clarity** → local reframe + credit here.
- **Private end-to-end factories** → stay in their own repos; they may depend on *this* pack. Never copy them into `skills/`.

| Local skill | Kind | Upstream / source |
|-------------|------|-------------------|
| `ef-starter` | submodule | [DoxxedDoxie/ef-skill](https://github.com/DoxxedDoxie/ef-skill) |
| `code-simplification` | reframe | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) |
| `output-compression` | reframe | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) |
| `specification-compliance` | reframe | [JuliusBrussee/cavekit](https://github.com/JuliusBrussee/cavekit) |
| `specification-pipeline` | reframe | [github/spec-kit](https://github.com/github/spec-kit) (thin wrapper + refs) |
| `idea-generator` | reframe | Personal ideation slice (not a product factory) |
| `idea-evaluation` | original | — |
| `focus-management` | original | — |
| `architectural-planning` | original | — |
| `continuous-improvement` | original | — |
| `developer-profile` | original | Generator only; personal data lives outside the skill |
| `personal-context` | original | Points at `~/.config/karlo/` (or `PERSONAL_CONTEXT_PATH`) |
| `email-management` | original | — |
| `git-signed-commit` | original | — |
| `free-tier-deploy` | reframe | Generalized from Fly ops patterns + CF Workers / Vercel / Railway |
| `thorough-code-review` | reframe | Process generalized; no product-domain content |
| `parallel-work-planning` | reframe | Process generalized; no product-domain content |

Optional installs (not vendored):

- [mattpocock/skills](https://github.com/mattpocock/skills) via `npx skills add mattpocock/skills`
