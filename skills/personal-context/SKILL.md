---
name: personal-context
description: >-
  Loads the user's personal systems, background, stack, and constraints from a
  context file so agents stop re-asking. Use when starting work, choosing stacks,
  planning projects, or when demotivated — read personal context before guessing.
  Triggers on personal context, about me, my stack, my systems, homelab defaults.
---

# Personal Context

Keep **who the user is** out of skill bodies. Skills stay portable; context stays local.

## Locate context

Resolve in order:

1. `$PERSONAL_CONTEXT_PATH` if set
2. `~/.config/karlo/CONTEXT.md` (preferred human-readable)
3. `~/.config/karlo/agy-context.json` (machine profile)
4. Repo `context/CONTEXT.md` only if the user said this project owns it

If none exist: run `developer-profile` to generate artifacts, then write `CONTEXT.md`.

## Always read (when this skill is active)

From context, extract and apply:

- Primary stack + hard skips (e.g. Podman not Docker, self-hosted > SaaS)
- Time/energy constraints (student schedule, ADHD protocols)
- Homelab / infra defaults
- “When demotivated” protocol (hand off to `focus-management`)

Do **not** paste the entire context into every reply. Use it silently for decisions.

## Maintenance

- Update after shipping major projects (every few months)
- Never commit private `~/.config/karlo/*` into the public skills repo
- Public skill pack may ship `examples/CONTEXT.template.md` only
