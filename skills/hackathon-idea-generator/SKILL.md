---
name: hackathon-idea-generator
description: Analyzes hackathon briefs (URLs or pasted content) and generates optimized project ideas with tech stacks and feature roadmaps. Generates 5+ ideas per problem/2+ per track, considering judging criteria, time constraints, team size, and winning potential. Outputs directly to Google Docs when a doc URL is provided. Use this skill whenever the user asks "what should I build" for a hackathon, provides a hackathon brief, or wants AI-powered project ideas optimized for hackathon judging criteria. Especially useful for analyzing prizes, judging rubrics, and suggesting ideas that maximize winning probability.
---

# Hackathon Idea Generator

Generate competitive hackathon project ideas directly optimized for winning, with full tech stacks and achievable feature roadmaps.

## Workflow

```
User Input:
  "what should I build for this hackathon: [URL or pasted brief]"
  "put it in: [Google Doc URL]" (optional)

Claude Output:
  1. Parses hackathon brief (scrapes URL or analyzes pasted content)
  2. Extracts: tracks/themes, judging criteria, prizes, time, team details
  3. Generates 5+ ideas per problem (2+ per track if multi-track)
  4. For each idea: name + rationale + killer product analysis + cons/risks + tech stack with effort breakdown
  5. Optimizes for: judging rubric, time constraints, team capacity, prize alignment
  6. (If Google Doc URL provided) Writes to existing doc per-track with timestamp
```

## Input Requirements

### Hackathon Brief Source
- **URL**: User provides direct link (e.g., hackathon.com/brief)
- **Pasted Content**: User pastes full brief text, problem statement, or theme

### Google Docs Output (Optional)
- User provides shareable Google Doc URL
- Skill detects any tab/subtab mentions in the brief and places ideas in relevant sections
- If no specific tabs mentioned, appends ideas to end of document

## Parsing Strategy

Extract from the brief:
- **Problem Statement(s)** or **Themes/Tracks**
- **Judging Criteria** (weightings, rubric, specific focus areas)
- **Prizes** (track-specific prizes guide what judges value)
- **Constraints**: Hackathon duration, team size restrictions, technology restrictions
- **User Context** (if provided): skills, experience level, team composition
- **Submission Requirements**: deliverable format (code repo, demo video, pitch deck, etc.)

## Idea Generation Framework

### Per Idea, Provide:

1. **Project Name** - Catchy, memorable, reflects the idea
2. **Confidence Score** (1-10) - How well this idea matches the hackathon:
   - 9-10: Perfect rubric fit, clear impact story, team skills align, low execution risk
   - 7-8: Strong rubric match, achievable in timeframe, minor concerns
   - 5-6: Decent potential but has meaningful tradeoffs (either innovation OR impact, not both)
   - 3-4: Risky or loose rubric fit; only pursue if desperation
   - Scoring considers: judging weight match, team fit, time feasibility, demo-ability, sustainability
3. **Rationale** (1-3 sentences max) - Why this solves the problem or fits the theme
4. **Killer Product Analysis** - Why this wins:
   - How it scores high on judging criteria
   - Why it's achievable in the time/team constraints
   - Competitive advantage (what makes it stand out vs. other hackathon submissions)
   - Prize alignment (if relevant)
5. **Potential Cons/Risks** - Be honest about downsides, with mitigation strategies:
   - **Technical blockers** (what could break) → Mitigation (how to prevent/recover)
   - **Execution risks** (scope creep, API failures, auth complexity) → Mitigation
   - **Market/judging risks** (problem fit, been-done factor) → Mitigation
   - **Data/legal risks** (need real data, scraping, IP) → Mitigation
   - **UX gaps** (what looks janky in crunch time) → Mitigation

### Tech Stack Guidance with Effort Breakdown:
- **Frontend**: Recommend based on time + team skills (React/Vue for quick MVPs, plain HTML+JS for minimal)
  - Estimate hours (e.g., "React setup + UI: 6-8h")
  - **Parallelizable**: Yes/No (can frontend be built while backend is being coded?)
- **Backend**: API choice based on deployment (Vercel Functions, simple Express, FastAPI)
  - Estimate hours (e.g., "API endpoints + database: 4-6h")
  - **Parallelizable**: Yes/No (can backend be coded while frontend scaffolds API contracts?)
- **Database**: Only if necessary (prefer in-memory or free tier services)
  - Estimate hours if applicable
  - **Parallelizable**: Yes/No
- **Deployment**: Free tier only (Vercel, Netlify, Railway, Replit, etc.)
  - Estimate hours ("Setup CI/CD: 1-2h")
  - **Parallelizable**: Usually Yes (can be done in parallel with feature dev)
- **Total MVP Time (Sequential)**: Sum of all components
- **Total MVP Time (Parallel)**: Longest blocking path (shows real time if team works in parallel)

### Feature Roadmap for Hackathon:
- **MVP (Must-Have)**: Core 1-2 features, achievable in 50% of time
- **Nice-to-Have**: 2-3 features if time permits
- **Demo Layer**: How to present it compellingly (UI polish, demo data, pre-recorded fallbacks)

## Optimization for Winning

Each idea should explicitly consider:

1. **Judging Rubric Match**: If brief mentions "innovation", "social impact", "technical complexity" — ideas should clearly map to these
2. **Time-to-Demo**: Can the core idea be demoed in 5 minutes with minimal setup?
3. **Scope Realism**: Be ruthless — cut scope that can't be done in the time window
4. **Team Fit**: If user mentioned 2 devs + 1 designer, suggest ideas where this split makes sense
5. **Wow Factor**: What's the demo moment that makes judges sit up? (visual, surprising output, novel integration, etc.)

## Output Formats

### Google Docs Integration (If User Provides Google Doc URL):

1. **Authentication**: Skill requests access to user's Google Drive
2. **Timestamp**: Insert date/time stamp before ideas section (e.g., "Generated: June 14, 2024 at 2:45 PM")
3. **Track Detection**: Parse brief for track names (e.g., "Open Banking", "Blockchain Solutions", "General")
4. **Per-Track Placement**: Create a subsection for each track and append ideas under that track header
5. **Formatting**: 
   - Use **bold** for project names
   - Use `---` dividers between ideas
   - Organize ideas by track with clear headers
   - Maintain readable Docs formatting (headings, bullet points, tables for effort breakdown)

### Markdown Output (If User Requests "as markdown" or "for github"):

- Generate clean markdown file with same structure as Google Docs output
- Include YAML frontmatter with metadata (hackathon name, duration, date generated, team info)
- Use markdown tables for effort breakdown (easy to version control + diff)
- Include confidence scores and parallelizable flags in collapsible sections
- Output ready to commit to GitHub / paste into wiki
- Example: `hackathon-ideas-june-2024.md`

### Workflow Examples:

**Google Docs only**:
```
"what should I build for [hackathon brief]: [url/pasted]
put it in: [google doc url]"
```

**Google Docs + Markdown**:
```
"what should I build for [hackathon brief]: [url/pasted]
put it in: [google doc url]
also give me markdown for github"
```

**Markdown only (no Google Docs)**:
```
"what should I build for [hackathon brief]: [url/pasted]
output as markdown for github"
```

## Example Idea Output

```
**Idea: AquaWatch** | Confidence: 8/10

Rationale: IoT sensors track real-time water quality in local watersheds, 
crowdsourced data feeds a mobile app for community reporting.

Killer Product Analysis:
- Judging criteria match: "Environmental impact" + "Data visualization" rubric (60% of judging weight)
- Achievable in 36 hours: 2 devs handle frontend + backend, 1 handles sensor mock data
- Wow factor: Live map showing water quality + citizen reports (users can contribute immediately)
- Prize alignment: Environmental track prizes = direct fit

Potential Cons/Risks & Mitigations:
- **Technical blocker**: Real IoT sensors won't arrive in time
  → **Mitigation**: Use mock data from public water quality APIs (OpenWeatherMap, AirVisual); pre-populate demo with realistic readings
- **Execution risk**: Map rendering with 100+ data points could slow down
  → **Mitigation**: Implement clustering; start with 20-30 points; optimize or defer to post-hackathon if needed
- **Judging perception**: Sensors feel gimmicky without real hardware
  → **Mitigation**: Frame as "citizen science platform" powered by public APIs; emphasize accessibility, not hardware
- **UX gap**: Crowdsourced data quality suffers without moderation
  → **Mitigation**: Pre-seed demo data with clean entries; disable user contributions for hackathon demo; position as future feature
- **Data accuracy**: Relying on free public APIs with rate limits
  → **Mitigation**: Cache API responses 1h; test API limits during dev; have offline fallback data

Tech Stack & Effort Breakdown:
| Component | Hours | Parallelizable | Notes |
|-----------|-------|----------------|-------|
| Frontend (React + Mapbox) | 7-8h | Yes (after API contracts defined) | App shell, map rendering, report UI |
| Backend (Node.js + APIs) | 5-6h | Yes (in parallel with frontend) | API polling, CRUD, caching |
| Data integration | 2-3h | Partial | Can start while backend scaffolds |
| Deployment (Vercel) | 1-2h | Yes (parallel with feature dev) | Auto-deploy setup |
| Testing/Polish | 3-4h | No (must wait for features) | Bug fixes, UI refinement |
| **Total (Sequential)** | **18-23h** | — | Linear path if done serially |
| **Total (Parallel)** | **~14h** | — | Realistic: frontend + backend in parallel (7-8h), then deploy (1h), then test (3-4h) |

**Team Parallelization Strategy**:
- **Dev 1** (Frontend): React setup, map component, form UI (7-8h, can start immediately)
- **Dev 2** (Backend): API contracts, water quality service, CRUD endpoints (5-6h, can start immediately in parallel)
- **Dev 1 + Dev 2** (Integration): Wire frontend to backend, test end-to-end (2-3h, sequential after both done)
- **Anyone** (Deployment): Set up Vercel, GitHub Actions (1-2h, can happen in parallel with integration)
- **Both** (Polish): Bug fixes, animations, edge cases (3-4h, final push)

Feature Roadmap:
- **MVP (must-have, 14h)**: Map UI + live water quality data + basic citizen reports + search by location
- **Nice-to-Have (if time, 5h)**: Trend graphs, notification alerts, water safety recommendations
- **Demo layer**: Pre-populate 10 report locations, cache real water quality data, show map with live user contributions
```

## Notes for Claude Using This Skill

- **Be Aggressive on Scope**: Hackathons reward finished demos, not ambitious failures. Suggest ideas where the MVP is tight and achievable.
- **Reference User Skills, Don't Constrain**: If user mentioned "junior dev" but the hackathon has a "technical excellence" prize, still suggest technically ambitious ideas with a tight MVP scope.
- **Assume Best Case**: Users will pull all-nighters; give them ideas worth staying up for.
- **Multiple Ideas = Optionality**: 5+ ideas per track lets the user pick based on their gut, team energy, and real-time constraints.
- **Justify Why It Wins**: Every idea needs a clear reason it'll score well on that specific rubric, not just be cool.

