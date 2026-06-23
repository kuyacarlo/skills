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
*   **Purpose**: Validates and refines software/app ideas before coding.
*   **Categorization**:
    *   **GO (`[TODO]`)** ➔ Stored in `ideas/ok/` (High stack alignment, low friction, high yield).
    *   **NO-GO (`[X]`)** ➔ Stored in `ideas/cancelled/` (Redundant, high friction, or high run cost).
    *   **PIVOT (`[?]`)** ➔ Stored in `ideas/reassess/` (Tech is viable, but needs a redirect or OS contribution).
*   **What Happens**:
    *   Grills you on alternatives and scopes features (MVP vs. V1).
    *   Generates a 7-factor quantitative scoring matrix and narrative story.
    *   Prepends a status block below the H1 title using templates: **[verdict-go.md](file:///home/kaoru/projects/skills/skills/idea-consultant/resources/templates/verdict-go.md)**, **[verdict-nogo.md](file:///home/kaoru/projects/skills/skills/idea-consultant/resources/templates/verdict-nogo.md)**, or **[verdict-pivot.md](file:///home/kaoru/projects/skills/skills/idea-consultant/resources/templates/verdict-pivot.md)**.
    *   Defaults to creating new notes with **[idea-template.md](file:///home/kaoru/projects/skills/skills/idea-consultant/resources/templates/idea-template.md)**. Offers to add ZenNotes-optimized **[idea-dump.md](file:///home/kaoru/projects/skills/skills/idea-consultant/resources/templates/idea-dump.md)** to your vault templates if ZenNotes is active.

### 2. [thinking-partner](file:///home/kaoru/projects/skills/skills/thinking-partner/SKILL.md)
*   **Purpose**: Logs technical plans, architecture, and general research.
*   **Categorization**:
    *   **General Thought Log** ➔ Stored in `thoughts/Thought Log YYYY-MM-DD HHMM.md`.
    *   **Project Plan / Roadmap** ➔ Stored in `projects/[project-name].md`.
*   **What Happens**:
    *   **Context Preservation**: Injects conversation history logs (ID, Date, Repository Links) at the top.
    *   **Architecture Flow**: Renders a Mermaid flowchart showing inter-module data flow.
    *   **⚡ Task Matrix**: Builds an Atomic Habits matrix mapping file paths, estimated hours, activation energy (1-10), dopamine yield (1-10), and habit loop strategies (Temptation Bundling, rewards) to kickstart your work friction-free.

### 3. [momentum-engine](file:///home/kaoru/projects/skills/skills/momentum-engine/SKILL.md)
*   **Purpose**: ADHD-optimized executive function crutch that prevents analysis paralysis, challenges unrealistic ideas, and restores context.
*   **Categorization**: Adapts behavior dynamically across three workflow states:
    *   **Prepping / Ingestion** ➔ Challenges ideas via `idea-consultant` to cut losses fast.
    *   **Coding / One-Shotting** ➔ Enforces standard `MarketDev` execution steps to build the MVP with zero-prompt/minimal interaction.
    *   **Vibe-Shifting** ➔ Updates and reads your ZenNotes index (`ideas/Project Index.md`) to jump between homelab, web dev, and cybersecurity.
*   **What Happens**:
    *   **State Diagnostics**: Monitors conversation pivots to gauge focus/energy state objectively.
    *   **Action Driver**: Cuts loops by forcing stack decisions based on lowest activation energy.
    *   **Cold-Start Reconnect Block**: Automatically appends a resume log with the last file line, next git command, and a <2min micro-step at the end of every session.


