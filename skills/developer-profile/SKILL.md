---
name: developer-profile
description: Generates a quantified developer profile to integrate with active AI tools, CLI agents, and IDEs. Captures developer capabilities, stacks, and constraints to prevent repetitive questions. Default to outputting to the chat.
---

# Developer Profile Skill

**Purpose:** Build a one-shot, composable profile that active agents, IDEs, and CLI tools can read to make intelligent recommendations without repetitive context questions.

**Dynamic Tooling Check & Default Output:** You must check the user context and environment dynamically to identify what AI tools, IDEs, or CLI tools are in use (e.g. VSCode, Cursor, Aider, standard CLI agents). If specific profiles or conventions files are supported, automatically generate files matching those formats. Otherwise, default to outputting the profile directly in the chat, creating a markdown artifact only when necessary (in lieu of chat).

---

## Pre-Filled Example: Karlo's Profile

### One-Page Summary

```
Name: Karlo
Role: CTO @ Seekers Guild | BSU CompE (2028)
Personality: ENTP, Type 5 | Civic tech focus | Self-hosted > managed SaaS

PRIMARY STACK:
  Backend:  FastAPI, Python, PostgreSQL (5+ shipped production services)
  Frontend: React, TypeScript
  DevOps:   Podman (rootless), GitHub Actions, Authentik (OIDC), Infisical

PERFORMANCE (Measured):
  Without AI:           1.0x time,  70% correctness,  strength: architecture
  With AI:              0.6x time,  92% correctness,  AI fills: syntax, edge cases, library patterns
  Architecting w/ AI:   0.4x time,  better design,    explores 3-5 alternatives upfront

WILL BUILD:
  ✅ Civic tech + social impact
  ✅ Self-hosted or portable (no lock-in)
  ✅ Novel integrations (OIDC + existing systems)
  ✅ Portfolio/learning value

WILL SKIP:
  ❌ Managed-SaaS-only solutions
  ❌ Boilerplate-heavy frameworks
  ❌ Framework churn without evaluation

CONSTRAINTS:
  • Student schedule (limited hours/week)
  • Homelab budget (high creativity, minimal spend)
  • Control-first mentality (prefers understanding internals)

CODE PATTERNS (Always Used):
  1. Layered backend:   routes → services → adapters → models (no cycles)
  2. Adapter pattern:   Swappable providers (Supabase, Authentik, databases)
  3. DI:                FastAPI Depends() for testability
  4. CI/CD-first:       GitHub Actions on every PR (lint → test → build → deploy)
  5. Secrets:           Infisical, never .env in git
  6. Observability:     Prometheus + Grafana + Loki
  7. Containers:        Podman quadlets, rootless, SELinux

KNOWN PAIN POINTS:
  • Pydantic enum serialization    → field_serializer workaround
  • Rootless Podman volumes        → :U flag on mounts
  • FastAPI exception + Depends()  → validate inside Depends()
  • libvirt DHCP conflicts         → (learned on homelab infrastructure)
  
RECENT SHIPPED:
  • ComplyAIgent:      FastAPI auth server + LangGraph compliance HITL (DevSecOps)
  • Bantay:            Secret scanner + LLM risk scoring + CIBA approval (Auth0)
  • Seekers Guild:     OIDC + Supabase auth integration (civic tech IAM)
  • Homelab:           Nextcloud AIO, Authentik, Netbird mesh, full observability
```

---

## Outputs (Copy-Paste Ready)

### 1. AGY CLI Tool (JSON)

File: `~/.config/karlo/agy-context.json`

```json
{
  "meta": {
    "format": "developer-context-v1",
    "lastUpdated": "2026-06-21",
    "projects_shipped": ["ComplyAIgent", "Bantay", "Seekers Guild", "homelab"]
  },
  
  "profile": {
    "name": "Karlo",
    "role": "CTO @ Seekers Guild, BSU CompE (2028)",
    "personality": "ENTP Type 5",
    "primary_interest": "Civic tech, data engineering, self-hosted DevOps"
  },
  
  "stack": {
    "backend": {
      "primary": ["FastAPI", "Python", "PostgreSQL"],
      "secondary": ["Golang", "Node.js"],
      "proficiency": "shipped production systems"
    },
    "frontend": {
      "primary": ["React", "TypeScript"],
      "proficiency": "shipped user-facing features"
    },
    "infrastructure": {
      "containerization": "Podman (rootless)",
      "auth": "Authentik (self-hosted OIDC)",
      "secrets": "Infisical",
      "networking": "Netbird (self-hosted mesh)",
      "observability": "Prometheus + Grafana + Loki",
      "ci_cd": "GitHub Actions",
      "proficiency": "built & maintained homelab 32GB andromeda"
    }
  },
  
  "performance": {
    "without_ai": {
      "time_baseline": 1.0,
      "correctness": 0.70,
      "strength": ["architecture design", "security patterns", "system thinking"],
      "weakness": ["edge cases", "syntax details", "library semantics"]
    },
    "with_ai": {
      "time_multiplier": 0.6,
      "correctness": 0.92,
      "ai_role": "debugging, syntax, library patterns, edge case discovery",
      "my_role": "design decisions, integration strategy, security scoping",
      "confidence": "high on logic/architecture, medium on library semantics"
    },
    "architecting_with_ai": {
      "time_multiplier": 0.4,
      "design_quality": "explores 3-5 alternatives, validates constraints upfront",
      "ai_role": "trade-off analysis, precedent research, integration examples",
      "my_role": "propose constraints, evaluate fit, make final calls",
      "strength": "faster exploration, catch design issues early"
    }
  },
  
  "decision_matrix": {
    "will_build": [
      "Civic tech or social impact",
      "Self-hosted or portable (no lock-in)",
      "Novel integrations (OIDC + existing)",
      "Portfolio/learning value"
    ],
    "will_skip": [
      "Managed-SaaS-only solutions",
      "Boilerplate-heavy frameworks",
      "Framework churn (evaluates tradeoffs first)"
    ],
    "constraints": [
      "Student schedule (limited hours/week)",
      "Homelab budget (high creativity, low spend)",
      "Control-first mentality (understand internals)"
    ]
  },
  
  "code_patterns": [
    {
      "name": "Layered Backend",
      "rule": "routes → services → adapters → models (never circular)",
      "structure": "models/, routes/, services/, adapters/, schemas/, utils/",
      "applies_to": "all backends"
    },
    {
      "name": "Adapter Pattern",
      "rule": "Swappable external providers (databases, auth, APIs)",
      "example": "OIDCProvider abstract → SupabaseOIDC, AuthentikOIDC concrete",
      "benefit": "swap providers without rewriting business logic"
    },
    {
      "name": "Dependency Injection",
      "tool": "FastAPI Depends()",
      "benefit": "testability, loose coupling, explicit dependencies"
    },
    {
      "name": "CI/CD-First",
      "rule": "GitHub Actions on every PR: lint → test → build → deploy",
      "tools": "ruff, mypy, pytest, Docker/Podman"
    }
  ],
  
  "known_issues": [
    {
      "issue": "Pydantic enum serialization",
      "symptom": "Enums serialize as enum_name.value instead of value",
      "resolution": "Use field_serializer on Pydantic model",
      "time_cost": "2-3 hours without AI guidance"
    },
    {
      "issue": "Rootless Podman volume permissions",
      "symptom": "Mounted volumes owned by nobody:nobody",
      "resolution": "Add :U flag on volume mount (-v /host:/container:U)",
      "time_cost": "1-2 hours debugging"
    },
    {
      "issue": "FastAPI exception handlers + Depends()",
      "symptom": "Custom exception handlers don't catch Depends() failures",
      "resolution": "Validate inside Depends(), raise from there",
      "time_cost": "1 hour"
    }
  ],
  
  "agent_instructions": {
    "when_suggesting_tech": "Always ask: Is this self-hosted compatible? Learning value? Swappable? Check stack fit first. If not in primary stacks, verify before recommending.",
    "when_recommending_projects": "Check will_build and will_skip lists. If it's civic tech + self-hosted potential, likely yes. If managed-only, rethink.",
    "when_facing_unknowns": "Karlo learns fast and reads code. Don't baby-step. Assume: FastAPI patterns, React hooks, Docker/Podman, deployment fundamentals. Explain: novel library semantics, security edge cases, integration quirks.",
    "on_architecture_questions": "ENTP personality: show trade-offs and alternatives, not dogma. Respect the exploration; final call is mine."
  }
}
```

**How AGY uses it:**
```bash
agy --profile ~/.config/karlo/agy-context.json
# OR in shell config:
export AGY_PROFILE=~/.config/karlo/agy-context.json
```

---

### 2. Cursor Rules (Drop in `.cursor/rules/`)

File: `.cursor/rules/KARLO_CONTEXT.mdc`

```markdown
---
type: "static"
---

# Developer Context: Karlo

## Quick Summary
- **Stack**: FastAPI + React + Podman (self-hosted), Python backend, TypeScript frontend
- **Experience**: 5+ shipped production FastAPI services, homelab infrastructure, civic tech
- **Personality**: ENTP, explores rigorously then decides, self-hosted > managed SaaS
- **Speed**: With AI assistance, ~0.6x baseline time. Without AI: 70% first-pass correctness.

## Backend Patterns
Code structure: `routes → services → adapters → models` (never circular)
- Use Pydantic models for everything (no dict/Any)
- FastAPI `Depends()` for testability and dependency injection
- Adapter pattern for external integrations (swappable providers)
- Type hints complete, docstrings on public functions

### Example
```python
# adapters/oidc.py
class OIDCProvider(ABC):
    @abstractmethod
    def token_endpoint(self) -> str: ...

class SupabaseOIDC(OIDCProvider): ...
class AuthentikOIDC(OIDCProvider): ...

# routes/auth.py
@app.post("/token")
async def get_token(provider: OIDCProvider = Depends(get_oidc_provider)):
    return await provider.fetch_token()
```

## Frontend Patterns
React: `components/` (views only) + `hooks/` (logic, portable) + `services/` (API clients)
- Logic lives in custom hooks, never buried in components
- TypeScript strict mode, no `any`
- Use hooks for shared state and side effects

## Infrastructure Standards
- **Container runtime**: Podman (rootless), quadlets, SELinux
- **Secrets**: Infisical (never .env in git)
- **Auth**: Authentik (self-hosted OIDC)
- **CI/CD**: GitHub Actions (lint → test → build → deploy)
- **Observability**: Prometheus metrics, Grafana dashboards, Loki logs (JSON-structured)
- **Code quality**: ruff (linting), mypy (typing), pytest (>80% coverage)

## Known Issues & Workarounds
| Problem | Fix |
|---------|-----|
| Pydantic enum serialization | Use `field_serializer` on model |
| Rootless Podman volumes | Add `:U` flag on mount |
| FastAPI exception handlers | Validate inside Depends() |

## Decision Framework
**Will build**: Civic tech, self-hosted, novel integrations, portfolio value
**Will skip**: Managed-SaaS-only, boilerplate sprawl, framework hype
**Constraints**: Student schedule, homelab budget, control-first mindset

## How to Help
- **When I ask for architecture**: Show alternatives + trade-offs, not dogma
- **When I ask for code**: Name specific patterns/frameworks. No vague generalities.
- **When I mention "self-hosted first"**: Don't suggest managed-only as Plan A
- **When I'm learning something new**: I read code well; give examples, not explanations
- **On error context**: Use Cursor's debug mode to capture stacks and logs

## Tech I Know
✅ FastAPI, Python, PostgreSQL, Docker/Podman, GitHub Actions, OIDC/OAuth2, React/TS, SELinux, Kubernetes basics, Linux sysadmin

❓ Not sure about: Mobile (Flutter/Kotlin/Dart), ML frameworks beyond basics, WebAssembly

## What Success Looks Like
- Code compiles/tests pass on first try
- Architecture decisions are sound (no rewrites)
- Secrets never leak (all in Infisical)
- Deployments are repeatable (CI/CD working)
- Code is readable & maintainable (patterns clear)
```

---

### 3. Aider Conventions (Drop in `CONVENTIONS.md`)

```markdown
# Code Conventions

## Backend (FastAPI)

### Folder Structure
```
src/
├── models/       # Pydantic + SQLAlchemy (data models)
├── routes/       # FastAPI endpoint handlers (thin, delegate to services)
├── services/     # Business logic (isolated, testable)
├── adapters/     # External API clients (Supabase, OIDC, databases)
├── schemas/      # Request/response Pydantic schemas
└── utils/        # Shared: logging, validators, error handlers
```

**Rule**: Routes (entry) → Services (logic) → Adapters (external) → Models (data).
No circular imports. No direct DB queries in routes.

### Patterns
- **Type hints**: Full Pydantic models, no `dict` or `Any`
- **Dependency Injection**: FastAPI `Depends()` everywhere
- **Error handling**: Validate in `Depends()`, raise appropriate exceptions
- **Secrets**: Infisical, load at runtime. Never hardcode API keys.

### Example: Auth Service
```python
# models/user.py
class User(BaseModel):
    id: UUID
    email: EmailStr
    is_active: bool

# adapters/oidc.py
class OIDCProvider(ABC):
    @abstractmethod
    async def fetch_token(self, code: str) -> dict: ...

# services/auth.py
class AuthService:
    def __init__(self, provider: OIDCProvider, db: AsyncSession):
        self.provider = provider
        self.db = db
    
    async def login(self, code: str) -> User:
        token = await self.provider.fetch_token(code)
        user = await self._get_or_create_user(token)
        return user

# routes/auth.py
@app.post("/callback")
async def auth_callback(
    code: str,
    service: AuthService = Depends(get_auth_service)
):
    return await service.login(code)
```

## Frontend (React)

### Structure
```
src/
├── components/   # UI components (one concern per file)
├── hooks/        # Custom React hooks (logic, reusable)
├── pages/        # Route-level wrappers
├── services/     # API client functions
└── types/        # TypeScript interfaces
```

**Rule**: Logic in hooks, views in components. No business logic in JSX.

### Example: Auth Hook
```typescript
// hooks/useAuth.ts
export function useAuth() {
  const [user, setUser] = useState<User | null>(null);
  
  const login = async (code: string) => {
    const response = await authService.login(code);
    setUser(response.user);
  };
  
  return { user, login };
}

// components/LoginButton.tsx
export function LoginButton() {
  const { login } = useAuth();
  return <button onClick={() => login(code)}>Login</button>;
}
```

## CI/CD (GitHub Actions)

```yaml
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Lint (ruff)
        run: ruff check .
      
      - name: Format check (ruff)
        run: ruff format . --check
      
      - name: Type check (mypy)
        run: mypy src/
      
      - name: Test (pytest)
        run: pytest --cov=src tests/
        env:
          DATABASE_URL: "postgresql://test:test@localhost/test"
      
      - name: Build Docker
        run: docker buildx build --push --tag ghcr.io/${{ github.repository }}:${{ github.sha }} .
```

## Secrets & Env
- **Never commit**: API keys, database passwords, private keys
- **Use Infisical**: Store all secrets, load at runtime via env vars
- **.env files**: Local development only, never committed
- **In production**: Secrets come from Infisical or cloud secret manager

## Testing
- **Framework**: pytest
- **Coverage**: >80% on src/
- **Mocking**: Use unittest.mock for external integrations
- **Database**: Use PostgreSQL fixtures for integration tests

## Documentation
- **Type hints**: Always include
- **Public functions**: Include docstring (1-2 lines)
- **Complex logic**: Inline comments (why, not what)
- **README**: Setup instructions, architecture overview, how to run tests/lint
```

---

## How to Build Your Own Profile

1. **List your shipped projects** (3-5 recent ones)
2. **Estimate performance metrics** (time without AI vs. with AI)
3. **Document your actual code patterns** (not aspirational)
4. **Copy the templates above** and fill in your data
5. **Version in git** (e.g., `setup-scripts/context/profile.json`)
6. **Test it**: Ask an AI agent for a project rec using just your profile

### Quick Checklist
- [ ] Shipped projects listed (with outcomes)
- [ ] Performance metrics estimated (3 modes)
- [ ] Decision matrix filled (will build / will skip)
- [ ] Code patterns documented (actual, not theoretical)
- [ ] Pain points & workarounds listed
- [ ] JSON generated (for AGY)
- [ ] Cursor rules created (for IDE)
- [ ] Aider conventions created (for CLI pair programming)
- [ ] Files version-controlled
- [ ] Tested with one agent (show it the profile, ask for recommendations)

---

## Integration Points

### With AGY
```bash
# Set in shell config
export AGY_PROFILE=~/.config/karlo/agy-context.json

# Or pass directly
agy --profile ~/.config/karlo/agy-context.json "help me evaluate project ideas"
```

### With Cursor
Copy `.cursor/rules/KARLO_CONTEXT.mdc` into your project's `.cursor/rules/` directory. Cursor auto-loads on startup.

### With Aider
```bash
# In .aider.conf.yml
read:
  - CONVENTIONS.md
  - ARCHITECTURE.md
```

### With Claude/ChatGPT/Gemini
Paste `ABOUT_ME.md` (Markdown summary) into the chat when asking for project advice.

### With Spec-Kit
If using spec-kit for new projects:
```bash
specify init my-project
# Then load your constitution
cp CONSTITUTION.yaml .specify/constitution.yaml
```

---

## Maintenance

Update **every 3-6 months** as you ship new projects:

```
2026-06-21: Initial (ComplyAIgent, Bantay, Seekers Guild, homelab)
2026-09-21: After Sanctuary hackathon (event-driven patterns)
2026-12-21: After next major project (new learnings)
```

Track in git:
```bash
git log --oneline context/profile.json
# Shows evolution of your capabilities over time
```

---

## Why This Works

- **One read, actionable decision**: Agents don't need clarification calls
- **Integrated everywhere**: Cursor, Aider, AGY, chatbots, all read the same source of truth
- **Prevents alignment problems**: All tools know your patterns, constraints, and what you'll ship
- **Portable**: Copy your profile to any new project/tool
- **Versioned**: Git history shows how you've evolved
