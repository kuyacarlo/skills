# Audit log format

Append one entry to `$AGENT_CONFIG_HOME/AUDIT.md` at the end of every session.

## Template

```markdown
### YYYY-MM-DD HH:MM — <agent> @ <project>
- **Duration**: ~Xm
- **Branch**: <branch name>
- **What happened**: <1-3 sentences summarizing work done>
- **Commits**: <count> (<short hashes or "none">)
- **Files touched**: <count> (<key files listed>)
- **User direction**: <what the user asked for, their exact framing if notable>
- **Decisions made**: <choices the agent made autonomously>
- **Left incomplete**: <what's still pending, if anything>
- **Next step**: <concrete next action for the next session>
```

## Rules

1. One entry per session. A session = one continuous agent conversation.
2. Keep entries concise. Max 10 lines per entry.
3. If multiple projects were touched, log one entry per project.
4. "User direction" captures intent — what the user actually said, not interpretation.
5. "Decisions made" logs autonomous choices so the user can audit later.
6. Never delete entries. Append only.
7. Agents read last 1-3 entries on session start. Do not read the full log.

## Example entries

```markdown
### 2026-07-28 14:30 — claude @ seekers-guild
- **Duration**: ~40m
- **Branch**: feat/auth-flow
- **What happened**: Implemented Authentik OIDC login flow with PKCE. Added callback route and session middleware.
- **Commits**: 4 (a1b2c3d, e4f5g6h, i7j8k9l, m0n1o2p)
- **Files touched**: 6 (src/auth/*, src/middleware/session.ts, .env.example)
- **User direction**: "wire up authentik login, use PKCE, keep it simple"
- **Decisions made**: Used iron-session over next-auth (lighter, no magic). Stored OIDC config in env vars not DB.
- **Left incomplete**: Logout endpoint not implemented yet.
- **Next step**: Add /api/auth/logout with token revocation.

### 2026-07-29 22:15 — agy @ homelab
- **Duration**: ~15m
- **Branch**: main
- **What happened**: Fixed Caddy reverse proxy config for new gitea instance. Added DNS entry to Netbird.
- **Commits**: 2 (q3r4s5t, u6v7w8x)
- **Files touched**: 3 (caddy/Caddyfile, dns/zones/home.zone, quadlets/gitea.container)
- **User direction**: "gitea isn't reachable from thinkpad, fix"
- **Decisions made**: Used internal Netbird DNS instead of public A record. Kept HTTP challenge for TLS.
- **Left incomplete**: None.
- **Next step**: None (complete).

### 2026-08-01 00:20 — kiro @ skills
- **Duration**: ~25m
- **Branch**: feat/package-skills-ci
- **What happened**: Modernized all 13 skills for agent-agnostic portability. Compressed heavy skills via references/. Created operations skill + audit format.
- **Commits**: 3 (0217436, b619a6b, 42fb7e1)
- **Files touched**: 17 (all skills/*/SKILL.md, new references/ files)
- **User direction**: "hit it" — modernize per agentskills.io spec, then set up commit discipline + audit
- **Decisions made**: Progressive disclosure pattern. Operations as a proper skill not just a config file.
- **Left incomplete**: Push to remote.
- **Next step**: Push branch, verify deploy.
```
