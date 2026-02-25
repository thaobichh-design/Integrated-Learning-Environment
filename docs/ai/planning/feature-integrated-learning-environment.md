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
* **Iteration 4: Enablement Leadership (Validate Scalability):** COE map representation; user→ClickUp mapping; sync to company space; configurable hierarchy/templates/space for reuse (other ClickUp spaces, other template sets). Operational hardening: health check, integration smoke test, concrete session walkthrough, lightweight runtime stats, doc duplication reduction, session recording for analytics, multi-user validation.

## 1.2 Master Scope Mapping
*Goal: One single source of truth for which Acceptance Criterion (from Requirements) is tackled in which Iteration. Must be MECE — each A.C. appears exactly once.*

**Status legend:** ⚪ Pending · 🔴 To Do / In Progress · 🔵 Draft Completed (by the Agent) · 🟢 Reviewed/Tested (by the User) · 🟠 Stuck (off-ramp when blocked). *Task flow: Pending → To Do → Draft Completed → Reviewed/Tested. All tasks must be reviewed and approved by the User before marking Reviewed/Tested.*

### Table A — By iteration (what’s in scope per iteration)

| Iteration | A.C. IDs in scope |
| :--- | :--- |
| **1** | Verb-AC1, Verb-AC2, Verb-AC3, SustainAdv-AC1 |
| **2** | Verb-AC4, Verb-AC5, SustainAdv-AC2, SustainAdv-AC3, Noun-AC1, Noun-AC2, Noun-AC3, Noun-AC4, Noun-AC5, SustainAdj-AC1, SustainAdj-AC2, SustainAdj-AC3 |
| **3** | EffAdv-AC1, EffAdv-AC2, EffAdv-AC3, **EffAdv-AC4**, EffAdj-AC1, EffAdj-AC2, EffAdj-AC3, **EffAdj-AC4**, **EffAdj-AC5**, Noun-AC9, **Noun-AC11**, **Verb-AC9**, **Verb-AC10** |
| **4** | ScalAdv-AC1, ScalAdv-AC2, ScalAdv-AC3, ScalAdv-AC4, **ScalAdv-AC5**, Noun-AC6, Noun-AC7, Noun-AC8, **Noun-AC10**, **Noun-AC12**, **Noun-AC13**, ScalAdj-AC1, ScalAdj-AC2, ScalAdj-AC3, ScalAdj-AC4, **SustainAdj-AC4**, **SustainAdj-AC5** |

*Use this table to see at a glance which A.C. are tackled in each iteration. For requirement text, evidence, and status, use Table B.*

### Table B — By A.C. (detail: requirement, iteration, evidence, status)

*One row per A.C. ID. Traceability: A.C. ID matches `docs/ai/requirements/feature-integrated-learning-environment.md` Phase 3.*

| A.C. ID | Requirement (from Req Phase 3) | Iter | Deterministic Evidence | Status |
| :--- | :--- | :---: | :--- | :---: |
| Verb-AC1 | User can start or resume a learning session for a chosen subject (COE → Area → Chapter → Topic) in one workspace. | 1 | `docs/ai/implementation/ile-minimal-flow.md`; User confirms. | 🟢 |
| Verb-AC2 | User can choose phase (A/B/C) and see entry points from Learning Map for that phase (informed by Subject Roadmap A). | 1 | `learning-book-tree-map.md` + `entry-point-to-template-mapping.md`; T-301: `ile-phase-and-entry-points.md` + rules; User confirms. | 🟢 |
| Verb-AC3 | User can select an entry point and have the correct template (questions × components) loaded and scoped to that entry. | 1 | `templates/0-overview-and-summary.md` + `entry-point-to-template-mapping.md`; User confirms. | 🟢 |
| SustainAdv-AC1 | Document structure (COE → Area → Chapter → Topic, phases A/B/C, components) defined and consistent; same path → same logical place. | 1 | `learning-book/COE_DS/` + `scripts/check-learning-book-structure.sh`; User confirms. | 🟢 |
| Verb-AC4 | User can conduct dialogue with the Agent; Agent's responses grounded in persistent memory and current document context. | 2 | Persistent memory wired (T-201); Agent uses memory + doc context per contract and `ile-minimal-flow.md`; T-201 approved. | 🟢 |
| Verb-AC5 | After a learning conversation, structural Markdown file(s) reflect new or updated content (no manual paste required). | 2 | `ile-conversation-to-doc-mapping.md` + rule: Agent writes to target file/section per mapping on approval; T-202 approved. | 🟢 |
| SustainAdv-AC2 | Updates from conversation map to a known template (questions × components); mapping rule is explicit. | 2 | `ile-conversation-to-doc-mapping.md` defines mapping rule; template from entry-point-to-template-mapping; T-202 approved. | 🟢 |
| SustainAdv-AC3 | User or Agent can point to the exact file(s) and section(s) created or updated for a given exchange. | 2 | Target path/section deterministic from subject + phase + entry point; Agent can state exact path/section; T-202 approved. | 🟢 |
| Noun-AC1 | One workspace supports both "conversation" and "structural document" (chat + Markdown repo); user does not switch app to edit Learning Book. | 2 | One workspace (chat + Markdown) per `ile-minimal-flow.md`; T-102, T-103 approved. | 🟢 |
| Noun-AC2 | Persistent memory (e.g. MCP) available to Agent, tied to current subject/Learning Book; context preserved across sessions. | 2 | `docs/ai/implementation/ile-persistent-memory.md` (A + Learning Book primary; optional MCP `ile:session:{subject}`; contract Option B/A); T-201 approved. | 🟢 |
| Noun-AC3 | When user selects phase and entry point, correct template is loaded and conversation/document context scoped to that entry. | 2 | `entry-point-to-template-mapping.md` § Loading procedure; `.cursor/rules/ile-learning-book.mdc` § Template loading; T-203 approved. | 🟢 |
| Noun-AC4 | Agent can read and write structural Markdown for current subject so conversation outcomes written into correct files/sections as byproduct. | 2 | `ile-conversation-to-doc-mapping.md` + `.cursor/rules/ile-learning-book.mdc`: read/write to target file/section per mapping on approval; T-202 approved. | 🟢 |
| Noun-AC5 | Entry points presented from Learning Map, informed by Subject Roadmap (A) (current level L1–L7); level-appropriate progression suggested. | 2 | Entry points from `learning-book-tree-map.md` + `entry-point-to-template-mapping.md`; A in structure; T-203, T-301 (`ile-phase-and-entry-points.md`) approved. | 🟢 |
| SustainAdj-AC1 | All writes to Learning Book conform to hierarchy (COE → Area → Chapter → Topic) and phase structure (A/B/C). COE hierarchy single source of truth: `config/coe-map.yaml`; other docs reference it (T-411). | 2 | `ile-conversation-to-doc-mapping.md` enforces path; `check-learning-book-structure.sh` verifies structure; T-202, T-204 approved; T-411: `ile-coe-map.md`, `learning-book-tree-map.md`, design, requirements, `ile-user-clickup-mapping.md`, `ile-minimal-flow.md` reference coe-map.yaml. | 🟢 |
| SustainAdj-AC2 | Template loading uses canonical component set (Overview, UBS, UDS, EPS, UES, EOP) and question set; no ad hoc structure. | 2 | `entry-point-to-template-mapping.md` + 7 page templates (canonical set); no ad hoc; T-203 approved. | 🟢 |
| SustainAdj-AC3 | User can verify (inspection or check command) that repo still matches expected structure after updates. | 2 | `scripts/check-learning-book-structure.sh` (5 phases + 6 chapters under C); run from repo root; T-204 approved. | 🟢 |
| EffAdv-AC1 | User can open a session, pick one entry point, complete or partially complete it, and close; progress is persisted. | 3 | Progress persisted; session can be closed and resumed. | ⚪ |
| EffAdv-AC2 | User can resume later without re-entering context; persistent memory and document state sufficient to continue. | 3 | Resume uses memory + document state; no re-entry of context. | ⚪ |
| EffAdv-AC3 | No mandatory "export" or "sync" step for local/Drive Book updates; updates to Markdown occur as byproduct of conversation. | 3 | `.cursor/rules/ile-learning-book.mdc` § Conversation→Doc + § Before entry/phase switch; `ile-minimal-flow.md` § T-302; T-302 approved. | 🟢 |
| EffAdj-AC1 | No separate "copy from chat and paste into doc" step required for content to appear in structural Markdown. | 3 | Rule § Before entry/phase switch (no copy-paste); `ile-conversation-to-doc-mapping.md`; T-302 approved. | 🟢 |
| EffAdj-AC2 | Updates to document triggered by conversation (Agent writes or user confirms); mechanism defined and repeatable. | 3 | Rule § Conversation→Doc + § Before entry/phase switch; mapping + checkpoint documented; T-302 approved. | 🟢 |
| EffAdj-AC3 | User can switch entry point or phase without losing in-progress context for current entry (draft retained or committed before switch). | 3 | Rule § Before entry/phase switch (Step 7, commit to doc + A before switch); contract § Step 7; T-302 approved. | 🟢 |
| Noun-AC9 | ILE can surface user's current mastery level and relevant Subject Roadmap (A) content so user can respect level-appropriate progression. | 3 | `ile-phase-and-entry-points.md` §4 (T-303): surface in chat current level + level requirements + next-step recommendations; rule § Present entry points; T-301, T-303 approved. | 🟢 |
| **Verb-AC9** | User experiences a clear completion moment after each chunk (e.g. one entry point or one component completed). | 3 | Rule § Completion moment and progress summary (T-304); `ile-minimal-flow.md` § T-304; T-304 approved. | 🟢 |
| **Verb-AC10** | User can view progress and, where implemented, stats/achievements (e.g. streaks, completed entry points). | 3, 4 | I3: progress summary in chat (rule § T-304); T-304 approved; I4: T-405, T-406; `ile-stats-achievements-streaks.md`, dashboard Stats stub; T-406 approved. | 🟢 |
| **EffAdv-AC4** | User receives immediate feedback after completing one chunk so completion is visible and rewarding. | 3 | Completion moment + optional reward per rule § T-304; T-304 approved. | 🟢 |
| **EffAdj-AC4** | Completion of a chunk is signalled clearly (e.g. confirmation message, optional lightweight reward). | 3 | Rule § Completion moment and progress summary (T-304); T-304 approved. | 🟢 |
| **EffAdj-AC5** | Engagement features do not add mandatory steps to the core flow; they are additive and optional. | 3 | Rule § T-304: "No new UI; no mandatory steps"; flow § T-304; T-304 approved. | 🟢 |
| **Noun-AC11** | ILE surfaces progress (and, where implemented, stats/achievements) in-conversation and/or via UI. | 3, 4 | I3: progress summary in chat (rule § T-304); T-304 approved; I4: T-405, T-406; `ile-stats-achievements-streaks.md`, dashboard Stats stub; T-406 approved. | 🟢 |
| ScalAdv-AC1 | Same SOP (phase → entry points → template load → conversation → doc update) applies to any subject within Learning Book structure. | 4 | `ile-minimal-flow.md` (same SOP); phase → entry points → template load → conversation → doc update; applies to any subject in Learning Book structure. | 🟢 |
| ScalAdv-AC2 | Adding a new subject (new Area/Chapter/Topic or new Learning Book) does not require changing core flow; only content and entry points change. | 4 | learning-book/README.md (new subject = new root folder + same structure); `config/ile.yaml`, coe-map; T-102, T-404. | 🟢 |
| ScalAdv-AC3 | System can reference Subject Roadmap (A) and Learning Map so entry points and templates scale with L1–L7 progression. | 4 | `ile-phase-and-entry-points.md`, `entry-point-to-template-mapping.md`; A and Learning Map referenced; L1–L7 in A. | 🟢 |
| ScalAdv-AC4 | Sync from user's Book (local or Google Drive) to company's ClickUp respects COE map and places content in user's respective location. | 4 | `ile-sync-clickup.md`, `scripts/sync-learning-book-to-clickup-dryrun.sh`; T-403 approved. | 🟢 |
| Noun-AC6 | ILE has a defined representation of LTC COE hierarchical map (COE → Chapter → Topic → Topic Members' Learning Area → each member's Personal Learning Area). | 4 | `docs/ai/implementation/ile-coe-map.md`, `config/coe-map.yaml`; T-401 approved. | 🟢 |
| Noun-AC7 | ILE can map a single user's learning to that user's respective location on ClickUp (correct Topic → that user's Personal Learning Area). | 4 | `ile-user-clickup-mapping.md`, `scripts/resolve-user-clickup-location.sh`, `config/coe-map.yaml`; T-402 approved; T-413 approved (USER_2, dry-run + smoke test both users). | 🟢 |
| Noun-AC8 | ILE supports (or will support) syncing user's learning from their Book to company's ClickUp in correct place (COE and User mapping). | 4 | `ile-sync-clickup.md`, `scripts/sync-learning-book-to-clickup-dryrun.sh`; T-403 approved. | 🟢 |
| ScalAdj-AC1 | New subjects reuse same Learning Book template (A. Subject Roadmap, B. Capture Facts & Data, C. Organise Information, D. Distill Understanding, E. Express Expertise). | 4 | learning-book/README.md (same folder layout A/B/C/D/E); T-102; Design § Scalability (1). | 🟢 |
| ScalAdj-AC2 | New entry points or templates can be added via configuration or defined structure without changing core integration (chat + memory + doc). | 4 | `entry-point-to-template-mapping.md`, templates in repo; `config/ile.yaml` templates_path; T-203, T-404. | 🟢 |
| ScalAdj-AC3 | Optional future capabilities (e.g. Audio Overview, Infographics, Quiz) can be added without breaking core flow. | 4 | Design § Scalability (3); dedicated UI and stats optional (T-405, T-406); core flow unchanged. | 🟢 |
| ScalAdj-AC4 | ILE pattern can be applied to other ClickUp spaces and different doc template sets; hierarchy, templates, space mapping configurable. | 4 | `config/ile.yaml`, `ile-configurable-mapping.md`; ILE_LEARNING_BOOK_ROOT in dry-run; T-404 approved. | 🟢 |
| **ScalAdv-AC5** | **Usage analytics (options open):** Product owner can obtain quality data from ILE usage (incl. vocal feedback) so Descriptive, Diagnostic, Predictive, Prescriptive analytics can drive feature development and bug fixes; data sources and implementation remain open. | 4 | `ile-session-recording.md` + `scripts/append_session_event.py` + rule § Session recording (T-412); JSONL event log; T-412 approved. | 🟢 |
| **Noun-AC10** | **Usage data for analytics (options open):** ILE supports (or will support) data collection and management of usage data for Descriptive, Diagnostic, Predictive, Prescriptive analytics to drive features and bug fixes; implementation options remain open. | 4 | `ile-session-recording.md` + `scripts/append_session_event.py` + `logs/ile-session-events.jsonl`; T-412 approved. | 🟢 |
| **Noun-AC12** | **Optional dedicated UI:** ILE may provide a dedicated UI for progress, entry points, and stats (e.g. Duolingo-style dashboard) as an optional entry point. | 4 | `ile-dedicated-ui.md`, `ile-dashboard-stub.html`; T-405 approved; T-406 for stats. | 🟢 |
| **Noun-AC13** | **Concrete session walkthrough:** A documented real-session transcript (not abstract) shows step-by-step what happens (user input, Agent response, file changes); onboarding and regression reference. | 4 | `docs/ai/examples/ile-session-walkthrough.md`; T-409 approved. | 🟢 |
| **SustainAdj-AC4** | **System health check:** Single command validates config (`ile.yaml`, `coe-map.yaml`) parseable and schema-valid (required keys/structure for both), templates exist for all page types, learning-book structure correct, A exists for at least one subject, rules present. Output: "system is healthy" or list of issues. | 4 | `scripts/health_check.py` + `.cursor/commands/health.md`; T-407 approved. | 🟢 |
| **SustainAdj-AC5** | **Integration smoke test:** Repeatable script validates dry-run sync output format and all Learning Book files map to valid PLAs in COE map. | 4 | `scripts/smoke-test-sync-dryrun.sh`; T-408 approved. | 🟢 |

*Populated from Requirements Phase 3. Use Table A to see scope per iteration; use Table B to trace each A.C. to its requirement and evidence.*

---

# 2. EXECUTION MATRIX (Micro Sequencing)
*Tasks are derived from the Master Scope Mapping above. Implementation details (how to build) come from Design. Do not invent new scope here.*

**Traceability rule:** Every A.C. in Table A for an iteration must be linked to at least one task (or prior work) and have explicit deterministic evidence in Table B. When adding tasks for an iteration, verify each A.C. in scope has evidence; if an A.C. is satisfied by prior structure, set Table B evidence to the relevant task(s) and doc(s).

## 2.2 Iteration Sequencing

### ITERATION 1: CONCEPT
*Focus: Desirable Wrapper & Core Verb Validation.*

**Active A.C. in Scope:** Verb-AC1, Verb-AC2, Verb-AC3, SustainAdv-AC1

| ID | Task (Verb) | Risk Validated | Deps | Status |
| :--- | :--- | :--- | :--- | :--- |
| **T-101** | Define and document the minimal ILE flow in the current IDE (phase A/B/C → entry points → template load → conversation → doc update) and confirm with User that this is the desired wrapper. | Desirability / Hook | None | 🟢 Reviewed/Tested |
| **T-102** | Create a minimal Learning Book folder structure for one COE Area (A. Subject Roadmap, B. Capture Facts & Data, C. Organise Information, D. Distill Understanding, E. Express Expertise) and one stub template (e.g. one questions×components table) so the wrapper is tangible. | UDO Resolution / One workspace | T-101 | 🟢 Reviewed/Tested |
| **T-103** | Validate with User: "One workspace (chat + Markdown) with no manual paste" solves the root blocker; approve moving to Iteration 2. | UDO Resolution | T-102 | 🟢 Reviewed/Tested |

### ITERATION 2: WORKING PROTOTYPE
*Focus: Effective Core & Sustainability.*

**Active A.C. in Scope:** Verb-AC4, Verb-AC5, SustainAdv-AC2, SustainAdv-AC3, Noun-AC1..AC5, SustainAdj-AC1..AC3

| ID | Task (Verb) | Risk Validated | Deps | Status |
| :--- | :--- | :--- | :--- | :--- |
| **T-201** | Wire persistent memory (e.g. MCP @ai-devkit/memory or equivalent) so the Agent can store/recall context tied to the current subject/Learning Book. **Done:** `ile-persistent-memory.md` (A + Learning Book; optional MCP `ile:session:{subject}`; contract Option B/A §3); `ile-effective-learning-contract.md`, `.cursor/rules/ile-effective-learning.mdc`, `ile-minimal-flow.md` aligned to EOP. **Next:** T-202. **I2 enhancements (no new task):** contract (minimal EPS + full EOP + Strategy), rule (all EOP steps 1–8, gates, RACI), flow↔EOP. | Technical Feasibility | T-103 | 🟢 Reviewed/Tested |
| **T-202** | Implement Agent read/write of one Learning Book Markdown file from conversation (e.g. one section updated as byproduct of one Q&A); document the mapping rule (conversation → file/section). | Technical Feasibility | T-201 | 🟢 Reviewed/Tested |
| **T-203** | Implement loading of one canonical template (questions × components) when user selects an entry point; scope conversation/document context to that entry. **Done:** Rule `.cursor/rules/ile-learning-book.mdc` § Template loading (resolve template from entry-point-to-template-mapping, load template file, scope context to entry). `docs/ai/implementation/entry-point-to-template-mapping.md` § Loading procedure (4 steps: resolve entry point → resolve template path → load template → scope context). Verb-AC3. | Technical Feasibility | T-202 | 🟢 Reviewed/Tested |
| **T-204** | Add a single check (e.g. script or manual step) that the repo still matches the expected Learning Book structure after updates. **Done:** `scripts/check-learning-book-structure.sh` extended (T-204): verifies 5 phases A/B/C/D/E and, under C. Organise Information, 6 chapter folders (0..5) per `learning-book/README.md`. Run from repo root: `./scripts/check-learning-book-structure.sh [learning-book]`. SustainAdj-AC3. | Sustainability | T-203 | 🟢 Reviewed/Tested |

### ITERATION 3: MINIMUM VIABLE ENABLEMENT (MVE)
*Focus: Fuse Wrapper & Core; Efficiency.*

**Active A.C. in Scope:** EffAdv-AC1..AC4, EffAdj-AC1..AC5, Noun-AC9, Noun-AC11, Verb-AC9, Verb-AC10

| ID | Task (Verb) | Risk Validated | Deps | Status |
| :--- | :--- | :--- | :--- | :--- |
| **T-301** | Implement phase choice (B. Capture \| C. Organise \| D. Distill) and present entry points from the Learning Map for the chosen phase; entry points informed by Subject Roadmap (A) / current level where A is available. | Efficiency / Usability | T-204 | 🟢 Reviewed/Tested |
| **T-302** | Ensure updates to Markdown occur as a byproduct of the conversation (no separate copy-paste); user can switch entry point or phase without losing in-progress context (retain or commit draft). | Zero-friction capture | T-301 | 🟢 Reviewed/Tested |
| **T-303** | Surface the user's current mastery level and relevant Subject Roadmap (A) content (e.g. level requirements, next-step recommendations) so the user can respect level-appropriate progression. | UDO Anchor | T-302 | 🟢 Reviewed/Tested |
| **T-304** | **Engagement light:** Deliver a clear completion moment after each chunk (e.g. one component or entry point) and a progress summary in chat (e.g. "X of Y completed for this phase"); Agent behavior only, no new UI. Ensures engagement does not add mandatory steps. | Engagement / Return | T-303 | 🟢 Reviewed/Tested |

### ITERATION 4: ENABLEMENT LEADERSHIP
*Focus: Scalability, COE map, ClickUp mapping, sync, configurable, operational hardening.*

**Active A.C. in Scope:** ScalAdv-AC1..AC5, Noun-AC6..AC8, Noun-AC10, Noun-AC12, Noun-AC13, ScalAdj-AC1..AC4, SustainAdj-AC4, SustainAdj-AC5

| ID | Task (Verb) | Risk Validated | Deps | Status |
| :--- | :--- | :--- | :--- | :--- |
| **T-401** | Define and implement the ILE's representation of the LTC COE hierarchical map (COE → Chapter → Topic → Topic Members' Learning Area → each member's Personal Learning Area). | Scalability | T-304 | 🟢 Reviewed/Tested |
| **T-402** | Implement mapping of a single user's learning to that user's respective location on ClickUp (correct Topic → that user's Personal Learning Area). | Scalability | T-401 | 🟢 Reviewed/Tested |
| **T-403** | Implement (or stub and document) sync of the user's Book (local or Google Drive) to the company's ClickUp in the correct place using the COE map and user mapping. | Scalability | T-402 | 🟢 Reviewed/Tested |
| **T-404** | Make hierarchy, templates, and ClickUp space mapping configurable (e.g. per workspace or mode) so the ILE pattern can be applied to other ClickUp spaces and different doc template sets. | Reusability | T-403 | 🟢 Reviewed/Tested |
| **T-405** | **Engagement full — dedicated UI:** Implement or stub a dedicated UI for progress, entry points, and optional stats (e.g. Duolingo-style dashboard) as an optional entry point; in-conversation progress remains sufficient for minimum engagement. | Engagement / Scalability | T-304 | 🟢 Reviewed/Tested |
| **T-406** | **Engagement full — stats/achievements/streaks:** Implement (or stub and document) stats, achievements, and streaks (e.g. completed entry points, daily return) so the user can view progress and sustain motivation; optional to consume, no mandatory steps. | Engagement / Return | T-405 | 🟢 Reviewed/Tested |
| **T-407** | **Health check command:** Add a `/health` command (or extend `/status`) that validates in one pass: config files `config/ile.yaml` and `config/coe-map.yaml` parseable **and** pass schema validation (required keys and structure for both; wrong key or missing field → enumerated issue); templates exist for all page types; learning-book structure passes `check-learning-book-structure.sh`; A exists for at least one subject; rules (`.cursor/rules/ile-*.mdc`) present. Output: "system is healthy" or enumerated list of issues. | Sustainability / Hardening | T-406 | 🟢 Reviewed/Tested |
| **T-408** | **Integration smoke test:** Create a script that runs `sync-learning-book-to-clickup-dryrun.sh`, validates the output format (expected fields and structure), and checks that all Learning Book files map to a valid PLA in `config/coe-map.yaml`. Repeatable smoke test for sync pipeline. | Sustainability / Hardening | T-407 | 🟢 Reviewed/Tested |
| **T-409** | **Concrete session walkthrough:** Document a real session as a step-by-step transcript (not abstract): "I typed X, the Agent did Y, the file at Z was updated with W." Concrete onboarding reference and regression baseline beyond `docs/ai/examples/walkthrough.md`. | Documentation / Onboarding | T-407 | 🟢 Reviewed/Tested |
| **T-410** | **Lightweight runtime stats:** Create a small script (Python or Node) that reads `config/ile.yaml` + `config/coe-map.yaml` + A's Session Log and computes stats (completed entry points, streak, last session). Dashboard gets real data without depending on the Agent; validates config files are consumable by code. | Scalability / Analytics | T-406 | 🟢 Reviewed/Tested |
| **T-411** | **Reduce doc duplication:** Make `config/coe-map.yaml` the single source of truth for the COE hierarchy; update other docs that re-describe the hierarchy to reference `coe-map.yaml` instead. | Sustainability / Single source of truth | T-401 | 🟢 Reviewed/Tested |
| **T-412** | **Session recording for analytics:** When a learning session happens, append structured events (session start, entry point selected, chunk completed, session end) to a simple JSON log. Lightest path to ScalAdv-AC5 / Noun-AC10 (usage analytics) without choosing a full analytics platform. | Scalability / Analytics | T-410 | 🟢 Reviewed/Tested |
| **T-413** | **Test multi-user:** Add a second user to `config/coe-map.yaml`, run the dry-run sync, and verify the output maps correctly for both users. Low effort; validates the design assumption that COE map and user→PLA mapping scales per user. | Scalability / Validation | T-408 | 🟢 Reviewed/Tested |

---

# 3. RESOURCE & BUDGET TRACKER
*Monitor constraints mapped to the Efficiency Adjectives. Update Hard Limit after User approval per Design §4 (Requesting Resources/Budget).*

| Metric | Current Usage | Hard Limit | Status |
| :--- | :--- | :--- | :--- |
| **Financial Cost (OpEx)** | $0.00 | TBD | 🟢 Safe |
| **API/Token/Compute Usage** | 0 | TBD | 🟢 Safe |

---

# 4. COMMANDS & RULES (ILE — Learner journey)

*MECE coverage for the Learner's journey with the Agent. Commands are user-invokable; rules apply when globs match (learning-book, implementation docs, templates).*

| Purpose | Command / Rule | Reference |
| :--- | :--- | :--- |
| Populate or refresh A (Subject Roadmap) | **`/roadmap-discovery`** | `docs/ai/implementation/ile-roadmap-discovery.md`; rule: `.cursor/rules/ile-learning-book.mdc` § Roadmap Discovery |
| Session start/resume, EOP 1–8, gates, RACI | Rule: **ile-effective-learning.mdc** | Contract: `ile-effective-learning-contract.md`; flow: `ile-minimal-flow.md` |
| Session memory (read A, optional MCP; session end append) | Rule: **ile-session-memory.mdc** | `ile-persistent-memory.md` |
| Phase choice, entry points, template load, conversation→doc, checkpoint before switch, Agent as teacher | Rule: **ile-learning-book.mdc** | `ile-phase-and-entry-points.md`, `ile-conversation-to-doc-mapping.md`, `entry-point-to-template-mapping.md` |

*No further ILE-specific commands required for current scope; journey is conversational (resume, phase choice, entry point) with rules applying in context. For execution: `/state-b` for next task.*

---

*Last updated: T-407 extended for schema validation of both `config/ile.yaml` and `config/coe-map.yaml`. I4 hardening T-407..T-413; Table A/B SustainAdj-AC4, AC5, Noun-AC13. Ready for State B: execute one task at a time with `/state-b`.*
