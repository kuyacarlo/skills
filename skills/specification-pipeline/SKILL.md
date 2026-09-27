---
name: specification-pipeline
author: kaoru
version: "1.0.0"
description: "Use to turn requirements into SPEC.md contracts, plans, checklists, tasks, implementation steps, and drift audits."
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
| Analyze | [references/analyze.md](references/analyze.md) | Review and validate artifacts for consistency and drift |
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

## Specification Contract

Keep `SPEC.md` as the source of truth for project goals, architecture, data and
API contracts, feature scope, and validation criteria. Create or update it
before implementation. When requirements change, update the spec first.

During analysis, compare the implementation and planning artifacts with the
contract. Flag scope creep, missing or incomplete requirements, contract drift,
and likely security, scale, or edge-case failures. See
[references/spec-contract.md](references/spec-contract.md) for the audit details.
