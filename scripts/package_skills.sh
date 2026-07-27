#!/usr/bin/env bash
# Build installable .skill packages (zip) for skills under skills/.
#
# Rebuild when:
#   - the skill directory changed between BASE..HEAD, or
#   - dist/<name>.skill is missing
#
# Usage:
#   scripts/package_skills.sh                 # vs previous commit
#   scripts/package_skills.sh <base> <head>   # explicit range
#   FORCE_ALL=1 scripts/package_skills.sh     # rebuild every skill
#   MISSING_ONLY=1 scripts/package_skills.sh  # only create absent packages
set -euo pipefail

repo_dir="$(cd "$(dirname "$0")/.." && pwd)"
cd "$repo_dir"

dist_dir="$repo_dir/dist"
mkdir -p "$dist_dir"

base_ref="${1:-}"
head_ref="${2:-HEAD}"

if [ "${FORCE_ALL:-0}" = "1" ]; then
  mode="force-all"
elif [ "${MISSING_ONLY:-0}" = "1" ]; then
  mode="missing-only"
else
  if [ -z "$base_ref" ]; then
    if [ -n "${GITHUB_EVENT_BEFORE:-}" ] && [[ ! "${GITHUB_EVENT_BEFORE}" =~ ^0+$ ]]; then
      base_ref="$GITHUB_EVENT_BEFORE"
    else
      base_ref="$(git rev-parse HEAD^ 2>/dev/null || true)"
    fi
  fi

  if [ -z "$base_ref" ] || [[ "$base_ref" =~ ^0+$ ]]; then
    mode="missing-only"
  elif ! git rev-parse --verify "$base_ref" >/dev/null 2>&1; then
    mode="missing-only"
  else
    mode="diff"
  fi
fi

changed_paths=""
if [ "$mode" = "force-all" ]; then
  changed_paths="FORCE_ALL"
elif [ "$mode" = "diff" ]; then
  changed_paths="$(git diff --name-only "$base_ref" "$head_ref" -- skills || true)"
fi

echo "mode=$mode  base=${base_ref:-none}  head=$head_ref"

skill_changed() {
  local name="$1"
  if [ "$changed_paths" = "FORCE_ALL" ]; then
    return 0
  fi
  printf '%s\n' "$changed_paths" | grep -q "^skills/${name}/" && return 0
  return 1
}

built=0
skipped=0

for skill_dir in skills/*/; do
  [ -f "${skill_dir}SKILL.md" ] || continue
  name="$(basename "$skill_dir")"
  out="$dist_dir/${name}.skill"

  need_build=0
  reason=""
  if skill_changed "$name"; then
    need_build=1
    reason="changed"
  elif [ ! -f "$out" ]; then
    need_build=1
    reason="missing"
  fi

  if [ "$need_build" -eq 0 ]; then
    skipped=$((skipped + 1))
    echo "skip  $name (unchanged, package exists)"
    continue
  fi

  tmp="$(mktemp "/tmp/${name}.XXXXXX.zip")"
  rm -f "$tmp"
  (
    cd "$skill_dir"
    zip -r -q "$tmp" . \
      -x '*/.git/*' \
      -x '.git/*' \
      -x '*.skill' \
      -x '*/__pycache__/*' \
      -x '*/*.pyc' \
      -x '*/.DS_Store' \
      -x '*/node_modules/*'
  )
  mv -f "$tmp" "$out"
  built=$((built + 1))
  echo "build $name → dist/${name}.skill ($reason)"
done

echo
echo "Built: $built  Skipped: $skipped"
if compgen -G "$dist_dir/*.skill" > /dev/null; then
  ls -la "$dist_dir"/*.skill
fi
