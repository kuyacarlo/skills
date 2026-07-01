"""Command-line interface for the token compressor."""

import argparse
import sys
from token_compressor.compressor import compress


def main():
    parser = argparse.ArgumentParser(
        description="Compress natural language and code blocks into compact forms."
    )
    parser.add_argument(
        "input",
        nargs="?",
        default="-",
        help="Input file path (or '-' for standard input).",
    )
    parser.add_argument(
        "--level",
        choices=["lite", "full", "ultra"],
        default="full",
        help="Compression level: 'lite', 'full', or 'ultra' (default: 'full').",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Output file path (default: standard output).",
    )

    args = parser.parse_args()

    # Read input
    if args.input == "-":
        text = sys.stdin.read()
    else:
        try:
            with open(args.input, "r", encoding="utf-8") as f:
                text = f.read()
        except FileNotFoundError:
            sys.stderr.write(f"Error: file not found: {args.input}\n")
            sys.exit(1)
        except Exception as e:
            sys.stderr.write(f"Error reading file: {e}\n")
            sys.exit(1)

    # Perform compression
    try:
        compressed_text = compress(text, level=args.level)
    except ValueError as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)

    # Write output
    if args.output:
        try:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(compressed_text + "\n")
        except Exception as e:
            sys.stderr.write(f"Error writing file: {e}\n")
            sys.exit(1)
    else:
        sys.stdout.write(compressed_text + "\n")


if __name__ == "__main__":
    main()
