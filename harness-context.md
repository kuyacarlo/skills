# Shared harness context

This file is linked into harness skill stores by `apply`.

Personal context lives at `$AGENT_CONFIG_HOME` (default `~/.config/karlo`). Load it progressively:

1. `CONTEXT.md` for identity and defaults.
2. `AGENTS.md` for communication and precedence.
3. Task-specific files only when needed.

Questions do not require Git status checks, commits, audits, or fleet setup. Engineering changes require permission and isolation checks before delegation. Existing project tooling wins over greenfield defaults. Preserve unrelated work.

Harness-local memory is not portable memory. Route durable lessons to repository docs, `INVENTORY.md`, `OPERATIONS.md`, `DECISIONS.md`, or the owning skill.
