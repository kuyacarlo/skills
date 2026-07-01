# 📊 Multi-Domain Skill Tree Test Matrix (Part A Baseline)

This document contains a 2D matrix view of unit test results and rule compliance for the initial baseline evaluation (Part A: Single Skill Isolation, No Rules).

---

## 🟢 Unit Test Matrix

| Configuration | Android | CI/CD | CLI (Go) | Desktop | Hardware (ESP32) | Web (React) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **`code-yagni`** | 🟢 Passed | 🟢 Passed | 🟢 Passed | 🔴 Failed | 🟢 Passed | 🟢 Passed |
| **`token-compressor`** | 🟢 Passed | 🟢 Passed | 🟢 Passed | 🔴 Failed | 🟢 Passed | 🔴 Failed |
| **`spec-builder`** | ➖ Excluded | ➖ Excluded | 🟢 Passed | ➖ Excluded | ➖ Excluded | 🟢 Passed |
| **`hackathon-idea-generator`** | ➖ Excluded | ➖ Excluded | 🟢 Passed | ➖ Excluded | ➖ Excluded | 🟢 Passed |

> [NOTE]
> *   **🔴 Desktop failures:** Primarily caused by virtual framebuffer requirements for PyQt GUI suites not being pre-configured in the run environment.
> *   **🔴 Web token-compressor failure:** The compressor model did not run the package compilation steps, choosing instead to output minimum boilerplate to reduce token counts.
> *   **➖ Excluded:** Skipped in the queue for new skills (`spec-builder` and `hackathon-idea-generator`) to protect your daily Gemini API quota.

---

## 🛡️ Rule Compliance Matrix

Tracks whether the model followed workspace guidelines (Podman defaults, Bluetooth Classic audio profile, inline PCB trays) in the absence of active workspace rules:

| Configuration | Android | CI/CD | CLI (Go) | Desktop | Hardware (ESP32) | Web (React) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **`code-yagni`** | ✓ Compliant | ✓ Compliant | ✓ Compliant | ✓ Compliant | ⚠️ **Violated** *(used BLE)* | ✓ Compliant |
| **`token-compressor`** | ✓ Compliant | ✓ Compliant | ✓ Compliant | ✓ Compliant | ⚠️ **Violated** *(used BLE)* | ✓ Compliant |
| **`spec-builder`** | ➖ Excluded | ➖ Excluded | ✓ Compliant | ➖ Excluded | ➖ Excluded | ✓ Compliant |
| **`hackathon-idea-generator`** | ➖ Excluded | ➖ Excluded | ✓ Compliant | ➖ Excluded | ➖ Excluded | ✓ Compliant |

> [IMPORTANT]
> The **hardware rule violations** serve as a critical validation control. Because `AGENTS.md` was disabled in Part A, the models were blind to physical audio/casing guidelines, resulting in non-compliant specifications. This highlights the absolute necessity of workspace-level rules for embedded hardware enforcement.
