import subprocess
from unittest.mock import patch

import src.gpg_verify as gpg_verify


def test_check_git_repo_success():
    with patch("src.gpg_verify.run_cmd") as mock_run:
        mock_run.return_value = subprocess.CompletedProcess(
            args=["git", "rev-parse", "--is-inside-work-tree"],
            returncode=0,
            stdout="true\n",
            stderr="",
        )
        assert gpg_verify.check_git_repo() is True
        mock_run.assert_called_once_with(["git", "rev-parse", "--is-inside-work-tree"])


def test_check_git_repo_failure():
    with patch("src.gpg_verify.run_cmd") as mock_run:
        mock_run.return_value = subprocess.CompletedProcess(
            args=["git", "rev-parse", "--is-inside-work-tree"],
            returncode=128,
            stdout="",
            stderr="fatal: not a git repository",
        )
        assert gpg_verify.check_git_repo() is False


def test_get_commits_to_check_default():
    assert gpg_verify.get_commits_to_check(None) == ["HEAD"]


def test_get_commits_to_check_range_success():
    with patch("src.gpg_verify.run_cmd") as mock_run:
        mock_run.return_value = subprocess.CompletedProcess(
            args=["git", "rev-list", "origin/main..HEAD"],
            returncode=0,
            stdout="commit1\ncommit2\n",
            stderr="",
        )
        assert gpg_verify.get_commits_to_check("origin/main..HEAD") == [
            "commit1",
            "commit2",
        ]


def test_get_commits_to_check_range_failure():
    with patch("src.gpg_verify.run_cmd") as mock_run:
        mock_run.return_value = subprocess.CompletedProcess(
            args=["git", "rev-list", "invalid..range"],
            returncode=128,
            stdout="",
            stderr="fatal: ambiguous argument",
        )
        assert gpg_verify.get_commits_to_check("invalid..range") is None


def test_verify_commit_success():
    with (
        patch("src.gpg_verify.run_cmd") as mock_run,
        patch("src.gpg_verify.get_commit_info") as mock_info,
    ):
        mock_run.return_value = subprocess.CompletedProcess(
            args=["git", "verify-commit", "commit_hash"],
            returncode=0,
            stdout="",
            stderr="gpg: Good signature",
        )
        mock_info.return_value = "commit_hash - Author: Subject"

        assert gpg_verify.verify_commit("commit_hash", verbose=True) is True
        mock_run.assert_called_once_with(["git", "verify-commit", "commit_hash"])


def test_verify_commit_failure():
    with (
        patch("src.gpg_verify.run_cmd") as mock_run,
        patch("src.gpg_verify.get_commit_info") as mock_info,
    ):
        mock_run.return_value = subprocess.CompletedProcess(
            args=["git", "verify-commit", "commit_hash"],
            returncode=1,
            stdout="",
            stderr="gpg: No signature found",
        )
        mock_info.return_value = "commit_hash - Author: Subject"

        assert gpg_verify.verify_commit("commit_hash", verbose=False) is False


@patch("src.gpg_verify.check_git_repo")
@patch("src.gpg_verify.get_commits_to_check")
@patch("src.gpg_verify.verify_commit")
def test_main_success(mock_verify, mock_get_commits, mock_check_repo):
    mock_check_repo.return_value = True
    mock_get_commits.return_value = ["commit1", "commit2"]
    mock_verify.side_effect = [True, True]

    with patch("sys.argv", ["gpg_verify.py", "--rev-range", "HEAD~2..HEAD"]):
        assert gpg_verify.main() == 0


@patch("src.gpg_verify.check_git_repo")
@patch("src.gpg_verify.get_commits_to_check")
@patch("src.gpg_verify.verify_commit")
def test_main_failure(mock_verify, mock_get_commits, mock_check_repo):
    mock_check_repo.return_value = True
    mock_get_commits.return_value = ["commit1", "commit2"]
    mock_verify.side_effect = [True, False]

    with patch("sys.argv", ["gpg_verify.py"]):
        assert gpg_verify.main() == 1


@patch("src.gpg_verify.check_git_repo")
def test_main_no_repo(mock_check_repo):
    mock_check_repo.return_value = False
    with patch("sys.argv", ["gpg_verify.py"]):
        assert gpg_verify.main() == 2


def test_get_commit_info_success():
    with patch("src.gpg_verify.run_cmd") as mock_run:
        mock_run.return_value = subprocess.CompletedProcess(
            args=["git", "log", "-1", "--format=%h - %an: %s", "commit_hash"],
            returncode=0,
            stdout="commit_hash - Author: Subject\n",
            stderr="",
        )
        assert (
            gpg_verify.get_commit_info("commit_hash") == "commit_hash - Author: Subject"
        )
        mock_run.assert_called_once_with(
            ["git", "log", "-1", "--format=%h - %an: %s", "commit_hash"]
        )


def test_get_commit_info_failure():
    with patch("src.gpg_verify.run_cmd") as mock_run:
        mock_run.return_value = subprocess.CompletedProcess(
            args=["git", "log", "-1", "--format=%h - %an: %s", "commit_hash"],
            returncode=128,
            stdout="",
            stderr="error",
        )
        assert gpg_verify.get_commit_info("commit_hash") == "commit_hash"


def test_run_cmd_file_not_found():
    with patch("subprocess.run", side_effect=FileNotFoundError):
        import sys

        with patch.object(sys, "exit") as mock_exit:
            gpg_verify.run_cmd(["non_existent_command"])
            mock_exit.assert_called_once_with(2)
