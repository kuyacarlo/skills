# SPEC.md - GPG Commit Verifier & CI/CD Pipeline

## 1. Overview & Core Goal
The core goal of this project is to implement a python-based command-line utility to verify GPG signatures on git commits, configure a `.pre-commit-config.yaml` to run local hooks for linting, formatting, GPG verification, and testing, and implement a GitHub Actions CI workflow in `.github/workflows/ci.yml`.

The GPG commit verifier utility should support:
- Verifying the signature of the current `HEAD` commit.
- Verifying the signatures of commits within a specified revision range.
- Providing verbose logs for valid or invalid signatures.

---

## 2. Architecture & Stack
- **Language**: Python (>= 3.12)
- **Dependency & Environment Manager**: uv (astral-sh)
- **Formatting & Linting**: Ruff
- **Test Framework**: pytest
- **Local Git Hooks**: pre-commit
- **CI/CD Platform**: GitHub Actions

---

## 3. API / Data Contracts

### 3.1 CLI Options for `src/gpg_verify.py`
The utility will support the following CLI arguments:
- `--rev-range`: Specifying the revision range of commits to verify (e.g. `HEAD~3..HEAD`). If omitted, default to checking `HEAD`.
- `--verbose`: Flag to print detail logs for signature checks.

### 3.2 Python Functions in `src/gpg_verify.py`
- `check_git_repo() -> bool`: Verifies that the tool is executed inside a Git repository.
- `get_commits_to_check(rev_range: Optional[str]) -> Optional[List[str]]`: Returns a list of commit hashes.
- `verify_commit(commit: str, verbose: bool) -> bool`: Verifies if a specific commit GPG signature is valid.
- `get_commit_info(commit: str) -> str`: Formats short commit information.

---

## 4. Feature Checklist

### MVP (Must-Have)
- [x] Write a robust GPG commit verifier CLI tool (`src/gpg_verify.py`).
- [x] Create a comprehensive test suite (`tests/test_gpg_verify.py`) mocking git subprocess runs.
- [x] Configure `.pre-commit-config.yaml` to enforce:
  - Ruff linting (`ruff`)
  - Ruff formatting (`ruff-format`)
  - Local commit GPG signature check (`gpg-verify`)
  - Local unit test runner (`run-tests`)
- [x] Create a GitHub Actions workflow (`.github/workflows/ci.yml`) to automatically run linting, formatting check, tests, and GPG commit checks.

### V1 (Should-Have)
- [ ] Allow specifying individual commit hashes instead of ranges.

### Future (Nice-to-Have)
- [ ] Auto-import keys or match against a list of allowed signing keys.

---

## 5. Validation Criteria
1. **Linting and Formatting**:
   - `uv run ruff check src/ tests/` executes without errors.
   - `uv run ruff format --check src/ tests/` executes without errors.
2. **Testing**:
   - `uv run pytest` runs and passes all tests successfully.
3. **Pre-commit**:
   - `pre-commit run --all-files` runs successfully on all hooks.
4. **CI/CD Action**:
   - The GitHub Actions workflow file `.github/workflows/ci.yml` is parsed correctly and runs to success.
