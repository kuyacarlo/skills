---
name: thorough-code-review
description: >-
  Systematic code review requiring file:line citations for every issue, cross-file
  pattern detection, and consolidation tables for duplication. Use when reviewing
  a PR, diff, or branch for bugs, inconsistencies, or DRY violations.
---

# Thorough Code Review

## Rules

1. Every finding cites `path:line` (or a range). No vibes-only comments.
2. Search for the **same bug class** elsewhere before closing the note.
3. Separate **Correctness**, **Security**, **Consistency/DRY**, **Maintainability**.
4. End with a consolidation table of duplicated patterns.

## Process

1. Establish the review base (`main...HEAD`, PR URL, or stated commit).
2. Read the diff, then open full files for touched symbols.
3. For each issue: severity · citation · why · suggested fix (minimal).
4. Grep for siblings of each issue; list extra hits.
5. Output consolidation:

| Pattern | Locations | Recommendation |
|---------|-----------|----------------|
| … | `a:10`, `b:22` | extract helper / delete dup |

## Severity

- **Blocker** — wrong behavior, data loss, auth hole
- **Should fix** — real bug or inconsistency likely to bite
- **Nit** — style only; batch or skip if noisy

Default to fewer, higher-signal notes. Prefer one accurate citation over three restatements.
