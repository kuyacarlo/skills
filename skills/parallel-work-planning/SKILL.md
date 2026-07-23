---
name: parallel-work-planning
description: >-
  Plan work for 2+ people on one codebase: decompose tasks, define interface
  contracts, branching, PR review, and handoffs so parallel streams do not block
  each other. Use when splitting work across engineers or agents.
---

# Parallel Work Planning

## Goal

1+1 > 2 only if **interfaces are explicit** before coding.

## Process

1. **Outcome** — one sentence for the shared milestone.
2. **Seams** — list modules/APIs each stream owns. No overlapping file ownership without a contract.
3. **Interface contracts** — for each seam, write:
   - Input / output types or API shapes
   - Error behavior
   - Fixture or mock the other side can use tomorrow
4. **Independence test** — for each task: can it finish with only the contract + mocks? If no, split again or serialize.
5. **Branching** — shared feature branch or stacked PRs; name owners.
6. **Definition of done** — tests, docs, and who merges.

## Output template

```markdown
## Milestone
…

## Streams
| Stream | Owner | Owns | Needs contract |
|--------|-------|------|----------------|
| A | … | … | … |

## Contracts
### Contract: …
- Request/response or type sketch
- Mock location

## Handoff order
1. …
```

## Anti-patterns

- Two people editing the same module “carefully”
- “We’ll sync in chat” instead of a written contract
- Starting UI and API without a frozen schema
