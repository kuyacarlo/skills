---
name: developer-profile
description: >-
  Generates a quantified developer profile and agent integration files. Use when
  setting up personal context, onboarding agents to a developer, or refreshing
  stack/constraint docs. Writes artifacts under ~/.config (or chosen path) — does
  not keep personal data inside this skill.
---

# Developer Profile (generator)

**Two parts:**

1. **Generator (this skill)** — interview + write artifacts  
2. **Downstream** — agents read those artifacts via `personal-context`

## Output targets

Prefer:

| Artifact | Path |
|----------|------|
| Human context | `~/.config/karlo/CONTEXT.md` |
| Machine JSON | `~/.config/karlo/agy-context.json` |
| Optional chat paste | `ABOUT_ME.md` (only if user asks) |

Template: [examples/CONTEXT.template.md](../../examples/CONTEXT.template.md)  
Full worked example (reference only): [examples/developer-profile.full.example.md](../../examples/developer-profile.full.example.md)

## Process

1. Detect tools in use (Antigravity/agy, Cursor, Gemini, etc.).
2. Collect: shipped projects, stack, constraints, will-build/will-skip, pain points.
3. Write `CONTEXT.md` (short) + JSON profile (structured).
4. Tell the user to rely on `personal-context` going forward — do not re-embed the profile into skills.

## Rules

- Never commit private profiles into the public skills repo.
- Keep `CONTEXT.md` under ~100 lines; put deep examples in JSON or dated notes.
- After generation, smoke-test: ask an agent for a stack recommendation using only the new files.
