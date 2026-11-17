#!/usr/bin/env bash
# Usage: grep-probe.sh <present|absent> <ERE pattern> <pathspec...>
# Contract: 0 PASS, 1 FAIL, 2 ERROR. Never leaks grep/xargs native codes.
mode="$1"; pat="$2"; shift 2
files=$(git ls-files -- "$@" 2>/dev/null) || { echo "ERROR git ls-files failed"; exit 2; }
[ -z "$files" ] && { echo "ERROR no files match pathspec: $*"; exit 2; }
hits=$(printf '%s\n' "$files" | tr '\n' '\0' | xargs -0 grep -nE -- "$pat" 2>/tmp/grep-probe.err); rc=$?
# xargs: 0 = some match, 123 = no match in any file, other = real error
if [ $rc -ne 0 ] && [ $rc -ne 123 ]; then echo "ERROR grep/xargs rc=$rc"; cat /tmp/grep-probe.err; exit 2; fi
found=0; [ -n "$hits" ] && found=1
[ -n "$hits" ] && printf '%s\n' "$hits" | head -20
if [ "$mode" = present ]; then
  [ $found = 1 ] && { echo "ok   pattern present"; echo "RESULT 1/1"; exit 0; } || { echo "FAIL pattern present :: no match"; echo "RESULT 0/1"; exit 1; }
else
  [ $found = 0 ] && { echo "ok   pattern absent"; echo "RESULT 1/1"; exit 0; } || { echo "FAIL pattern absent :: matches above"; echo "RESULT 0/1"; exit 1; }
fi
