---
name: thinking-partner
description: Research partner. Auto-generates Mermaid architecture flowcharts and habit-dopamine task matrices.
---

# Thinking Partner Skill

Use this skill when the user asks for thinking support, research, plans, or questions like "what to do" or "what to know".

## 🚀 Workflow

### Step 1: Classify the Input
Determine if the requested thinking is a **General Thought Log** or a **Project Plan / Roadmap**:
*   **General Thought Log**: Quick answers, research summaries, or transient brainstorms.
*   **Project Plan / Roadmap**: Long-term technical specs, architecture designs, milestones, or structured task lists for a specific project.

### Step 2: Perform the Thinking / Planning
Generate the content requested by the user.

### Step 3: Detect Storage Location & Save
#### Path A: General Thought Log
1.  **Storage**:
    *   *MCP*: Create note under `thoughts/` (e.g., `thoughts/Thought Log YYYY-MM-DD HHMM.md`).
    *   *Local Fallback*: Write to `notes/thought_log_YYYY-MM-DD_HHMM.md`.
2.  **Format**: Include Title, Date, Trigger, and Content.

#### Path B: Project Plan / Roadmap (Context Preservation & Atomic Habits Execution)
To prevent the user from losing context, forgetting gold ideas, or experiencing execution friction:
1.  **Storage**:
    *   *MCP*: Create a dedicated note under a project subpath (e.g., `projects/[Project-Name].md` or `projects/ok/[Project-Name].md`).
    *   *Local Fallback*: Write to `projects/[Project-Name]/README.md` in the workspace.
2.  **Required Structure**:
    *   **H1 Title**: `# [TODO] 🛡️ [Project Name]` (or `# 🚀 Project Plan: [Project Name]`)
    *   **Context Preservation Block**:
        ```markdown
        > [!IMPORTANT]
        > **Conversation ID**: `[Active Conversation ID]` (Use this to search history/transcripts)
        > **Date**: YYYY-MM-DD
        > **Local Repository**: [[Path label]](file:///absolute/path/to/repo) (If local repo exists)
        > **GitHub Remote**: [[Remote label]](https://github.com/owner/repo) (If remote repo is linked)
        > **Status**: GO / Plan to Build (GO Probability: % - Narrative summary)
        ```
    *   **Repository Ingestion**: Before building the roadmap, search for and parse the project's local `README.md` to extract precise folders, setup commands, and stack dependencies. Link key scripts or files using absolute clickable file links (`file:///...`).
    *   **⚙️ Architecture Flow**: Embed a Mermaid flowchart illustrating how CLI modules, backend services, databases, web UI, and authentication layers interlock.
    *   **⚡ Atomic Habits Task Matrix**: Group the execution tasks into a table with the following columns:
        *   *Component / Task*: Title and path of files to be created/edited.
        *   *Est. Hours*: Estimated effort.
        *   *Activation Energy (1-10)*: Ease of start (1 = high initial friction/boilerplate setup, 10 = low friction/easy to start).
        *   *Dopamine Yield (1-10)*: Satisfaction level (1 = invisible backend config, 10 = high visual/interactive win).
        *   *Habit Loop / Strategy*: Suggest a practical atomic habit strategy:
            *   *Temptation Bundling*: Pairing a dry setup task with a high-dopamine element (favorite music, coffee).
            *   *Make it Easy / Friction Reduction*: Mocking complex APIs first, using starter templates, or breaking the task down into a tiny 5-minute action to cross the starting line.
            *   *Immediate Reward*: Granting a short break or celebration reward immediately upon completion.
    *   **📅 Milestones & Tasks**: Use checkbox task lists (`- [ ]`) grouped by timeline target milestones to facilitate active tracking.

---

## 💬 Conversation Starters & Prompts
*   *"I've logged this project roadmap to projects/[Project]/README.md and linked it to Conversation ID [ID] so you can easily reference our chat context later."*
*   *"Saved this general research log to thoughts/Thought Log..."*
