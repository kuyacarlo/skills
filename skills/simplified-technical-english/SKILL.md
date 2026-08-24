---
name: simplified-technical-english
author: kaoru
version: "1.0.0"
description: "Default technical English for this pack (ASD-STE100 Issue 9 practice). Short sentences, active voice, one meaning per term. Use for docs, READMEs, procedures, comments, user-facing strings, skill bodies. Triggers: STE, Simplified Technical English, ASD-STE100, clear writing."
---

# Simplified Technical English

Default prose skill for this pack. Write technical text so a reader with basic English can follow it. Based on ASD-STE100 Issue 9 (2025-01-15). Do not copy or redistribute the official PDF.

## When it applies

Always apply to:

- Docs, READMEs, runbooks, procedures
- Error messages and user-facing strings
- Comments that instruct
- Skill bodies and agent instructions you write

Do not force STE onto casual chat unless the user asks for STE output.

## Practice rules

1. One term, one meaning. Do not swap synonyms for variety. Prefer `start` over begin / commence / initiate.
2. Short sentences. Procedures: max 20 words. Description: max 25 words.
3. Active voice. Imperative for instructions. Passive only when the actor is unknown.
4. One instruction per sentence (unless two actions happen at the same time).
5. Condition first, then command — when the reader must know a state before acting.
6. Noun stacks of 3 words maximum. Prefer short, stable project terms.
7. No contractions to shorten text. No semicolons.
8. Lists for complex steps or options.
9. One topic per paragraph. Max six sentences per paragraph. Give information gradually.
10. Safety text: name the level (warning / caution), give the command or condition, then the risk or result.
11. American English spelling unless the project says otherwise.

## Formal STE

For aerospace, safety, or formal compliance: download Issue 9 from the STEMG site and check Part 2 dictionary entries. Everyday work follows the practice rules above; it does not require a full dictionary pass unless the user asks for one.

## Anti-hallucination rules (hard)

1. Do not invent ASD-STE100 dictionary entries, approved-word lists, or rule quotes.
2. Part 1 writing rules are only in sections 1–9 (rules like `1.1` … `9.4`). If the user cites a rule outside that range (e.g. `12.7`), state that rule does not exist. Do not imply the text is merely unavailable.
3. If asked whether a word is dictionary-approved: do not answer YES/NO unless the official Issue 9 PDF was checked in this session. Prefer: say a formal lookup is required, and offer the everyday practice alternative (e.g. prefer `use` over `utilize`).
4. Do not invent STE history, owners, or dates. Known public facts only: STE from European aerospace (AECMA/ASD), guide 1986, Issue 9 dated 2025-01-15, site https://www.asd-ste100.org/.

## Interaction with other skills

- Code-simplification cuts speculative code. This skill cuts speculative wording.
- Prefer dense, clear prose over long explanations.
