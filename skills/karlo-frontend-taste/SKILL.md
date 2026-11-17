---
name: karlo-frontend-taste
author: kaoru
version: "1.0.0"
description: "Use whenever designing, critiquing, or building UI for Karlo: landing pages, marketing sites, app screens, pricing, docs, dashboards, canvases, mockups, and logos. Stops patterns he has rejected (eyebrow labels, clever slogans, toy demos, icon-card grids, static heroes, layout shift, cartoon marks, invented claims) and applies the replacements he approved."
---

# Karlo frontend taste

Karlo wants interfaces that look like working products, not templates or pitch decks. He calls his taste real and prim: brutalist, functional first, no luxury fonts, no novelty palettes. He would rather copy how NetBird, Orca, Coder, and GitHub structure a nav, a pricing page, or a demo than invent a clever layout. Decoration with no information, witty copy, and anything that looks like a toy get rejected. His comments are short. Treat each one as a rule for every page, not a one-off.

This skill is the whole taste profile. Do not depend on another design skill.

Two labels:

- **Stated** — he said it. Do not bend it.
- **Inferred** — read from a rejection or an approved reference. Bend it only when the brief asks.

Quotes live in [evidence](references/evidence.md). Before/after markup lives in [patterns](references/patterns.md). Timing lives in [motion](references/motion.md). Mark sheets live in [logo](references/logo.md).

## Standing behavior

After a critique, apply the fixes. Then report what changed. Do not ask permission first.

A short canvas comment applies to every page with the same pattern. Reply in the thread with what changed.

UI copy and chat stay in English.

When he adds a rule, append the quote and date in evidence, add the rule here, and add a checklist line.

## Hard rules

Each rule is stated. The fix is the whole rule.

1. **No eyebrow or kicker.** Nothing smaller than the heading sits above an `h1`–`h3` in the same block. That includes uppercase overlines, mono numbers ("01 · gate"), accent chips, and announcement pills. Delete it. If those words name a real destination, make them a link beside the content (top-right, module color, ↗). Never a pill, and never above the heading.
2. **No install command or code in the hero or under a CTA.** Put it in a popover on hover and focus of the install button, with a Copy control.
3. **No clever pricing slogans.** The header is "Pricing". The subhead is one factual sentence.
4. **Copy structure from category leaders when unsure.** Match their nav, tiers, compare table, and demo chapters. Do not copy logos, names, or exact art. He has pointed at Orca, NetBird, Coder, and GitHub.
5. **A subhead is one specific sentence.** It says what the thing is, or how it is priced. No stacked conditions. No paired antithesis. No slogan triplets.
6. **No competitor trademark in a headline or tagline.** Name the category. A neutral comparison table may name competitors.
7. **Do not frame the product as one integration.** Lead with the broad category. Integrations are supporting facts.
8. **Demos look like the product.** Real file trees, the real language, tabs, breadcrumbs, a status bar, timestamped logs, a real pull-request page. No toy editor.
9. **Every page header has the primary action.** Same header everywhere: nav, Sign in as a text link, and a solid primary verb. The current page is marked.
10. **Demos are chaptered and animated.** Three chapters is the pattern (for example Code, Run, Review). Tabs, progress, auto-advance, click to jump, pause, and a reduced-motion fallback. Timing is in the motion note.
11. **No equal feature-card grids.** Not a row of 3 or 4 cards with a tinted icon, a blurb, checks, and "Explore". Replace it with a tabbed showcase of the real feature, an alternating text-and-mock row, or a bento cell that holds a real visual.
12. **No static equal-column "how it works".** Steps stack on the left: icon, title, paragraph, progress. The right panel animates the active step.
13. **A real logo row moves.** Infinite marquee, pause on hover, faded edges, reduced motion. Real logos only with permission. Otherwise plain wordmarks. Never invent customers, counts, or testimonials.
14. **The hero is animated.** Headline, then subtext, then CTAs. The product shot tilts into place and floats. One living detail inside the shot. Reduced motion shows the still.
15. **Nothing shifts layout.** Progress tracks always render. Animation panels have a fixed height. Tab panels share one height. A jump on interaction is a bug.
16. **Icons are plain and they render.** Inline stroke icons, about 1.5px, in the accent, with no tinted tile. No emoji. Check the pixels. A conditional that can render nothing is a bug.
17. **Copy states the real proposition.** Take it from the owner or a stated source. Do not infer it from a module name. Unconfirmed lines are `TODO(positioning)`. No fake stats, quotes, logos, or user counts. Unknowns are `[PRICE]`, `[INSTALL URL]`, `[DATE]`.
18. **A mark is a flat silhouette, not a face.** No eyes, no cartoon expression, no sharp V chin. Personality comes from the cut-out. The sheet process is in the logo note.

## Copy

Headlines name the category plus the one differentiator. No puns. No "X, but Y" on a brand. No questions as headlines.

Buttons are a verb plus an object: "Get started", "Install on your server", "Open in browser", "Contact sales".

Pricing is the tier name, who it is for in one line, the price or `[PRICE]`, and what is included. He rejected "Pro" and "Personal" as the middle tier. Use plain names such as Maker, Team, and Business unless the product already has real names.

## Visual defaults

Inferred, except the dark Orca/NetBird reference, which is stated. Break one only when the brief asks.

Never:

- Gradient washes, glowing blobs, mesh backgrounds, glass, or neon outlines.
- A palette chosen to look new, including purple-to-blue "AI" gradients.
- Display serifs, condensed fashion faces, or ultra-thin weights.
- Emoji icons, icon-in-a-circle grids, left-border accent cards, floating 3D, or stock people.
- Stickers that carry no state.
- Fake browser chrome, fake metrics, or fake customer logos.

Prefer:

- Dark graphite first. One accent, for the primary action and focus.
- A status color only with a word beside it: running, building, stopped, failed.
- A masked line-grid behind the hero and the closing CTA. It fades from the top center. This is the one backdrop he asked for. Glows stay off.
- Tables, logs, file trees, and status rows.
- Borders over shadows. Radius about 6–12 px.
- A workhorse sans, plus mono for code.
- Left-aligned sections. The hero and the final CTA may be centered.
- Real controls. Targets about 44 px. Text contrast at least 4.5:1, including muted labels. It works at phone width. In an alternating row, text stays first on a phone.

Light theme only when asked.

## Marketing skeleton

Use this when the page is a marketing site, or when he says "like Orca" or "like NetBird". App screens and docs skip the skeleton and still follow the hard rules.

1. Centered animated hero on the masked grid, with the product window in the hero.
2. Logo marquee, if there is a real integration list.
3. Features as alternating rows, a tabbed showcase, or a mixed-size bento. Each bento cell holds a real snippet, status, or input. A bento is not the banned equal icon-card row.
4. Centered closing CTA on the same grid.

## Interaction

Commands, shortcuts, and long explanations open on hover and focus. They are not static clutter.

Feature tabs and how-it-works steps auto-advance until clicked, then stop. Chaptered demos follow rule 10.

Every visible control does the thing it shows. A dead control reads as fake.

Two offerings, such as Cloud and Self-hosted, use a segmented switch. Each side has its own tiers.

## Pre-ship checklist

Run this on the output before showing it.

- [ ] No text sits above a heading as a label. Scan every `h1`–`h3`.
- [ ] No code, commands, or long technical strings in a hero or under CTAs.
- [ ] Every headline names the category. No competitor mark in our own claims.
- [ ] Every subhead is one specific sentence. No slogan pairs or triplets.
- [ ] The proposition matches a stated source, or the line is `TODO(positioning)`.
- [ ] No invented numbers, logos, or testimonials. Unknowns are `[PLACEHOLDERS]`.
- [ ] No 3–4 equal icon-card rows. No equal-column step strips.
- [ ] No gradients, glows, glass, emoji icons, icon tiles, or left-border cards.
- [ ] Accent is only for primary actions and focus. A status color has a word.
- [ ] Same header on every page, with Sign in and a primary CTA.
- [ ] Hero motion, marquees, and demos have a reduced-motion fallback.
- [ ] Clicking or advancing a control does not move the content below it.
- [ ] Icons render. Plain strokes. No tiles.
- [ ] Demos look like the product, and every visible control works.
- [ ] Contrast at least 4.5:1, about 44 px targets, real controls, usable at phone width.
- [ ] A logo has no eyes, no cartoon face, and no sharp chin. The silhouette reads correctly.
