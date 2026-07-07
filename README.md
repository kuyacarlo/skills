# ⚙️ Antigravity Customizations: Rules & Skills

This repository stores and version-controls your personal configurations, instructions, and custom skills for the Antigravity agentic coding assistant.

---

## 🎯 Rationale

This project structure is designed around three core principles:

1. Have a proper backup method for all of the skills I built and use frequently.
2. Have it be deployed to Linux/macOS host with no prerequisite and through a single command.

---

## 🚀 Quick Start (How to Use)

To load and enable these customizations on your current machine:

1. Open your terminal inside this repository folder.
2. Run the interactive installer:
   ```bash
   ./apply
   ```
3. The installer scans all available skills in the `skills/` directory, lists them in your terminal, and lets you select which ones to activate:
   * **Toggle a skill**: Enter the corresponding list number.
   * **Select all / none**: Enter `a` or `n`.
   * **Apply & Confirm**: Press `Enter` (or enter `y`).
   * **Quit**: Enter `q`.

The installer script will:
* Copy your workspace rules (**[AGENTS.md](file:///home/kaoru/projects/skills/AGENTS.md)**) to your local agent configuration directory (`~/.agents/AGENTS.md`).
* Copy the selected skill folders directly into **`~/.agents/skills/`**, enabling the agent to automatically discover and load them. (This also cleans up any old `skills.json` or symlinks from previous configurations).

---

## 🛠️ Skills

Use this guide to decide which skills to select during installation:

### 1. [idea-consultant](file:///home/kaoru/projects/skills/skills/idea-consultant/SKILL.md)
*   **Idea sanitizer**: Grills options against alternatives, calculates Go/No-Go/Pivot viability, and records decisions in ZenNotes.

### 2. [thinking-partner](file:///home/kaoru/projects/skills/skills/thinking-partner/SKILL.md)
*   **Research partner**: Documents thoughts, diagrams architectures via Mermaid, and outputs habit-inducing dopamine/friction task matrices.

### 3. [momentum-engine](file:///home/kaoru/projects/skills/skills/momentum-engine/SKILL.md)
*   **ADHD developer crutch**: Monitors focus states objectively, bypasses choice paralysis by forcing tech choices, and logs reconnect steps.

### 4. [hackathon-idea-generator](file:///home/kaoru/projects/skills/skills/hackathon-idea-generator/SKILL.md)
*   **Hackathon factory**: Parses briefs, scores ideas, sets up parallelized team effort sheets, and exports to Google Docs. *(Adapted from kuya-carlo/marketdev).*

### 5. [code-yagni](file:///home/kaoru/projects/skills/skills/code-yagni/SKILL.md)
*   **YAGNI checker**: Applies the 6-tier Decision Ladder to prune over-engineered blocks and traces `yagni:` debt tags. *(Adapted from DietrichGebert/ponytail).*

### 6. [token-compressor](file:///home/kaoru/projects/skills/skills/token-compressor/SKILL.md)
*   **Caveman compressor**: Strips polite conversational waffle to produce high-density responses and compact code diffs. *(Adapted from JuliusBrussee/caveman).*

### 7. [spec-builder](file:///home/kaoru/projects/skills/skills/spec-builder/SKILL.md)
*   **Spec keeper**: Governs projects with `SPEC.md` contracts, detects implementation drift, and reviews API gaps. *(Adapted from JuliusBrussee/cavekit & github/spec-kit).*
