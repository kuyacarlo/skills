# Motion

Product profile only. The brutalist personal profile has no motion. A project design file overrides this note.

Animate real activity and state changes. Never decoration. Use these tokens and do not invent a second timing system on the same page.

| Job | Token |
| --- | --- |
| Hero text rise | 0.7s, `cubic-bezier(.2, .7, .2, 1)`, stagger from 0.05s to 0.4s |
| Product shot entrance | `perspective(112rem) rotateX(16deg) translateY(3rem)` to identity, over 1.1s. No float loop after |
| Integration marquee | 40s linear. Duplicate the list and translate −50%. Pause on hover and a visible pause control. Fade both edges with a mask |
| How-it-works step | Fill the active track for 4.5s, then advance. A click selects that step and stops the timer |
| Feature tabs | Advance about every 6s until a click, then stop |
| Demo chapters | Advance about every 8s. A click jumps. A pause control is always visible |

Banned: bounce or elastic easing, pulsing status dots on static status, blinking cursors outside a typing demo, floating loops.

## Visible by default

- Content renders visible in the HTML. Entrance animations start from a class added by script, so a failed script still shows the page.
- No element waits on scroll triggers to become readable.

## Reduced motion

Honor `prefers-reduced-motion: reduce`.

- No rise, tilt, marquee travel, or auto-advance.
- Show the settled hero and the first chapter.
- Leave progress tracks in the layout. Do not remove them.

## No layout shift

- The animation panel has one fixed height for every step.
- Progress tracks are always in the document. Animate the fill, not the element's presence.
- Tab panels share one height. Shorter content does not pull the page up.
