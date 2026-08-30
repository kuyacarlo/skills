#!/usr/bin/env bash
# Cursor sessionStart/sessionEnd hook: auto-pull personal context when clean.
# Fail-open. Never blocks the agent. Never auto-commits (signing stays explicit).
set -euo pipefail

# Consume hook stdin (JSON event payload)
cat >/dev/null 2>&1 || true

SYNC="${AGENT_CONFIG_HOME:-$HOME/.config/karlo}/bin/context-sync"
EVENT="${CURSOR_HOOK_EVENT_NAME:-sessionStart}"

if [ ! -x "$SYNC" ]; then
  printf '%s\n' '{"additional_context":"context-sync missing; personal context not auto-pulled."}'
  exit 0
fi

# Pull on start (and on end as a cheap catch-up if another device pushed).
# --skills optional via KARLO_SYNC_SKILLS=1
extra=()
if [ "${KARLO_SYNC_SKILLS:-0}" = "1" ]; then
  extra+=(--skills)
fi

out="$("$SYNC" pull --json "${extra[@]}" 2>/tmp/context-sync-hook.err || true)"
karlo="$(printf '%s' "$out" | sed -n 's/.*"karlo":"\([^"]*\)".*/\1/p')"
skills="$(printf '%s' "$out" | sed -n 's/.*"skills":"\([^"]*\)".*/\1/p')"
err="$(tr '\n' ' ' </tmp/context-sync-hook.err 2>/dev/null || true)"

ctx="context-sync ($EVENT): karlo=${karlo:-unknown}"
if [ -n "$skills" ] && [ "$skills" != "skipped" ]; then
  ctx="$ctx; skills=$skills"
fi
if [ -n "$err" ]; then
  ctx="$ctx. $err"
fi
ctx="$ctx. Auto-pull only when clean; commit+push still explicit (GPG)."

# Escape for JSON string
ctx_esc="$(printf '%s' "$ctx" | python3 -c 'import json,sys; print(json.dumps(sys.stdin.read())[1:-1])')"

printf '{"env":{"KARLO_SYNC_LAST":"%s","KARLO_SYNC_SKILLS_LAST":"%s"},"additional_context":"%s"}\n' \
  "${karlo:-unknown}" "${skills:-skipped}" "$ctx_esc"
exit 0
