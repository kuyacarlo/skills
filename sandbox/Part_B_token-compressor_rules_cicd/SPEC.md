# Specification: Token Compressor

This specification defines the requirements, architecture, API, and test scenarios for the `token-compressor` Python utility and its CI/CD verification workflows.

---

## 1. Requirements

### 1.1 Functional Requirements
- **Waffle / Filler Stripper**: Identify and remove conversational greetings, pleasantries, sign-offs, and framing sentences.
- **Shorthand Replacer**: Map verbose technical phrases into standard developers' shorthand (e.g. "constant time complexity" -> "O(1)").
- **Action Tuples Converter**: Convert edit descriptions into `[File Path] -> [Action]: [Rationale]` syntax.
- **Code Block Compactor**: Condense markdown code blocks by truncating long unchanged parts and adding line-range comments.
- **CLI Interface**: Accept input via file path or standard input, returning compressed content to standard output.
- **Configuration-driven**: Allow level customization (`lite`, `full`, `ultra`).

### 1.2 Non-Functional Requirements
- **Performance**: Compress inputs under 100ms.
- **Safety**: Ensure code blocks and important technical terms are not corrupted.
- **CI/CD & Code Quality**:
  - GPG signature checks on commits.
  - Linting and formatting via Ruff.
  - Automated tests via Pytest.

---

## 2. API & CLI Design

### 2.1 Python API
The utility exposes the following interfaces under the `token_compressor` package:

```python
def compress(text: str, level: str = "full") -> str:
    """Compresses the input text based on the compression level."""
    ...
```

### 2.2 CLI Usage
```bash
# Compress standard input
echo "Sure, I can help. In config.json, update the port to 8080 to fix conflict." | python3 -m token_compressor.cli

# Compress a file
python3 -m token_compressor.cli input.md --level ultra --output output.md
```

---

## 3. CI/CD & GPG Configuration

### 3.1 Pre-Commit Hooks
Pre-commit checks will verify:
- Code quality & style: Python linting and formatting via `ruff`.
- File validation: YAML validation for config files.
- Local GPG Check: Verifies that commit signing (`commit.gpgsign = true`) is configured in the local git repository.

### 3.2 GitHub Actions
The `ci.yml` workflow will:
- Check out code and set up Python.
- Install dependencies (ruff, pytest).
- Run linter (`ruff check`) and formatter check (`ruff format --check`).
- Run GPG Signature verification on all commits in the push/PR range.
- Execute unit tests using `pytest`.

---

## 4. Test Scenarios
- **Scenario 1 (Waffle Stripping)**: Validate that greeting and sign-off templates are cleanly removed.
- **Scenario 2 (Shorthand Mapping)**: Validate conversion of time complexities and typical developer terms.
- **Scenario 3 (Action Tuples)**: Parse "In src/main.py, add error handling to prevent crash." to `src/main.py -> add error handling: prevent crash`.
- **Scenario 4 (Code Blocks)**: Truncate code blocks that exceed 15 lines without modifications.
- **Scenario 5 (CLI Integration)**: Test piping input and output file generation.
