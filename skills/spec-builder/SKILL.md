---
name: spec-builder
description: Spec-driven development assistant that manages project specifications (SPEC.md), enforces design contracts, detects drift between code and specs, and runs build loops. Use this skill when initiating new projects, writing technical specifications, checking code compliance against requirements, or conducting adversarial design reviews.
---

# 🛠️ Spec Builder (Spec-Driven Development)

Use this skill to anchor development around a single source of truth: `SPEC.md`. This prevents "vibe coding" by keeping requirements, interfaces, and checklists synchronized with implementation.

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

### 1. Spec Initialization & Refinement (`/ck:spec`)
*   Create or update `SPEC.md` before writing code.
*   If requirements change during coding, **always update SPEC.md first** before changing code. Do not let the code and spec drift.

### 2. Autonomous Build Loop (`/ck:build`)
*   Run the build-and-test loop systematically against the features declared in the MVP checklist of `SPEC.md`.
*   Complete one checklist item at a time. Do not move to the next item until tests pass for the current item.

### 3. Drift Analysis (`/ck:check`)
*   Scan the codebase and compare it against the `SPEC.md` file.
*   Generate a report flagging:
    *   Features implemented in code but missing from the spec (accidental scope creep).
    *   Features listed in the spec but missing or incomplete in code.
    *   Variations in API contracts or data models.

### 4. Adversarial Review (`/ck:review`)
*   Evaluate `SPEC.md` for potential failure modes:
    *   *Security bounds*: Are endpoints authenticated?
    *   *Scale constraints*: What happens if rate limits are hit?
    *   *Edge cases*: What if the network fails or inputs are null?
    *   *Creep detection*: Are there V1 or Future features sneakily marked as MVP?
