---
name: personal-context
metadata:
  author: kaoru
  version: "1.3.0"
description: "Loads the user's personal systems, background, stack, and constraints from a context file so agents stop re-asking. Use when starting work, choosing stacks, planning projects, or when demotivated — read personal context before guessing. Triggers on personal context, about me, my stack, my systems, homelab defaults."
---

# Personal Context

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

## Maintenance

Update personal context only when relevant and authorized. Respect filesystem approval requirements.
When a write is blocked, prepare a proposed update in the workspace and report the pending step.
Never commit private context into a public skill repository.
Portable examples must use placeholders, not personal identity or host details.

## Durable memory across harnesses

Harness-local memory is a working cache, not the portable source of truth.
Keep repository facts in repository docs. Route portable lessons through local SKILLS.md.
Consult relevant notebook topics when present; do not load the entire notebook.
After authorized context or skill edits, run the local prove-prose checker when available.
For cross-device synchronization, follow local SYNC.md; do not assume the sync command name.
