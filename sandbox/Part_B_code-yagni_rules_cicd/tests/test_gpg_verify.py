import subprocess
from unittest.mock import patch

import src.gpg_verify as gpg_verify


def test_check_git_repo_success():
    # Verify success path for checking git repository presence
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
    # Verify behavior when repository is not found
    with patch("src.gpg_verify.run_cmd") as mock_run:
        mock_run.return_value = subprocess.CompletedProcess(
            args=["git", "rev-parse", "--is-inside-work-tree"],
            returncode=128,
            stdout="",
            stderr="fatal: not a git repository",
        )
        assert gpg_verify.check_git_repo() is False


def test_get_commits_to_check_default():
    # Verify fallback to HEAD when no range is provided
    assert gpg_verify.get_commits_to_check(None) == ["HEAD"]


def test_get_commits_to_check_range_success():
    # Verify commit listing for a valid revision range
    with patch("src.gpg_verify.run_cmd") as mock_run:
        mock_run.return_value = subprocess.CompletedProcess(
            args=["git", "rev-list", "origin/master..HEAD"],
            returncode=0,
            stdout="commit1\ncommit2\n",
            stderr="",
        )
        assert gpg_verify.get_commits_to_check("origin/master..HEAD") == [
            "commit1",
            "commit2",
        ]


def test_get_commits_to_check_range_failure():
    # Verify behavior with an invalid revision range
    with patch("src.gpg_verify.run_cmd") as mock_run:
        mock_run.return_value = subprocess.CompletedProcess(
            args=["git", "rev-list", "invalid..range"],
            returncode=128,
            stdout="",
            stderr="fatal: ambiguous argument",
        )
        assert gpg_verify.get_commits_to_check("invalid..range") is None


def test_verify_commit_success():
    # Verify check for a validly signed commit
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
    # Verify check for an unsigned or invalidly signed commit
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
    # Verify main script execution with all commits successfully signed
    mock_check_repo.return_value = True
    mock_get_commits.return_value = ["commit1", "commit2"]
    mock_verify.side_effect = [True, True]

    with patch("sys.argv", ["gpg_verify.py", "--rev-range", "HEAD~2..HEAD"]):
        assert gpg_verify.main() == 0


@patch("src.gpg_verify.check_git_repo")
@patch("src.gpg_verify.get_commits_to_check")
@patch("src.gpg_verify.verify_commit")
def test_main_failure(mock_verify, mock_get_commits, mock_check_repo):
    # Verify main script execution with a signature check failure
    mock_check_repo.return_value = True
    mock_get_commits.return_value = ["commit1", "commit2"]
    mock_verify.side_effect = [True, False]

    with patch("sys.argv", ["gpg_verify.py"]):
        assert gpg_verify.main() == 1


@patch("src.gpg_verify.check_git_repo")
def test_main_no_repo(mock_check_repo):
    # Verify main script behavior outside of a git repository
    mock_check_repo.return_value = False
    with patch("sys.argv", ["gpg_verify.py"]):
        assert gpg_verify.main() == 2


def test_get_github_actions_range_not_in_actions(monkeypatch):
    # Verify range resolves to None when not running inside GitHub Actions environment
    monkeypatch.delenv("GITHUB_ACTIONS", raising=False)
    assert gpg_verify.get_github_actions_range() is None


def test_get_github_actions_range_missing_path(monkeypatch):
    # Verify range resolves to None if GITHUB_ACTIONS is active but no event path is configured
    monkeypatch.setenv("GITHUB_ACTIONS", "true")
    monkeypatch.delenv("GITHUB_EVENT_PATH", raising=False)
    assert gpg_verify.get_github_actions_range() is None


def test_get_github_actions_range_invalid_json(monkeypatch, tmp_path):
    # Verify error resilience when the event JSON payload is malformed
    event_file = tmp_path / "event.json"
    event_file.write_text("invalid json")
    monkeypatch.setenv("GITHUB_ACTIONS", "true")
    monkeypatch.setenv("GITHUB_EVENT_PATH", str(event_file))
    assert gpg_verify.get_github_actions_range() is None


def test_get_github_actions_range_pull_request(monkeypatch, tmp_path):
    # Verify extraction of revision range from a pull request event payload
    event_file = tmp_path / "event.json"
    import json

    event_data = {
        "pull_request": {
            "base": {"sha": "basesha123"},
            "head": {"sha": "headsha456"},
        }
    }
    event_file.write_text(json.dumps(event_data))
    monkeypatch.setenv("GITHUB_ACTIONS", "true")
    monkeypatch.setenv("GITHUB_EVENT_NAME", "pull_request")
    monkeypatch.setenv("GITHUB_EVENT_PATH", str(event_file))
    assert gpg_verify.get_github_actions_range() == "basesha123..headsha456"


def test_get_github_actions_range_push(monkeypatch, tmp_path):
    # Verify extraction of revision range from a push event payload
    event_file = tmp_path / "event.json"
    import json

    event_data = {
        "before": "beforesha123",
        "after": "aftersha456",
    }
    event_file.write_text(json.dumps(event_data))
    monkeypatch.setenv("GITHUB_ACTIONS", "true")
    monkeypatch.setenv("GITHUB_EVENT_NAME", "push")
    monkeypatch.setenv("GITHUB_EVENT_PATH", str(event_file))
    assert gpg_verify.get_github_actions_range() == "beforesha123..aftersha456"


def test_get_github_actions_range_push_initial(monkeypatch, tmp_path):
    # Verify range is None (fallback to HEAD) on push when the before SHA is all zeroes
    event_file = tmp_path / "event.json"
    import json

    event_data = {
        "before": "0000000000000000000000000000000000000000",
        "after": "aftersha456",
    }
    event_file.write_text(json.dumps(event_data))
    monkeypatch.setenv("GITHUB_ACTIONS", "true")
    monkeypatch.setenv("GITHUB_EVENT_NAME", "push")
    monkeypatch.setenv("GITHUB_EVENT_PATH", str(event_file))
    assert gpg_verify.get_github_actions_range() is None
