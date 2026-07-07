---
name: specification-pipeline
description: The complete specification pipeline. Automates project specification, design, and execution. Defaults to outputting in the chat.
---

# 🧭 Specification Pipeline

This skill houses the complete specification pipeline guidelines. When any specification command or phase is triggered, refer to the detailed instructions in the `references/` subdirectory:

*   **Specify:** [specify.md](file:///home/kaoru/projects/skills/skills/specification-pipeline/references/specify.md) - Creates the initial feature branch, outline, and drafts the `SPEC.md` contract.
*   **Clarify:** [clarify.md](file:///home/kaoru/projects/skills/skills/specification-pipeline/references/clarify.md) - Identifies gaps in requirements and resolves them with structured options.
*   **Plan:** [plan.md](file:///home/kaoru/projects/skills/skills/specification-pipeline/references/plan.md) - Estimates task durations and establishes implementation plans.
*   **Checklist:** [checklist.md](file:///home/kaoru/projects/skills/skills/specification-pipeline/references/checklist.md) - Generates validation check matrices.
*   **Tasks:** [tasks.md](file:///home/kaoru/projects/skills/skills/specification-pipeline/references/tasks.md) - Creates dependency-ordered `tasks.md`.
*   **Tasks to Issues:** [taskstoissues.md](file:///home/kaoru/projects/skills/skills/specification-pipeline/references/taskstoissues.md) - Converts tasks to tracking issues.
*   **Implement:** [implement.md](file:///home/kaoru/projects/skills/skills/specification-pipeline/references/implement.md) - Iterates through implementation checks.
*   **Analyze:** [analyze.md](file:///home/kaoru/projects/skills/skills/specification-pipeline/references/analyze.md) - Reviews and validates artifacts for consistency.
*   **Constitution:** [constitution.md](file:///home/kaoru/projects/skills/skills/specification-pipeline/references/constitution.md) - Syncs project core principles.

---

## 🧭 Automations Flow
As defined in `AGENTS.md`, you must automatically chain these commands in sequence (specify → clarify → plan → implement) whenever possible, utilizing sensible defaults to resolve minor ambiguities instead of stopping the pipeline.

## 🔗 Collaboration & Loop Directives
*   **Architecture Flow (Specify & Plan Phases):** Run hand-in-hand with the `architectural-planning` skill. While drafting specs and plans, utilize it to generate visual Mermaid system flowcharts, database schemas, and data flow diagrams.
*   **Implementation Hand-off (Tasks & Implement Phases):** When transitioning tasks to coding, use `specification-compliance` to verify API contract boundaries, `code-simplification` to prune speculative code wrappers, and `output-compression` to enforce concise, waffle-free diff outputs.
*   **Default Output:** By default, output all spec updates, tasks, and checklists directly in the chat, creating a markdown artifact only when necessary (in lieu of chat).
