---
phase: planning
title: LTC Integrated Learning Environment — 4-Iteration Roadmap
description: Execution matrix for the ILE. State A Sub-Step 4.
feature: integrated-learning-environment
---

# 1. THE ITERATIVE ROADMAP (Macro Prioritization)
*Goal: Sequence the engineering effort to manage risk. Do not build Scalability (Iteration 4) before proving Desirability (Iteration 1).*

* **Iteration 1: Concept (Validate the Wrapper & Verb):** Prove the User wants the ILE (learn-and-capture in one environment) and that the core action solves the root blocker (no chat→docs handoff). Validate desirability of phase → entry point → template → conversation flow.
* **Iteration 2: Working Prototype (Validate the Core & Sustainability):** Prove the Effective Core is feasible: persistent memory + real-time Markdown update + template loading. Prove structure is deterministic (Learning Book hierarchy, templates).
* **Iteration 3: Minimum Viable Enablement / MVE (Validate Efficiency):** Fuse Wrapper and Core. Full SOP in one workspace; zero-friction capture; progress persisted; Subject Roadmap (A) surfaced and entry points informed by level.
* **Iteration 4: Enablement Leadership (Validate Scalability):** COE map representation; user→ClickUp mapping; sync to company space; configurable hierarchy/templates/space for reuse (other ClickUp spaces, other template sets).

---

# 2. EXECUTION MATRIX (Micro Sequencing)
*Tasks pulled from Requirements and Design. One task per row; execute in order within iteration; State B runs one task at a time with User approval.*

## ITERATION 1: CONCEPT
*Focus: Validate Verb (learn-and-capture) and Desirable Wrapper (one workspace, phase → entry → template → conversation).*

### Iteration 1 — Exact Verb & Adverb A.C. in scope

| Grammar | Acceptance criteria in scope for I1 | Deferred to later iteration |
|--------|-------------------------------------|-----------------------------|
| **Verb** (learn-and-capture) | **V1** User can start/resume a learning session for a chosen subject (COE → Area → Chapter → Topic) in one workspace. **V2** User can choose phase (A/B/C) and see a list of entry points from the Learning Map for that phase (informed by A where available). **V3** User can select an entry point and have the correct template (questions × components) loaded and scoped to that entry. | V4 (Agent grounded in memory + doc) → I2. V5 (Markdown reflects conversation, no manual paste) → I2. |
| **Adverb** | **S1** (Sustainability – Deterministically): Document structure (COE → Area → Chapter → Topic and phases A/B/C, components) is clearly defined and consistent; the same path always resolves to the same logical place. | S2, S3 → I2. Efficiency (E1–E3) and Scalability (X1–X4) → I3/I4. |

### How we know they are met after I1 execution

| A.C. | Evidence of completion |
|------|-------------------------|
| **V1** | A written flow/spec states: "User starts or resumes in one workspace by choosing COE → Area → Chapter → Topic"; Founder confirms this is the desired behaviour. Optional: one example path (e.g. COE Effectiveness → Chapter 9 → Topic 1) is documented and resolvable to a folder path. |
| **V2** | A written flow/spec states: "User chooses phase A or B or C; system presents a list of entry points for that phase (from Learning Map; informed by Subject Roadmap A where available)." T-102 delivers at least one stub list of entry points for one phase so the wrapper is tangible; Founder confirms. |
| **V3** | T-102 delivers one stub template (questions × components) and the rule "selecting entry point X loads template Y"; Founder can see the template and confirm it is the desired shape. |
| **S1** | T-102 creates a minimal Learning Book folder structure (A., B. Captured, B. Organised Knowledge, D., E.) for one COE Area; the same path (e.g. `{Book root}/A. Subject Roadmap/`) is defined and exists. A one-line checklist or script can verify the expected folders exist. |
| **I1 gate** | T-103: Founder explicitly confirms "One workspace (chat + Markdown) with no manual paste solves my root blocker" and approves moving to Iteration 2. |

| ID | Task (Verb) | Target Grammar (From Requirements) | Risk Validated | Deps | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **T-101** | Define and document the minimal ILE flow in the current IDE (phase A/B/C → entry points → template load → conversation → doc update) and confirm with User that this is the desired wrapper. | **Verb:** Learn-and-capture (V1, V2, V3) | Desirability / Hook | None | 🔴 To Do |
| **T-102** | Create a minimal Learning Book folder structure for one COE Area (A. Subject Roadmap, B. Captured, B. Organised Knowledge, D. Distilled, E. Expressed Expertise) and one stub template (e.g. one questions×components table) so the wrapper is tangible. | **Verb:** V1, V3; **Adverb:** S1 | UDO Resolution / One workspace | T-101 | 🔴 To Do |
| **T-103** | Validate with User: "One workspace (chat + Markdown) with no manual paste" solves the root blocker; approve moving to Iteration 2. | **Verb:** Learn-and-capture | UDO Resolution | T-102 | 🔴 To Do |

## ITERATION 2: WORKING PROTOTYPE
*Focus: Effective Core — persistent memory, real-time Markdown update, template loading; Sustainability (structure-faithful, deterministic).*
| ID | Task (Verb) | Target Grammar (From Requirements) | Risk Validated | Deps | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **T-201** | Wire persistent memory (e.g. MCP @ai-devkit/memory or equivalent) so the Agent can store/recall context tied to the current subject/Learning Book. | **Noun:** N2 (Persistent memory); **Sustainability:** Deterministically | Technical Feasibility | T-103 | 🔴 To Do |
| **T-202** | Implement Agent read/write of one Learning Book Markdown file from conversation (e.g. one section updated as byproduct of one Q&A); document the mapping rule (conversation → file/section). | **Noun:** N4; **Sustainability:** S2, S3; **Adjective:** A-S1 | Technical Feasibility | T-201 | 🔴 To Do |
| **T-203** | Implement loading of one canonical template (questions × components) when user selects an entry point; scope conversation/document context to that entry. | **Noun:** N3; **Adjective:** A-S2 | Technical Feasibility | T-202 | 🔴 To Do |
| **T-204** | Add a single check (e.g. script or manual step) that the repo still matches the expected Learning Book structure after updates. | **Adjective:** A-S3 | Sustainability | T-203 | 🔴 To Do |

## ITERATION 3: MINIMUM VIABLE ENABLEMENT (MVE)
*Focus: Full SOP in one workspace; zero-friction capture; progress persisted; Subject Roadmap (A) as UDO anchor.*
| ID | Task (Verb) | Target Grammar (From Requirements) | Risk Validated | Deps | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **T-301** | Implement phase choice (A. Capture | B. Organise | C. Distill) and present entry points from the Learning Map for the chosen phase; entry points informed by Subject Roadmap (A) / current level where A is available. | **Verb:** V2; **Noun:** N5, N9 | Efficiency / Usability | T-204 | 🔴 To Do |
| **T-302** | Ensure updates to Markdown occur as a byproduct of the conversation (no separate copy-paste); user can switch entry point or phase without losing in-progress context (retain or commit draft). | **Adverb:** E3; **Adjective:** A-E1, A-E2, A-E3 | Zero-friction capture | T-301 | 🔴 To Do |
| **T-303** | Surface the user's current mastery level and relevant Subject Roadmap (A) content (e.g. level requirements, next-step recommendations) so the user can respect level-appropriate progression. | **Noun:** N9; **SOP step 6** | UDO Anchor | T-302 | 🔴 To Do |

## ITERATION 4: ENABLEMENT LEADERSHIP
*Focus: COE map; user→ClickUp mapping; sync to company space; configurable for other spaces/templates.*
| ID | Task (Verb) | Target Grammar (From Requirements) | Risk Validated | Deps | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **T-401** | Define and implement the ILE's representation of the LTC COE hierarchical map (COE → Chapter → Topic → Topic Members' Learning Area → each member's Personal Learning Area). | **Noun:** N6 | Scalability | T-303 | 🔴 To Do |
| **T-402** | Implement mapping of a single user's learning to that user's respective location on ClickUp (correct Topic → that user's Personal Learning Area). | **Noun:** N7; **Adverb:** X4 | Scalability | T-401 | 🔴 To Do |
| **T-403** | Implement (or stub and document) sync of the user's Book (local or Google Drive) to the company's ClickUp in the correct place using the COE map and user mapping. | **Noun:** N8 | Scalability | T-402 | 🔴 To Do |
| **T-404** | Make hierarchy, templates, and ClickUp space mapping configurable (e.g. per workspace or mode) so the ILE pattern can be applied to other ClickUp spaces and different doc template sets. | **Adjective:** A-X4; **Design §1.3** | Reusability | T-403 | 🔴 To Do |

---

# 3. RESOURCE & BUDGET TRACKER
*Monitor constraints mapped to the Efficiency Adjectives.*
| Metric | Current Usage | Hard Limit | Status |
| :--- | :--- | :--- | :--- |
| **Financial Cost (OpEx)** | $0.00 | TBD | 🟢 Safe |
| **API/Token/Compute Usage** | 0 | TBD | 🟢 Safe |

---

*Last updated: State A Sub-Step 4 approved. Ready for State B: execute one task at a time with `/state-b`.*
