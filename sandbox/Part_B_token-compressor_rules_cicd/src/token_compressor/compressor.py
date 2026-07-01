"""Core token compression algorithms."""

import re

# Map of verbose developer phrasing to technical shorthand.
SHORTHAND_MAP = {
    r"\bconstant\s+time(?:\s+complexity)?\b": "O(1)",
    r"\blinear\s+time(?:\s+complexity)?\b": "O(n)",
    r"\blogarithmic\s+time(?:\s+complexity)?\b": "O(log n)",
    r"\bquadratic\s+time(?:\s+complexity)?\b": "O(n^2)",
    r"\bpull\s+requests?\b": "PR",
    r"\bdatabases?\b": "DB",
    r"\brepositories?\b": "repo",
    r"\brepository\b": "repo",
    r"\bconfigurations?\b": "config",
    r"\bconfiguration\b": "config",
    r"\bas\s+soon\s+as\s+possible\b": "ASAP",
    r"\bby\s+the\s+way\b": "BTW",
    r"\bfor\s+example\b": "e.g.",
    r"\bthat\s+is\b": "i.e.",
}


def strip_waffle(text: str) -> str:
    """Removes conversational pleasantries, greetings, and sign-offs."""
    lines = text.splitlines()
    if not lines:
        return text

    # Match greetings and opening filler
    greeting_re = re.compile(
        r"^(?:hello|hi|hey|good\s+(?:morning|afternoon|evening))\b[,.!\s]*",
        re.IGNORECASE,
    )
    opening_re = re.compile(
        r"^(?:sure|certainly|absolutely|of\s+course|okay|ok|i\s+can\s+help\s+with\s+that)\b[,.!\s]*",
        re.IGNORECASE,
    )

    # Process start lines
    while lines:
        first_line = lines[0].strip()
        matched = False
        while True:
            m_greet = greeting_re.match(first_line)
            if m_greet:
                first_line = first_line[m_greet.end() :].lstrip()
                matched = True
                continue
            m_open = opening_re.match(first_line)
            if m_open:
                first_line = first_line[m_open.end() :].lstrip()
                matched = True
                continue
            break

        if matched:
            if first_line:
                lines[0] = first_line
                break
            else:
                lines.pop(0)
        else:
            break

    # Framing intro (e.g. "Here is the updated configuration file:")
    framing_re = re.compile(
        r"^\s*(?:here\s+(?:is|are)\s+(?:the\s+)?(?:updated\s+)?(?:[a-z0-9_-]+\s+)*(?:files?|code|configs?|configurations?|diffs?|changes?):\s*)$",
        re.IGNORECASE,
    )
    while lines:
        if framing_re.match(lines[0]):
            lines.pop(0)
        else:
            break

    # Sign-offs / closing remarks
    closing_re = re.compile(
        r"^\s*(?:hope\s+this\s+helps|let\s+me\s+know\s+if\s+you\s+need\s+anything\s+else|thanks|thank\s+you|regards|best\s+regards|sincerely)\b.*$",
        re.IGNORECASE,
    )
    while lines:
        last_line = lines[-1].strip()
        if closing_re.match(last_line) or not last_line:
            lines.pop()
        else:
            break

    return "\n".join(lines)


def replace_shorthand(text: str) -> str:
    """Replaces verbose terms with technical shorthand."""
    for pattern, replacement in SHORTHAND_MAP.items():

        def case_repl(match):
            val = match.group(0)
            if val.istitle():
                return replacement.title()
            if val.isupper():
                return replacement.upper()
            return replacement

        text = re.sub(pattern, case_repl, text, flags=re.IGNORECASE)
    return text


def format_action_tuples(text: str) -> str:
    """Converts verbose file action sentences into action tuples."""
    sentences = re.split(r"(?<=[.!?])\s+", text)
    result = []

    # Matches: In/For <file>, <action> (to/because/in order to/so that) <rationale>
    pattern = re.compile(
        r"^(?:in|for)\s+([a-zA-Z0-9_\-\.\/]+),\s+(.+?)\s+(?:to|because|in\s+order\s+to|so\s+that)\s+(.+)$",
        re.IGNORECASE,
    )

    for sentence in sentences:
        s_clean = sentence.strip()
        has_period = s_clean.endswith(".")
        if has_period:
            s_clean = s_clean[:-1]

        match = pattern.match(s_clean)
        if match:
            file_path = match.group(1).strip()
            action = match.group(2).strip()
            rationale = match.group(3).strip()
            # Remove verb prefix filler
            action = re.sub(
                r"^(?:please|we\s+should|you\s+need\s+to|should)\s+",
                "",
                action,
                flags=re.IGNORECASE,
            )
            formatted = f"{file_path} -> {action}: {rationale}"
            result.append(formatted)
        else:
            result.append(sentence)

    return " ".join(result)


def compact_code_blocks(text: str) -> str:
    """Truncates unchanged portions of code blocks to save space."""
    pattern = r"(```[a-zA-Z0-9_-]*\n)([\s\S]*?)(```)"

    def repl(match):
        header = match.group(1)
        content = match.group(2)
        footer = match.group(3)
        lines = content.splitlines()

        if len(lines) <= 15:
            return match.group(0)

        # Check if the block is a diff or has edits
        has_diff = any(line.startswith("+") or line.startswith("-") for line in lines)

        # Determine comment symbol
        comment_char = "#"
        if any(ext in header for ext in ["js", "ts", "cpp", "java", "c", "css"]):
            comment_char = "//"
        elif "html" in header or "xml" in header:
            comment_char = "<!-- ... -->"

        def make_placeholder(num_lines):
            if comment_char == "<!-- ... -->":
                return f"<!-- ... {num_lines} lines unchanged ... -->"
            return f"{comment_char} ... {num_lines} lines unchanged ..."

        if has_diff:
            keep = [False] * len(lines)
            for i, line in enumerate(lines):
                if line.startswith("+") or line.startswith("-"):
                    for j in range(max(0, i - 3), min(len(lines), i + 4)):
                        keep[j] = True

            new_lines = []
            in_unchanged = False
            unchanged_start = 0
            for i, k in enumerate(keep):
                if k:
                    if in_unchanged:
                        num_unchanged = i - unchanged_start
                        new_lines.append(make_placeholder(num_unchanged))
                        in_unchanged = False
                    new_lines.append(lines[i])
                else:
                    if not in_unchanged:
                        in_unchanged = True
                        unchanged_start = i
            if in_unchanged:
                num_unchanged = len(lines) - unchanged_start
                new_lines.append(make_placeholder(num_unchanged))

            return header + "\n".join(new_lines) + "\n" + footer
        else:
            placeholder = make_placeholder(len(lines) - 10)
            return (
                header
                + "\n".join(lines[:5])
                + f"\n{placeholder}\n"
                + "\n".join(lines[-5:])
                + "\n"
                + footer
            )

    return re.sub(pattern, repl, text)


def compress_ultra(text: str) -> str:
    """Applies aggressive compression (removing articles, helping verbs)."""
    # Remove articles (the, a, an) outside of code blocks
    parts = re.split(r"(```[\s\S]*?```)", text)
    for i in range(len(parts)):
        if not parts[i].startswith("```"):
            parts[i] = re.sub(r"\b(?:the|a|an)\b\s*", "", parts[i], flags=re.IGNORECASE)
            parts[i] = re.sub(
                r"\b(?:is|am|are|was|were|be|been|being)\b\s*",
                "",
                parts[i],
                flags=re.IGNORECASE,
            )
            parts[i] = re.sub(
                r"\b(?:do|does|did|have|has|had)\b\s*",
                "",
                parts[i],
                flags=re.IGNORECASE,
            )
            parts[i] = re.sub(r" {2,}", " ", parts[i])
    return "".join(parts)


def compress(text: str, level: str = "full") -> str:
    """Main function to compress input text based on configuration level."""
    if level not in ["lite", "full", "ultra"]:
        raise ValueError(
            "Invalid compression level. Must be 'lite', 'full', or 'ultra'."
        )

    # Lite: just strip waffle
    text = strip_waffle(text)

    if level == "lite":
        return text

    # Full/Ultra: Apply shorthand and action tuple formatting
    text = replace_shorthand(text)
    text = format_action_tuples(text)
    text = compact_code_blocks(text)

    if level == "ultra":
        text = compress_ultra(text)

    return text.strip()
