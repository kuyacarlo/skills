---
name: architectural-planning
description: Research and architectural planning partner. Auto-generates Mermaid architecture flowcharts, milestones, and task matrices. Defaults to outputting in the chat.
---

# Architectural Planning Skill

Use this skill when you need thinking support, technical research, architecture designs, roadmaps, or structured planning.

---

## 🚀 Workflow

### Step 1: Classify the Input
Determine if the requested thinking is a **General Thought Log** or a **Project Plan / Roadmap**:
*   **General Thought Log**: Quick answers, research summaries, or transient brainstorms.
*   **Project Plan / Roadmap**: Long-term technical specs, architecture designs, milestones, or structured task lists for a specific project.

### Step 2: Perform the Thinking / Planning
Generate the content requested.

### Step 3: Detect Storage Location & Save

#### Path A: General Thought Log
1.  **Storage**:
    *   Check user context or connected MCP servers to see if note-taking tools or personal vaults are connected. If so, create the note under a thoughts directory (e.g., `thoughts/Thought Log YYYY-MM-DD.md`).
    *   Otherwise, default to outputting directly in the chat.
2.  **Format**: Include Title, Date, Trigger, and Content.

#### Path B: Project Plan / Roadmap (Context Preservation & Execution Strategy)
To prevent context loss and execution friction:
1.  **Storage**:
    *   Check user context or connected MCP servers to see if note-taking tools or personal vaults are connected. If so, create a dedicated note under a project subpath (e.g., `projects/[Project-Name].md`).
    *   Otherwise, save to `projects/[Project-Name]/README.md` in the workspace or default to outputting directly in the chat.
2.  **Required Structure**:
    *   **H1 Title**: `# 🚀 Project Plan: [Project Name]`
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
    *   **⚙️ Architecture Flow**: Embed a Mermaid flowchart illustrating how modules, services, databases, user interfaces, and authentication layers interlock.
    *   **⚡ Task Matrix**: Group the execution tasks into a table with the following columns:
        *   *Component / Task*: Title and path of files to be created/edited.
        *   *Est. Hours*: Estimated effort.
        *   *Activation Energy (1-10)*: Ease of start (1 = high initial friction/boilerplate setup, 10 = low friction/easy to start).
        *   *Yield (1-10)*: Satisfaction level / immediate value.
        *   *Strategy*: Suggest a practical progress strategy (e.g., temptation bundling, breaking down into micro-tasks, immediate reward).
    *   **📅 Milestones & Tasks**: Use checkbox task lists (`- [ ]`) grouped by timeline target milestones to facilitate active tracking.

### Step 4: Default Output Behavior
By default, all plans, research summaries, and matrices should be outputted directly in the chat, creating a markdown artifact only when necessary (in lieu of chat). If note-taking tools or vaults are detected, sync them automatically.
