---
name: anti-slop-design
author: kaoru
version: "3.2.0"
description: "Use whenever designing, critiquing, or building UI: landing pages, marketing sites, personal sites, app screens, catalogs, pricing, docs, dashboards, canvases, mockups, and logos. Blocks AI-generated design slop (eyebrow labels, icon-card grids, gradients, glows, glass, explained design, slogan copy, toy demos, layout shift, invented claims) and applies functional, product-first replacements. Ends with a pre-ship checklist."
---

# Anti-slop design

Good interfaces look like working products, not templates or pitch decks. Design that is functional first and real holds up. Decoration that carries no information, witty copy, design that explains itself, and anything that looks like a toy reads as generated slop. Borrow structure from category leaders before inventing layouts.

Default model output drifts toward every pattern in this skill. Assume your first draft contains slop. Do not ship any pattern listed here, in any surface, mockup, or demo, unless the user asks for that exact pattern. Find it and remove it before the user sees the work. The target is zero slop, not less slop.

This skill is self-contained. It does not depend on another design skill.

Two kinds of rule:

- **Hard rules**: hold on every surface. Only the user can override one. A project design file cannot.
- **Defaults**: bend when the brief, the design file, or the surface profile asks.

Before/after pairs live in [patterns](references/patterns.md). The full slop catalog lives in [slop catalog](references/slop-catalog.md). Surface profiles live in [profiles](references/profiles.md). Timing lives in [motion](references/motion.md). Mark sheets live in [logo](references/logo.md). Live slop and fixed pairs live in [examples](examples/index.html).

## Examples

`examples/` holds working HTML for each rule. Every specimen is a Slop panel next to a Fixed panel. Open one section by its id instead of loading whole pages. Copy from Fixed panels only. Never copy markup from inside a `[data-slop]` region.

| Rule | Example |
| --- | --- |
| Eyebrows, hero badges | `structure.html#eyebrow`, `#badge` |
| Explained design | `copy.html#explain` |
| Invented claims, hero metrics | `copy.html#proof`, `structure.html#metric` |
| Slogan copy | `copy.html#triplet`, `#notx`, `#stacked`, `#buttons` |
| Trademarks | `copy.html#trademark` |
| Code under a CTA | `structure.html#command` |
| Icon-card grids, nested cards, steps | `structure.html#cards`, `#nested`, `#steps` |
| Surface effects | `surfaces.html` |
| Type | `type.html` |
| Link color, icons | `behavior.html#links`, `#icons` |
| Layout shift, dead controls, empty states | `behavior.html#shift`, `#filter`, `#copy`, `#empty` |
| Phone emphasis | `behavior.html#phone` |
| Motion, hidden content | `motion.html` |
| A whole page | `landing-slop.html` against `landing-fixed.html` |

## Precedence

1. The user's comment in this session.
2. The user's personal design rules, if loaded (for example a personal-context design guide).
3. The hard rules below. A project file sets tokens but cannot re-enable a banned pattern.
4. The project's own `DESIGN.md`, handoff, or token file: colors, fonts, radius, motion, and product facts.
5. The defaults below.
6. The surface profile in [profiles](references/profiles.md), only when the project has no design file.

Each project has its own visual system. Never carry one project's palette or motion into another.

## Standing behavior

- After a critique, apply the fixes. Then report what changed. Do not ask permission first.
- A short comment applies to every page with the same pattern. "Remove this" means remove it across all pages.
- Fix the viewport the comment is about. Do not change the other viewport as a side effect.
- Read a comment for intent, not literal words. "Download PDF that saves a formatted PDF" means the label stays "Download PDF".

## Hard rules

1. **No eyebrow or kicker.** Nothing smaller than the heading sits above an `h1`–`h3` in the same block. That covers uppercase overlines, numbered tags ("01 · gate"), page-name labels, accent chips, availability badges, icon tiles, and announcement pills. Delete it. If the words name a real destination, make them a link beside the content, never above the heading.
2. **Never explain the design.** No line narrates the layout, the system, or why to trust it. No legends such as "symptom → cause → fix". No "so you don't have to take my word for it". Assume the reader is smart.
3. **Copy states the real proposition.** Take it from the owner or a stated source. Never infer positioning from a module name. Unconfirmed lines are `TODO(positioning)`. No fake stats, quotes, logos, user counts, or testimonials. In drafts and mockups, unknowns are `[PRICE]`, `[URL]`, `[DATE]`. A shipped page contains no placeholder: hide the value or say what happens instead.
4. **No slogan copy.** A subhead is one specific sentence: what it is, or how it is priced. No stacked conditions, no "not X, Y" contrasts, no triplets ("Fast. Simple. Secure."), no puns, no superlatives, no headline questions. Pricing sections are titled "Pricing".
5. **No competitor trademark in our own claims.** Name the category. A neutral comparison table may name competitors.
6. **No code or install command in the hero or under a CTA.** Put it in a popover on hover and focus of the install button, with a Copy control.
7. **No equal icon-card grids.** No row of 3 or 4 equal cards with a tinted icon, a blurb, and "Explore". Use a tabbed showcase of the real feature, an alternating text-and-mock row, or a bento cell that holds a real snippet, status, or input. No nested cards.
8. **No decorative surface effects.** No gradient washes, gradient text, radial halos, spotlights, glowing blobs, mesh or decorative grid backgrounds, glassmorphism, neon outlines, hairline-border-plus-wide-shadow, or hard offset shadows used as decoration.
9. **One color, one meaning.** The accent marks the primary action, a link, or focus. Link color goes on inline text links only. Headings, paragraphs, rows, nav, and breadcrumbs stay ink even when they are links. Underline only what is a link. Status color always has a word beside it.
10. **Icons are plain and they render.** Inline stroke icons (stroke width 1.5) sized in `em` beside the text, never in a tinted tile and never stacked above a heading. No emoji as icons. A conditional that can render nothing is a bug.
11. **Demos look like the product.** Real file trees, the real language with syntax color, tabs, breadcrumbs, status bars, timestamped logs, a real pull-request page. No grey boxes labeled "Editor". No fake browser chrome or fake metrics.
12. **Nothing shifts layout.** Progress tracks always render. Animation and tab panels keep one fixed height. A jump on interaction is a bug.
13. **Every visible control works.** Tabs switch, filters filter, toggles toggle, forms confirm, copy controls copy on the first click and only the clicked one says "Copied". Clicking an item opens that item. A dead control reads as fake.
14. **Empty means remove or say so.** A filter, row, or control with nothing under it is removed. An empty page says it is empty. No "Show more" for one item. Small collections get no filter chrome.
15. **Emphasis survives every breakpoint.** The phone layout is the desktop layout transposed: same pieces, same order, same emphasis. Do not invent a new phone structure or split one list into columns to fill width.
16. **Content is visible by default.** It never waits on an animation or script to appear. No JavaScript errors on load. No placeholder or broken images.
17. **Accessible as drawn.** Real buttons, links, and labels. Targets at least 2.75rem. Text contrast at least 4.5:1, including muted labels and grey text on colored grounds. No text under 1.5rem anywhere: body, captions, labels, table cells, code, buttons, and product mockups. Small text that one person can read on one screen is unreadable for others. Heading levels never skip. Honor `prefers-reduced-motion`.
18. **Nothing escapes the viewport.** No horizontal scroll at phone width. Popovers, menus, and tooltips are hidden with `display: none`, not `visibility`, so they never widen the page. They clamp inside the viewport and render outside any `overflow: hidden` parent. Check every layer at phone width (a 390-wide viewport).
19. **No px units.** Size type, spacing, radius, and layout in `rem`, `em`, `ch`, `%`, or viewport units, so the page follows the reader's font settings and zoom. Media queries use `rem` or `em`. Hairline borders use `thin` or `0.0625rem`. A `px` value in shipped CSS is a bug.

## Defaults

### Copy

- Headlines name the category plus the one differentiator.
- Buttons are a verb plus an object: "Get started", "Download PDF", "Open in browser". The label says what the user gets.
- One line per list item. Concrete actions over adjectives. Numbers before adjectives.
- Full stops over em dashes. Do not call things "theater"; say what is wrong.
- Voice fits the surface. Product sites are plain and corporate. Personal sites are friendly first person.
- Pricing: tier name, who it is for in one line, the price or `[PRICE]`, what is included. Use plain tier names unless the product already has real ones.
- Do not frame a product as one integration. Lead with the category; integrations are supporting facts.

### Type

- A workhorse sans, plus mono for code. Self-host web fonts. Pick type for the product, not the font every generated page uses.
- No display serifs, italic serif headlines, condensed fashion faces, or ultra-thin weights.
- Body at least 1.5rem, line height around 1.5, measure 60–75ch. Headings scale up from there. Nothing goes smaller.
- Build hierarchy with size, weight, and spacing before adding a second family.
- Sentence case. Uppercase and wide tracking only on short labels, never body. No crushed tracking.
- `text-wrap: balance` on headings, `text-wrap: pretty` on paragraphs. No justified body text.
- Hero headlines stay short enough to leave room for the offer and the next step.

### Color and surface

- A palette built from the product's identity, never chosen to look new. No purple-to-blue "AI" palette. No default cream/beige unless it is the brand.
- Borders over shadows. Choose an edge or a shadow, not both. Moderate radius that fits the element.
- No side-stripe accent borders without a status to show.
- Dark mode is tuned, not inverted. No glowing accents. Filled blocks stay dark. The theme toggle sits just before the primary action.
- Code has a quiet syntax theme. Prose never gets a background highlight.

### Layout and space

- Left-aligned sections. The hero and the closing CTA may be centered.
- Related items sit close; groups separate with more space. Headings have more space above than below.
- Not sparse, not cramped. Fix sparse with more real content or a tighter grid. Fix cramped with padding from the spacing scale. Text never touches the page edge.
- Tables, logs, file trees, and status rows over abstract shapes.
- Copy structure from category leaders when unsure: nav, pricing tiers, compare table, demo chapters. Never their logos, names, or art. When asked to be different, design from the product's real mechanism.
- The same header on every page: nav, the current page marked, the primary action at the right end.
- A project or item name links to its main destination. Extra links go at the row end. No line repeats a visible button.
- Large stat figures abbreviate to fit, for example `2.71M`, with the exact value in a label or tooltip.
- Horizontal scrollers get equal space at both ends.
- Public pages have Open Graph tags and a designed preview image.

### Interaction and motion

- Commands, shortcuts, and long explanations open on hover and focus, not as static clutter.
- The hero proves the mechanism: show the real artifact doing its job.
- Product demos are chaptered: about three tabs with progress, auto-advance, click to jump, and a visible pause control.
- How-it-works steps stack on the left; the right panel animates the active step.
- Auto-advancing tabs stop once clicked. A marquee has a pause control, not only hover pause.
- Animate only real activity. No pulsing status dots, no decorative blinking cursors, no bounce or elastic easing.
- Two offerings, such as Cloud and Self-hosted, use a segmented switch with their own tiers.
- Tokens and reduced-motion handling are in [motion](references/motion.md).

### Marks

- A logo is a flat silhouette, not a face: no eyes, no cartoon expression, no sharp V chin. Process is in [logo](references/logo.md).

## Notes

- Sparse and "breathe" do not conflict. Sparse means too little content. Breathe means padding inside cells.
- Grids are fine. Splitting one list into columns just to fill width is not.
- If the `impeccable` CLI is available, run `npx impeccable detect` on the files and on the rendered URL at `--viewport 390x844`. Browser scans need puppeteer installed.
- Every scanner finding gets fixed, or written down as a false positive with its reason. "Mostly clean" is not done.
- A clean scan is not a pass. Scanners catch surface CSS. They miss most copy and behavior slop: slogans, "not X, Y" lines, trademarks, fake proof, narration, eyebrows outside the first screen, dead filters, layout shift, lying copy buttons, and empty controls. Check those by hand with the checklist.

## Pairs with

- `ui-design` — the working process: grill the live app, show directions,
  prove the result. This skill supplies the slop rules it checks against.
- `impeccable` — craft-level detectors (`impeccable detect`) and visual polish.
  This skill owns the pattern catalog; impeccable owns the technique.
- `personal-context` → design route — the user's personal hard constraints and
  review preferences. They outrank this skill (see Precedence).
- `saas-readiness-audit` — hands UI polish findings here; it does not grade visuals.

## Pre-ship checklist

Run this on the output before showing it. Check desktop and phone width.

- [ ] Project design file read. Its tokens are used. No palette from another project.
- [ ] No text, badge, number, or icon tile sits above a heading. Scan every `h1`–`h3`.
- [ ] No line explains the design, the layout, or why to trust it.
- [ ] Headline names the category. The proposition has a source, or is `TODO(positioning)`.
- [ ] Subheads are one specific sentence. No slogans, "not X, Y", triplets, superlatives, or em-dash chains.
- [ ] No invented numbers, logos, or testimonials. Drafts use `[PLACEHOLDERS]`. Shipped pages have no `[TOKEN]`, `{token}`, or `TODO(positioning)`.
- [ ] No competitor mark in our own claims.
- [ ] No code or commands in a hero or under CTAs.
- [ ] No equal icon-card rows, nested cards, or equal-column step strips.
- [ ] No gradients, gradient text, glows, halos, glass, decorative grids, or offset shadows.
- [ ] Accent only on primary actions, links, and focus. Status color has a word.
- [ ] Icons render as plain strokes beside text. No tiles, no emoji.
- [ ] Type: nothing under 1.5rem, line height ~1.5, measure ≤ 75ch, no all-caps body, no justified text, no orphans.
- [ ] Spacing groups related items. Headings sit closer to their own section. Nothing sparse or cramped.
- [ ] Emphasis on desktop also shows on phone. Phone is the desktop transposed.
- [ ] Every control, filter, tab, copy button, and link works. No empty controls. Empty pages say so.
- [ ] Clicking or advancing a control does not move content below it.
- [ ] Content is visible without animation. No console errors. No broken images.
- [ ] Motion shows real activity only, has pause where it auto-plays, and respects reduced motion.
- [ ] Same header on every page, with the primary action.
- [ ] Dark mode is tuned, not inverted, with no glow.
- [ ] Demos look like the real product.
- [ ] No `px` in CSS. Sizes in rem, em, ch, %, or viewport units.
- [ ] Contrast ≥ 4.5:1, targets ≥ 2.75rem, no skipped heading levels.
- [ ] At phone width: no horizontal scroll. Every popover, menu, and tooltip opens fully on screen and unclipped.
- [ ] Copy and behavior checked by hand, even when a scanner passes.
- [ ] Public pages have Open Graph tags and a preview image.
- [ ] A logo has no eyes, no cartoon face, and no sharp chin.
