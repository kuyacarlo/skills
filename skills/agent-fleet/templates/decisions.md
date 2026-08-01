# Decisions

Append-only. **Newest first.** Rulings that settle contested paths, issues or
ordering. Never edit an old entry — supersede it with a new one and say which.

Every agent reads this from the top before acting. It overrides claim files.

Format:

```markdown
## <ISO date> — <short title>

**Question:** <what was contested, in one line>
**Ruling:** <who gets it, who waits, what happens>
**Reason:** <why — this is the part that stops it being reopened>
**Affects:** <agents, branches, issues>
```

Use a `#` heading instead of `##`, plus a leading emoji, for entries every agent
must see immediately — a hard stop, a reversed rule, a machine-wide fault.

---

## <date> — EXAMPLE: path X goes to agent A

**Question:** Both A and B claimed `src/thing/**`.
**Ruling:** A takes it. B's claim now excludes it. B may proceed on everything
else it holds.
**Reason:** A had already pushed 6 commits touching those files; B had a handoff
only. Discarding the smaller duplicate cost less. The original claim was written
too wide.
**Affects:** A (#101), B (#102).

---

## Entries worth writing that agents often skip

- **A correction to your own earlier ruling.** Supersede it in writing, state
  what you got wrong and why. Silent edits destroy the record's value.
- **A machine fault everyone will hit** — with the exact error text, so the next
  agent recognises it instead of debugging it.
- **A frozen area** — work nobody may start, and why. Without a reason it gets
  picked up by the next idle agent.
- **A ruling that binds you.** The rules an agent writes for others are the ones
  it will find reasons to exempt itself from.
