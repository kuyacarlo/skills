#!/usr/bin/env bash
# Regression check for the anti-slop-design examples.
# 1. Shared clean CSS has no px.  2. impeccable: slop pages fail, the fixed landing passes.
# 3. Browser probe (needs puppeteer): text floor, no px, no overflow, slop zones present.
# Env: PUPPETEER_MODULE (path to a puppeteer install), PUPPETEER_EXECUTABLE_PATH (Chrome).
set -uo pipefail
cd "$(dirname "$0")/.."
EX=skills/anti-slop-design/examples
fail=0

# Shared stylesheet for clean regions must be px-free.
if grep -nE '[0-9]px' "$EX/assets/site.css"; then echo "FAIL: px in $EX/assets/site.css"; fail=1; else echo "ok   site.css has no px"; fi

# impeccable static scan: every slop page must still fail; the fixed landing must pass.
if command -v npx >/dev/null; then
  for f in "$EX"/*.html; do
    # impeccable exits non-zero when it finds anything, so read its JSON regardless of exit code.
    out=$(npx -y impeccable detect --json --no-advisory "$f" 2>/dev/null || true)
    n=$(printf '%s' "$out" | python3 -I -c 'import json,sys; print(len(json.load(sys.stdin)))' 2>/dev/null || echo "?")
    name=$(basename "$f")
    if [ "$name" = landing-fixed.html ]; then
      [ "$n" = 0 ] && echo "ok   $name clean (0 findings)" || { echo "FAIL $name has $n findings"; fail=1; }
    else
      [ "$n" != "?" ] && [ "$n" -gt 0 ] && echo "ok   $name fails impeccable ($n findings)" || { echo "FAIL $name: expected findings, got $n"; fail=1; }
    fi
  done
else
  echo "SKIP impeccable (npx missing)"
fi

# Browser probe.
MOD="${PUPPETEER_MODULE:-puppeteer}"
if node -e "require('$MOD')" 2>/dev/null; then
  node scripts/check_slop_examples.cjs "$MOD" || fail=1
else
  echo "SKIP browser probe (set PUPPETEER_MODULE to a puppeteer install)"
fi

exit $fail
