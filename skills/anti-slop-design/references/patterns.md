# Patterns

Synthetic before/after pairs for the rules in [SKILL.md](../SKILL.md). Copy the shape, not the samples. The samples are a cloud dev environment, a personal site, and a tools catalog. None have real customers.

## Eyebrow

Before: a tracked label `HOW IT WORKS` above the heading.

After: the heading alone. If the label was a destination, it becomes a link on the top-right of the block: `Runtime ↗`. It is not a pill and it is not above the heading.

## Install command

Before: `curl -fsSL https://example.com/install | sh` under the hero buttons.

After: a button, `Install on your server`. Hover and focus open a popover with the command and a Copy control. The hero itself shows no command.

## Pricing slogan

Before: `Free to run. Pay for help.`

After: heading `Pricing`. Subhead: `Self-hosted is free. Support is a paid plan.`

## Invented layout

Before: a custom pricing mosaic with the buy button in a corner.

After: the category leader's structure. Tiers in a row, a compare table under them, the primary action in the header. No copied logos or illustrations.

## Subhead

Before: `Free forever for open source. Pay when your code is private, your team needs to share, or your company needs SSO.`

After: `Cloud dev environments on hardware you own.`

## Trademark tagline

Before: `Codespaces, but on your own server.`

After: `Cloud dev environments on hardware you own.` A compare table may still name other products in a neutral column.

## Narrow frame

Before: a hero that leads with one forge brand.

After: the category first. The forge is one row in an integration list.

## Toy demo

Before: three grey rectangles labeled File, Editor, and Terminal.

After: a file tree with plausible paths, tabs, breadcrumbs, a status bar, syntax in the real language, and timestamped log lines.

## Header

Before: a logo and four links. No account action.

After: the same header on every page. Links, `Sign in` as text, and a solid `Get started`. The current page is marked.

## Chapters

Before: one static screenshot for the whole product.

After: three tabs, `Code`, `Run`, `Review`. Each tab has a progress bar. They advance on their own. A click jumps. A pause control is visible. Reduced motion starts on the first chapter and stays there.

## Feature cards

Before: four equal cards, each with an icon in a tinted square, a title, a sentence, and `Explore →`.

After, pick one:

- Tabs. Each tab shows that feature's real headline and product mock, plus a link to the page.
- An alternating row. Text on one side, the mock on the other.
- A bento cell with a real snippet, status, or input. Not an icon tile.

## How it works

Before: four equal columns, each a number, a title, and a paragraph.

After: a left stack of steps. Each step is an icon, a title, a paragraph, and a progress track. The right panel is one fixed-height animation of the active step.

## Logo row

Before: a static line, `Plugs into GitHub GitLab …`, or a row of invented customer logos.

After: a marquee of permitted product marks, or plain wordmarks when there is no permission, with a pause control. No invented customers. If there is no real list, omit the row.

## Static hero

Before: a centered headline and two buttons, with no motion and no product.

After: the headline, subtext, and buttons rise in sequence. The product window tilts up into place and shows the product doing its real job, such as rows revealing as a run completes. No float loop, no decorative pulse or blink. Reduced motion shows the settled frame.

## Layout shift

Before: the progress bar mounts only on the active step, so the list jumps.

After: every step has a track. Only the fill moves. The animation panel height does not change between steps.

## Icons

Before: an emoji, or an icon inside a colored rounded square, or a step whose icon node renders empty.

After: a stroke icon (stroke width 1.5, sized 1em) beside the text, sitting directly on the row. Confirm it is visible.

## Invented claim

Before: a headline guessed from a module name, or `10,000 teams` with no source.

After: the proposition from the owner, or `TODO(positioning)`. Missing numbers stay `[PRICE]` or `[DATE]`.

## Logo

Before: a cartoon animal face with eyes.

After: one flat path. Rounded snout, a cut-out for the nose, no eyes, no sharp chin. See [logo](logo.md) for the sheet.

## Explained design

Before: a caption under a list, `Each one links to the issuer, so you don't have to take my word for it.` Or a legend, `symptom → cause → fix`.

After: the list alone. The links prove it. The row structure shows the order.

## Stray link color

Before: a card that is one big link, so its heading, paragraph, and bullets all render in link blue. The table of contents and breadcrumbs use browser-default blue.

After: everything in ink. The card title underlines on hover. Only inline links in body text use the link color.

## Lost emphasis

Before: desktop inverts the featured project row. The phone version drops the inversion to save space.

After: the phone card keeps the inverted block. The layout changes. The emphasis does not.

## Sparse versus cramped

Before: a resume page with three short entries and large empty bands. Or a phone layout with text against the cell edge.

After: the resume shows every real entry in a packed single column. Cells get padding from the spacing scale.

## Empty control

Before: a filter with three choices, two of which show zero results. A `Show more` button under a list of one. A blank certificates page.

After: the filter offers only choices with results, and hides under two choices. No `Show more`. The page says `No certificates yet.`

## Phone layout

Before: a six-item layer strip on desktop becomes a two-column card stack on phone, in a new order.

After: the same strip, transposed. Numbers in one row, labels in the next, same order.

## Link target

Before: a row with the name as plain text, then `source` and `live` links, and a line `or write to [email]` under a `Send an email` button.

After: the name links to live, or to source when there is no live. Other links sit at the row end. The repeated email line is gone.

## Stat overflow

Before: `2,713,408` clipped inside a stat card.

After: `2.71M`, with the exact value in an accessible label or tooltip.

## Dark mode

Before: a hard color inversion. Black blocks turn white and glare.

After: a tuned dark palette. Filled blocks stay dark, slightly raised. The toggle sits just before the primary action.

## Copy button

Before: `Copy this stack` opens a dialog and copies nothing. Or every copy button on the page flips to `Copied`.

After: one click copies. Only that button reads `Copied` for a moment.

## Link preview

Before: a shared link shows the bare URL and a generic favicon.

After: Open Graph title, description, and a designed preview image in the site's own style.

## Code and prose

Before: monochrome code blocks. Inline prose words with a tinted highlight background.

After: a quiet syntax theme in code. Prose has no highlight.

## Voice

Before, personal site: `Let's talk.` and `I am a software and systems engineer.`

After: a friendly first-person line in the owner's words, or `TODO(positioning)`.

## Dead filter

Before: a filter bar on a page of six notes, or a filter that does not change the list.

After: no filter for a small set. Any filter that ships changes the results, with a test.

## Surface effects

Before: a hero on a purple-to-blue gradient with a radial glow behind the headline, gradient headline text, and glass cards.

After: a plain ground in the project palette. The headline is one solid color. Cards use a border or the background, not blur.

## Slogan copy

Before: `Not just a tool — a teammate.` and `Fast. Simple. Secure.`

After: `Reviews pull requests and opens fixes in your repo.` One plain sentence, no em dash.

## Pulsing status

Before: a green dot that pulses beside `Online`, forever.

After: a still dot beside the word `Online`. Motion only while a deploy is actually running.
