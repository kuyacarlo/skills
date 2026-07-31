# Generation Framework

Detailed template and scoring reference for the idea-generator skill.

## Confidence Score Scale

| Score | Meaning |
|-------|---------|
| 9–10 | Perfect fit, clear impact, team skills align, low execution risk |
| 7–8 | Strong match, achievable in timeframe, minor concerns |
| 5–6 | Decent potential but has meaningful tradeoffs |
| 3–4 | Risky or loose fit |

## Per-Idea Template

### 1. Project Name
Catchy, memorable, reflects the idea.

### 2. Confidence Score (1–10)
Rate against the extracted criteria using the scale above.

### 3. Rationale
1–3 sentences max. Why this solves the problem.

### 4. Competitive Product Analysis
- How it scores high on criteria
- Why it's achievable in the constraints
- Competitive advantage (what makes it stand out)

### 5. Potential Cons/Risks

Structure as:
- **Technical blockers** (what could break) → Mitigation
- **Execution risks** (scope creep, API failures, auth complexity) → Mitigation
- **Data/legal risks** (need real data, scraping, IP) → Mitigation
- **UX gaps** (what looks janky in crunch time) → Mitigation

### 6. Tech Stack with Effort Breakdown

| Component | Hours | Parallelizable | Notes |
|-----------|-------|----------------|-------|
| Frontend | Est. hours | Yes/No | Framework choice + rationale |
| Backend | Est. hours | Yes/No | API choice based on deployment |
| Database | Est. hours (if needed) | — | Prefer in-memory or free tier |
| Deployment | Est. hours | Yes (usually) | Free tier only |
| Testing/Polish | Est. hours | No (blocks on features) | Bug fixes, UI refinement |
| **Total (Sequential)** | Sum | — | Linear path |
| **Total (Parallel)** | Longest blocking path | — | Realistic team time |

Stack selection guidance:
- **Frontend**: Based on time + team skills (React/Vue for quick MVPs, plain HTML+JS for minimal)
- **Backend**: API choice based on deployment (serverless functions, Express, FastAPI)
- **Database**: Only if necessary (prefer in-memory or free tier services)
- **Deployment**: Free tier only (Vercel, Netlify, Railway, etc.)

### 7. Feature Roadmap

- **MVP (Must-Have)**: Core 1–2 features, achievable in 50% of available time
- **Nice-to-Have**: 2–3 features if time permits
- **Demo Layer**: How to present compellingly (UI polish, demo data, pre-recorded fallbacks)

## Output Formatting

- Use **bold** for project names
- Use `---` dividers between ideas
- Use markdown tables for effort breakdown
- Include confidence scores and parallelizable flags

## Example Output

```markdown
**Idea: AquaWatch** | Confidence: 8/10

Rationale: IoT sensors track real-time water quality in local watersheds,
crowdsourced data feeds a mobile app for community reporting.

Product Analysis:
- Focus area match: "Environmental impact" + "Data visualization" (60% of target weight)
- Achievable in 36 hours: 2 devs handle frontend + backend, 1 handles sensor mock data
- Wow factor: Live map showing water quality + citizen reports

Potential Cons/Risks & Mitigations:
- **Technical blocker**: Real IoT sensors won't arrive in time
  → **Mitigation**: Use mock data from public water quality APIs; pre-populate
    demo with realistic readings
- **Execution risk**: Map rendering with 100+ data points could slow down
  → **Mitigation**: Implement clustering; start with 20-30 points
- **UX gap**: Crowdsourced data quality suffers without moderation
  → **Mitigation**: Pre-seed demo data with clean entries; disable user
    contributions for initial demo

Tech Stack & Effort Breakdown:
| Component | Hours | Parallelizable | Notes |
|-----------|-------|----------------|-------|
| Frontend (React + Mapbox) | 7-8h | Yes (after API contracts defined) | App shell, map rendering, report UI |
| Backend (Node.js + APIs) | 5-6h | Yes (in parallel with frontend) | API polling, CRUD, caching |
| Data integration | 2-3h | Partial | Can start while backend scaffolds |
| Deployment (Vercel) | 1-2h | Yes (parallel with feature dev) | Auto-deploy setup |
| Testing/Polish | 3-4h | No (must wait for features) | Bug fixes, UI refinement |
| **Total (Sequential)** | **18-23h** | — | Linear path if done serially |
| **Total (Parallel)** | **~14h** | — | Frontend + backend in parallel, then deploy, then test |

Feature Roadmap:
- **MVP (must-have, 14h)**: Map UI + live water quality data + basic citizen reports
- **Nice-to-Have (if time, 5h)**: Trend graphs, notification alerts, water safety recommendations
- **Demo layer**: Pre-populate 10 report locations, cache real water quality data
```
