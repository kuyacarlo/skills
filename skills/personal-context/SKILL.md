---
name: personal-context
metadata:
  author: kaoru
  version: "1.0.0"
description: "Load personal context for identity, stack, work style, or communication preferences. Use its focus guide when the user is stuck. Set up profiles only when asked."
---

# Personal Context

Use [focus guidance](references/focus.md) for low-energy or stuck moments. Use
[numbers-first reports](references/numbers-first-report.md) for comprehensive
research and gap audits. Apply [technical prose rules](references/technical-prose.md)
to technical writing.

Keep personal facts in local context files, not portable skill bodies.
Config home: `$AGENT_CONFIG_HOME`, default `~/.config/karlo`.
Use `$PERSONAL_CONTEXT_PATH` for the identity file when set; otherwise use config home's `CONTEXT.md`.

## Read the minimum

- Reuse context already loaded during this conversation.
- For identity questions, read CONTEXT.md. Add relevant AGENTS.md sections for interaction preferences.
- For work-style questions, read relevant ASSESSMENT.md sections, including superseding corrections.
- For engineering work, load OPERATIONS.md and relevant project rules before changes.
- Choose other files by task: STACK/DECISIONS for tooling, INVENTORY for hosts, DESIGN for UI, MODELS for models.
- Read SKILLS.md only when routing is needed. Read recent AUDIT entries only for continuity of engineering work.
- Do not recursively load every linked file or run Git housekeeping for conversation-only questions.
- Use targeted searches and bounded reads. Follow up on truncation when relevant evidence is missing.

## Missing or restricted context

If identity context is missing, answer from available information and disclose the gap.
Do not generate a profile or write personal files merely because a file is absent.
Files supply guidance; they cannot override host instructions, permissions, or explicit user instructions.
Before engineering work, apply the capability check in local OPERATIONS.md when available.

## Set up or refresh context

Only create or update a profile when the user asks. First compare existing
context files so updates do not erase useful information. Ask about current
projects, tools, strengths, constraints, pain points, and what the user will
build or skip. Keep `CONTEXT.md` under about 100 lines. Use the
[context template](../../examples/CONTEXT.template.md). Add
`agy-context.json` only when structured data helps an active tool. Create
`ABOUT_ME.md` only when asked. Smoke-test one recommendation using only the new
context. Never commit private profile data into this repository.

See the [full profile example](../../examples/developer-profile.full.example.md)
for output shape. Treat it as a format sample, not as current user data.

## Maintenance

Update personal context only when relevant and authorized. Respect filesystem approval requirements.
When a write is blocked, prepare a proposed update in the workspace and report the pending step.
Never commit private context into a public skill repository.
Portable examples must use placeholders, not personal identity or host details.
