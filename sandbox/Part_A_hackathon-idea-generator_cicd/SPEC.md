# 🛠️ Project Specification: GPG Commit Signature Checker & CI

## 1. Overview & Core Goal
This project provides a lightweight command-line tool `gpg_verify.py` to audit and verify GPG signatures of Git commits. It integrates into local workflows via `pre-commit` and is enforced in CI/CD using GitHub Actions, ensuring that only verified, signed commits are pushed or merged.

The primary target users are developers and repository maintainers seeking to enforce commit integrity.

---

## 2. Architecture & Stack
- **Language**: Python 3.14+
- **External Dependencies (Runtime)**: None (uses Python standard library exclusively to align with YAGNI guidelines).
- **Development & Testing Tools**:
  - `pytest`: For running unit tests.
  - `ruff`: For linting and formatting.
  - `pre-commit`: To orchestrate local git hooks.
  - `uv`: Package and tool runner.
- **CI Platform**: GitHub Actions

---

## 3. API / Data Contracts
The CLI tool `src/gpg_verify.py` behaves as follows:

### CLI Signature
```bash
python src/gpg_verify.py [--rev-range REV_RANGE] [--verbose]
```

### Options
- `--rev-range`: The revision range to check (e.g. `HEAD~1..HEAD` or `origin/main..HEAD`). If omitted, defaults to checking only the `HEAD` commit.
- `--verbose`: Prints verification details and key IDs for each checked commit.

### Exit Codes
- `0`: Success. All commits in the range have valid GPG signatures.
- `1`: Failure. One or more commits in the range are unsigned or have invalid signatures.
- `2`: Error. Invalid arguments, not a Git repository, or other environment issues.

---

## 4. Feature Checklist
- [x] **MVP (Must-Have)**
  - [x] Implement `src/gpg_verify.py` core functionality to invoke `git verify-commit` on a range of commits.
  - [x] Parse CLI arguments (`--rev-range`, `--verbose`).
  - [x] Write unit tests for `gpg_verify.py` mocking `subprocess.run` to cover various git outputs and exit codes.
  - [x] Configure `.pre-commit-config.yaml` to run `ruff check`, `ruff format`, unit tests, and GPG signature checks.
  - [x] Create `.github/workflows/ci.yml` to lint, format, run tests, and check commit GPG signatures in GitHub Actions.

- [x] **V1 (Should-Have)**
  - [x] Automatic fallback to checking only commits in the current branch against target branch if running in GitHub Actions.

- [ ] **Future (Nice-to-Have)**
  - [ ] Support checking specific files or tags.

---

## 5. Validation Criteria
### Automated Verification
1. **Linting**:
   ```bash
   uv run --with ruff ruff check src/ tests/
   ```
2. **Formatting**:
   ```bash
   uv run --with ruff ruff format --check src/ tests/
   ```
3. **Unit Tests**:
   ```bash
   uv run pytest
   ```
4. **Integration/GPG Verification**:
   ```bash
   python src/gpg_verify.py --rev-range HEAD~1..HEAD
   ```
   Must exit with 0 on verified commits, and non-zero on unsigned commits.
