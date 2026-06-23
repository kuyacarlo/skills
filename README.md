# ⚙️ Antigravity Customizations: Rules & Skills

This repository stores and version-controls your personal configurations, instructions, and custom skills for the Antigravity agentic coding assistant.

---

## 🚀 Quick Start (Apply Customizations)

To load and enable customizations on your current machine:

1. Run the interactive installer:
   ```bash
   ./apply
   ```
2. The installer will scan all skills in the `skills/` directory, present a list in the terminal, and let you select which ones to activate:
   * **Toggle a skill**: Enter the corresponding list number.
   * **Select all / none**: Enter `a` or `n`.
   * **Apply & Confirm**: Press `Enter` (or enter `y`).
   * **Quit**: Enter `q`.

This registers the active skills under your `~/.agents/skills.json` and symlinks your workspace rules (`AGENTS.md`) without fragile directory symlinks.

---

## 📁 Repository Structure

```
├── skills/
│   ├── idea-consultant/   # Refine & evaluate project ideas
│   │   ├── SKILL.md       # Core grilling and verdict logic
│   │   └── resources/
│   │       └── templates/
│   │           └── idea-dump.md  # Standard template for raw idea ingestion
│   └── thinking-partner/  # Dedicated research and log writer
│       └── SKILL.md
├── AGENTS.md              # Workspace-wide system rules & constraints
├── apply                  # Interactive installer shell script
└── README.md              # Project documentation
```

---

## 🛠️ Development & Updates
Since this repository uses a dependency-free shell script, you don't need compilation tools or Go. Any changes you make to the skills or rules files inside this directory are immediately active (via symlinks and direct file references). You only need to run `./apply` again if you add new skill directories or want to toggle specific skills.
