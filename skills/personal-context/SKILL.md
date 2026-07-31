---
name: personal-context
author: kaoru
version: "1.0.0"
description: >-
  Loads the user's personal systems, background, stack, and constraints from a
  context file so agents stop re-asking. Use when starting work, choosing stacks,
  planning projects, or when demotivated — read personal context before guessing.
  Triggers on personal context, about me, my stack, my systems, homelab defaults.
---

# Personal Context

Keep who the user is out of skill bodies. Skills stay portable; context stays local.

## Locate context

Config home: `$AGENT_CONFIG_HOME` (default `~/.config/karlo`).

Resolve in order:

1. `$AGENT_CONFIG_HOME/CONTEXT.md` (short identity + defaults)
2. `$AGENT_CONFIG_HOME/INVENTORY.md` (canonical profile + tools + hosts)
3. `$AGENT_CONFIG_HOME/AGENTS.md` (interaction preferences)
4. `$AGENT_CONFIG_HOME/SKILLS.md` (global vs scoped skill boundaries)
5. `$AGENT_CONFIG_HOME/OPERATIONS.md` (commit discipline, signing, session protocol)
6. `$AGENT_CONFIG_HOME/AUDIT.md` (session log — read last 1-3 entries only)
7. `$AGENT_CONFIG_HOME/agy-context.json` (machine profile)
8. Repo `context/CONTEXT.md` only if the user said this project owns it

If none exist: run `developer-profile` to generate artifacts, then write `CONTEXT.md`.

## Always read (when this skill is active)

From context, extract and apply:

- Drive: love of the game first; money is cherry on top
- Primary stack + hard skips (e.g. Podman not Docker, self-hosted > SaaS)
- Time/energy constraints (student schedule, ADHD protocols)
- Homelab / infra defaults (thinkpad / idea / andromeda — see INVENTORY)
- Operational rules: commit discipline, signing, guardrails (see OPERATIONS)
- Session continuity: last audit entries for what happened recently (see AUDIT)
- "When demotivated" protocol (hand off to `focus-management`)
- Skills scope: never load Millia/work skills outside `~/work/millia/`

Do not paste the entire context into every reply. Use it silently for decisions.
Prefer INVENTORY + AGENTS for "who am I / what tools / how to talk to me."

## Maintenance

1. Update after shipping major projects (every few months).
2. Never commit private `~/.config/karlo/*` into the public skills repo.
3. Public skill pack may ship `examples/CONTEXT.template.md` only.
