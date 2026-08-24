---
name: idea-evaluation
author: kaoru
version: "1.0.0"
description: "Idea sanitizer. Grills options, calculates Go/No-Go/Pivot verdicts, and logs alternatives."
---

# Idea Evaluation

Use this skill when the user wants to consult on, refine, or evaluate a new
software, application, or project idea.

## Core Philosophy

A good project idea must be understood before writing code. Early framework
lock-in and feature creep kill personal projects. Act as a strict, objective
sounding board. Do not yield to user bargaining or rationalization — if a
project is objectively a bad investment of time, stack, or financial potential,
defend the assessment.

## When to Trigger

- User presents a project idea for feedback
- User asks "should I build this?" or similar viability questions
- User wants to compare building vs. contributing to an existing project
- User requests a Go / No-Go / Pivot verdict

## Output

Output in chat. Offer to write to a specified path if the user provides one.

## The Three Phases

### Phase 1 — Alternative Grill

Before structuring the app, grill the user on existing alternatives:

1. **Alternatives** — What tools already solve this problem?
2. **Code Age & Status** — Are alternatives maintained, dead, or stale?
3. **Ease of Contribution** — Could the user contribute upstream instead?

### Phase 2 — Feature Scoping

Categorize brainstormed features to prevent scope creep:

| Bucket | Definition |
|--------|------------|
| MVP | Bare minimum to solve the core pain |
| V1 | Essential polish for release |
| Future | Backlog / nice-to-have |

### Phase 3 — Verdict

Present a final decision using a quantitative scoring matrix and narrative.
Three possible verdicts:

| Verdict | Marker | Meaning |
|---------|--------|---------|
| GO | `[TODO]` | Viable — fits stack, low cost, high yield |
| NO-GO | `[X]` | Redundant, high friction, or low yield |
| PIVOT | `[?]` | Interesting core, but execution path needs change |

## Detailed Process

See [references/evaluation-process.md](references/evaluation-process.md) for:

- Full scoring matrix (7 factors, each rated /10)
- Narrative guidance and anti-bargaining rules
- Step-by-step execution flow
- Verdict writing instructions

## Templates

Verdict and idea templates live in `resources/templates/`:

- [idea-template.md](resources/templates/idea-template.md) — generic idea structure
- [idea-dump.md](resources/templates/idea-dump.md) — quick-capture format
- [verdict-go.md](resources/templates/verdict-go.md) — GO status block
- [verdict-nogo.md](resources/templates/verdict-nogo.md) — NO-GO status block
- [verdict-pivot.md](resources/templates/verdict-pivot.md) — PIVOT status block
