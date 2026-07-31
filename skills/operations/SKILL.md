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

Persistent operational baseline for all agent sessions. These rules prevent
work loss, enforce signing, and maintain an audit trail. They apply regardless
of project, agent, or model.

## Session start protocol

1. Run `git status` in the working directory. Report if dirty.
2. If uncommitted changes exist from a prior session, commit them before new work.
3. Read the last 1-3 entries of `~/.config/karlo/AUDIT.md` for continuity.
4. If HEAD is detached or the branch is >1 week stale, mention it.
5. Run inventory checks (see below) if the repo is unfamiliar or after a long gap.

## Commit discipline

1. Commit after every meaningful unit: file created, function complete, test passing, config changed.
2. Never accumulate more than 3 modified files without committing.
3. Never go more than 15 minutes of active work without a checkpoint commit.
4. Stage specific files only. Never `git add .` or `git add -A` unless explicitly told to.
5. Concise single-line messages. Body only for multi-file changes.
6. If a commit message needs two topics, it should have been two commits.

## Signing

1. All commits are signed. `commit.gpgsign = true` is global — do not override.
2. If signing fails, stop and report. Do not commit unsigned.
3. Never use `--no-verify` unless the user explicitly says to skip hooks.

## Guardrails

1. Never force-push without explicit permission.
2. Never amend a pushed commit.
3. Before destructive operations (reset, clean, branch -D, drop table), stash or confirm.
4. Never commit secrets, tokens, or .env files.
5. Do not modify files outside the working project unless the task requires it.

## Inventory checks

Run when starting in an unfamiliar repo or after a long gap:

1. Build/test config: `package.json`, `Makefile`, `Cargo.toml`, `pyproject.toml`, etc.
2. CI presence: `.github/workflows/`, `.gitlab-ci.yml`.
3. Contract file: `SPEC.md`, `AGENTS.md`, or similar.
4. Branch protection: are we on main? Should we branch first?

## Session end protocol

1. Commit all pending work. Do not leave dirty state.
2. Append an entry to `~/.config/karlo/AUDIT.md` (see [references/audit-format.md](references/audit-format.md)).
3. If work is incomplete, note it in the audit entry and leave a TODO in code.

## When things break

1. Build fails after your change — fix before moving on.
2. Cannot fix in 2 attempts — revert last commit and explain.
3. Context about to be lost (restart, token limit) — commit immediately. WIP is better than lost.

## Priority

These rules override agent defaults. If built-in behavior conflicts (e.g., wanting to batch changes), these rules win.
