---
name: thorough-code-review
author: kaoru
version: "1.0.0"
description: >-
  Systematic code review requiring file:line citations for every issue, cross-file
  pattern detection, and consolidation tables for duplication. Use when reviewing
  a PR, diff, or branch for bugs, inconsistencies, or DRY violations. Covers
  correctness, security, consistency, maintainability. Outputs severity-ranked
  findings with actionable fix suggestions.
---

# Thorough Code Review

A systematic, citation-driven review process. Every finding must reference
concrete code locations. No vibes-only commentary.

## Severity levels

| Level | Label | Meaning |
|-------|-------|---------|
| S1 | Blocker | Wrong behavior, data loss, auth bypass, crash in happy path |
| S2 | Should-fix | Real bug or inconsistency likely to bite under normal use |
| S3 | Nit | Style, naming, minor readability — batch or skip if noisy |

Default to fewer, higher-signal notes. One accurate citation beats three restatements.

## Review process

### 1. Establish the base

- Determine the review scope: `main...HEAD`, a PR URL, a commit range, or a set of files the user specifies.
- If the scope is unclear, ask once. Do not guess.

### 2. Read the diff

- Read the full diff first to build a mental map of what changed.
- Note: new files, deleted files, renamed files, moved logic.
- Identify the intent of the change (feature, bugfix, refactor, config).

### 3. Open full files for context

- For every touched symbol (function, class, constant), open the full file — not just the diff hunk.
- Read callers and callees of modified functions.
- Check test files that cover modified code paths.

### 4. Find siblings

- For every issue found, search the codebase for the same pattern or bug class.
- Use grep/ripgrep/AST search as needed.
- Report all sibling occurrences, not just the one in the diff.

### 5. Categorize findings

Assign each finding to exactly one category:

1. Correctness — logic errors, off-by-one, null derefs, race conditions, wrong return types, broken contracts.
2. Security — injection, auth gaps, secrets in code, unsafe deserialization, missing input validation, SSRF, path traversal.
3. Consistency / DRY — duplicated logic, divergent implementations of the same concern, inconsistent naming or patterns across the codebase.
4. Maintainability — dead code, unclear naming, missing error handling, excessive complexity, missing or misleading comments.

### 6. Write findings

Each finding uses this format:

```
### [S1|S2|S3] Category: Short title

**Location:** `path/to/file.ext:42` (or range `path:42-58`)

**Issue:** One-sentence description of what is wrong.

**Why it matters:** Impact or failure scenario.

**Suggested fix:** Minimal code or description showing the correction.

**Siblings:** Other locations with the same pattern (if any).
- `path/other.ext:17`
- `path/another.ext:93`
```

### 7. Consolidation table

After all findings, output a table of duplicated or repeated patterns:

| Pattern | Locations | Recommendation |
|---------|-----------|----------------|
| Unchecked `.unwrap()` on user input | `api/handler.rs:34`, `api/handler.rs:78`, `api/auth.rs:12` | Replace with `?` or contextual error |
| Hardcoded timeout 5000ms | `client.ts:19`, `client.ts:45`, `worker.ts:8` | Extract to config constant |
| Duplicated validation logic | `routes/user.ts:30-45`, `routes/admin.ts:55-70` | Extract shared validator |

Only include patterns that appear in 2+ locations. Skip if nothing qualifies.

### 8. Summary verdict

End with a one-paragraph summary:

- Overall risk level (ship as-is / ship after S2 fixes / block on S1).
- Count of findings by severity.
- The single highest-risk item restated in one line.

## Rules

1. Every finding cites `path:line` or `path:line-line`. No exceptions.
2. Search for the same bug class elsewhere before closing a note. Report siblings.
3. Do not rephrase the same issue multiple times. State it once with all locations.
4. Prefer concrete fix suggestions over abstract advice ("add validation" → show the guard clause).
5. If the diff is large (>500 lines), group findings by file, then by category within each file.
6. If the diff is small (<50 lines), a flat list sorted by severity is fine.
7. Do not review generated files (lockfiles, compiled output, vendor) unless the user asks.
8. Do not comment on formatting if an autoformatter is configured in the project.
9. When uncertain whether something is a bug, state the assumption and mark it S2 with a note.
10. Keep total output proportional to the diff. A 10-line fix does not need 200 lines of review.

## Cross-file pattern detection

These patterns require checking beyond the immediate diff:

- A new function duplicates logic already present elsewhere.
- A modified interface has callers that were not updated.
- A deleted export is still imported somewhere.
- A new dependency overlaps with an existing one.
- Error handling in the diff differs from the project's established pattern.
- A constant is defined that already exists under a different name.

When any of these are detected, include them as Consistency/DRY findings with all locations cited.

## What this skill does NOT do

- Does not run tests or linters (suggest the user run them).
- Does not approve or merge — only reports findings.
- Does not rewrite code wholesale. Fix suggestions are minimal and targeted.
