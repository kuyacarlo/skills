# Profiles

[SKILL.md](../SKILL.md) owns the hard rules. This file picks the palette, shape, and motion when a project has no design file. A project `DESIGN.md`, handoff, or token file always wins over this file.

Ask which profile fits only when the surface is new and nothing in the repo says.

## Product

Use for a developer or infrastructure product site, or when he says "like Orca" or "like NetBird". Stated reference. Details inferred.

- Dark graphite first. Light only when asked.
- One warm accent for the primary action and focus.
- A masked line-grid behind the hero and the closing CTA. It fades from the top center. No glows.
- Radius about 6–12 px. Borders over shadows.
- Header: nav, `Sign in` as a text link, and a solid primary verb.
- Motion on. Rules 10, 12, 13, and 14 apply. Tokens are in [motion](motion.md).
- Voice: minimal, sleek, corporate.

Skeleton:

1. Centered animated hero on the masked grid, with the product window in the hero.
2. Logo marquee, if there is a real integration list.
3. Features as alternating rows, a tabbed showcase, or a mixed-size bento with real visuals.
4. Centered closing CTA on the same grid.

## Brutalist personal

Use for a personal site, portfolio, resume, or notes. Approved in his own brand handoff.

- Black on white. One honest system. Every region is a cell with a hard rule.
- No gradients, shadows, blur, rounded corners, pills, or decorative icons.
- Emphasis is inversion: a black block with white text. It is the only highlight.
- Link blue marks inline links only. A primary button may use it when he asks.
- Status is text, never color.
- Motion off. No transitions. State changes are instant.
- A tuned dark theme when asked. Not a hard inversion.
- Voice: first person, friendly, plain. One joke at most.
- The concept is shown through structure, never spelled out in copy.
- Dense. Real content fills the page. The resume is one packed A4 page set.

## Catalog or app

Use for a directory, a tool, a dashboard, or an app screen. Read from his approved catalog design.

- A light ground with one ink color for text, header, and primary buttons.
- One loud color for exactly one main action per screen, and for one approved tag. Nothing else.
- One extra color only for a single overdue or warning state.
- One type family in a few widths. Numbers before adjectives.
- Exact vendor figures. Unknowns shown as unknown, with an invite to check.
- Lead with the catch.
- Motion only where it shows state.
- Every strip or row that holds a link is at least 44 px tall.

## Choosing

| Signal | Profile |
| --- | --- |
| Product with pricing, install, or sign in | Product |
| A person's name is the brand | Brutalist personal |
| Lists, filters, records, or labels are the point | Catalog or app |
| The repo has a design file | That file. No profile |
