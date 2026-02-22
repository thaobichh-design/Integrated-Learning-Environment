---
phase: requirements
title: LTC Integrated Learning Environment — Requirements
description: Causal map and system design for the Integrated Agentic Learning Workspace. State A Sub-Step 1 & 2 approved.
feature: integrated-learning-environment
---

# PHASE 1: PROBLEM DISCOVERY (The User's System Map)
*Goal: Understand the human reality before introducing technology.*

* **User Persona & Anti-Persona:** Solo learner / User mastering new domains (L1–L7 SFIA) using the LTC Advanced Effective Learning Framework. Anti-persona: passive consumer who does not write their own learning book.
* **Ultimate Desired Outcome (UDO):** The User reaches biological mastery (from L1 to L7 SFIA) of a new domain, with deterministic proof generated automatically in the form of a strictly structured Markdown repository (B. Capture Facts & Data → C. Organise Information → D. Distill Understanding). **The Subject Roadmap (A) is the UDO anchor:** it defines the target mastery levels, requirements, and recommended progression (L1→L7) per subject. Learning that respects A is level-appropriate and sequenced; learning that ignores A tends to be scattered (e.g. jumping to L4 content while still at L1/L2/L3).
* **User's Action:** Learn via hierarchical questioning and active recall, while the structural Learning Book (Markdown) is updated in real time as a byproduct of the conversation—no manual extract/format/paste. The user is encouraged to respect the Subject Roadmap (A) so progression is deliberate, not ad hoc.

## The Drivers (UDS - Ultimate Driving System)
* **UDS:** The User's drive to master new domains rapidly using the LTC Advanced Effective Learning Framework.
* **UDS.UD (Driver of the Driver):** Deep, hierarchical questioning and active recall that force knowledge to be organised structurally from high-level concepts down to deep-root layers.
* **UDS.UB (Blocker of the Driver):** Linear, chronological AI chat interfaces that suffer from context collapse, breaking the hierarchical structure and forcing the user to repeat context.

## The Blockers (UBS - Ultimate Blocking System)
* **UBS:** The massive administrative tax (energy and friction) required to manually extract, format, and copy-paste fragmented knowledge (e.g. from Gemini chat on web into ClickUp docs using Advanced Effective Learning Templates).
* **UBS.UD (Driver of the Blocker):** The physical separation between the "Learning Environment" (chat) and the "Documentation Environment" (ClickUp/Markdown).
* **UBS.UB (Blocker of the Blocker):** An Integrated Agentic Learning Workspace where the AI shares persistent memory with a local Markdown file, updating the structural document in real time as a natural byproduct of the learning conversation.

---

# PHASE 2: THE SYSTEM DESIGN (Context & Bridge)
*Goal: Define the conceptual solution space based ONLY on what we understand about the User in Phase 1.*

* **Principles (Why):**
  * **Hierarchy over chronology:** Knowledge is organised top-down (high-level → deep layers); flat chat-only streams are not the source of truth.
  * **Active recall and deep questioning:** The system supports Socratic, hierarchical Q&A so the user is forced to structure knowledge, not just consume it.
  * **Single persistent context:** One shared context (AI memory + document) so the user does not repeat themselves and structure is preserved.
  * **Documentation as byproduct:** Structural Markdown is updated in real time from the learning conversation; no separate "export" or copy-paste step.
  * **One environment:** Learning and documentation happen in the same place; no handoff from "chat" to "docs."
  * **You are the author:** The learner is the best teacher for themselves; the AI (and others) are references. The user writes their own book per subject, continuously from L1 to L7.
  * **Consumption in-scope, digestion out-of-scope:** The system supports consumption (capture, organise, distill with the Agent). Digestion (reflection, internalisation) is explicitly outside the system.
  * **Subject Roadmap (A) as UDO anchor:** The user's learning path and the system's presentation of entry points should be informed by the user's current mastery level and the Subject Roadmap (A). Respecting A (level-appropriate progression L1→L7) prevents scattered learning; the ILE should surface A, suggest level-aligned entry points, and let the user choose while making the "right" path visible.

* **Environment (Where):** Digital, local-first. Primary artifact: a Markdown repository (Learning Book) on the user's machine. Structure: LTC COE → Areas of Expertise (Effectiveness, Data Science, WellBeing, Business Excellence, Investment, Technology, Leadership, …) → Chapters → Topics. Per subject: A. Subject Roadmap & Level Specifications (SFIA L1–L7); B. Capture Facts & Data; C. Organise Information (components: 0. Overview, 1. UBS, 2. UDS, 3. EPS, 4. UES, 5. EOP, …); D. Distill Understanding; E. Express Expertise. Primary interfaces: Cursor Chat and/or AntiGravity; optional later: NotebookLM-like capabilities (Audio Overview, Infographics, Quiz) with the constraint that the system must allow exploration outside given sources.

* **Tools (What):**
  * *Desirable Wrapper:* The experience of a learning conversation (natural dialogue, hierarchical Q&A, active recall) where notes are never lost, stay structured, and the user does not do manual admin. The user chooses which phase (A/B/C) and which entry point to work on; the Agent assists within that structure.
  * *Effective Core:* The mechanism that (a) keeps persistent memory shared with the document, (b) updates the structural Markdown in real time from the conversation, (c) respects Capture → Organise → Distill and the Learning Book template (e.g. L1–L7 SFIA), (d) loads the correct template when the user picks an entry point (table: headers = questions, rows = components, cells = answers), (e) uses the Learning Map to present entry points per phase.

* **SOP (How):**
  1. **Start a new area of expertise:** User selects COE → Area of Expertise → Chapter → Topic (or creates a new subject). System resolves or creates the Learning Book for that subject.
  2. **Phase and entry point:** Agent asks which phase (B. Capture Facts & Data | C. Organise Information | D. Distill Understanding) and presents a relevant list of entry points from the Learning Map for that phase. **Entry points are informed by the Subject Roadmap (A):** the user's current level (L1–L7) and A's recommended requirements/sources are used to prioritise or suggest level-appropriate entry points, so the user can respect A and avoid scattered learning. User can still choose any entry point.
  3. **Load template:** User selects an entry point; Agent loads the corresponding template (table: headers = questions, rows = components, cells = answers). Conversation and document context are scoped to that entry.
  4. **Conduct learning conversation:** User and Agent work through the template; Agent updates the structural document in real time as a byproduct; user can switch entry point or phase at any time.
  5. **Optional: Distill:** When the user chooses Phase D (Distill), Agent helps condense Organise Information into the Distill Understanding format (on demand).
  6. **Progress and roadmap:** The Markdown repo accumulates the Learning Book as deterministic proof. **Subject Roadmap (A) is the UDO anchor:** it is used to assess growth (SFIA L1–L7), identify gaps, and plan next steps. The user is encouraged to consult A and to respect level-appropriate progression so learning stays on track.
  7. **Digestion:** Consumption (steps 1–6) is in-scope. Digestion (reflection, practice, internalisation) is outside the system.

---

# PHASE 3: THE FORMALIZATION (The Output)
*State A Sub-Step 3 approved. Deterministic User's Requirements.*

**A.C. ID naming convention (use across Requirements, Design, and Planning):** Short, stable IDs so Planning can reference exactly one A.C. per row. Format: `{Grammar}-AC{n}`. Grammar prefixes: **Verb**, **SustainAdv**, **EffAdv**, **ScalAdv**, **Noun**, **SustainAdj**, **EffAdj**, **ScalAdj**. Do not rename once used in Planning.

---

## 1. USER(S)

* **Primary User Persona:** Solo learner / User mastering new domains (L1–L7 SFIA) using the LTC Advanced Effective Learning Framework, who writes their own Learning Book (Capture → Organise → Distill) in a strictly structured Markdown repository. Learns via hierarchical questioning and active recall; wants the structural document updated in real time from the conversation. May sync learning to the company's ClickUp space.
* **Anti-Persona:** Passive consumer who does not author their own learning book; or someone satisfied with manual copy-paste from chat into a separate docs tool and who does not need an integrated learning + documentation environment.

## 2. DESIRED USER ACTION(S)

**Verb:** *Learn-and-capture* — Conduct a learning conversation (hierarchical Q&A, active recall) in one environment with the structural Learning Book (Markdown) updated in real time as a byproduct; no separate export or copy-paste step.

| A.C. ID | Acceptance Criteria |
| :--- | :--- |
| Verb-AC1 | User can start or resume a learning session for a chosen subject (COE → Area → Chapter → Topic) in one workspace. |
| Verb-AC2 | User can choose phase (B. Capture Facts & Data \| C. Organise Information \| D. Distill Understanding) and see a list of entry points from the Learning Map for that phase; entry points are informed by the user's current level and Subject Roadmap (A) so level-appropriate options are visible. |
| Verb-AC3 | User can select an entry point and have the correct template (e.g. table: questions × components) loaded and scoped to that entry. |
| Verb-AC4 | User can conduct dialogue with the Agent; the Agent's responses are grounded in persistent memory and the current document context. |
| Verb-AC5 | After a learning conversation, the corresponding structural Markdown file(s) reflect the new or updated content (no manual paste required). |

**Adverbs (Effectiveness Outcomes)**

* **Sustainability Adverb:** *Deterministically* — Learning Book structure and updates are reproducible and traceable.

| A.C. ID | Acceptance Criteria |
| :--- | :--- |
| SustainAdv-AC1 | Document structure at LTC Company level and User's personal level (COE → Area → Chapter → Topic and phases A/B/C, components) is clearly defined and consistent; the same path always resolves to the same logical place. |
| SustainAdv-AC2 | Updates from conversation map to a known template (e.g. questions × components); the mapping rule is explicit. |
| SustainAdv-AC3 | User or Agent can point to the exact file(s) and section(s) created or updated for a given exchange. |

* **Efficiency Adverb:** *Incrementally* — User can do small, focused sessions without redoing prior work.

| A.C. ID | Acceptance Criteria |
| :--- | :--- |
| EffAdv-AC1 | User can open a session, pick one entry point, complete or partially complete it, and close; progress is persisted. |
| EffAdv-AC2 | User can resume later without re-entering context; persistent memory and document state are sufficient to continue. |
| EffAdv-AC3 | No mandatory "export" or "sync" step for local/Drive Book updates; updates to Markdown occur as a byproduct of the conversation (within session or defined sync rule). |

* **Scalability Adverb:** *Repeatedly* — Same flow works across subjects and over the L1–L7 journey.

| A.C. ID | Acceptance Criteria |
| :--- | :--- |
| ScalAdv-AC1 | The same SOP (phase choice → entry points → template load → conversation → doc update) applies to any subject within the Learning Book structure. |
| ScalAdv-AC2 | Adding a new subject (new Area/Chapter/Topic or new Learning Book) does not require changing the core flow; only content and entry points change. |
| ScalAdv-AC3 | The system can reference Subject Roadmap (A) and Learning Map so entry points and templates scale with L1–L7 progression; A acts as the UDO anchor so the user can respect level-appropriate learning. |
| ScalAdv-AC4 | Sync from the user's Book (local or Google Drive) to the company's ClickUp respects the COE map and places content in the user's respective location (Topic → that user's Personal Learning Area). |

## 3. FEATURE

**Noun:** *ILE (Integrated Learning Environment)* — The IDE (or later OpenClaw) equipped with the **Master Effective Learning Template** and the integration (persistent memory, real-time structural Markdown, phase/entry-point/template loading, Learning Map). The template + integration is what makes the IDE an ILE. **Scope:** One Learning Book per COE Area. Each Book is stored **locally** or in the **company's Google Drive**; when using Drive, folder structure matches the existing ClickUp COE Area spaces.

| A.C. ID | Acceptance Criteria |
| :--- | :--- |
| Noun-AC1 | One workspace supports both "conversation" and "structural document" (e.g. chat + Markdown repo); the user does not switch to another app to edit the Learning Book. |
| Noun-AC2 | Persistent memory (e.g. MCP or equivalent) is available to the Agent and is tied to the current subject/Learning Book so context is preserved across sessions. |
| Noun-AC3 | When the user selects phase and entry point, the correct template (e.g. table with questions × components) is loaded and conversation/document context is scoped to that entry. |
| Noun-AC4 | The Agent can read and write the structural Markdown for the current subject so that conversation outcomes are written into the correct files/sections as a byproduct. |
| Noun-AC5 | Entry points presented to the user are derived from the Learning Map and **informed by Subject Roadmap (A)** (user's current level L1–L7, recommended requirements/sources) so level-appropriate progression is suggested; user can still choose any entry point. |
| Noun-AC6 | The ILE has a defined representation of the **LTC COE hierarchical map** (COE → Chapter → Topic → Topic Members' Learning Area → each member's Personal Learning Area). |
| Noun-AC7 | The ILE can **map a single user's learning** to **that user's respective location on ClickUp** (correct Topic → that user's Personal Learning Area within the Chapter/Topic Members' Learning Area). |
| Noun-AC8 | The ILE supports (or will support) **syncing** the user's learning (from their Book) **to the company's ClickUp** in the correct place, using the LTC ClickUp Space for COE and User mapping. |
| Noun-AC9 | The ILE can **surface the user's current mastery level** and the relevant **Subject Roadmap (A)** content (e.g. level requirements, recommended sources) so the user can consciously respect level-appropriate progression and avoid scattered learning. |

**Adjectives (Attributes of the Noun)**

* **Sustainability Adjective:** *Structure-faithful* — The workspace preserves the Learning Book structure and does not corrupt or bypass it.

| A.C. ID | Acceptance Criteria |
| :--- | :--- |
| SustainAdj-AC1 | All writes to the Learning Book conform to the defined hierarchy (COE → Area → Chapter → Topic) and phase structure (A/B/C). |
| SustainAdj-AC2 | Template loading uses the canonical component set (e.g. Overview, UBS, UDS, EPS, UES, EOP) and question set; no ad hoc structure is introduced without definition. |
| SustainAdj-AC3 | User can verify (e.g. by inspection or a single check command) that the repo still matches the expected structure after updates. |

* **Efficiency Adjective:** *Zero-friction capture* — No extra steps for "saving" or "exporting" from chat to doc.

| A.C. ID | Acceptance Criteria |
| :--- | :--- |
| EffAdj-AC1 | No separate "copy from chat and paste into doc" step is required for content to appear in the structural Markdown. |
| EffAdj-AC2 | Updates to the document are triggered by the conversation (e.g. Agent writes, or user confirms a write); the mechanism is defined and repeatable. |
| EffAdj-AC3 | User can switch entry point or phase without losing in-progress context for the current entry (e.g. draft is retained or committed to the doc before switch). |

* **Scalability Adjective:** *Template-driven* — New subjects and levels use the same template and flow; sync respects company COE map.

| A.C. ID | Acceptance Criteria |
| :--- | :--- |
| ScalAdj-AC1 | New subjects reuse the same Learning Book template (A. Subject Roadmap, B. Capture Facts & Data, C. Organise Information, D. Distill Understanding, E. Express Expertise). |
| ScalAdj-AC2 | New entry points or templates (e.g. new component types) can be added via configuration or defined structure without changing the core integration (chat + memory + doc). |
| ScalAdj-AC3 | Optional future capabilities (e.g. Audio Overview, Infographics, Quiz) can be added without breaking the core flow of phase → entry point → template → conversation → doc update. |
| ScalAdj-AC4 | **Reusability:** The ILE pattern (Capture, Organise, Distill with AI Agent; template-driven; sync to a defined location) can later be applied to **other ClickUp spaces** (not only COE) and **different doc template sets**. Hierarchy, templates, and space mapping are **configurable** so the same setup can drive other use cases (e.g. project spaces, sales, operations) with their own templates and ClickUp structure. |

---

*Last updated: State A Sub-Step 4 approved. Planning: `docs/ai/planning/feature-integrated-learning-environment.md`. Ready for State B.*
