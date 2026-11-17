#!/usr/bin/env bash
# Runs every fixture in evals/fixtures against its expected/<name>.json.
# Usage: bash evals/run-evals.sh [fixture-name]   (needs node >= 20, git, pnpm or npm)
set -euo pipefail
SKILL="$(cd "$(dirname "$0")/.." && pwd)"
names=("${1:-}"); [ -z "${names[0]}" ] && names=($(ls "$SKILL/evals/fixtures"))
fail=0
for n in "${names[@]}"; do
  work="$(mktemp -d)/$n"; cp -r "$SKILL/evals/fixtures/$n" "$work"; cd "$work"
  if command -v pnpm >/dev/null; then pnpm install --silent >/dev/null; else npm install --silent >/dev/null; fi
  git init -q && git add -A && git -c user.email=eval@local -c user.name=eval commit -qm fixture
  echo "== $n: compile dry-run"
  READINESS_PHASE=compile node "$SKILL/scripts/runner.mjs" . >/dev/null
  if grep -q '"status":"ERROR"' .readiness/runs/*-compile/findings.jsonl; then echo "  broken probes (ERROR on dry-run)"; fail=1; fi
  echo "== $n: audit"
  READINESS_PHASE=audit node "$SKILL/scripts/runner.mjs" .
  run=$(ls -d .readiness/runs/*-audit | sort | tail -1)
  node "$SKILL/scripts/score.mjs" . "$run" "$SKILL/evals/expected/$n.json" | tee /tmp/score-$n.txt
  grep -qE 'FALSE-PASS: 0' /tmp/score-$n.txt || fail=1
  grep -qE '^\s+FAIL ' /tmp/score-$n.txt && fail=1 || true
  echo "  workdir: $work"
done
exit $fail
