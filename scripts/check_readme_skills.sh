#!/usr/bin/env bash
# Fail if README Live skills table drifts from skills/*/SKILL.md frontmatter names.
set -euo pipefail
repo_dir="$(cd "$(dirname "$0")/.." && pwd)"
cd "$repo_dir"

readme="README.md"
[ -f "$readme" ] || { echo "FAIL: missing $readme" >&2; exit 1; }

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

frontmatter_name() {
  local file="$1" dir_name="$2"
  local n
  n="$(awk '
    BEGIN { in_fm=0 }
    /^---[[:space:]]*$/ {
      if (in_fm==0) { in_fm=1; next }
      else { exit }
    }
    in_fm && /^name:/ {
      line=$0
      sub(/^name:[[:space:]]*/, "", line)
      gsub(/^["'\'']|["'\'']$/, "", line)
      print line
      exit
    }
  ' "$file")"
  if [ -z "$n" ]; then
    echo "$dir_name"
  else
    echo "$n"
  fi
}

: >"$tmp/disk"
for dir in skills/*/; do
  [ -f "${dir}SKILL.md" ] || continue
  base="$(basename "$dir")"
  frontmatter_name "${dir}SKILL.md" "$base" >>"$tmp/disk"
done
sort -u "$tmp/disk" -o "$tmp/disk"

# Extract backtick names only from the Live skills section
awk '
  BEGIN { in_live=0 }
  /^## Live skills/ { in_live=1; next }
  in_live && /^## / { exit }
  in_live { print }
' "$readme" | grep -oE '`[a-z0-9][a-z0-9-]*`' | tr -d '`' | sort -u >"$tmp/readme"

errors=0
while read -r name; do
  [ -z "$name" ] && continue
  if ! grep -qxF "$name" "$tmp/readme"; then
    echo "FAIL: skill on disk missing from README Live skills: $name" >&2
    errors=$((errors + 1))
  fi
done <"$tmp/disk"

while read -r name; do
  [ -z "$name" ] && continue
  if ! grep -qxF "$name" "$tmp/disk"; then
    echo "FAIL: README Live skills names missing skill on disk: $name" >&2
    errors=$((errors + 1))
  fi
done <"$tmp/readme"

if [ "$errors" -ne 0 ]; then
  echo "check_readme_skills: $errors failure(s)" >&2
  echo "disk:" >&2
  cat "$tmp/disk" >&2
  echo "readme:" >&2
  cat "$tmp/readme" >&2
  exit 1
fi

count="$(wc -l <"$tmp/disk" | tr -d ' ')"
echo "check_readme_skills: ok — ${count} skills match README"
