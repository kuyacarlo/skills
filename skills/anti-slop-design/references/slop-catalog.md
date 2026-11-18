# Slop catalog

Generated-UI tells and their fixes, grouped by area. [SKILL.md](../SKILL.md) holds the rules and checklist. This file is the long scan list.

Adapted from the [impeccable slop catalog](https://impeccable.style/slop). Slop changes with trends and models. A hit is a reason to look closer, not an automatic verdict. Intent and context still matter.

## Design system

| Tell | Fix |
| --- | --- |
| Font, color, radius, or font size outside the project's `DESIGN.md` | Use an approved value, or update `DESIGN.md` on purpose |

## Visual details

| Tell | Fix |
| --- | --- |
| Decorative grid-line background | Keep grids for work that needs measurement |
| Hard offset shadow | Only as a deliberate style |
| Colored border on a rounded card | A lighter border, or let the background define the card |
| Glassmorphism everywhere | Blur only to solve a real layering problem |
| Side-stripe accent border | Remove it when there is no status to show |
| Hairline border plus wide shadow | Pick the edge or the shadow |
| Repeating gradient stripes | A plain surface or a texture that fits |
| Extreme radius on cards | Scale the curve to the card size |
| Rough SVG illustrations | Polished art, photography, or nothing |

## Typography

| Tell | Fix |
| --- | --- |
| Label above a heading | Remove it, or fold it into the heading |
| Badge above the hero headline | Remove it, or move the information into the headline or body |
| Icon tile stacked above a heading | Icon beside the heading, no container |
| Tiny interface text | Readable without zoom |
| One word alone on the last line | `text-wrap: pretty`, or adjust the measure |
| Heading with a stub last line | `text-wrap: balance` |
| Flat type hierarchy | Vary size, weight, and spacing |
| Italic serif display headline | A face that fits the product |
| Oversized hero headline | Shorter, or smaller, so the offer and next step fit |
| Crushed letter spacing | Loosen tracking, especially on phones |
| The font every generated page uses | Choose for the product and reading needs; keep real brand fonts |
| One font for everything | Vary size and weight before adding a family |
| All-caps body text | Sentence case; uppercase for short labels only |

## Color and contrast

| Tell | Fix |
| --- | --- |
| Radial gradient halo behind content | Remove it if it competes with content |
| Soft spotlight behind content | Guide attention with spacing, contrast, headings |
| "AI" palette | Build it from the product's identity |
| Dark mode with glowing accents | Keep dark, drop the glow |
| Gradient text | One solid color; size or weight for emphasis |
| Grey text on a colored ground | A darker tint or light text; check contrast on the real ground |
| Default cream or beige palette | Only when it is the brand |

## Layout and space

| Tell | Fix |
| --- | --- |
| Tiny numbered section labels | Number only real steps or sequences |
| Cards flush against a scroller edge | Equal space at both ends |
| Text covered by another layer | Move the layer or give the text room |
| Unbalanced opening columns | Rebalance, or move the long part below both |
| Heading closer to the previous section | More space above a heading than below |
| Hero metric layout | Lead with a metric only when it explains the product |
| Identical card grids | Group related ideas, vary the layout to the content |
| Monotonous spacing | Close within groups, wider between them |
| Nested cards | Flatten with spacing, type, and dividers |
| Lines too long | About 65–75 characters |
| Content overflowing its container | Wrap, shrink, or use a scroll region |
| Clipped menus and popovers | Allow overflow, or render outside the clip |

## Motion

| Tell | Fix |
| --- | --- |
| Pulsing status dot | Static status stays still; animate real activity only |
| Decorative blinking cursor | Only where someone is typing |
| Auto-scrolling marquee | Stop it, or add pause and browse controls |
| Bounce or elastic easing | Settle routine UI quickly |

## Copy

| Tell | Fix |
| --- | --- |
| The same text twice in one container | Keep the label once |
| Em-dash overuse | Full stops or clearer punctuation |
| Generic marketing claims | Concrete actions and improvements |
| Forced "not X, Y" contrast | State the point directly |
| Calling things "theater" | Say what is ineffective and why |

## Imagery

| Tell | Fix |
| --- | --- |
| Placeholder-style illustrations | Imagery that says something specific |
| Jagged image masks | A prepared cut-out or a clean crop |
| Images buried under overlays | Lighten the overlay or drop the image |
| Broken or placeholder image | Add the real asset and confirm it loads, or remove it |

## General quality

| Tell | Fix |
| --- | --- |
| JavaScript errors on load | Fix before polishing visuals |
| Content waiting on an animation to appear | Visible by default |
| Cramped padding | Padding from the spacing scale |
| Body text touching the page edge | Container padding that holds at narrow widths |
| Justified text | Start-aligned body text |
| Low-contrast text | WCAG AA: 4.5:1 regular, 3:1 large |
| Skipped heading level | Levels match the page structure |
| Tight line height | Start near 1.5× |
| Tiny body text | Start near 16px |
| Wide tracking on body text | Default tracking; wide only on short labels |
