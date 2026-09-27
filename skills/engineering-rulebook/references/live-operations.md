# Live operations

Read this guide only when its workflow applies.

## Changing something that is live

1. **Read-only discovery first.** Look at the running state. Do not design from
   documentation — it goes stale, and the box is the truth.
2. **Back the file up, dated.** `foo.yaml.bak-20260731`.
3. **Change one thing.** Never run the full deployment path for a small edit.
4. **Verify by diffing, not by looking.** "It looked fine" is not verification.
5. **Guarantee nothing notified anyone, or do not ship it.** Red line 1.
6. **Record the drift, then close it.** A live change is not finished until the
   repo matches it. Everything else is step 3 and 4 of the loop, deferred.

One config file can wedge a whole service's boot, not just the feature it
configures. Validate before you restart, and know your rollback before you need
it.

## Cost is a constraint

Before moving work onto a metered service, name the scarce resource and its
marginal cost. This includes CI minutes, hosted runners, databases, and APIs.

- A paid plan may buy seats or support while the metered resource remains metered.
- Do not move work to a more expensive machine class without a need.
- Check standing spending directives before proposing a purchase.

Treat “X does not need Y” as a finding. Do not select Y without resolving it.

## Promoting between environments

Portable rules. The names change; the ordering does not.

- **Development deploys from the trunk. Production deploys from a tagged,
  released commit.** Never the reverse, and never a direct push to production.
- **A second human approves the promotion.** Not the person who cut the release.
- **Migrations go first, alone, and verified — then the code.** They must be
  backward-compatible with the code currently running, because there is always a
  window where the old code meets the new schema. Expand, then contract.
- **Every gate must query the environment it is actually gating.** A gate reading
  the wrong environment's config is worse than no gate: it answers with
  authority.
- **Promote the artifact, not the source.** Two builds from one commit are not
  the same thing. Dependency resolution drifts between them.
- **Secrets are never promoted, copied, or cloned between environments.**
- **Rollback is a promotion.** It goes through the same gates.
- **When the artifact bakes its environment in at build time** (mobile apps,
  compiled binaries, container images with embedded config), promotion cannot
  mean re-pointing a running instance. The release cadence sets the clock, and
  the backend must stay compatible with versions already in the field.
## One rule about other people

**Never probe a shared interactive resource to find out whether it works.**
Signing agents, browser logins, passphrase prompts, a device, a lock. The probe
costs you a timeout and costs the human their prompt. **A failed real command is
already the answer** — do not confirm it a second time. Read stored state instead
of triggering a new interaction.

This one is here rather than in `agent-fleet` because it binds when you are
working alone too. Everything else about working alongside other agents is
`agent-fleet`'s.
