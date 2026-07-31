---
name: specification-pipeline
author: kaoru
version: "1.0.0"
description: >-
  The complete specification pipeline. Automates project specification, design,
  and execution through structured phases: specify, clarify, plan, checklist,
  tasks, implement, analyze, and constitution sync. Produces SPEC.md contracts,
  requirement clarifications, implementation plans, validation checklists,
  dependency-ordered task lists, and artifact analysis. Chains phases
  automatically using sensible defaults for minor ambiguities.
---

# Specification Pipeline

This skill houses the complete specification pipeline. When any specification
phase is triggered, refer to the detailed instructions in the `references/`
subdirectory.

---

## Phases

| Phase | Reference | Purpose |
|-------|-----------|---------|
| Specify | [references/specify.md](references/specify.md) | Create feature branch, outline, and draft the SPEC.md contract |
| Clarify | [references/clarify.md](references/clarify.md) | Identify requirement gaps and resolve with structured options |
| Plan | [references/plan.md](references/plan.md) | Estimate task durations and establish implementation plans |
| Checklist | [references/checklist.md](references/checklist.md) | Generate validation check matrices |
| Tasks | [references/tasks.md](references/tasks.md) | Create dependency-ordered tasks.md |
| Tasks to Issues | [references/taskstoissues.md](references/taskstoissues.md) | Convert tasks to tracking issues |
| Implement | [references/implement.md](references/implement.md) | Iterate through implementation checks |
| Analyze | [references/analyze.md](references/analyze.md) | Review and validate artifacts for consistency |
| Constitution | [references/constitution.md](references/constitution.md) | Sync project core principles |

---

## Execution Rules

1. Chain phases in sequence (specify → clarify → plan → implement) automatically
   when possible.
2. Use sensible defaults to resolve minor ambiguities instead of halting the
   pipeline.
3. Stop and ask only when a major design fork requires an explicit user choice.
4. Output all spec updates, tasks, and checklists directly in the chat unless a
   target path is specified.
5. Prefer compact diffs over full-file dumps when reporting changes.
