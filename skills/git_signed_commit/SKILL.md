---
name: git-signed-commit
description: Guide to configuring Git repositories with custom git-profiles, GPG signatures, sign-offs, and custom SSH hostnames.
---

# 🔑 Git Signed-Off GPG Commits & SSH Hostname Configuration

This skill provides step-by-step instructions on how to set up local Git repositories for GPG-signed commits, apply custom Git profiles, sign off changes, and route Git push traffic through specific SSH configurations.

---

## 📋 Steps & Instructions

### 1. Apply a Git Profile via `git-profile`
Use the custom `git-profile` utility to configure the local repository's user details:
```bash
# List available profiles
git-profile list

# Apply the profile to the current repository (e.g. kuya-carlo)
git-profile use kuya-carlo
```
This automatically configures local Git attributes:
- `user.name`
- `user.email`
- `user.signingkey` (used for GPG signatures)

---

### 2. Configure GPG Commit Signing
Ensure GPG commit signing is enabled locally in the repository so that every commit is signed:
```bash
git config --local commit.gpgsign true
```

---

### 3. Exclude Regenerated Datasets and Build Files
Ensure that all temporary data files, databases, or environment variables are excluded from the repository. Modify `.gitignore` to add:
```gitignore
# Virtual environments
.venv

# Generated database and datasets
hackathons.db
*.json
*.csv
gallery.html
```

---

### 4. Configure Git SSH Hostname Alias
Check `~/.ssh/config` for custom hosts (e.g., `Host kuyacarlo.github.com`).
When setting up Git remotes, replace the default `github.com` domain with the custom SSH host alias:
```bash
# Add or set remote URL
git remote set-url origin git@kuyacarlo.github.com:username/repository.git
```
This ensures Git uses the correct SSH key file associated with that profile instead of the default key.

---

### 5. Commit with GPG Sign and Signed-Off Trailers
Create a commit passing both `-S` (GPG sign) and `-s` (Signed-off-by):
```bash
git commit -S -s -m "feat: your commit message"
```

---

### 6. Verification
To verify the GPG signature and Signed-off-by trailer in the latest commit:
```bash
git log --show-signature -n 1
```
