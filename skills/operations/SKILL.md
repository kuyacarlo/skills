---
name: operations
author: kaoru
version: "1.0.0"
description: >-
  Global agent operational rules. Enforces commit discipline, GPG signing,
  session start/end protocol, inventory checks, and audit logging. Always active.
  Use on every session start, before first action, and before session end.
  Triggers on session start, commit, signing, checkpoint, audit, inventory check,
  dirty state, WIP, context loss, restart risk.
---

# Operations

Operational baseline for all agent sessions. Prevents work loss, enforces
signing, maintains an audit trail. Applies regardless of project, agent,
or model.

Config home: `$AGENT_CONFIG_HOME` (default `~/.config/karlo`).

## Session start

1. Run `git status`. Report if dirty.
2. Uncommitted changes from a prior session: commit before new work.
3. Read last 1-3 entries of `$AGENT_CONFIG_HOME/AUDIT.md` for continuity.
4. HEAD detached or branch >1 week stale: mention it.
5. Unfamiliar repo or long gap: run inventory checks.

## Commit discipline

Group related changes into one cohesive commit. One commit should tell one
story: "added auth middleware", "modernized all skills", "fixed DNS config."

1. Batch 3-5 related file changes into a single commit.
2. Each commit has one clear purpose. If the message needs "and" to describe
   two unrelated things, split it.
3. Stage specific files. Never `git add .` or `git add -A` unless told to.
4. Concise subject line (under 72 chars). Add body for multi-file context.
5. Do not leave dirty state for more than one logical task. Finish the unit,
   commit, move on.
6. Context about to be lost (restart, token limit): commit immediately as WIP.

## Signing

1. All commits signed. `commit.gpgsign = true` is global. Do not override.
2. Signing fails: stop and report. Do not commit unsigned.
3. Never `--no-verify` unless user says to skip hooks.

## Authentication

The user authenticates via SSH and GPG. Do not change these:

- **Git remote**: SSH (`git@github.com:...`). Do not switch to HTTPS.
- **Commit signing**: GPG (ed25519 key). Auto-signs via global config.
- **Push**: requires SSH agent with loaded key. If push fails with permission
  error, report — do not attempt HTTPS fallback or credential helpers.

## Guardrails

1. Never force-push without explicit permission.
2. Never amend a pushed commit.
3. Destructive operations (reset, clean, branch -D, drop): stash or confirm.
4. Never commit secrets, tokens, or .env files.
5. Do not modify files outside the working project unless the task requires it.

## Inventory checks

Run on unfamiliar repo or after a long gap:

1. Build/test config: `package.json`, `Makefile`, `Cargo.toml`, `pyproject.toml`.
2. CI: `.github/workflows/`, `.gitlab-ci.yml`.
3. Contract: `SPEC.md`, `AGENTS.md`.
4. Branch: on main? Should we branch first?

## Session end

1. Commit all pending work. No dirty state left.
2. Append entry to `$AGENT_CONFIG_HOME/AUDIT.md` (format: [references/audit-format.md](references/audit-format.md)).
3. Incomplete work: note in audit entry and leave TODO in code.

## Recovery

1. Build fails: fix before moving on.
2. Cannot fix in 2 attempts: revert and explain.
3. Context dying: commit WIP immediately.

## Priority

These rules override agent defaults.
