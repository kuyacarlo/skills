# Specification Contract and Drift Audit

Keep the project root `SPEC.md` as the source of truth. It should define:

1. The product goal and intended users.
2. Architecture, stack, and important constraints.
3. API, data, and interface contracts.
4. Features grouped into MVP, V1, and Future.
5. Validation criteria for each committed requirement.

Create or update the spec before implementation. If requirements change during
implementation, update the spec first. Keep implementation scope aligned with
the MVP checklist.

## Drift audit

Compare the spec with implementation and planning artifacts. Report:

- Implemented behavior that the spec does not require.
- Required behavior that is missing or incomplete.
- Differences in API contracts, data models, or terminology.
- Requirements without validation criteria or task coverage.
- Risks involving security bounds, scale limits, network failure, null inputs,
  or other relevant edge cases.

Use a compact, actionable report. Cite artifact locations when available.
Separate defects from optional improvements. Do not expand the MVP to include
V1 or Future work.
