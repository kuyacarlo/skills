---
name: karlo-frontend-taste
author: kaoru
version: "2.0.0"
description: "Use whenever designing, critiquing, or building UI for Karlo: landing pages, marketing sites, personal sites, app screens, catalogs, pricing, docs, dashboards, canvases, mockups, and logos. Stops patterns he has rejected (eyebrow labels, explained design, stray link color, sparse layouts, empty controls, clever slogans, toy demos, icon-card grids, layout shift, harsh dark mode, cartoon marks, invented claims) and applies the replacements he approved."
---

# Karlo frontend taste

Karlo wants interfaces that look like working products, not templates or pitch decks. He calls his taste real and prim: brutalist, functional first, no luxury fonts, no novelty palettes. He copies structure from category leaders before he invents layouts. Decoration with no information, witty copy, and explained design get rejected. His comments are short. Treat each one as a rule for every page, not a one-off.

This skill is the whole taste profile. Do not depend on another design skill.

Two labels:

- **Stated**: he said it. Do not bend it.
- **Inferred**: read from a rejection or an approved reference. Bend it only when the brief asks.

Quotes live in [evidence](references/evidence.md). Before/after markup lives in [patterns](references/patterns.md). Surface profiles live in [profiles](references/profiles.md). Timing lives in [motion](references/motion.md). Mark sheets live in [logo](references/logo.md).

## Precedence

1. His comment in this session.
2. The project's own `DESIGN.md`, handoff, or token file. Its colors, fonts, radius, and motion win.
3. The hard rules below. They hold on every surface.
4. The surface profile in [profiles](references/profiles.md). Use it only when the project has no design file.

Each project has its own visual system. Never carry one project's palette or motion into another.

## Standing behavior

After a critique, apply the fixes. Then report what changed. Do not ask permission first.

A short comment applies to every page with the same pattern. "Remove this across all pages" is the default reading.

Fix the viewport he commented on. Do not change the other viewport as a side effect.

Read a comment for intent, not for its literal words. "Download PDF that saves a Harvard-style PDF" means the label stays "Download PDF".

UI copy and chat stay in English.

When he adds a rule, append the quote and date in evidence, add the rule here, and add a checklist line.

## Hard rules

Each rule is stated unless marked. The fix is the whole rule. Rules 10, 12, 13, and 14 apply to the product profile only.

1. **No eyebrow or kicker.** Nothing smaller than the heading sits above an `h1`–`h3` in the same block. That includes uppercase overlines, mono numbers ("01 · gate"), page-name labels, accent chips, availability badges, and announcement pills. Delete it. If those words name a real destination, make them a link beside the content. Never a pill, and never above the heading.
2. **No install command or code in the hero or under a CTA.** Put it in a popover on hover and focus of the install button, with a Copy control.
3. **No clever pricing slogans.** The header is "Pricing". The subhead is one factual sentence.
4. **Copy structure from category leaders when unsure.** Match their nav, tiers, compare table, and demo chapters. Do not copy logos, names, or exact art. He has pointed at Orca, NetBird, Coder, and GitHub. When he says "be different", copy no layout. Design from the product's real mechanism.
5. **A subhead is one specific sentence.** It says what the thing is, or how it is priced. No stacked conditions. No paired antithesis. No slogan triplets.
6. **No competitor trademark in a headline or tagline.** Name the category. A neutral comparison table may name competitors.
7. **Do not frame the product as one integration.** Lead with the broad category. Integrations are supporting facts.
8. **Demos look like the product.** Real file trees, the real language, tabs, breadcrumbs, a status bar, timestamped logs, a real pull-request page. No toy editor.
9. **Every page header has the primary action.** Same header everywhere: nav, then the primary action at the right end. The current page is marked.
10. **Demos are chaptered and animated.** Product profile. Three chapters, for example Code, Run, Review. Tabs, progress, auto-advance, click to jump, pause, and a reduced-motion fallback.
11. **No equal feature-card grids.** Not a row of 3 or 4 cards with a tinted icon, a blurb, and "Explore". Use a tabbed showcase, an alternating text-and-mock row, or a bento cell that holds a real visual.
12. **No static equal-column "how it works".** Product profile. Steps stack on the left. The right panel animates the active step.
13. **A real logo row moves.** Product profile. Infinite marquee, pause on hover, faded edges. Real logos only with permission. Never invent customers.
14. **The hero proves the mechanism.** Show the real artifact doing its job. For a document product, that is the raw page, selectable, with overlay boxes and short essence labels. Product profile: it is also animated, with a reduced-motion still.
15. **Nothing shifts layout.** Progress tracks always render. Animation panels and tab panels have one fixed height. A jump on interaction is a bug.
16. **Icons are plain and they render.** Inline stroke icons, about 1.5px, with no tinted tile. No emoji. A conditional that can render nothing is a bug.
17. **Copy states the real proposition.** Take it from the owner or a stated source. Unconfirmed lines are `TODO(positioning)`. No fake stats, quotes, logos, or counts. Unknowns are `[PRICE]`, `[URL]`, `[DATE]`.
18. **A mark is a flat silhouette, not a face.** No eyes, no cartoon expression, no sharp V chin. The sheet process is in the logo note.
19. **Never explain the design to the user.** No line that narrates the layout, the system, or why to trust it. No legends such as "symptom → cause → fix". No "so you don't have to take my word for it". Assume the reader is smart.
20. **One color, one meaning.** The link color goes on inline text links only. Headings, paragraphs, list rows, nav, table-of-contents links, and breadcrumbs stay ink, even when they are links. Underline only what is a link. Card and row links underline on hover.
21. **Emphasis survives every breakpoint.** If desktop marks a row as important, the phone marks it too.
22. **No sparse pages.** Fix a sparse page with more real content or a tighter grid. Fix a cramped page with padding from the spacing scale. Do not fill space with empty margin.
23. **Empty means remove or say so.** A filter, row, or control with nothing under it is removed. An empty page says it is empty. No "Show more" for one item.
24. **The phone layout is the desktop layout transposed.** Same pieces, same order, same emphasis. Do not invent a new phone structure. Do not split one list into side-by-side columns to fill width.
25. **The name is the link.** A project or item name links to its main destination: live if it exists, else source. Extra links go at the end of the row. A line that repeats a visible button is removed.
26. **Numbers fit their cell.** Abbreviate large figures, for example `2.71M`. No thousands commas in stat cells. Big stat numerals are not text-selectable.
27. **Dark mode is tuned, not inverted.** Filled blocks stay dark. Contrast stays soft. The theme toggle sits just before the primary action in the header.
28. **Copy controls copy on the first click.** Only the clicked control changes to "Copied". Other copy controls keep their label.
29. **Public pages have a real link preview.** Open Graph and social-card tags, plus a designed preview image.
30. **Code has syntax color. Prose has no highlight.** Code blocks use a quiet syntax theme. Never put a background highlight on body words.
31. **Voice fits the surface.** Product sites are minimal, sleek, and corporate. Personal sites are friendly, first person, and plain. Stiff lines like "Let's talk." are rejected on a personal site.
32. **Every filter filters.** A filter, sort, or tab that does nothing is a bug, not a placeholder. Small collections get no filter chrome at all.

## Copy

Headlines name the category plus the one differentiator. No puns. No "X, but Y" on a brand. No questions as headlines.

Buttons are a verb plus an object: "Get started", "Download PDF", "Open in browser". The label says what the user gets, not the file format or the implementation.

Descriptions are short. One line per item in a list.

Pricing is the tier name, who it is for in one line, the price or `[PRICE]`, and what is included. He rejected "Pro" and "Personal" as the middle tier. Use plain names such as Maker, Team, and Business unless the product already has real names.

## Visual defaults

These hold on every surface unless the project's design file says otherwise.

Never:

- Gradient washes, glowing blobs, mesh backgrounds, glass, or neon outlines.
- A palette chosen to look new, including purple-to-blue "AI" gradients.
- Display serifs, condensed fashion faces, or ultra-thin weights.
- Emoji icons, icon-in-a-circle grids, left-border accent cards, floating 3D, or stock people.
- Stickers or pills that carry no state.
- Fake browser chrome, fake metrics, or fake customer logos.
- Browser-default link blue on navigation or headings.

Prefer:

- One accent with one job. It marks the primary action, a link, or focus. Never decoration.
- Status as a word. A status color needs a word beside it.
- Tables, logs, file trees, and status rows.
- Borders over shadows.
- A workhorse sans, plus mono for code. Self-host web fonts.
- Left-aligned sections.
- Real controls. Targets about 44 px. Text contrast at least 4.5:1, including muted labels. No horizontal scroll at phone width.

Pick the palette, radius, and motion from the profile in [profiles](references/profiles.md).

## Interaction

Commands, shortcuts, and long explanations open on hover and focus. They are not static clutter.

Feature tabs and how-it-works steps auto-advance until clicked, then stop. Chaptered demos follow rule 10.

Every visible control does the thing it shows. A dead control reads as fake.

Clicking an item opens that item. A row that says "read note" opens the note, not a summary.

Two offerings, such as Cloud and Self-hosted, use a segmented switch. Each side has its own tiers.

## Pre-ship checklist

Run this on the output before showing it. Check desktop and phone width.

- [ ] Project design file read. Its tokens are used. No palette from another project.
- [ ] No text sits above a heading as a label. Scan every `h1`–`h3`.
- [ ] No line explains the design, the layout, or why to trust it.
- [ ] No code, commands, or long technical strings in a hero or under CTAs.
- [ ] Every headline names the category. No competitor mark in our own claims.
- [ ] Every subhead is one specific sentence. No slogan pairs or triplets.
- [ ] The proposition matches a stated source, or the line is `TODO(positioning)`.
- [ ] No invented numbers, logos, or testimonials. Unknowns are `[PLACEHOLDERS]`.
- [ ] No 3–4 equal icon-card rows. No equal-column step strips.
- [ ] No gradients, glows, glass, emoji icons, icon tiles, or left-border cards.
- [ ] Link color only on inline links. Nav, headings, and rows stay ink. Underline only on links.
- [ ] Emphasis on desktop also shows on phone.
- [ ] Phone layout is the desktop transposed. Desktop unchanged by a phone fix.
- [ ] Not sparse and not cramped. Spacing comes from the scale.
- [ ] No empty filter, row, or control. Empty pages say they are empty.
- [ ] Names link to the main destination. No line repeats a visible button.
- [ ] Stat numbers fit. Abbreviated, no commas.
- [ ] Same header on every page, with the primary action. Theme toggle just before it.
- [ ] Dark mode is tuned, not a hard inversion.
- [ ] Copy controls copy on first click. Only the clicked one says "Copied".
- [ ] Every filter, tab, and link works.
- [ ] Code blocks have syntax color. No highlight on prose.
- [ ] Open Graph tags and a preview image exist on public pages.
- [ ] Motion, marquees, and demos have a reduced-motion fallback. Brutalist profile has no motion.
- [ ] Clicking or advancing a control does not move the content below it.
- [ ] Timeline and connector lines start and end at their first and last dot.
- [ ] Icons render. Plain strokes. No tiles.
- [ ] Contrast at least 4.5:1, about 44 px targets, usable at phone width.
- [ ] A logo has no eyes, no cartoon face, and no sharp chin.
