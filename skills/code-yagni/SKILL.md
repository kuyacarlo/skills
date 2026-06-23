---
name: code-yagni
description: YAGNI-enforcing development assistant that fights over-engineering, scans for dead code or unnecessary abstractions, and implements a strict "laziest dev in the room" code pruning checklist. Use this skill when reviewing code diffs, optimizing file sizes, or when the user asks to clean up technical debt and unnecessary complexity.
---

# 🦄 Code YAGNI (Simplification & Pruning)

Use this skill to review code, prevent premature abstractions, and ensure that only the minimum required code is written. Enforce YAGNI (You Ain't Gonna Need It) ruthlessly.

---

## 🎯 The YAGNI Decision Ladder

Before writing any new lines of code, declaring new variables, or introducing abstractions, you must evaluate the requirement against this ladder:

1.  **Skip It**: Does this feature actually need to exist right now to satisfy the current acceptance criteria? If not, do not write it.
2.  **Standard Library**: Can the language's built-in standard library solve this problem without any external dependencies? (e.g. `pathlib` in Python, standard array methods in JS).
3.  **Native Platform**: Is there a native operating system, browser, or database feature that makes this code redundant? (e.g., standard CSS instead of JS animations, database constraints instead of complex app logic).
4.  **Existing Dependency**: Can a dependency already listed in the package configuration solve it? Do not add new dependencies if you can help it.
5.  **One-liner**: Can it be written cleanly in a single line or short block?
6.  **Minimum Custom Code**: If you must write custom code, write the absolute minimum. Avoid "future-proofing" (no "we might need this hook/method/class later").

---

## 🪓 Code Review Guidelines

When reviewing code or git diffs (either automatically or when asked for a review):

1.  **Generate a "Delete List"**:
    *   List specific lines, functions, or classes that can be deleted.
    *   Point out early optimizations, unused imports, or dead branches.
2.  **Abstractions Check**:
    *   Flag any interface with only one implementation.
    *   Flag "wrapper" functions that simply call another function with the same arguments.
    *   Flag excessive configuration files or options.
3.  **Code Golf & Dry Runs**:
    *   Propose shorter, cleaner equivalents of verbose code blocks.
    *   Keep documentation concise and inline comments to a minimum (only explain *why*, not *what*).

---

## 📝 Technical Debt Ledger (`yagni:` tags)

*   When you deliberately defer a feature, take a shortcut, or leave a stub to maintain momentum, insert a comment:
    `// yagni: [Short explanation of why it was skipped and what the bare minimum fallback is]`
*   Use this tag to compile a quick "debt ledger" file (e.g., `DEBT.md` or a ZenNotes log) when the user asks to review codebase health.
