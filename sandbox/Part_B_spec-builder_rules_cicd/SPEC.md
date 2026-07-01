# Specification: GPG Commit Signature Checker & CI/CD Pipeline

This specification defines the requirements, architecture, API, and validation scenarios for the GPG commit signature verifier utility, along with its pre-commit hooks and GitHub Actions workflow in `Part_B_spec-builder_rules_cicd`.

---

## 1. Overview & Core Goal

The objective is to establish an automated pipeline ensuring codebase quality and cryptographic provenance. The key deliverables are:
- A command-line script (`gpg_verify.py`) to audit git commit ranges and verify GPG signatures.
- A pre-commit configuration (`.pre-commit-config.yaml`) integrating style checks (Ruff), GPG verification, and tests.
- A GitHub Actions workflow (`.github/workflows/ci.yml`) validating all code changes on pull requests and branch pushes.

---

## 2. Architecture & Stack

- **Runtime**: Python 3.12+ (managed via `uv` toolchain)
- **Code Quality**:
  - **Linter & Formatter**: Ruff
  - **Unit Testing**: Pytest
- **Hooks & CI**:
  - Pre-commit framework
  - GitHub Actions (Ubuntu environment)

---

## 3. API / Data Contracts

### 3.1 GPG Commit Signature Checker CLI
- **Path**: `src/gpg_verify.py`
- **Command-line Interface**:
  ```bash
  python3 src/gpg_verify.py [--rev-range <REV_RANGE>] [--verbose]
  ```
  - `--rev-range`: Git revision range to verify (e.g. `origin/master..HEAD`). If omitted, defaults to verifying the single commit `HEAD`.
  - `--verbose`: Print status details for each commit checked, including stdout/stderr from `git verify-commit`.

#### Return Codes
- `0`: Success. All analyzed commits are correctly signed with a valid GPG signature.
- `1`: Failure. One or more commits lack a valid signature or fail verification.
- `2`: Error. Execution environment issues (e.g., directory is not a Git repo) or invalid arguments.

---

## 4. Feature Checklist

- [x] **MVP (Must-Have)**
  - [x] **Commit Signatures Script**: Implement `src/gpg_verify.py` using `git verify-commit` via subprocess.
  - [x] **Unit Tests**: Implement comprehensive test suite in `tests/test_gpg_verify.py` using `pytest` and mock subprocesses.
  - [x] **Python Packaging**: Configure `pyproject.toml` containing dependency groups and metadata.
  - [x] **Pre-Commit Hooks**: Configure `.pre-commit-config.yaml` to run `ruff`, `gpg-verify`, and tests.
  - [x] **GitHub Actions Workflow**: Configure `.github/workflows/ci.yml` targeting pulls and pushes, running linting, verification, and tests.

- [x] **V1 (Should-Have)**
  - [x] **Validation of Git Repository**: Gracefully fail with code 2 if checked outside a Git worktree.

- [ ] **Future (Nice-to-Have)**
  - [ ] **GPG Key Ring Verification**: Add parameter to enforce GPG signature validity against a specific list of public key fingerprints.

---

## 5. Validation Criteria

- **Unit Testing Verification**:
  ```bash
  uv run pytest
  ```
  All tests must pass.
- **Linter & Formatter Validation**:
  ```bash
  uv run ruff check src/ tests/
  uv run ruff format --check src/ tests/
  ```
- **Local Hook Verification**:
  ```bash
  pre-commit run --all-files --hook-stage manual
  ```
- **CI/CD Run**: Github Action runs all steps successfully on pushed commits.
