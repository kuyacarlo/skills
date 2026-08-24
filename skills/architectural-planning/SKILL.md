---
name: architectural-planning
author: kaoru
version: "1.0.0"
description: "Research and architectural planning partner. Generates Mermaid architecture flowcharts, milestone timelines, and task matrices with activation energy scoring. Supports general thought logs, technical research summaries, project roadmaps, system design diagrams, database schemas, and data flow visualizations. Helps overcome execution friction with strategy suggestions."
---

# Architectural Planning

Use this skill for thinking support, technical research, architecture designs,
roadmaps, or structured planning.

---

## Workflow

### Step 1: Classify the Input

Determine if the request is a **General Thought Log** or a **Project Plan /
Roadmap**:

- **General Thought Log** — Quick answers, research summaries, or transient
  brainstorms.
- **Project Plan / Roadmap** — Long-term technical specs, architecture designs,
  milestones, or structured task lists for a specific project.

### Step 2: Perform the Thinking / Planning

Generate the content requested.

### Step 3: Format and Deliver

#### Path A: General Thought Log

Format with: Title, Date, Trigger, and Content.

Output in chat unless a target path is specified.

#### Path B: Project Plan / Roadmap

Before building the roadmap, search for and parse the project's `README.md` to
extract folders, setup commands, and stack dependencies.

Required structure:

1. **Title** — `# Project Plan: [Project Name]`

2. **Context Block**:
   ```markdown
   > **Date**: YYYY-MM-DD
   > **Local Repository**: /path/to/repo
   > **Remote**: https://... (if linked)
   > **Status**: GO / Plan to Build (GO Probability: % - summary)
   ```

3. **Architecture Flow** — Embed a Mermaid flowchart illustrating how modules,
   services, databases, user interfaces, and authentication layers interlock.
   Example structure:
   ```mermaid
   graph TD
     A[Client] --> B[API Gateway]
     B --> C[Auth Service]
     B --> D[Core Service]
     D --> E[(Database)]
   ```

4. **Task Matrix** — Group execution tasks into a table with columns:
   | Component / Task | Est. Hours | Activation Energy (1-10) | Yield (1-10) | Strategy |
   |------------------|-----------|--------------------------|--------------|----------|
   - *Activation Energy*: Ease of start. 1 = high friction/boilerplate setup,
     10 = low friction/easy start.
   - *Yield*: Satisfaction level / immediate value delivered.
   - *Strategy*: Practical progress approach (temptation bundling, micro-tasks,
     immediate reward, etc.).

5. **Milestones and Tasks** — Checkbox task lists (`- [ ]`) grouped by timeline
   target milestones for active tracking.

---

## Output Rules

1. Output all plans, research summaries, and matrices directly in the chat
   unless a target path is specified.
2. When a target path is provided, write the file there.
3. Link key scripts or files using relative paths where possible.
