# SPEC.md - GPG Commit Verifier & CI/CD Pipeline

## 1. Overview & Core Goal
The core goal of this project is to implement a Python-based command-line utility to verify GPG signatures on git commits, configure a `.pre-commit-config.yaml` to run local hooks for linting, formatting, GPG verification, and testing, and implement a GitHub Actions CI workflow in `.github/workflows/ci.yml`.

The GPG commit verifier utility supports:
- Verifying the GPG signature of the current `HEAD` commit.
- Verifying the GPG signatures of commits within a specified git revision range.
- Providing verbose logs for valid or invalid signatures.
- Checking individual commit hashes directly.

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
The utility supports the following command-line interface arguments:
- `--rev-range`: Specifying the revision range of commits to verify (e.g. `HEAD~3..HEAD`). If omitted, default to checking `HEAD` (unless specific commits are provided).
- `--commits`: Space-separated list of individual commit hashes/references to verify.
- `--verbose`: Flag to print detailed logs for signature checks.

### 3.2 Python Functions in `src/gpg_verify.py`
- [run_cmd](file:///home/kaoru/projects/skills/sandbox/Part_C_C5_cicd/src/gpg_verify.py): Helper to run system commands safely.
- [check_git_repo](file:///home/kaoru/projects/skills/sandbox/Part_C_C5_cicd/src/gpg_verify.py): Verifies that the tool is executed inside a Git repository.
- [get_commit_info](file:///home/kaoru/projects/skills/sandbox/Part_C_C5_cicd/src/gpg_verify.py): Gets a short summary (hash, author, subject) of a commit.
- [get_commits_to_check](file:///home/kaoru/projects/skills/sandbox/Part_C_C5_cicd/src/gpg_verify.py): Resolves and returns a list of commit hashes.
- [verify_commit](file:///home/kaoru/projects/skills/sandbox/Part_C_C5_cicd/src/gpg_verify.py): Verifies if a specific commit's GPG signature is valid.

---

## 4. Feature Checklist

### MVP (Must-Have)
- [ ] Write a GPG commit verifier CLI tool ([gpg_verify.py](file:///home/kaoru/projects/skills/sandbox/Part_C_C5_cicd/src/gpg_verify.py)).
- [ ] Create a test suite ([test_gpg_verify.py](file:///home/kaoru/projects/skills/sandbox/Part_C_C5_cicd/tests/test_gpg_verify.py)) mocking git subprocess runs.
- [ ] Configure [.pre-commit-config.yaml](file:///home/kaoru/projects/skills/sandbox/Part_C_C5_cicd/.pre-commit-config.yaml) to enforce:
  - Ruff linting (`ruff`)
  - Ruff formatting (`ruff-format`)
  - Local commit GPG signature check (`gpg-verify`)
  - Local unit test runner (`run-tests`)
- [ ] Create a GitHub Actions workflow ([ci.yml](file:///home/kaoru/projects/skills/sandbox/Part_C_C5_cicd/.github/workflows/ci.yml)) to run linting, formatting check, tests, and GPG commit checks.

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
   - `uv run pre-commit run --config .pre-commit-config.yaml --all-files --hook-stage manual` runs successfully on all hooks.
 4. **CI/CD Action**:
   - The GitHub Actions workflow file `.github/workflows/ci.yml` is parsed correctly and configured to execute.
