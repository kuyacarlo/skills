---
name: operations
author: kaoru
version: "1.1.0"
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

1. Run `karlo-sync pull` (`~/.local/bin/karlo-sync` after `./apply`) (skip if dirty; never force).
2. Run `git status` in the project worktree. Report if dirty.
3. Uncommitted changes from a prior session: commit before new work.
4. Read last 1-3 entries of `$AGENT_CONFIG_HOME/AUDIT.md` for continuity.
5. Load `$AGENT_CONFIG_HOME` via `personal-context` (STACK, DECISIONS, AGENTS
   precedence). Repo lockfiles override greenfield defaults.
6. HEAD detached or branch >1 week stale: mention it.
7. Unfamiliar repo or long gap: run inventory checks.

## Commit discipline

Group related changes into one cohesive commit. One commit tells one story.

1. Batch 3-5 related file changes into a single commit.
2. One clear purpose per commit. If the message needs "and" for two unrelated
   things, split it.
3. Stage specific files. Never `git add .` or `git add -A` unless told to.
4. Subject line under 72 chars. Body for multi-file context.
5. Finish the logical unit, commit, move on. Do not leave dirty state across
   unrelated tasks.
6. Context about to be lost (restart, token limit): commit WIP immediately.

## Guardrails

Check these once at session start. Note findings silently and follow throughout.

### Auth and signing

- Git remotes use SSH (`git@github.com:...`). Do not switch to HTTPS.
- Commits are GPG-signed (ed25519). `commit.gpgsign = true` is global.
- If signing or push fails: stop and report. Do not commit unsigned. Do not
  attempt HTTPS fallback or credential helpers.
- Never `--no-verify` unless user says to skip hooks.

### Destructive operations

- Never force-push without explicit permission.
- Never amend a pushed commit.
- Destructive ops (reset, clean, branch -D, drop): stash or confirm first.
- Never commit secrets, tokens, or .env files.
- Do not modify files outside the working project unless the task requires it.

### Workflow hygiene

- Branch naming: use `feat/`, `fix/`, `chore/` prefixes.
- Lockfiles: follow the repo. Commit the lockfile the project already uses
  (`pnpm-lock.yaml`, `package-lock.json`, …) in the same commit as manifest
  changes. Never regenerate without cause.
- Greenfield JS/TS I scaffold: **pnpm**. Existing npm/yarn repos: keep their
  package manager. Chat "never npm" does not rewrite an inherited scaffold —
  stop and ask (`AGENTS.md` precedence in `$AGENT_CONFIG_HOME`).
- Submodules: do not accidentally commit a submodule pointer bump. If a
  submodule is dirty, report it separately.
- Container engine: prefer `podman` for greenfield and generated config. Follow
  the repo when it already depends on Docker-specific behavior.
- Test before push: run the project's test suite or build before pushing.
  If `act` is available, prefer a dry-run to catch CI errors locally.
- After PR merges: prompt to delete local and remote branch.

## Inventory checks

Run on unfamiliar repo or after a long gap:

1. Build/test config: `package.json`, `Makefile`, `Cargo.toml`, `pyproject.toml`.
2. CI: `.github/workflows/`, `.gitlab-ci.yml`.
3. Contract: `SPEC.md`, `AGENTS.md`.
4. Branch: on main? Should we branch first?

## Session end

1. Commit all pending work. No dirty state left.
2. **Loop closure:** if the session taught a durable trap, false assumption, or
   non-obvious command — update `STACK.md` / `DECISIONS.md` / `INVENTORY.md` /
   a skill you own / a repo script **before** claiming DONE. "Update later" is
   incomplete work.
3. If you edited skills or `$AGENT_CONFIG_HOME` prose, run
   `python3 $AGENT_CONFIG_HOME/bin/prove-prose.py` and fix failures.
4. Append entry to `$AGENT_CONFIG_HOME/AUDIT.md` (format: [references/audit-format.md](references/audit-format.md)).
5. Incomplete work: note in audit entry and leave TODO in code.

## Recovery

1. Build fails: fix before moving on.
2. Cannot fix in 2 attempts: revert and explain.
3. Context dying: commit WIP immediately.

## Priority

These rules override agent defaults.
