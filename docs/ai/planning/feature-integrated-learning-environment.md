---
phase: planning
title: LTC Integrated Learning Environment — 4-Iteration Roadmap
description: Execution matrix for the ILE. Single source of truth: Master Scope Mapping. Aligned with template 1.1.0.
feature: integrated-learning-environment
---

# 1. THE ITERATIVE ROADMAP (Macro Prioritization)
*Goal: Sequence the engineering effort to manage risk. Do not build Scalability (Iteration 4) before proving Desirability (Iteration 1).*

* **Iteration 1: Concept (Validate the Wrapper & Verb):** Prove the User wants the ILE (learn-and-capture in one environment) and that the core action solves the root blocker (no chat→docs handoff). Validate desirability of phase → entry point → template → conversation flow.
* **Iteration 2: Working Prototype (Validate the Core & Sustainability):** Prove the Effective Core is feasible: persistent memory + real-time Markdown update + template loading. Prove structure is deterministic (Learning Book hierarchy, templates).
* **Iteration 3: Minimum Viable Enablement / MVE (Validate Efficiency):** Fuse Wrapper and Core. Full SOP in one workspace; zero-friction capture; progress persisted; Subject Roadmap (A) surfaced and entry points informed by level.
* **Iteration 4: Enablement Leadership (Validate Scalability):** COE map representation; user→ClickUp mapping; sync to company space; configurable hierarchy/templates/space for reuse (other ClickUp spaces, other template sets).

## 1.2 Master Scope Mapping
*Goal: One single source of truth for which Acceptance Criterion (from Requirements) is tackled in which Iteration. Must be MECE — each A.C. appears exactly once.*

**Status legend:** ⚪ Pending · 🔴 To Do / In Progress · 🔵 Draft Completed (by the Agent) · 🟢 Reviewed/Tested (by the User) · 🟠 Stuck (off-ramp when blocked). *Task flow: Pending → To Do → Draft Completed → Reviewed/Tested. All tasks must be reviewed and approved by the User before marking Reviewed/Tested.*

### Table A — By iteration (what’s in scope per iteration)

| Iteration | A.C. IDs in scope |
| :--- | :--- |
| **1** | Verb-AC1, Verb-AC2, Verb-AC3, SustainAdv-AC1 |
| **2** | Verb-AC4, Verb-AC5, SustainAdv-AC2, SustainAdv-AC3, Noun-AC1, Noun-AC2, Noun-AC3, Noun-AC4, Noun-AC5, SustainAdj-AC1, SustainAdj-AC2, SustainAdj-AC3 |
| **3** | EffAdv-AC1, EffAdv-AC2, EffAdv-AC3, EffAdj-AC1, EffAdj-AC2, EffAdj-AC3, Noun-AC9 |
| **4** | ScalAdv-AC1, ScalAdv-AC2, ScalAdv-AC3, ScalAdv-AC4, Noun-AC6, Noun-AC7, Noun-AC8, ScalAdj-AC1, ScalAdj-AC2, ScalAdj-AC3, ScalAdj-AC4 |

*Use this table to see at a glance which A.C. are tackled in each iteration. For requirement text, evidence, and status, use Table B.*

### Table B — By A.C. (detail: requirement, iteration, evidence, status)

*One row per A.C. ID. Traceability: A.C. ID matches `docs/ai/requirements/feature-integrated-learning-environment.md` Phase 3.*

| A.C. ID | Requirement (from Req Phase 3) | Iter | Deterministic Evidence | Status |
| :--- | :--- | :---: | :--- | :---: |
| Verb-AC1 | User can start or resume a learning session for a chosen subject (COE → Area → Chapter → Topic) in one workspace. | 1 | `docs/ai/implementation/ile-minimal-flow.md`; User confirms. | 🟢 |
| Verb-AC2 | User can choose phase (A/B/C) and see entry points from Learning Map for that phase (informed by Subject Roadmap A). | 1 | `learning-book-tree-map.md` + `entry-point-to-template-mapping.md`; User confirms. | 🟢 |
| Verb-AC3 | User can select an entry point and have the correct template (questions × components) loaded and scoped to that entry. | 1 | `templates/0-overview-and-summary.md` + `entry-point-to-template-mapping.md`; User confirms. | 🟢 |
| SustainAdv-AC1 | Document structure (COE → Area → Chapter → Topic, phases A/B/C, components) defined and consistent; same path → same logical place. | 1 | `learning-book/COE_DS/` + `scripts/check-learning-book-structure.sh`; User confirms. | 🟢 |
| Verb-AC4 | User can conduct dialogue with the Agent; Agent's responses grounded in persistent memory and current document context. | 2 | Persistent memory wired; Agent uses memory + doc context. | ⚪ |
| Verb-AC5 | After a learning conversation, structural Markdown file(s) reflect new or updated content (no manual paste required). | 2 | Agent read/write of Learning Book from conversation; mapping rule documented. | ⚪ |
| SustainAdv-AC2 | Updates from conversation map to a known template (questions × components); mapping rule is explicit. | 2 | Mapping rule (conversation → file/section) documented and used. | ⚪ |
| SustainAdv-AC3 | User or Agent can point to the exact file(s) and section(s) created or updated for a given exchange. | 2 | Agent can point to exact file/section; or user can inspect. | ⚪ |
| Noun-AC1 | One workspace supports both "conversation" and "structural document" (chat + Markdown repo); user does not switch app to edit Learning Book. | 2 | Same workspace used for chat and Markdown. | ⚪ |
| Noun-AC2 | Persistent memory (e.g. MCP) available to Agent, tied to current subject/Learning Book; context preserved across sessions. | 2 | MCP or equivalent wired; context tied to subject/Book. | ⚪ |
| Noun-AC3 | When user selects phase and entry point, correct template is loaded and conversation/document context scoped to that entry. | 2 | Template loading implemented; context scoped to entry. | ⚪ |
| Noun-AC4 | Agent can read and write structural Markdown for current subject so conversation outcomes written into correct files/sections as byproduct. | 2 | Agent read/write of Markdown from conversation implemented. | ⚪ |
| Noun-AC5 | Entry points presented from Learning Map, informed by Subject Roadmap (A) (current level L1–L7); level-appropriate progression suggested. | 2 | Entry points derived from Learning Map; A used where available. | ⚪ |
| SustainAdj-AC1 | All writes to Learning Book conform to hierarchy (COE → Area → Chapter → Topic) and phase structure (A/B/C). | 2 | Writes conform; hierarchy and phase structure enforced or checked. | ⚪ |
| SustainAdj-AC2 | Template loading uses canonical component set (Overview, UBS, UDS, EPS, UES, EOP) and question set; no ad hoc structure. | 2 | Canonical template set used; no ad hoc structure. | ⚪ |
| SustainAdj-AC3 | User can verify (inspection or check command) that repo still matches expected structure after updates. | 2 | Check script or manual step added; structure verifiable. | ⚪ |
| EffAdv-AC1 | User can open a session, pick one entry point, complete or partially complete it, and close; progress is persisted. | 3 | Progress persisted; session can be closed and resumed. | ⚪ |
| EffAdv-AC2 | User can resume later without re-entering context; persistent memory and document state sufficient to continue. | 3 | Resume uses memory + document state; no re-entry of context. | ⚪ |
| EffAdv-AC3 | No mandatory "export" or "sync" step for local/Drive Book updates; updates to Markdown occur as byproduct of conversation. | 3 | Updates occur as byproduct; no separate export/sync step. | ⚪ |
| EffAdj-AC1 | No separate "copy from chat and paste into doc" step required for content to appear in structural Markdown. | 3 | Content appears in Markdown as byproduct of conversation. | ⚪ |
| EffAdj-AC2 | Updates to document triggered by conversation (Agent writes or user confirms); mechanism defined and repeatable. | 3 | Trigger and mechanism documented and repeatable. | ⚪ |
| EffAdj-AC3 | User can switch entry point or phase without losing in-progress context for current entry (draft retained or committed before switch). | 3 | Context retained or committed on switch; no loss of draft. | ⚪ |
| Noun-AC9 | ILE can surface user's current mastery level and relevant Subject Roadmap (A) content so user can respect level-appropriate progression. | 3 | Current level and A content visible; entry points informed by A. | ⚪ |
| ScalAdv-AC1 | Same SOP (phase → entry points → template load → conversation → doc update) applies to any subject within Learning Book structure. | 4 | SOP applies to any subject; flow unchanged. | ⚪ |
| ScalAdv-AC2 | Adding a new subject (new Area/Chapter/Topic or new Learning Book) does not require changing core flow; only content and entry points change. | 4 | New subject = new content/entry points; core flow unchanged. | ⚪ |
| ScalAdv-AC3 | System can reference Subject Roadmap (A) and Learning Map so entry points and templates scale with L1–L7 progression. | 4 | A and Learning Map referenced; scaling with L1–L7. | ⚪ |
| ScalAdv-AC4 | Sync from user's Book (local or Google Drive) to company's ClickUp respects COE map and places content in user's respective location. | 4 | Sync to ClickUp implemented or stubbed; COE map and user location respected. | ⚪ |
| Noun-AC6 | ILE has a defined representation of LTC COE hierarchical map (COE → Chapter → Topic → Topic Members' Learning Area → each member's Personal Learning Area). | 4 | COE map representation defined and implemented. | ⚪ |
| Noun-AC7 | ILE can map a single user's learning to that user's respective location on ClickUp (correct Topic → that user's Personal Learning Area). | 4 | User→ClickUp location mapping implemented. | ⚪ |
| Noun-AC8 | ILE supports (or will support) syncing user's learning from their Book to company's ClickUp in correct place (COE and User mapping). | 4 | Sync to ClickUp implemented or stubbed; correct place per COE/User mapping. | ⚪ |
| ScalAdj-AC1 | New subjects reuse same Learning Book template (A. Subject Roadmap, B. Captured, B. Organised Knowledge, D. Distilled, E. Expressed Expertise). | 4 | Template reused for new subjects. | ⚪ |
| ScalAdj-AC2 | New entry points or templates can be added via configuration or defined structure without changing core integration (chat + memory + doc). | 4 | Configurable entry points/templates; core integration unchanged. | ⚪ |
| ScalAdj-AC3 | Optional future capabilities (e.g. Audio Overview, Infographics, Quiz) can be added without breaking core flow. | 4 | Optional capabilities addable without breaking flow. | ⚪ |
| ScalAdj-AC4 | ILE pattern can be applied to other ClickUp spaces and different doc template sets; hierarchy, templates, space mapping configurable. | 4 | Hierarchy, templates, ClickUp space mapping configurable (e.g. per workspace or mode). | ⚪ |

*Populated from Requirements Phase 3. Use Table A to see scope per iteration; use Table B to trace each A.C. to its requirement and evidence.*

---

# 2. EXECUTION MATRIX (Micro Sequencing)
*Tasks are derived from the Master Scope Mapping above. Implementation details (how to build) come from Design. Do not invent new scope here.*

## 2.2 Iteration Sequencing

### ITERATION 1: CONCEPT
*Focus: Desirable Wrapper & Core Verb Validation.*

**Active A.C. in Scope:** Verb-AC1, Verb-AC2, Verb-AC3, SustainAdv-AC1

| ID | Task (Verb) | Risk Validated | Deps | Status |
| :--- | :--- | :--- | :--- | :--- |
| **T-101** | Define and document the minimal ILE flow in the current IDE (phase A/B/C → entry points → template load → conversation → doc update) and confirm with User that this is the desired wrapper. | Desirability / Hook | None | 🟢 Reviewed/Tested |
| **T-102** | Create a minimal Learning Book folder structure for one COE Area (A. Subject Roadmap, B. Captured, B. Organised Knowledge, D. Distilled, E. Expressed Expertise) and one stub template (e.g. one questions×components table) so the wrapper is tangible. | UDO Resolution / One workspace | T-101 | 🟢 Reviewed/Tested |
| **T-103** | Validate with User: "One workspace (chat + Markdown) with no manual paste" solves the root blocker; approve moving to Iteration 2. | UDO Resolution | T-102 | 🟢 Reviewed/Tested |

### ITERATION 2: WORKING PROTOTYPE
*Focus: Effective Core & Sustainability.*

**Active A.C. in Scope:** Verb-AC4, Verb-AC5, SustainAdv-AC2, SustainAdv-AC3, Noun-AC1..AC5, SustainAdj-AC1..AC3

| ID | Task (Verb) | Risk Validated | Deps | Status |
| :--- | :--- | :--- | :--- | :--- |
| **T-201** | Wire persistent memory (e.g. MCP @ai-devkit/memory or equivalent) so the Agent can store/recall context tied to the current subject/Learning Book. | Technical Feasibility | T-103 | 🔴 To Do |
| **T-202** | Implement Agent read/write of one Learning Book Markdown file from conversation (e.g. one section updated as byproduct of one Q&A); document the mapping rule (conversation → file/section). | Technical Feasibility | T-201 | 🔴 To Do |
| **T-203** | Implement loading of one canonical template (questions × components) when user selects an entry point; scope conversation/document context to that entry. | Technical Feasibility | T-202 | 🔴 To Do |
| **T-204** | Add a single check (e.g. script or manual step) that the repo still matches the expected Learning Book structure after updates. | Sustainability | T-203 | 🔴 To Do |

### ITERATION 3: MINIMUM VIABLE ENABLEMENT (MVE)
*Focus: Fuse Wrapper & Core; Efficiency.*

**Active A.C. in Scope:** EffAdv-AC1..AC3, EffAdj-AC1..AC3, Noun-AC9

| ID | Task (Verb) | Risk Validated | Deps | Status |
| :--- | :--- | :--- | :--- | :--- |
| **T-301** | Implement phase choice (A. Capture \| B. Organise \| C. Distill) and present entry points from the Learning Map for the chosen phase; entry points informed by Subject Roadmap (A) / current level where A is available. | Efficiency / Usability | T-204 | 🔴 To Do |
| **T-302** | Ensure updates to Markdown occur as a byproduct of the conversation (no separate copy-paste); user can switch entry point or phase without losing in-progress context (retain or commit draft). | Zero-friction capture | T-301 | 🔴 To Do |
| **T-303** | Surface the user's current mastery level and relevant Subject Roadmap (A) content (e.g. level requirements, next-step recommendations) so the user can respect level-appropriate progression. | UDO Anchor | T-302 | 🔴 To Do |

### ITERATION 4: ENABLEMENT LEADERSHIP
*Focus: Scalability, COE map, ClickUp mapping, sync, configurable.*

**Active A.C. in Scope:** ScalAdv-AC1..AC4, Noun-AC6..AC8, ScalAdj-AC1..AC4

| ID | Task (Verb) | Risk Validated | Deps | Status |
| :--- | :--- | :--- | :--- | :--- |
| **T-401** | Define and implement the ILE's representation of the LTC COE hierarchical map (COE → Chapter → Topic → Topic Members' Learning Area → each member's Personal Learning Area). | Scalability | T-303 | 🔴 To Do |
| **T-402** | Implement mapping of a single user's learning to that user's respective location on ClickUp (correct Topic → that user's Personal Learning Area). | Scalability | T-401 | 🔴 To Do |
| **T-403** | Implement (or stub and document) sync of the user's Book (local or Google Drive) to the company's ClickUp in the correct place using the COE map and user mapping. | Scalability | T-402 | 🔴 To Do |
| **T-404** | Make hierarchy, templates, and ClickUp space mapping configurable (e.g. per workspace or mode) so the ILE pattern can be applied to other ClickUp spaces and different doc template sets. | Reusability | T-403 | 🔴 To Do |

---

# 3. RESOURCE & BUDGET TRACKER
*Monitor constraints mapped to the Efficiency Adjectives. Update Hard Limit after User approval per Design §4 (Requesting Resources/Budget).*

| Metric | Current Usage | Hard Limit | Status |
| :--- | :--- | :--- | :--- |
| **Financial Cost (OpEx)** | $0.00 | TBD | 🟢 Safe |
| **API/Token/Compute Usage** | 0 | TBD | 🟢 Safe |

---

*Last updated: Aligned with template 1.1.0. Ready for State B: execute one task at a time with `/state-b`.*
