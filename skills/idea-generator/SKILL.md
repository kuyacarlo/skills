---
name: idea-generator
description: Project idea generator. Parses problem briefs, lists high-scoring project ideas, and organizes milestones. Defaults to outputting in the chat.
---

# 🏆 Project Idea Generator

Generate competitive project ideas optimized for implementation success, with full tech stack options and achievable feature roadmaps.

## Workflow

```
User Input:
  "what should I build for this problem: [URL, description, or pasted brief]"
  "put it in: [Document or Vault URL/Path]" (optional)

Agent Output:
  1. Parses the problem description (scrapes URL or analyzes pasted content)
  2. Extracts: themes/tracks, success criteria, constraints, time, team details
  3. Generates 5+ ideas per problem
  4. For each idea: name + rationale + competitive product analysis + cons/risks + tech stack with effort breakdown
  5. Optimizes for: constraints, team capacity, and value alignment
  6. (If target document path provided) Writes to the target document with timestamp
```

## Input Requirements

### Problem Brief Source
- **URL**: User provides a direct link (e.g. github repository, project brief)
- **Pasted Content**: User pastes the full problem statement, requirements, or theme

### Document Export Integration (Optional)
- Check user context or connected MCP servers to see if note-taking tools, personal vaults (like ZenNotes), or document editors (like Google Docs or office suites) are connected.
- If a target path or URL is provided, automatically connect and write the output to that document.
- **Default Action:** By default, output the generated ideas directly in the chat, creating a markdown artifact only when necessary (in lieu of chat).

## Parsing Strategy

Extract from the brief:
- **Problem Statement(s)** or **Core Themes**
- **Constraints**: Deadline/timeframe, team size restrictions, technology restrictions
- **User Context** (if provided): skills, experience level, team composition
- **Deliverable Requirements**: code repo, documentation, or demo expectations

## Idea Generation Framework

### Per Idea, Provide:

1. **Project Name** - Catchy, memorable, reflects the idea
2. **Confidence Score** (1-10) - How well this idea matches the criteria:
   - 9-10: Perfect fit, clear impact, team skills align, low execution risk
   - 7-8: Strong match, achievable in timeframe, minor concerns
   - 5-6: Decent potential but has meaningful tradeoffs
   - 3-4: Risky or loose fit
3. **Rationale** (1-3 sentences max) - Why this solves the problem
4. **Competitive Product Analysis** - Why this wins:
   - How it scores high on criteria
   - Why it's achievable in the constraints
   - Competitive advantage (what makes it stand out)
5. **Potential Cons/Risks** - Be honest about downsides, with mitigation strategies:
   - **Technical blockers** (what could break) → Mitigation
   - **Execution risks** (scope creep, API failures, auth complexity) → Mitigation
   - **Data/legal risks** (need real data, scraping, IP) → Mitigation
   - **UX gaps** (what looks janky in crunch time) → Mitigation

### Tech Stack Guidance with Effort Breakdown:
- **Frontend**: Recommend based on time + team skills (React/Vue for quick MVPs, plain HTML+JS for minimal)
  - Estimate hours (e.g., "React setup + UI: 6-8h")
  - **Parallelizable**: Yes/No (can frontend be built while backend is being coded?)
- **Backend**: API choice based on deployment (Vercel Functions, simple Express, FastAPI)
  - Estimate hours (e.g., "API endpoints + database: 4-6h")
  - **Parallelizable**: Yes/No
- **Database**: Only if necessary (prefer in-memory or free tier services)
  - Estimate hours if applicable
- **Deployment**: Free tier only (Vercel, Netlify, Railway, Replit, etc.)
  - Estimate hours ("Setup CI/CD: 1-2h")
  - **Parallelizable**: Usually Yes
- **Total MVP Time (Sequential)**: Sum of all components
- **Total MVP Time (Parallel)**: Longest blocking path (shows real time if team works in parallel)

### Feature Roadmap:
- **MVP (Must-Have)**: Core 1-2 features, achievable in 50% of time
- **Nice-to-Have**: 2-3 features if time permits
- **Demo Layer**: How to present it compellingly (UI polish, demo data, pre-recorded fallbacks)

## Optimization for Success

Each idea should explicitly consider:
1. **Rubric/Goal Match**: Ideas should clearly map to user goals
2. **Scope Realism**: Be ruthless — cut scope that can't be done in the time window
3. **Team Fit**: Suggest ideas where team composition splits make sense
4. **Wow Factor**: What's the standout feature that makes the demo memorable?

## Output Formats

Format the output cleanly in markdown:
- Use **bold** for project names
- Use `---` dividers between ideas
- Use markdown tables for effort breakdown (easy to version control + diff)
- Include confidence scores and parallelizable flags in collapsible sections

## Example Idea Output

```
**Idea: AquaWatch** | Confidence: 8/10

Rationale: IoT sensors track real-time water quality in local watersheds,
crowdsourced data feeds a mobile app for community reporting.

Product Analysis:
- Focus area match: "Environmental impact" + "Data visualization" (60% of target weight)
- Achievable in 36 hours: 2 devs handle frontend + backend, 1 handles sensor mock data
- Wow factor: Live map showing water quality + citizen reports (users can contribute immediately)

Potential Cons/Risks & Mitigations:
- **Technical blocker**: Real IoT sensors won't arrive in time
  → **Mitigation**: Use mock data from public water quality APIs; pre-populate demo with realistic readings
- **Execution risk**: Map rendering with 100+ data points could slow down
  → **Mitigation**: Implement clustering; start with 20-30 points
- **UX gap**: Crowdsourced data quality suffers without moderation
  → **Mitigation**: Pre-seed demo data with clean entries; disable user contributions for initial demo

Tech Stack & Effort Breakdown:
| Component | Hours | Parallelizable | Notes |
|-----------|-------|----------------|-------|
| Frontend (React + Mapbox) | 7-8h | Yes (after API contracts defined) | App shell, map rendering, report UI |
| Backend (Node.js + APIs) | 5-6h | Yes (in parallel with frontend) | API polling, CRUD, caching |
| Data integration | 2-3h | Partial | Can start while backend scaffolds |
| Deployment (Vercel) | 1-2h | Yes (parallel with feature dev) | Auto-deploy setup |
| Testing/Polish | 3-4h | No (must wait for features) | Bug fixes, UI refinement |
| **Total (Sequential)** | **18-23h** | — | Linear path if done serially |
| **Total (Parallel)** | **~14h** | — | Realistic: frontend + backend in parallel, then deploy, then test |

Feature Roadmap:
- **MVP (must-have, 14h)**: Map UI + live water quality data + basic citizen reports
- **Nice-to-Have (if time, 5h)**: Trend graphs, notification alerts, water safety recommendations
- **Demo layer**: Pre-populate 10 report locations, cache real water quality data
```

## 🔗 Collaboration & Loop Directives
*   **Transition to Grilling (Divergent → Convergent):** Once ideas are generated and the user selects/suggests alternatives, **immediately trigger the `idea-evaluation` skill**. Formally transition the conversation to the grilling phase, challenging assumptions, auditing pitfalls, and calculating Go/No-Go/Pivot verdicts to narrow down the choices to 1-2 project ideas.
