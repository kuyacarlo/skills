---
name: free-tier-deploy
description: >-
  Deploy and debug apps on free-tier hosts — Cloudflare Workers/Pages, Vercel,
  Fly.io, Railway, Render. Use when deploying, fixing cold starts, env/secrets,
  custom domains, or choosing a free host. Prefer working commands over theory.
---

# Free-Tier Deploy

Pick the lightest host that fits. Prefer **static / edge** when the app allows it.

## Host picker

| Shape | Default | Notes |
|-------|---------|--------|
| Static site / Astro / Vite SPA | **Cloudflare Pages** or **Vercel** | Fast CI; custom domain easy |
| Edge API / cron / KV | **Cloudflare Workers** | Generous free tier; no long CPU |
| Containers / Docker | **Fly.io** or **Railway** | Fly = global VMs; watch free allowances |
| Classic Node web | **Vercel** or **Render** | Serverless functions vs always-on |

Student / low-budget rule: start on **Pages/Workers or Vercel**; move to Fly only if you need containers or persistent sockets.

## Cloudflare Pages / Workers

```bash
npx wrangler login
npx wrangler pages project create <name>
npx wrangler pages deploy dist --project-name=<name>
# Workers
npx wrangler deploy
```

- Secrets: `wrangler secret put NAME` (never commit)
- Local: `wrangler dev`
- Trap: Node APIs that need full Node — check Workers compatibility flags / `nodejs_compat`

## Vercel

```bash
npx vercel          # preview
npx vercel --prod   # production
```

- Env: dashboard or `vercel env pull`
- Trap: serverless timeouts / payload limits on hobby

## Fly.io (containers)

```bash
fly launch
fly deploy
fly logs
fly ssh console
```

Minimal images often lack `curl`/`ps`. Prefer language-native health checks:

```bash
# Python
python3 -c "import urllib.request; print(urllib.request.urlopen('http://127.0.0.1:8080/health', timeout=5).read())"
```

Bind dual-stack when using Fly private networking: host `::` not only `0.0.0.0`.

## Railway / Render

- Connect GitHub → set start command → add env vars in UI
- Trap: sleeping free dynos → cold start; keep health endpoint cheap

## Checklist before “it works”

- [ ] Health route returns 200
- [ ] Secrets not in git
- [ ] Build output path matches host (`dist`, `.vercel/output`, etc.)
- [ ] Custom domain DNS verified
- [ ] One smoke hit from outside (`curl -I https://…`)
