---
name: ui-design
author: kaoru
version: "1.0.0"
description: >-
  How to run UI work with this user: grill a live interface, offer visual
  directions, redesign an app shell, and prove the result. Use for "grill the
  UI", "redesign", "the design is ass", "looks like a sitemap", "feels off",
  "make it touch friendly", landing pages, demo modes, and UI review feedback
  pasted from a browser tool. Loads the user's design rules from personal
  context; defers visual craft to `impeccable`.
---

# UI design

This skill covers the process: what to look at, what to show, and what counts
as done. Taste and rules live elsewhere:

1. **Personal design rules** come from `personal-context`. Load the design route
   (`domains/design/GUIDE.md`) before you change anything. Those rules beat
   project DESIGN.md files and beat any skill, including this one.
2. **Craft** (type, color, spacing, motion, detectors) is `impeccable`'s job.
3. **Slop patterns** (eyebrows, slogan copy, icon-card grids, surface effects,
   dead controls, the pre-ship checklist) are `anti-slop-design`'s catalog.
   Run its checklist on every surface you touch.
4. **Project facts** belong in the repo's `PRODUCT.md` and `DESIGN.md`.

## 1. Grill from the running app, not the source

- Start the app yourself before you critique it. "Nothing was running" is not a
  finding. If the backend fails (DB down, missing creds), fix that first and
  say so. Park the critique until the app runs.
- Bind dev servers to the host (`--host`, `0.0.0.0`) so the user can open them
  from another device. Add that origin to CORS and allowed hosts locally. Keep
  those additions out of git when they name a private host.
- Critique what renders: screenshot desktop and phone, then name each problem
  against a screen and an element. Give the user a way to see it.
- Judge the purpose before the pixels. If the screens do not match what the
  product really is (an "inventory app" built as a POS, a business tool that
  reads as a sitemap), say so first. Restructure before you restyle.
- Strip what the operator does not use: developer content (API reference,
  debug panels), environment labels, and concepts the business does not have
  (bins or cubbies for a shop with one printer).

## 2. Show directions; don't describe them

- When you offer a direction, render it as a viewable mockup or a live route,
  never as prose. Check that each one actually renders before you ask. "I
  can't see any" means the step failed.
- Expect "mix of all of them". Name what you took from each direction.
- When the user says it "feels off" or points at a competitor, study the
  competitor's UI and say what it does that this one does not. Then adapt it;
  never copy it.

## 3. Shell and layout defaults

Use these unless the product brief says otherwise:

- **Operate mode.** The signed-in app opens on the task, never on marketing.
  The public landing page is a separate route.
- **No persistent top bar by default.** The page title and the account control
  share one touch-sized row.
- **Account control:** show the name, with the email below it. Clicking it
  opens a dropdown with Sign out. Never a bare kebab or a monogram.
- **Touch first:** controls at least 44 px, comfortable tap spacing, and a
  phone tab bar or bottom action bar for step flows.
- **Peer actions sit side by side.** Primary tasks go three in a row on desktop,
  and pairs like Import | Export go left | right. Stack them on phones.
- **Lists:** put search above the table. Pick sensible filters by default
  (All, the most-used grouping). Every entry the user creates can be deleted.
  Every detail page has a way back.
- **Sidebars must be logical.** Each item answers "where do I go to do X".
  Re-derive them from the tasks; never keep them out of habit.
- **Add-in-place:** adding from a list opens the full form in a dialog. On
  success, the dialog closes back to the list with the new row visible. Do
  not cut fields to make a "quick add" unless asked.
- **Previews zoom.** Any file, image, or 3D preview can open full-viewport
  with zoom and page controls.
- **Footer** sits at the bottom of the page or of the screen, whichever is
  lower, and carries the legal links (privacy, retention, terms).
- **Copy:** hints go above inputs. Never use format-only placeholders. Never
  ship template tokens (`{quote_by}`, `[HOURS]`), `0` prices, or empty
  states that hide a misconfiguration. Hide the value or say what happens
  instead. When a choice is missing on purpose, say why.
- **Money and computed values:** show the breakdown, not just the total, and
  label each line with its tier.

## 4. Demo mode

- Gate the demo with a runtime env var, off by default. It is read-only on a
  seeded dataset.
- The demo must render the **same components and routes** as the real app. A
  separate mock drifts within a day. Test the demo for parity whenever you
  touch the real screens.

## 5. Handling review feedback

The user often pastes structured feedback from a browser picker: selector,
bounds, computed styles, then a `**Feedback:**` line. The feedback line is the
instruction; the rest only locates the element. Do every item. Ask only when
two items conflict. When the user changes their mind ("erm, let's put the
comprehensive one instead"), take the latest word and keep moving.

Record shell-level decisions in the project's `DESIGN.md` as you make them, from
the built app, so the next agent does not undo them.

## 6. Done means proven on screen

Before you say a UI change is done:

- [ ] Run the detector on **every** screen, demo routes included, for example
      `pnpm dlx impeccable detect <url>` per route. Fix every anti-pattern.
      Fix advisories unless you have a stated reason.
- [ ] Screenshot desktop (1440) and phone (390). Check that nothing scrolls
      sideways and that the layout reflows at 320 px.
- [ ] axe WCAG 2.1 AA has no violations at both sizes.
- [ ] Check the screens against the personal design rules (no gradients, no
      card in a card, no icon-only or letter-only tiles).
- [ ] Run the project's done gate (for example `check && build && test:e2e`).
- [ ] Mobile runtime proof per `engineering-rulebook` → "Responsive UI needs
      runtime proof".

Report what you saw, with the screenshots or detector output. Do not report
what you expect the screen to show.
