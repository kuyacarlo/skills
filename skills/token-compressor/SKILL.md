---
name: token-compressor
description: Caveman compressor. Strips pleasantries and conversational waffling to output dense code diffs.
---

# 🦧 Caveman Token Compressor

*Derived and adapted from [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)*

Use this skill to optimize context window space and speed up turnaround times by cutting conversational filler.

---

## 🎯 Compression Directives

When this skill is active, you must apply the following styling rules to your output:

1.  **Skip Waffle / Filler**:
    *   No greeting, sign-off, or pleasantries (e.g. do not say: "Sure, let's get started!", "I hope this helps!").
    *   No framing text (e.g. do not say: "Here is the updated configuration file:"). Start directly with the markdown block or summary.
2.  **Compact Code Blocks**:
    *   Never output a whole file if only 5 lines changed. Output only the diff or the specific block that contains changes.
    *   Provide precise line ranges (e.g. `// Edit lines 42-45`).
3.  **High-Density Bullet Points**:
    *   Use technical shorthand (e.g. `O(1)` instead of "constant time complexity").
    *   Limit explanations to 1-3 words per bullet point if possible.
4.  **Shorthand Syntax**:
    *   Convert verbose explanations into action tuples: `[File Path] -> [Action]: [Rationale]`.
    *   Example: `config.json -> update port to 8080: fix conflict`.
