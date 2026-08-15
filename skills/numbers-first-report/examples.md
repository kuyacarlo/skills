# Example: freestack catalog gap report (Aug 2026)

Canonical sample of a numbers-first report. Condensed from the freestack session.

## Current shape

- **187 tools** in `src/data/tools.ts` across 17 categories.
- **Heavy:** AI (47, ~25%), student (20), startup (17), security (13).
- **Thin:** learning (4), cloud (5), storage (5), jobs (5), auth (6), design (6), observability (6).
- Source of truth: `tools.ts`. Talks in `talks/saas-stack/` list Pack partners not yet in the catalog.
- Prior research: PR `#4` / commits adding agy gaps + AI IDEs. Chat-only Claude/Grok free tiers skipped on purpose.

## What forums and lists keep recommending

1. Claim GitHub Pack first, then JetBrains / Azure / domains / DO.
2. Edge-first $0 stack: Workers + D1/Neon + R2 + Clerk/Better Auth + Resend.
3. Self-host PaaS (Coolify and peers) as the escape-SaaS path.
4. DB free-tier volatility: PlanetScale free gone; Cockroach / Firebase / Surreal compared often.
5. Cloudflare surface beyond Workers/D1/R2: KV, Queues, Hyperdrive, Email Routing, Durable Objects.
6. Pack long-tail (QA, Git GUIs, Mailgun, Bootstrap Studio, Deepnote) lives in talks, not `tools.ts`.
7. Microsoft for Startups / Founders Hub as the accessible large credit program for bootstrappers.

## Highest-value adds

### P0 — ship-the-stack

| Candidate | Category | Why |
|-----------|----------|-----|
| Cloudflare KV | storage | Always in CF-only stack posts |
| Cloudflare Queues | jobs | Free-tier messaging with Workers |
| Cloudflare Hyperdrive | databases | Neon/Postgres from Workers |
| Cloudflare Email Routing | email | Free inbound aliases |
| CockroachDB Serverless | databases | ~10 GiB free; comparison staple |
| Firebase / Firestore | databases | Tutorial default BaaS |
| Umami | observability | Privacy analytics; already in talks |
| Microsoft for Startups | startup | Up to ~$150k Azure; bootstrap-friendly |

### P1 — Pack long-tail (verify live)

GitKraken, BrowserStack / LambdaTest, Bootstrap Studio, Deepnote, Mailgun (if live), ConfigCat, Polypane, Imgbot, `.TECH` domain.

### P2 — thin fills

freeCodeCamp / Odin / Exercism; Grafana Cloud; Dokploy; AWS Free Tier row distinct from Activate.

### P3 — niche

Hack Club Nest, Replit Education — only if youth / campus scope matters.

## Explicitly skip

| Item | Reason |
|------|--------|
| PlanetScale Hobby | Free tier removed — caution / anti-reco only |
| Chat-only Claude/Grok “free” | No solid free *API* tier |
| Spotify / Apple Education | Lifestyle, not developer stack |
| Blind Pack dump | Offers pause; verify or mark `check` |

## Suggested implementation wave

1. Cloudflare surface + Cockroach + Firebase + Umami + Microsoft for Startups.
2. Top verified Pack long-tail.
3. Thin learning / obs / self-host fills.
4. Re-verify limits, bump `verified` dates, `pnpm sync:awesome`.

## Bottom line

freestack is already strong on AI, core free SaaS, and must-claim student programs. Largest gaps vs 2026 discourse: Cloudflare product depth, Pack long-tail stuck in talk decks, DB comparison staples, Microsoft for Startups, thin learning/obs. Prefer verifying and promoting those over adding more LLM APIs.
