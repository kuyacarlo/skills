---
name: speckit
description: The complete Spec-Kit pipeline (specify, clarify, plan, tasks, implement, analyze, checklist, constitution, taskstoissues). Automates project specification, design, and execution.
---

# 🧭 Spec-Kit Pipeline

This skill houses the complete Spec-Kit pipeline guidelines. When any Spec-Kit command or phase is triggered, refer to the detailed instructions in the `references/` subdirectory:

*   **Specify (`/speckit.specify`):** [specify.md](file:///home/kaoru/projects/skills/skills/speckit/references/specify.md) - Creates the initial feature branch, outline, and drafts the `SPEC.md` contract.
*   **Clarify (`/speckit.clarify`):** [clarify.md](file:///home/kaoru/projects/skills/skills/speckit/references/clarify.md) - Identifies gaps in requirements and resolves them with structured options.
*   **Plan (`/speckit.plan`):** [plan.md](file:///home/kaoru/projects/skills/skills/speckit/references/plan.md) - Estimates task durations and establishes implementation plans.
*   **Checklist (`/speckit.checklist`):** [checklist.md](file:///home/kaoru/projects/skills/skills/speckit/references/checklist.md) - Generates validation check matrices.
*   **Tasks (`/speckit.tasks`):** [tasks.md](file:///home/kaoru/projects/skills/skills/speckit/references/tasks.md) - Creates dependency-ordered `tasks.md`.
*   **Tasks to Issues (`/speckit.taskstoissues`):** [taskstoissues.md](file:///home/kaoru/projects/skills/skills/speckit/references/taskstoissues.md) - Converts tasks to GitHub issues.
*   **Implement (`/speckit.implement`):** [implement.md](file:///home/kaoru/projects/skills/skills/speckit/references/implement.md) - Iterates through implementation checks.
*   **Analyze (`/speckit.analyze`):** [analyze.md](file:///home/kaoru/projects/skills/skills/speckit/references/analyze.md) - Reviews and validates artifacts for consistency.
*   **Constitution (`/speckit.constitution`):** [constitution.md](file:///home/kaoru/projects/skills/skills/speckit/references/constitution.md) - Syncs project core principles.

---

## 🧭 Spec-Kit Automations Flow
As defined in `AGENTS.md`, you must automatically chain these commands in sequence (`specify` → `clarify` → `plan` → `implement`) whenever possible, utilizing sensible defaults to resolve minor ambiguities instead of stopping the pipeline.

## 🔗 Collaboration & Loop Directives
*   **Architecture Flow (Specify & Plan Phases):** Run hand-in-hand with the `thinking-partner` skill. While drafting specs and plans, utilize it to generate visual Mermaid system flowcharts, database schemas, and data flow diagrams.
*   **Implementation Hand-off (Tasks & Implement Phases):** When transitioning tasks to coding, use `spec-builder` to verify API contract boundaries, `code-yagni` to prune speculative code wrappers, and `token-compressor` to enforce concise, waffle-free diff outputs.

