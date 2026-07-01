---
name: continuous-improvement
description: Continuous improvement and self-reinforcing iteration loop. Parses test/lint outputs, records lessons learned to .agents/LEARNINGS.md, and optimizes code structure incrementally.
---

# 🔄 Continuous Improvement & Self-Reinforcing Loop

Use this skill when you need to run compilation checks, patch test failures, lint code, or perform refactoring on an existing codebase. This skill enforces a self-reinforcing feedback loop via a shared blackboard file: `.agents/LEARNINGS.md`.

---

## 📋 The Self-Reinforcing Workflow

### 1. Startup: Load Existing Constraints
Before writing any code or updating specifications:
1. Check if `.agents/LEARNINGS.md` exists in the active workspace.
2. Read it to load historical failure modes, rules, and guidelines accumulated from previous runs.
3. Treat those guidelines as strict project constraints (in addition to `SPEC.md` and `AGENTS.md`).

### 2. Execution: Parse & Patch Failures Incremental
When running unit tests or linters:
1. Parse the command output to identify the exact file, line number, and error type (do not guess).
2. Apply modifications in small, contiguous blocks.
3. Run tests/builds *after every single change* to isolate variables.
4. If a test fails, verify that the failure is not a regression of a previously resolved item in `LEARNINGS.md`.

### 3. Closure: Update the Blackboard
After code is verified and unit tests pass:
1. Create or update `.agents/LEARNINGS.md` in the project root.
2. Structure it using the layout in `resources/LEARNINGS_template.md`.
3. Document:
   * **Learnings:** Critical edge cases or compiler traps found (e.g., "Vitest fails if React is imported but unused when noUnusedLocals is enabled").
   * **Refactor Stats:** LOC changed, tests added, and build performance changes.
   * **Next Guidelines:** Actions or cautions for the next agent/session.

---

## 🛡️ Integration Guidelines

*   **With `spec-builder`:** If a test failure requires a design change, update both `SPEC.md` and `.agents/LEARNINGS.md` to keep documentation and memory synced.
*   **With `code-yagni`:** Ensure refactored code remains minimal. Do not add wrappers, utilities, or abstractions that are not explicitly requested by the specs or required to fix an error.
*   **With `token-compressor`:** Format `LEARNINGS.md` compactly. Use brief bullet points, lists, and direct trace citations to preserve context tokens.
