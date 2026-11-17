# Motion

Use these tokens. Do not invent a second timing system on the same page.

| Job | Token |
| --- | --- |
| Hero text rise | 0.7s, `cubic-bezier(.2, .7, .2, 1)`, stagger from 0.05s to 0.4s |
| Product shot entrance | `perspective(1800px) rotateX(16deg) translateY(48px)` to identity, over 1.1s |
| Float after entrance | ±6px over 6s |
| Logo marquee | 40s linear. Duplicate the list and translate −50%. Pause on hover. Fade both edges with a mask |
| How-it-works step | Fill the active track for 4.5s, then advance. A click selects that step and stops the timer |
| Feature tabs | Advance about every 6s until a click, then stop |
| Demo chapters | Advance about every 8s. A click jumps. A pause control is always available |

## Reduced motion

Honor `prefers-reduced-motion: reduce`.

- No rise, tilt, float, marquee travel, or auto-advance.
- Show the settled hero and the first chapter.
- Leave progress tracks in the layout. Do not remove them.

## No layout shift

- The animation panel has one fixed height for every step.
- Progress tracks are always in the document. Animate the fill, not the element's presence.
- Tab panels share one height. Shorter content does not pull the page up.
