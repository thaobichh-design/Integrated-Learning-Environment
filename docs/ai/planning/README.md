---
phase: planning
title: Effective Execution Matrix (The 4-Iteration Roadmap)
description: Strict prioritization and sequencing of tasks to manage failure risks efficiently & scalably, moving from Concept to Leadership. Single source of truth: Master Scope Mapping.
---

# 1. THE ITERATIVE ROADMAP (Macro Prioritization)
*Goal: Sequence the engineering effort to manage risk. Do not build Scalability (Iteration 4) before proving Desirability (Iteration 1).*

* **Iteration 1: Concept (Validate the Wrapper & Verb):** Prove the User actually wants this (Desirability) and that the core action solves the root blocker.
* **Iteration 2: Working Prototype (Validate the Core & Sustainability):** Prove the Effective Core is technically feasible, secure, and deterministic.
* **Iteration 3: Minimum Viable Enablement / MVE (Validate Efficiency):** Fuse the Wrapper and Core. Ensure the SOP is fast, automated, and frugal.
* **Iteration 4: Enablement Leadership (Validate Scalability):** Fortify the system to handle volume, edge cases, and modular growth.

## 1.2 Master Scope Mapping
*Goal: One single source of truth for which Acceptance Criterion (from Requirements) is tackled in which Iteration. Must be MECE — each A.C. appears exactly once.*

*Typically: Iteration 1 → Verb A.C.; Iteration 2 → Sustainability (Adverb/Adjective); Iteration 3 → Efficiency; Iteration 4 → Scalability. Use the standardized A.C. IDs from Requirements Phase 3 (see naming convention there).*

**Status legend:** ⚪ Pending · 🔴 To Do / In Progress · 🔵 Draft Completed (by the Agent) · 🟢 Reviewed/Tested (by the User) · 🟠 Stuck (off-ramp when blocked). *Task flow: Pending → To Do → Draft Completed → Reviewed/Tested. All tasks must be reviewed and approved by the User before marking Reviewed/Tested (last node for solo User projects).* When syncing to company board: map To Do → TODO/READY TO DO, Draft Completed → DRAFT COMPLETED, Reviewed/Tested → REVIEWED/TESTED, Stuck → STUCK. To unblock 🟠 Stuck: User resolves (decision, resource, or dependency), then move the task back to 🔴 To Do.

| Target A.C. (from Req) | Targeted Iteration | Deterministic Evidence of Completion | Status |
| :--- | :--- | :--- | :--- |
| Verb-AC1 | Iteration 1 | [e.g. CLI log / Screenshot] | 🔴 |
| Verb-AC2 | Iteration 1 | [e.g. User flow screenshot] | 🔴 |
| SustainAdv-AC1 | Iteration 2 | [e.g. Security / audit log] | ⚪ |
| ScalAdj-AC1 | Iteration 4 | [e.g. Load test report] | ⚪ |

*Populate from Requirements Phase 3 (Verb, Adverb, Noun, Adjective A.C.). Do not invent A.C. here.*

---

# 2. EXECUTION MATRIX (Micro Sequencing)
*Tasks are derived from the Master Scope Mapping above. Implementation details (how to build) come from Design (Component Mapping, Data Models). Do not invent new scope here. Add task rows as needed per iteration.*

## 2.2 Iteration Sequencing

### ITERATION 1: CONCEPT
*Focus: Desirable Wrapper & Core Verb Validation.*

**Active A.C. in Scope:** [List only A.C. IDs from Master Scope Mapping above, e.g. Verb-AC1, Verb-AC2]

| ID | Task (Verb) | Risk Validated | Deps | Status |
| :--- | :--- | :--- | :--- | :--- |
| **T-101** | [Task Name] | Desirability / Hook | None | 🔴 To Do |
| **T-102** | [Task Name] | UDO Resolution | T-101 | 🔴 To Do |

### ITERATION 2: WORKING PROTOTYPE
*Focus: Effective Core & Sustainability.*

**Active A.C. in Scope:** [List only A.C. IDs from Master Scope Mapping above]

| ID | Task (Verb) | Risk Validated | Deps | Status |
| :--- | :--- | :--- | :--- | :--- |
| **T-201** | [Task Name] | Technical Feasibility | T-102 | ⚪ Pending |

### ITERATION 3: MINIMUM VIABLE ENABLEMENT (MVE)
*Focus: Fuse Wrapper & Core; Efficiency.*

**Active A.C. in Scope:** [List only A.C. IDs from Master Scope Mapping above]

| ID | Task (Verb) | Risk Validated | Deps | Status |
| :--- | :--- | :--- | :--- | :--- |
| **T-301** | [Task Name] | Usability / Friction | T-201 | ⚪ Pending |

### ITERATION 4: ENABLEMENT LEADERSHIP
*Focus: Scalability, volume, edge cases, modular growth.*

**Active A.C. in Scope:** [List only A.C. IDs from Master Scope Mapping above]

| ID | Task (Verb) | Risk Validated | Deps | Status |
| :--- | :--- | :--- | :--- | :--- |
| **T-401** | [Task Name] | Concurrency / Volume | T-301 | ⚪ Pending |

---

# 3. RESOURCE & BUDGET TRACKER
*Monitor constraints mapped to the Efficiency Adjectives. Update Hard Limit after User approval per Design §4 (Requesting Resources/Budget).*

| Metric | Current Usage | Hard Limit | Status |
| :--- | :--- | :--- | :--- |
| **Financial Cost (OpEx)** | $0.00 | $[Limit] | 🟢 Safe |
| **API/Token/Compute Usage** | 0 | [Limit] | 🟢 Safe |
