#!/usr/bin/env python3
"""GPG Commit Signature Checker.

Verifies that commits in a given revision range (or HEAD) are GPG-signed.
"""

import argparse
import subprocess
import sys
from typing import List, Optional


def run_cmd(cmd: List[str]) -> subprocess.CompletedProcess[str]:
    """Helper to run system commands safely."""
    try:
        return subprocess.run(cmd, capture_output=True, text=True, check=False)
    except FileNotFoundError:
        print(f"Error: Command '{cmd[0]}' not found.", file=sys.stderr)
        sys.exit(2)


def get_commit_info(commit: str) -> str:
    """Gets a short summary (hash, author, subject) of a commit."""
    res = run_cmd(["git", "log", "-1", "--format=%h - %an: %s", commit])
    if res.returncode == 0:
        return res.stdout.strip()
    return commit


def check_git_repo() -> bool:
    """Checks if the current directory is inside a git repository."""
    res = run_cmd(["git", "rev-parse", "--is-inside-work-tree"])
    return res.returncode == 0


def get_commits_to_check(rev_range: Optional[str]) -> Optional[List[str]]:
    """Retrieves commit hashes in the specified range.

    Returns None if a git error occurs.
    """
    if not rev_range:
        # Default to checking just HEAD
        return ["HEAD"]

    res = run_cmd(["git", "rev-list", rev_range])
    if res.returncode != 0:
        print(
            f"Error: Invalid revision range or git error: {res.stderr.strip()}",
            file=sys.stderr,
        )
        return None

    commits = [line.strip() for line in res.stdout.splitlines() if line.strip()]
    return commits


def verify_commit(commit: str, verbose: bool) -> bool:
    """Verifies the GPG signature of a single commit.

    Returns True if valid, False otherwise.
    """
    res = run_cmd(["git", "verify-commit", commit])
    commit_info = get_commit_info(commit)

    if res.returncode == 0:
        if verbose:
            print(f"✓ {commit_info} (Signature OK)")
            if res.stderr.strip():
                print(res.stderr.strip())
        return True
    else:
        print(f"✗ {commit_info} (Verification FAILED)", file=sys.stderr)
        if res.stderr.strip():
            print(res.stderr.strip(), file=sys.stderr)
        return False


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify GPG signatures of git commits in a revision range."
    )
    parser.add_argument(
        "--rev-range",
        type=str,
        help="Revision range to check (e.g. origin/main..HEAD). Defaults to HEAD.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print signature details for valid commits.",
    )
    args = parser.parse_args()

    if not check_git_repo():
        print("Error: Not in a git repository.", file=sys.stderr)
        return 2

    commits = get_commits_to_check(args.rev_range)
    if commits is None:
        return 2

    if not commits:
        print("No commits found to verify in the given range.")
        return 0

    print(f"Checking GPG signatures for {len(commits)} commit(s)...")
    failed = 0
    for commit in commits:
        if not verify_commit(commit, args.verbose):
            failed += 1

    if failed > 0:
        print(
            f"\nVerification failed: {failed} commit(s) lacked valid GPG signatures.",
            file=sys.stderr,
        )
        return 1

    print("\nAll commits verified successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
