---
name: operations
metadata:
  author: kaoru
  version: "1.0.0"
description: "Operational guidance for engineering changes, commits, deployments, and substantive handoffs. Not needed for greetings, identity questions, or read-only explanations."
---

# Operations

Apply to engineering work. Do not turn conversational questions into repository maintenance.
Config home: `$AGENT_CONFIG_HOME`, default `~/.config/karlo`.

## Canonical local policy

Read local AGENTS.md for precedence, tooling defaults, signing, and delivery preferences.
Read local OPERATIONS.md for capability checks, verification, session protocol, and fleet coordination.
Reuse these files when already loaded. Do not duplicate their rules here.
These files remain subject to host instructions, permissions, and explicit user instructions.

## Portable fallback

When local policy is absent:
- Inspect repository status before editing. Preserve pre-existing changes.
- Follow established repository tooling unless the user authorizes a change.
- Check writable paths and approval requirements before mutations.
- Before delegation, verify authorization and isolation. Spawning does not imply a separate worktree.
- Use supported budget controls; identify prompt-only limits as advisory.
- Verify the changed behavior and report any untested scope.
- Commit only identified task changes when authorized. Never force a clean tree by committing unrelated work.
- Preserve signing requirements. If signing fails, keep the work and report the failure.
- Do not push, merge, or rewrite shared history without applicable authorization.
- Record useful handoffs and durable lessons within writable, authorized paths.
- If personal maintenance is blocked, prepare the update in the workspace and report it separately.

Use [the audit format](references/audit-format.md) only when recording a substantive engineering session.
Do not create audit entries for greetings or routine read-only answers.
