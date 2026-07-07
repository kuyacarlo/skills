# 🛠️ Workspace Rules

These guidelines apply to all project scoping, roadmaps, and code generation within this workspace.

---

## 🗃️ Homelab & Container Deployments
*   **Container Engine**: Assume **Podman** is the default container runtime instead of Docker.
*   **Tracking Buckets**: Categorize and design container setups using the following 3-bucket system:
    *   `~c`: Podman/Docker Compose files.
    *   `~s`: systemd service files for compose configurations (autostart) and beyond.
    *   `~q`: Native Podman **Quadlet** container units (`.container` and `.volume` systemd files).

---

## 🔌 Embedded Systems & Hardware Prototyping
*   **Wireless Audio Compatibility**: For music/audio projects, default to **Bluetooth Classic (A2DP)** rather than BLE/LE Audio to ensure maximum compatibility with standard consumer headphones. Prefer the original ESP32-WROVER-E (with PSRAM) to handle buffering.
*   **Cylindrical Footprints (e.g., NW-S20x style)**:
    *   Avoid vertical component stacking (Sandwich layouts) as they exceed physical thickness budgets.
    *   Default to **Inline layouts** (positioning the PCB and flat batteries lengthwise).
    *   Incorporate a **sliding internal tray** and threaded screw-cap closure to guarantee clean modular assembly and easy manual repair.

---

## 💻 Codebase & Styling Standards
*   **Styling**: Use **TailwindCSS** for styling to maintain developer simplicity. Do not force raw CSS unless explicitly requested.
*   **Scoping & Implementation**: Target the full defined project scope, but prioritize simple, understandable code. Pragmatic shortcuts are acceptable as long as code readability is maintained.
*   **Comments & Documentation**: Keep comments as a high-level supplement rather than verbose line-by-line annotations. Aim for approximately one clear comment per functional block (e.g., explaining "this part does x, does y") to avoid code noise.
*   **Comment Integrity**: Proactively preserve pre-existing comments and docstrings in edited files.

---

## 🧭 Specification Pipeline & Automations Flow
*   **Automatic Workflow Chaining**: When executing any specification pipeline phase or related workspace task planning:
    1.  **Constitution Check**: Check for `.specify/memory/constitution.md` (or the templates) first. Read it, present a 1-2 sentence gist of it to the user, ask for any overrides/improvements, and ensure the task conforms to it.
    2.  **Task Context & Outline**: Outlines the task/problem context before writing any files.
    3.  **Phase Transitions**: Automatically chain the subsequent phases (`specify` → `clarify` → `plan` → `implement`) without stopping to wait for slash commands, using sensible defaults to resolve minor ambiguities, unless a major design fork requires an explicit user choice.


