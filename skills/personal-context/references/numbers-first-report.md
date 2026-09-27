# Numbers-First Report

Not a landing page full of vibes. Numbers first.

Produce comprehensive research / gap reports in Karlo’s blunt voice. Pair with
[technical prose rules](technical-prose.md) for sentence mechanics. This skill owns
**structure + voice**.

## When to use

- “What more can we add?” / coverage audit / catalog gaps
- Comprehensive research dump vs forums, Pack lists, comparison blogs
- Any inventory → external signal → ranked backlog report

Do not use for idea viability (`idea-generator`) or code diffs
(the engineering-rulebook simplification guide).

## Voice

| Do | Don’t |
|----|-------|
| Lead with counts and shape | Soft marketing paragraphs |
| Blunt one-liners | Hedging (“might be worth considering”) |
| One GO implementation wave | Neutral menus of five equal options |
| Tables: current / missing / skip / priority | Walls of prose |
| Explicit skip list with reasons | Treat every suggestion as good |
| Triangulate inventory + shadow docs + external signal | Only web search, or only gut feel |
| Call saturated areas (“don’t add more LLM APIs”) | Inflate the fattest bucket |
| Note offer churn / verify-before-bet | Treat Pack/forum claims as eternal |
| Bottom line in 2–4 sentences | Restate the whole report at the end |
| Short STE-ish sentences; American English | Emoji status theater |

Honor `~/.config/karlo/AGENTS.md`: strong GO/NO-GO, assume literacy, prefer
portable / self-host when relevant.

## Workflow

Copy and track:

```
Report progress:
- [ ] 1. Inventory
- [ ] 2. Shadow sources
- [ ] 3. External signal
- [ ] 4. Diagnose shape
- [ ] 5. Rank gaps P0–P3
- [ ] 6. Skip / caution
- [ ] 7. One implementation wave
- [ ] 8. Bottom line
```

1. **Inventory** — counts by category/bucket; name source-of-truth files; note prior research commits/docs.
2. **Shadow sources** — talks, matrices, READMEs, awesome mirrors that list items missing from the primary catalog.
3. **External signal** — Pack pages, comparison blogs, HN/Reddit-style roundups, vendor pricing. Cite themes, not linkspam.
4. **Diagnose shape** — heavy vs thin buckets; saturated areas to stop feeding.
5. **Rank gaps** — P0 ship-the-core · P1 documented-but-missing · P2 thin fills · P3 niche.
6. **Skip / caution** — removed free tiers, lifestyle noise, unverified chat freebies, duplicates. Table with reason.
7. **One wave** — cohesive next PR, not a mega-dump. Optional mermaid only if it clarifies flow.
8. **Bottom line** — what is already strong; largest real gaps; what not to do.

## Report template

```markdown
# [Subject] gap report ([Month Year])

## Current shape
- Counts, heavy/thin, source of truth, prior research

## What forums and lists keep recommending
1. Theme…
2. Theme…

## Highest-value adds
### P0 — …
### P1 — …
### P2 — …
### P3 — …

## Product / content gaps (beyond more rows)
- Process / UX / docs leverage

## Explicitly skip or treat carefully
| Item | Reason |
|------|--------|

## Suggested implementation wave
1. …
2. …

## Bottom line
…
```

Prefer compact tables for candidates (`Candidate | Category | Why`).

## Output

- Default: chat (or plan doc if already in plan mode).
- Offer a file path only if the user asks to persist.
- Do not implement the backlog unless the user explicitly asks to execute.

## Example

Worked sample (freestack catalog, Aug 2026): [example](numbers-first-report-example.md)
