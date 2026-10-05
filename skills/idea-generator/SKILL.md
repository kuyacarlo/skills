---
name: idea-generator
author: kaoru
version: "1.0.0"
description: "Use to generate and evaluate ideas, compare alternatives, and make Go/No-Go/Pivot decisions. Does not run an end-to-end product factory."
---

# Idea Workshop

Generate useful project ideas, then test the strongest options against user
needs, existing alternatives, time, team capacity, and likely value.

## When to Trigger

- User provides a problem brief, hackathon theme, or competition URL
- User asks what to build, requests brainstorming, or wants scored options
- User asks whether an idea is worth building or wants a Go / No-Go / Pivot verdict
- User wants to compare building against an existing tool or contributing upstream

## Output

Output in chat. Write to a specified path if provided.

## Workflow

1. Parse the brief or idea. Research current alternatives when the decision depends on them.
2. Extract goals, constraints, success criteria, time, team, and deliverables.
3. For brainstorming, generate and score at least five distinct ideas.
4. For a specific idea, check alternatives and whether contribution or adoption is better.
5. Scope promising ideas into MVP, V1, and Future.
6. Give a verdict with evidence, risks, and a practical next step.

Use the [evaluation process](references/evaluation-process.md) for detailed
scoring and verdict guidance. Templates are in `resources/templates/`.

## Evidence loop before commitment

- Frame the prompt with the target user, pain, constraints, non-goals, and observable success.
- Load only relevant personal preferences and current alternatives. Never copy private work context into public artifacts.
- Separate sourced facts from assumptions. Scores are decision aids, not calibrated success probabilities.
- Rank the riskiest assumption and choose one cheap, falsifiable test before expanding scope.
- Define its pass/fail threshold, time/cost cap, and stop condition before running it.
- Research is allowed within scope; prototypes, outreach, purchases, and deployment require appropriate authorization.
- Record the result, update the ranking, and stop when evidence supports adoption, contribution, GO, NO-GO, or PIVOT.
- Generate broadly, then present the strongest two options unless the user requests the full scoring table.

For agent-based ideas, compare a simple non-agent baseline first.
Test representative tasks, failure cases, and unsafe inputs against the proposed prompts, context, and tool harness.
Measure task success, human corrections, latency, and cost. More agents are not evidence of more value.
Hand the selected outcome and acceptance checks to [specification-pipeline](../specification-pipeline/SKILL.md); do not launch implementation automatically.

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

For idea evaluation, score the option across the seven factors in the
evaluation process. Use **GO**, **NO-GO**, or **PIVOT** and explain the main
trade-off. Do not defend a weak idea because the user is attached to it.

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
