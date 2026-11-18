# Profiles

[SKILL.md](../SKILL.md) owns the rules. This file picks the palette, shape, and motion when a project has no design file. A project `DESIGN.md`, handoff, or token file always wins over this file.

Ask which profile fits only when the surface is new and nothing in the repo says.

## Product

Use for a developer or infrastructure product site. Reference sites in that category include Orca, NetBird, Coder, and GitHub.

- Dark graphite first. Light only when asked.
- One warm accent for the primary action and focus.
- A plain ground. No grid backdrop, glow, or halo unless the design file asks.
- Radius about 6–12 px. Borders over shadows.
- Header: nav, `Sign in` as a text link, and a solid primary verb.
- Motion on, for real activity only. Tokens are in [motion](motion.md).
- Voice: minimal, sleek, corporate.

Skeleton:

1. Hero with the product window doing its real job.
2. An integration marquee with a pause control, only if there is a real list.
3. Features as alternating rows, a tabbed showcase, or a mixed-size bento with real visuals.
4. A closing CTA.

## Brutalist personal

Use for a personal site, portfolio, resume, or notes.

- Black on white. One honest system. Every region is a cell with a hard rule.
- No gradients, shadows, blur, rounded corners, pills, or decorative icons.
- Emphasis is inversion: a black block with white text. It is the only highlight.
- Link color marks inline links only. A primary button may use it when asked.
- Status is text, never color.
- Motion off. State changes are instant.
- A tuned dark theme when asked. Not a hard inversion.
- Voice: first person, friendly, plain. One joke at most.
- The concept shows through structure, never spelled out in copy.
- Dense. Real content fills the page. A resume is one packed page.

## Catalog or app

Use for a directory, a tool, a dashboard, or an app screen.

- A light ground with one ink color for text, header, and primary buttons.
- One loud color for exactly one main action per screen, and for one tag. Nothing else.
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
