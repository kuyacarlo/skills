---
name: idea-generator
author: kaoru
version: "1.0.0"
description: "Hackathon ideation only: parse a problem brief, score 5+ ideas, stacks, and effort. Does not build products or run a full factory pipeline. Use when the user wants ideas, pitches options, or hackathon brainstorming — not end-to-end implementation."
---

# Project Idea Generator

Generate competitive project ideas optimized for implementation success, with
full tech stack options and achievable feature roadmaps.

## When to Trigger

- User provides a problem brief, hackathon theme, or competition URL
- User asks "what should I build", "brainstorm ideas", or similar
- User pastes requirements and wants scored options

## Output

Output in chat. Write to a specified path if provided.

## Workflow

```
1. Parse the problem description (scrape URL or analyze pasted content)
2. Extract: themes/tracks, success criteria, constraints, time, team details
3. Generate 5+ ideas per problem
4. Score each idea against extracted criteria
5. Optimize for: constraints, team capacity, and value alignment
```

## Input Requirements

### Problem Brief Source
- **URL**: Direct link (e.g. GitHub repository, project brief page)
- **Pasted Content**: Full problem statement, requirements, or theme

### Parsing Strategy

Extract from the brief:
- **Problem Statement(s)** or **Core Themes**
- **Constraints**: Deadline/timeframe, team size, technology restrictions
- **User Context** (if provided): skills, experience level, team composition
- **Deliverable Requirements**: code repo, documentation, or demo expectations

## Per-Idea Structure

Each generated idea includes:

| Field | Description |
|-------|-------------|
| Project Name | Catchy, memorable, reflects the idea |
| Confidence Score | 1–10 rating against criteria (see framework) |
| Rationale | 1–3 sentences: why this solves the problem |
| Competitive Analysis | Why it wins: criteria fit, achievability, standout factor |
| Cons/Risks | Honest downsides with mitigation strategies |
| Tech Stack | Frontend, backend, database, deployment with effort hours |
| Feature Roadmap | MVP (must-have), nice-to-have, demo layer |

## Optimization Criteria

Each idea should explicitly consider:
1. **Goal Match** — clearly maps to stated criteria or rubric
2. **Scope Realism** — ruthlessly cut what can't ship in the time window
3. **Team Fit** — suggest where team composition splits make sense
4. **Wow Factor** — the standout feature that makes the demo memorable

## Detailed Framework

For the full per-idea template, confidence scale, effort breakdown tables, and
a complete example output, see:

→ [references/generation-framework.md](references/generation-framework.md)
