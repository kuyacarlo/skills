# Evaluation Process — Full Reference

This document contains the detailed scoring matrix, narrative guidance, and
step-by-step evaluation flow for the idea-workshop skill.

## Scoring Matrix

Rate each factor out of 10. Combine into a **GO Probability (%)**.

| # | Factor | What to assess |
|---|--------|----------------|
| 1 | Stack Alignment | Does this build on the user's primary technologies? |
| 2 | Alternative Maturity | Are there existing tools that make this redundant? |
| 3 | Implementation Friction | How painful is the implementation? |
| 4 | Time-to-Value (TTV) | How quickly can they see results relative to their schedule? |
| 5 | Long-Term Compounding Yield | Does this keep giving — ongoing utility, leverage, or foundation for future work? |
| 6 | Profitability / Monetization | Viable path to revenue (SaaS, open-core, B2B, self-hosted licensing)? |
| 7 | Cost of Building | Financial and infra cost — hosting, API keys, GPU, storage, third-party services? |

## Scope Assumption Rule

When scoring Implementation Friction, Stack Alignment, and Time-to-Value,
evaluate against the **final target scope** (the complete long-term end state
the user expects to run and maintain) — not a minimized MVP prototype. This
prevents scoping biases where a user justifies a large project by looking only
at the initial prototype phase.

## Anti-Bargaining Rule

Refuse to downgrade friction or complexity scores because the user bargains or
downplays the effort. If a project is objectively high-friction, maintain the
score and explain why.

## Narrative Guidance

Present the quantitative matrix clearly, but explain it through a narrative
story of how this project fits into the user's daily developer lifecycle,
obligations, and focus windows.

## Verdict Definitions

### GO (`[TODO]`)

Highly viable — fits stack, low cost, or high long-term compounding yield /
profitability.

### NO-GO (`[X]`)

Redundant, high friction, high building/compute cost, or low compounding yield.

### PIVOT (`[?]`)

The core idea is interesting but the execution path needs a major change.

For PIVOT verdicts, you MUST include:

- **Pivot Customer Stories / Paths** — alternative angles or customer targets
  where this tech has higher value.
- **Ease of Contribution & Top 3 Projects** — if they want to contribute to
  the domain rather than building custom, list the top 3 open-source projects
  in that domain that are easier to contribute to.

## Writing the Verdict

Once the verdict is decided:

1. Prepend `[TODO]`, `[X]`, or `[?]` to the H1 header.
2. Append the structured status block directly under the H1 header using the
   appropriate verdict template:
   - GO: [resources/templates/verdict-go.md](../resources/templates/verdict-go.md)
   - NO-GO: [resources/templates/verdict-nogo.md](../resources/templates/verdict-nogo.md)
   - PIVOT: [resources/templates/verdict-pivot.md](../resources/templates/verdict-pivot.md)

## Step-by-Step Execution Flow

### 1. Ingestion

Extract the user's raw details and map them into the generic template sections:

- **Motivation & Why** — populate core pain points and alternatives.
- **Brainstorm Dump** — add their raw feature list.
- **Raw Tech Requirements** — document platform and data needs.

Use [resources/templates/idea-template.md](../resources/templates/idea-template.md)
as the structural guide. When prompting the user for more context, present this
template format.

### 2. Refinement

Maintain the structure as a living document throughout the grilling process.
Walk through Phases 1–3 (Alternative Grill → Feature Scoping → Verdict).

### 3. Verdict Output

Prepend the Phase 3 verdict block at the top of the final document. Output in
chat by default; write to a file path if the user provides one.
