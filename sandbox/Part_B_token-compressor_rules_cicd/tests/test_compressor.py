"""Unit tests for the token compressor."""

import sys
from unittest.mock import patch
import pytest
from token_compressor.compressor import (
    compress,
    strip_waffle,
    replace_shorthand,
    format_action_tuples,
    compact_code_blocks,
    compress_ultra,
)
from token_compressor.cli import main


def test_strip_waffle():
    # Test greeting and pleasantries removal
    input_text = "Hello, sure I can help with that!\nThis is actual content.\nHope this helps! Regards."
    assert strip_waffle(input_text).strip() == "This is actual content."

    # Test framing removal
    input_text_2 = "Here is the updated configuration file:\n```yaml\nports: 80\n```"
    assert strip_waffle(input_text_2).strip() == "```yaml\nports: 80\n```"


def test_replace_shorthand():
    text = "We achieved constant time complexity for the database. By the way, look at this pull request."
    expected = "We achieved O(1) for the DB. BTW, look at this PR."
    assert replace_shorthand(text) == expected

    # Test case preservation
    assert replace_shorthand("Database") == "Db"
    assert replace_shorthand("DATABASE") == "DB"


def test_format_action_tuples():
    text = "In src/main.py, add error handling to prevent crash."
    expected = "src/main.py -> add error handling: prevent crash"
    assert format_action_tuples(text) == expected

    text2 = "For config.json, please update port because it conflicts."
    expected2 = "config.json -> update port: it conflicts"
    assert format_action_tuples(text2) == expected2


def test_compact_code_blocks():
    # Long block without edits -> placeholder in the middle
    lines = [f"line{i}" for i in range(20)]
    text = "```python\n" + "\n".join(lines) + "\n```"
    compacted = compact_code_blocks(text)
    assert "# ... 10 lines unchanged ..." in compacted
    assert "line0" in compacted
    assert "line19" in compacted

    # Diff block with edits -> context lines preserved
    diff_lines = [
        " unchanged1",
        " unchanged2",
        " unchanged3",
        " unchanged4",
        " unchanged5",
        " unchanged6",
        "-old line",
        "+new line",
        " unchanged7",
        " unchanged8",
        " unchanged9",
        " unchanged10",
        " unchanged11",
        " unchanged12",
        " unchanged13",
        " unchanged14",
    ]
    text_diff = "```diff\n" + "\n".join(diff_lines) + "\n```"
    compacted_diff = compact_code_blocks(text_diff)
    assert "-old line" in compacted_diff
    assert "+new line" in compacted_diff
    assert "# ... 3 lines unchanged ..." in compacted_diff


def test_compress_ultra():
    text = "This is the configuration file which has a database. Inside code: ```python\nthis is a database\n```"
    expected = "This configuration file which database. Inside code: ```python\nthis is a database\n```"
    assert compress_ultra(text) == expected


def test_compress_levels():
    text = (
        "Hello!\nIn config.json, update the port so that we avoid conflicts.\nRegards."
    )

    # Lite level: only waffle stripped
    lite_res = compress(text, level="lite")
    assert "In config.json" in lite_res
    assert "Hello" not in lite_res
    assert "Regards" not in lite_res
    assert "config.json ->" not in lite_res  # action tuples not applied

    # Full level: full compression except ultra
    full_res = compress(text, level="full")
    assert "config.json -> update the port: we avoid conflicts" in full_res
    assert "the" in full_res  # articles preserved

    # Ultra level: aggressive compression
    ultra_res = compress(text, level="ultra")
    assert "the" not in ultra_res  # articles removed

    with pytest.raises(ValueError):
        compress(text, level="invalid")


def test_cli_stdin(capsys):
    test_input = "Hello!\nThis is a database check."
    with patch.object(sys, "argv", ["token_compressor"]), patch(
        "sys.stdin.read", return_value=test_input
    ):
        main()
    captured = capsys.readouterr()
    assert "This is a DB check." in captured.out


def test_cli_file(tmp_path, capsys):
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "output.txt"
    input_file.write_text("Hello!\nThis is a database check.")

    with patch.object(
        sys, "argv", ["token_compressor", str(input_file), "--output", str(output_file)]
    ):
        main()

    assert output_file.read_text() == "This is a DB check.\n"
