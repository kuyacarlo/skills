---
name: continuous-improvement
author: kaoru
version: "1.1.0"
description: "Build/test/lint iteration loop with a project blackboard at `.agents/LEARNINGS.md`. Use when fixing failures, refactoring under tests, or recording lessons that die with the task. Triggers on LEARNINGS.md, patch failures, self-reinforcing loop, record what broke."
---

# Continuous improvement

Project-scoped lessons only. Durable cross-repo rules go to
`engineering-rulebook` (see that skill’s three-way route).

## Workflow

1. **Load** — If `.agents/LEARNINGS.md` exists, treat it as constraints alongside
   SPEC/AGENTS.
2. **Patch** — Parse tool output for file/line/error. Change one contiguous
   block; re-run tests after each change. Check LEARNINGS before repeating a
   known trap.
3. **Record** — After green: append learnings, refactor stats, next cautions.
   Use `resources/LEARNINGS_template.md` when present. Keep entries short
   (bullets + paths). Prefer STE density over prose.

## Boundaries

- Design change required → update SPEC + LEARNINGS (`specification-compliance`).
- Stay minimal when refactoring (`code-simplification`).
- Do not invent vault/MCP logging unless the user asked.
