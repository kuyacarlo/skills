#!/usr/bin/env bash
# Fleet watchdog. Emits one line per event on stdout; wire it into whatever
# background-monitor facility your harness provides.
#
#   bash fleet-monitor.sh [/path/to/.coordination] [poll-seconds]
#
# Reports ONLY things that need a decision:
#   CLAIM-EDIT      an agent updated its claim file (or came back alive)
#   OUR PUSH        a branch we own reached origin
#   *** UNSIGNED    one of our commits reached origin unsigned
#   HELD-SET        the SET of branches holding unpushed, unmerged work changed
#
# Deliberately silent about: dirty-file churn, teammate pushes, and counts
# changing on a branch already known to be holding work. Each of those was
# added, found to be noise, and removed. A watcher that reports every file save
# trains the reader to ignore it.

set -u
ONCE=0
COORD=""
POLL="120"

for arg in "$@"; do
  case "$arg" in
    --once|-1) ONCE=1 ;;
    *) if [ -z "$COORD" ]; then COORD="$arg"; else POLL="$arg"; fi ;;
  esac
done

COORD="${COORD:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)/../.coordination}"
US="${FLEET_AUTHOR_MATCH:-$(git config user.email 2>/dev/null || echo '')}"

trap 'kill $(jobs -p) 2>/dev/null || true' EXIT INT TERM

command -v inotifywait >/dev/null 2>&1 || echo "note: inotifywait missing — claim-file watch disabled" >&2

# --- claim-file watch -------------------------------------------------------
# Skip temp files and the orchestrator's own writes, or it reports itself.
if [ "$ONCE" -eq 0 ] && command -v inotifywait >/dev/null 2>&1; then
  inotifywait -m -q -e close_write --format '%f' "$COORD" 2>/dev/null | while read -r f; do
    case "$f" in
      *.tmp.*|*.swp|decisions.md) continue ;;
      *.md) echo "CLAIM-EDIT $f" ;;
    esac
  done &
fi

git fetch -q origin --prune 2>/dev/null || true
prev=$(git for-each-ref --format='%(refname:short) %(objectname:short)' refs/remotes/origin 2>/dev/null | sort)
heldset=""

while true; do
  if [ "$ONCE" -eq 0 ]; then
    sleep "$POLL"
    git fetch -q origin --prune 2>/dev/null || true
  fi
  cur=$(git for-each-ref --format='%(refname:short) %(objectname:short)' refs/remotes/origin 2>/dev/null | sort)

  # --- new/moved refs on origin --------------------------------------------
  join -j1 -v2 <(echo "$prev") <(echo "$cur") 2>/dev/null | while read -r b sha; do
    [ -n "$b" ] || continue
    case "$(git log -1 --format='%ae' "$sha" 2>/dev/null)" in
      *"$US"*)
        bad=$(git log --format='%G?|%ae' "origin/main..$b" 2>/dev/null \
              | grep "$US" | grep -cv '^G|')
        if [ "${bad:-0}" != "0" ]; then
          echo "*** OUR UNSIGNED COMMIT ON ORIGIN *** $b : $bad"
        else
          echo "OUR PUSH $b : $(git log -1 --format='%s' "$sha" 2>/dev/null | cut -c1-56)"
        fi ;;
      *) : ;;   # someone else's branch — not ours to police
    esac
  done
  prev=$cur

  # --- work committed but not pushed, excluding already-merged branches ----
  # NOTE: --limit must exceed the repo's merged-PR count. A result exactly
  # equal to the limit is truncation, not a total.
  MERGED=$(gh pr list --limit 1000 --state merged --json headRefName --jq '.[].headRefName' 2>/dev/null)
  nowset=""; detail=""
  # Unfiltered on purpose: agents create worktrees under /tmp and inside other
  # checkouts. Filtering those out hides exactly what this is looking for.
  for d in $(git worktree list --porcelain 2>/dev/null | awk '/^worktree /{print $2}'); do
    [ -d "$d" ] || continue
    br=$(git -C "$d" rev-parse --abbrev-ref HEAD 2>/dev/null) || continue
    [ -z "$br" ] || [ "$br" = "HEAD" ] && continue
    echo "$MERGED" | grep -qx "$br" && continue
    # origin/<branch> does not resolve for a never-pushed branch; fall back.
    if git rev-parse --verify -q "origin/$br" >/dev/null 2>&1; then
      base="origin/$br"
    else
      base="origin/main"
    fi
    a=$(git -C "$d" rev-list --count "$base..HEAD" 2>/dev/null || echo 0)
    [ "$a" = "0" ] && continue
    u=$(git -C "$d" log --format='%G?' "$base..HEAD" 2>/dev/null | grep -cv '^G$')
    nowset="$nowset$br "
    f=""; [ "${u:-0}" != "0" ] && f="  <== ${u} UNSIGNED"
    detail="$detail  $br: $a unpushed$f
"
  done
  # Compare the SET, not the counts — a known branch simply growing is not news.
  nowset=$(echo "$nowset" | tr ' ' '\n' | sort | tr '\n' ' ')
  if [ "$nowset" != "$heldset" ]; then
    if [ -n "$detail" ]; then
      echo "HELD-SET changed (unmerged only):"; printf '%s' "$detail"
    else
      echo "HELD-SET: empty — nothing unmerged is held locally"
    fi
    heldset="$nowset"
  fi
  [ "$ONCE" -eq 1 ] && break
done
