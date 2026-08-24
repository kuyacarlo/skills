---
name: specification-compliance
author: kaoru
version: "1.0.0"
description: "Specification compliance keeper. Enforces SPEC.md project contracts, detects feature drift between code and spec, reviews API gaps, runs adversarial failure-mode analysis, and prevents scope creep. Anchors development around a single source of truth to eliminate vibe coding. Produces drift reports, contract audits, and compliance checklists."
---

# Specification Compliance

Use this skill to anchor development around a single source of truth: `SPEC.md`.
This prevents feature creep and vibe coding by keeping requirements, interfaces,
and checklists synchronized with implementation.

---

## The SPEC.md Contract

The specification file `SPEC.md` must live in the project root and contain:

1. **Overview and Core Goal** — What the software does and who the user is.
2. **Architecture and Stack** — Frameworks, databases, and APIs with precise
   versions or constraints.
3. **API / Data Contracts** — Exact interfaces: JSON schemas, function
   signatures, database schemas.
4. **Feature Checklist** — Tasks divided into:
   - `[ ]` MVP (Must-Have)
   - `[ ]` V1 (Should-Have)
   - `[ ]` Future (Nice-to-Have)
5. **Validation Criteria** — How to test that each checklist item is complete.

---

## Core Workflows

### 1. Spec Initialization and Refinement

1. Create or update `SPEC.md` before writing code.
2. If requirements change during coding, update SPEC.md first — then change
   code. Never let the code and spec drift apart.

### 2. Autonomous Build Loop

1. Run the build-and-test loop systematically against the MVP checklist in
   SPEC.md.
2. Complete one checklist item at a time.
3. Do not move to the next item until tests pass for the current item.

### 3. Drift Analysis

Scan the codebase and compare it against SPEC.md. Generate a report flagging:

- Features implemented in code but missing from the spec (accidental scope
  creep).
- Features listed in the spec but missing or incomplete in code.
- Variations in API contracts or data models between spec and implementation.

### 4. Adversarial Review

Evaluate SPEC.md for potential failure modes:

- **Security bounds** — Are endpoints authenticated? Are inputs validated?
- **Scale constraints** — What happens if rate limits are hit?
- **Edge cases** — What if the network fails or inputs are null?
- **Creep detection** — Are V1 or Future features sneakily marked as MVP?

---

## Output Rules

1. Output spec initializations, checklists, drift reports, and review findings
   directly in the chat unless a target path is specified.
2. Prefer compact diff blocks over full-file dumps when reporting changes.
3. When enforcing compliance during implementation, strip any code abstractions
   not explicitly documented in the MVP checklist of SPEC.md.
