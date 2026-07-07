---
name: specification-compliance
description: Specification compliance keeper. Enforces SPEC.md project contracts, detects feature drift, and reviews API gaps. Defaults to outputting in the chat.
---

# 🛠️ Specification Compliance Skill

Use this skill to anchor development around a single source of truth: `SPEC.md`. This prevents feature creep and "vibe coding" by keeping requirements, interfaces, and checklists synchronized with implementation.

---

## 🎯 The SPEC.md Contract

The specification file `SPEC.md` must live in the root of the project directory and contain the following sections:

1.  **Overview & Core Goal**: What does the software do, and who is the user?
2.  **Architecture & Stack**: Precise details on frameworks, databases, and APIs.
3.  **API / Data Contracts**: Exact interfaces (JSON schemas, function signatures, database schemas).
4.  **Feature Checklist**: A list of tasks divided into:
    *   `[ ]` MVP (Must-Have)
    *   `[ ]` V1 (Should-Have)
    *   `[ ]` Future (Nice-to-Have)
5.  **Validation Criteria**: How to test that each checklist item is actually complete.

---

## 🔄 Core Workflows

### 1. Spec Initialization & Refinement
*   Create or update `SPEC.md` before writing code.
*   If requirements change during coding, **always update SPEC.md first** before changing code. Do not let the code and spec drift.

### 2. Autonomous Build Loop
*   Run the build-and-test loop systematically against the features declared in the MVP checklist of `SPEC.md`.
*   Complete one checklist item at a time. Do not move to the next item until tests pass for the current item.

### 3. Drift Analysis
*   Scan the codebase and compare it against the `SPEC.md` file.
*   Generate a report flagging:
    *   Features implemented in code but missing from the spec (accidental scope creep).
    *   Features listed in the spec but missing or incomplete in code.
    *   Variations in API contracts or data models.

### 4. Adversarial Review
*   Evaluate `SPEC.md` for potential failure modes:
    *   *Security bounds*: Are endpoints authenticated?
    *   *Scale constraints*: What happens if rate limits are hit?
    *   *Edge cases*: What if the network fails or inputs are null?
    *   *Creep detection*: Are there V1 or Future features sneakily marked as MVP?

### 5. Output Configuration
By default, output spec initializations, checklists, drift reports, and review findings directly in the chat, creating a markdown artifact only when necessary (in lieu of chat).

---

## 🔗 Collaboration & Loop Directives
*   **Transition to Implementation Optimizations (Build & Check Phases):** During codebase construction:
    1.  **YAGNI Audit:** Enforce strict adherence to the spec using the `code-simplification` skill, stripping any code abstractions that are not explicitly documented in the MVP checklist of `SPEC.md`.
    2.  **Compressor Formatting:** Apply `output-compression` guidelines to format all modifications as compact diff blocks, keeping output tokens minimized.
