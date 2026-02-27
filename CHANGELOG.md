# Changelog — Integrated-Learning-Environment (ILE)

This project uses the **engine and brain** from [my-ai-devkit-templates](https://github.com/chrislongnguyen/my-ai-devkit-templates). Template updates are brought in manually; ILE-specific changes are documented here. **Template changelog (what was brought in) is below.**

---

## Template 1.1.0 (brought in 2026-02-21)

*Source: my-ai-devkit-templates CHANGELOG [1.1.0] — 2026-02-21*

### Added
- **Master Scope Mapping** (Planning): Single source of truth for which A.C. is tackled in which iteration; MECE, no redundant Deferred lists.
- **Standardized A.C. IDs** (Holy Trinity): Naming convention across Requirements, Design, Planning (Verb-ACn, SustainAdv-ACn, EffAdv-ACn, ScalAdv-ACn, Noun-ACn, SustainAdj-ACn, EffAdj-ACn, ScalAdj-ACn).
- **Status flow (solo User):** ⚪ Pending → 🔴 To Do → 🔵 Draft Completed (by the Agent) → 🟢 Reviewed/Tested (by the User); 🟠 Stuck = off-ramp.
- **Design §4:** Optional guidance on requesting Resources/Budget from the User (when to ask, what to specify, approval gate).
- **Document flow:** Explicit chain Req → Design → Planning → Execution Matrix in README and Manifesto.
- **Utility Belt & When to use which:** Manifesto lists /state-a, /state-b, /ship, /debug, /remember and when to use each.
- **New venture checklist:** README: clone → open in Cursor → /state-a → /state-b.
- **Archive clarification:** README states docs/ai/archive/ is historical only; live docs are requirements/, design/, planning/.
- **Company board sync:** Planning README maps template statuses to Scrumban (TODO, READY TO DO, DRAFT COMPLETED, REVIEWED/TESTED, STUCK).
- **Ship ↔ Planning:** Ship command considers updating planning doc (e.g. task 🟢 Reviewed/Tested) before proposing commit.
- **Debug ↔ Holy Trinity:** Debug command notes task ID and A.C. from Planning when relevant for traceability.
- **.gitignore:** .DS_Store ignored.
- **Ambient flow rule** (`.cursor/rules/ambient-flow.mdc`): When user requests a new feature/add-on without /state-a or /state-b, nudge to /state-a, help populate requirements/design/planning from their request, get approval before any execution.

### Changed
- State B and execute-micro-task use `docs/ai/planning/README.md` (Execution Matrix, Iteration Sequencing); A.C. resolved from Master Scope Mapping.
- State A (strategy-mapping) Sub-Step 4: populate Master Scope Mapping from Requirements Phase 3 A.C. IDs.
- Planning §3 (Resource & Budget Tracker): note to update Hard Limit after User approval per Design §4.

---

## ILE-specific

- **State A complete:** Causal Map, System Design, User's Requirements, 4-Iteration Roadmap for feature `integrated-learning-environment`; docs in `docs/ai/requirements/`, `docs/ai/design/`, `docs/ai/planning/` (feature-integrated-learning-environment.md).
- **Repo:** [Integrated-Learning-Environment](https://github.com/chrislongnguyen/Integrated-Learning-Environment).
- **Template 1.1.0 brought in (2026-02-21):** `.cursor/` (commands, rules/ambient-flow.mdc, skills), `docs/ai/` READMEs and Manifesto, CHANGELOG, README from local my-ai-devkit-templates. Feature docs (requirements, design, planning) updated to new template: standardized A.C. IDs, Design §4, Master Scope Mapping two-table structure (Table A by iteration, Table B by A.C. with requirement + evidence + status).

---

## ILE Iteration 2 — T-201 Reviewed/Tested (2026-02-21)

**T-201: Persistent memory wired. 🟢 Reviewed/Tested.**

### Added
- **ile-effective-learning-contract.md** — Minimal EPS (3 principles), full EOP (RACI + all 8 steps with Required Input, Desired Output, RACI, gates), ILE Strategy. Contract loading: Option B (MCP digest `ile:contract`) preferred; Option A (load doc) fallback.
- **ile-persistent-memory.md** — Persistent memory contract: primary A + Learning Book; optional MCP key `ile:session:{subject}`; §3 Principles and EOP (contract) Option B/A. Wiring: contract, rules.
- **.cursor/rules/ile-effective-learning.mdc** — Follow contract at ILE session start; all EOP steps 1–8; mandatory gates (Step 2 before Step 3, Step 7 before switch/exit); RACI (no A write or switch without Learner approval).
- **.cursor/rules/ile-session-memory.mdc** — Session start/resume (read A, optional MCP recall); session end/switch (append Session Log, optional MCP store). Key by subject/Learning Book.
- **docs/ai/reference/** — ltc-advanced-effective-learning-system.md (Section 8 replaced with pointer to implementation contract).

### Changed
- **ile-minimal-flow.md** — Maps 1:1 to EOP steps 1–8; cross-refs contract, persistent memory, rule; pre-session (Step 2) and checkpoint (Step 7) gates; “What counts as persistent memory” includes contract Option B/A; core flow table EOP step mapping.
- **ltc-advanced-effective-learning-system.md** — Section 8 (ILE Strategy) moved to implementation; §8 now points to `ile-effective-learning-contract.md`. Chain of Logic item 8 updated.
- **Planning** — T-201 marked 🟢 Reviewed/Tested. Noun-AC2 evidence and status (🔵) updated. T-201 task cell: Done, Next (T-202), I2 enhancements (contract, rule, flow↔EOP).

---

## ILE Iteration 1 Complete (2026-02-22)

**Iteration 1: Concept — T-101, T-102, T-103 all 🟢 Reviewed/Tested.**

### Added
- **A. Subject Roadmap & Level Specifications** — Universal template and populated Data Science example with Learner Progress Tracker, Level Completion Checklist, Session Log, Gap Analysis, Links to Learning Book. A is the canonical checkpoint for session start/resume.
- **ile-minimal-flow.md** — Minimal ILE flow (phase B/C/D: Capture, Organise, Distill → entry points → template load → conversation → doc update). A as checking point. Agent Persistent Memory (file-based: A + Learning Book). Mid-session context (hierarchy over chronology, scoped context, checkpointing).
- **ile-iteration-1-validation.md** — T-103 validation checklist; User confirmed one workspace + no manual paste solves UBS; approved moving to Iteration 2.
- **learning-book-tree-map.md** — Full tree map (6 Chapters × 6 Topics). **entry-point-to-template-mapping.md** — Entry point → template resolution.
- **learning-book/COE_DS/** — Minimal Learning Book structure (A, B. Capture Facts & Data, C. Organise Information, D, E); Data Science Subject Roadmap populated.
- **templates/** — A-subject-roadmap-and-level-specifications.md, 0-overview-and-summary.md.
- **scripts/** — check-learning-book-structure.sh.
- **.cursor/rules/** — ile-learning-book.mdc, long-n-naming-convention.mdc, use-user-not-founder.mdc.

### Changed
- **README.md** — Rewritten for LTC Advanced Effective Learning Framework. Removed Effective Execution Engine. Added: Framework, Process (Capture → Organise → Distill), How ILE Helps (6 principles with UDS/UBS mappings), Quick Start, Project Structure.
- **Planning** — T-103 marked 🟢 Reviewed/Tested. Iteration 2 (T-201) unlocked.

---

## ILE Iteration 3 — T-302, T-303, T-304 Reviewed/Tested (2026-02-21)

**Iteration 3 (MVE): Zero-friction capture, UDO anchor surfacing, engagement light. All 🟢 Reviewed/Tested.**

### Added
- **T-302 (Zero-friction capture and retain-on-switch):** `.cursor/rules/ile-learning-book.mdc` § Before entry/phase switch — no switch until Step 7 (Checkpoint); prompt to save; commit to target file/section + A's Session Log before switch; no copy-paste. `ile-minimal-flow.md` § T-302. EffAdv-AC3, EffAdj-AC1, EffAdj-AC2, EffAdj-AC3.
- **T-303 (Surface current mastery level and A content):** `ile-phase-and-entry-points.md` §4 T-303 — surface in chat: current mastery level; level requirements; next-step recommendations (session start/resume and when presenting entry points). Rule § Present entry points; flow § A as anchor (T-303). Noun-AC9.
- **T-304 (Engagement light — completion moment + progress summary):** `ile-minimal-flow.md` § T-304; `.cursor/rules/ile-learning-book.mdc` § Completion moment and progress summary (T-304). After each chunk (one component or entry point completed): (1) completion moment (explicit confirmation; optional lightweight reward); (2) when appropriate, progress summary in chat (e.g. "X of Y completed for this phase"). Agent behavior only; no new UI; no mandatory steps. Verb-AC9, Verb-AC10, EffAdv-AC4, EffAdj-AC4, EffAdj-AC5, Noun-AC11.
- **Roadmap Discovery (populate A via Learner interview):** `docs/ai/implementation/ile-roadmap-discovery.md` — structured interview (Context, Goal, Learning habits, Current level & gaps, Curriculum fit, Level specifications) so A is fitted to the individual (PM Problem Discovery / User's Requirements style). Blocks 5 & 6: if Learner cannot populate, Agent populates from standard + blocks 1–4; Learner confirms or edits. `.cursor/commands/roadmap-discovery.md` — `/roadmap-discovery`. Rule § Roadmap Discovery; flow § (a) Entirely new book.
- **ile-phase-and-entry-points.md** — Procedure: phase choice (B/C/D), Learning Map entry points per phase, §3 Informed by A, §4 T-303 surfacing, §5 Procedure summary, §6 Evidence. Cross-refs flow, tree map, entry→template, conversation→doc.
- **Planning §4 Commands & rules (ILE)** — MECE table: `/roadmap-discovery`, ile-effective-learning.mdc, ile-session-memory.mdc, ile-learning-book.mdc with purpose and references.
- **Agent as teacher (Verb-AC6, AC7, AC8):** Rule § Conversation → Doc — explicit: generate multiple possibilities for Learner to contemplate and choose; no append without Learner's explicit choice or approval.

### Changed
- **ile-minimal-flow.md** — Initial check: if A missing, run Roadmap Discovery first. (a) Entirely new book: Roadmap Discovery per ile-roadmap-discovery.md; `/roadmap-discovery`. § T-302, § T-304. A as anchor (T-303) resume: surface in chat current level + A content.
- **Planning** — T-302, T-303, T-304 marked 🟢 Reviewed/Tested. Table B updated for EffAdv-AC3, EffAdj-AC1–AC3, Noun-AC9, Verb-AC9, Verb-AC10, EffAdv-AC4, EffAdj-AC4, EffAdj-AC5, Noun-AC11 with deterministic evidence. §4 Commands & rules (ILE) added.
- **ile-learning-book.mdc** — Globs: + ile-roadmap-discovery.md. § Roadmap Discovery (populate A). § Before entry/phase switch (T-302). § Completion moment and progress summary (T-304). § Agent as teacher: + generate possibilities; Learner chooses (Verb-AC6, AC7, AC8).

---

## Distilled-understanding template + archive cleanup (2026-02-21)

### Added
- **distilled-understanding-template-spec.md** — Optional read-only duplicate: `templates/D-distilled-understanding-full.json` (same content as xlsx; keys = sheet names, values = row arrays).
- **templates/D-distilled-understanding-full.json** — JSON duplicate of D-distilled-understanding-full.xlsx for read-only consumption.
- **archive/** — Obsolete MD/HTML and scripts moved here: archive/templates/ (D-distilled-understanding-full.md, D-distilled-understanding-table-editor.html), archive/scripts/ (build_table_editor_html.py, build_distilled_understanding_md.py, pdf_table_to_md.py).

### Removed
- **templates/** — D-distilled-understanding-full.backup-*.md, _table_data.json, _table_data_escaped.txt (backups/temp). D-distilled-understanding-full.md, D-distilled-understanding-table-editor.html (→ archive).
- **scripts/** — README-pdf-table-to-md.md (removed). pdf_table_to_md.py, build_table_editor_html.py, build_distilled_understanding_md.py (→ archive).

### Changed
- **docs/ai/implementation/distilled-understanding-template-spec.md** — Canonical source: D-distilled-understanding-full.xlsx; optional duplicate: D-distilled-understanding-full.json.

---

## Template improvement recommendations (2026-02-25)

*Logged for session resumption. These are recommendations from an objective review of `templates/` in the ILE project — not yet implemented.*

### Recommendations — Phase B and phase seams

1. **B → C derivation gap**  
   B template uses a wide capture table (LEARN / WATCH / LISTEN / READ / VIEW / DO). Phase C uses the 16-column causal question set. There is **no documented derivation path** from B to C (e.g. "captured source in B row X.Y informs C row UBS.UB in chapter/topic Z"). Consider adding a short implementation note or rule: how B captures map into Phase C seeds (or that the learner re-derives C from B manually).

2. **B template: add agent-facing instructions**  
   B has only a USER GUIDE (three bullets for the learner). Phase C templates have Purpose, Derivation Rules, Causal Logic, Format, Rules for the agent. Add an agent-facing section to `templates/B-captured-facts-and-information.md`: e.g. how many rows per subtopic, how to link a source to a subtopic, how "Consumed = Green" is represented in Markdown (or that it is human-only).

3. **A template: L-level requirements are placeholders**  
   The Level Specifications table uses `*Define for this subject*` for every level. There is no default or heuristic for a new subject. Consider: (a) a generic L1–L7 default in the template or a separate "generic level spec" doc agents can copy from, or (b) documenting in Roadmap Discovery / A-population that the agent must obtain or propose L1–L7 requirements before A is usable.

### Recommendations — Consistency and maintenance

4. **Page 7: markdown vs HTML**  
   Pages 0–5 use markdown tables; Page 7 uses raw HTML (`<table>`, `colspan`, `rowspan`). Document in `entry-point-to-template-mapping.md` or the page-7 template that Page 7 is HTML for column-grouping reasons, so agents treat it as a special case.

5. **Template versioning**  
   If the 16-column set or row structure changes, all pre-generated topic files (e.g. 252 under C) can become stale with no way to detect it. Consider adding a `template_version` or `canonical_question_set_version` field to templates and/or generated files, and a check in `health_check.py` or `check-learning-book-structure.sh` that reports version mismatch.

6. **Topic 0 vs Topics 1–5**  
   Every page template branches on "Topic 0: N rows; Topics 1–5: M rows." The agent must know (chapter, topic) before generating. Consider making this explicit in the loading procedure (e.g. "resolve topic index first; then apply template branch") so it is never ambiguous.

### Summary for resumption

- **Phase C (pages 0–5, 7):** Causal chain and 16-column set are strong; no structural change recommended.  
- **Risks:** B→C bridge undocumented; B not agent-ready; A L-levels blank; Page 7 format inconsistency; no template versioning; Topic 0 vs 1–5 branch must be resolved at load time.  
- **Next steps (optional):** Implement one or more of the above (e.g. B agent section, B→C mapping note, A generic L1–L7 stub, template_version field, or health-check version check).

---

## Session handoff (2025-02-21)

**What was done this session:**
- Iteration 1 completed: T-101, T-102, T-103 all 🟢 Reviewed/Tested.
- A. Subject Roadmap template + populated Data Science example (Learner Progress Tracker, Session Log, Level Completion Checklist, Gap Analysis, Links to Learning Book).
- ile-minimal-flow.md: A as checkpoint; Agent Persistent Memory; Mid-session context (UDS.UB resolution).
- README rewritten for LTC Advanced Effective Learning Framework (removed Effective Execution Engine).
- T-103 validated: one workspace + no manual paste solves root blocker; approved Iteration 2.

**What to do when you continue (laptop):**
- Tell the Agent: *"We're on the ILE project. Iteration 1 complete (T-101, T-102, T-103). Next: T-201 — Wire persistent memory (MCP or equivalent) so Agent can store/recall context tied to subject/Learning Book."*
- First uncompleted task: **T-201** (Iteration 2: Working Prototype).
- Key context: A (Subject Roadmap) is the checking point. Doc is source of truth; chat is ephemeral. See `docs/ai/implementation/ile-minimal-flow.md`.
# Changelog — LTC Master Template

All notable changes to the Master Template (this repo) are documented here. Ventures clone a snapshot; this log helps you see what changed in the template over time. **When you update the Master Template, add an entry with date and change.**

---

## [1.3.0] — 2026-02-20

### Added
- **Glossary** in `docs/ai/frameworks/effective-system-design.md`: 20+ terms (UDO, UBS, Verb, Noun, A.C., MECE, Holy Trinity, etc.) with plain-English definitions. Referenced from README.
- **Approval language guide** in Manifesto: table mapping every approval situation to the exact phrase the User should type.
- **`/help` command:** Decision tree — "What do I run?" with all commands, approval phrases, and first-time instructions.
- **Worked example walkthrough** (`docs/ai/examples/walkthrough.md`): End-to-end habit tracker example showing /state-a (4 sub-steps with sample output) through first /state-b task execution and approval.
- **Recovery Protocol** in Manifesto: table covering undo approval, revert bad code, redo State A, agent gone off rails, undo entire iteration, context window issues.
- **Context Preservation rule** (`.cursor/rules/context-preservation.mdc`, `alwaysApply: true`): Session start re-hydration (agent reads planning doc + handoff doc); periodic checkpoint nudge (after 3 approved tasks); pre-ship handoff reminder; cross-device continuity protocol; planning doc as single source of truth over chat memory.
- **Multi-feature dashboard** in `/status`: when multiple `feature-*.md` files exist, outputs a summary table of all features before the detailed report.
- **`/review` command:** Iteration retrospective — gathers all evidence from a completed iteration, lists validated A.C., gaps/risks, and prompts the User to confirm UDO still holds before advancing. Usable at iteration boundaries, mid-iteration, or before handoff.
- **Guided mode for State A:** strategy-mapping now asks "Are you familiar with the framework, or would you like guided mode with examples?" before the Causal Map. Lowers the entry barrier for beginners.

### Changed
- README: added `/help`, `/review`, guided mode mention, context preservation, approval phrases quick reference, walkthrough link, and updated new venture checklist.
- strategy-mapping Sub-Step 1: added guided mode check (step 2), renumbered subsequent steps.
- Manifesto: added Recovery Protocol and User approval phrases sections.

---

## [1.2.0] — 2026-02-20

### Added
- **`/status` command:** Read-only "where am I?" snapshot — active feature, planning doc, template version, current iteration, next task, last approved task and evidence, task counts (🟢/🔵/🔴/🟠/⚪), next actions. Use when resuming (e.g. new computer).
- **Iteration transition gate (State B):** Before executing a task in a *new* iteration (e.g. first task of Iteration 2), the agent HARD STOPS and asks the User to confirm "Proceed to Iteration N+1" or "Re-plan". Ensures current iteration is validated before advancing.
- **Memory search at start of State A:** In strategy-mapping Sub-Step 1, after feature name is confirmed, the agent searches `@ai-devkit/memory` for principles/rules/learnings relevant to the feature or domain and presents findings to the User before the Causal Map.
- **Anti-pattern rule** (`.cursor/rules/anti-patterns.mdc`, `alwaysApply: true`): Hard rules — no code before design; no new dependencies without Resource Impact (Design §4); no optimize/refactor outside A.C.; no skip of evidence step in State B; no iteration jump without gate.
- **`/handoff` command:** Generates `project_handoff_status.md` in repo root with active feature, current iteration, next task ID, last approved task, modified/uncommitted files (from `git status`), and next actions for resuming.
- **Template version tracking:** `.template-version` file (e.g. 1.2.0). `/status` reports this version; use with CHANGELOG for "what changed" when syncing from master template.

### Changed
- execute-micro-task Step 1: renumbered steps; step 3 is the iteration transition gate (HARD STOP when next 🔴 is in a higher iteration than last 🟢).
- strategy-mapping Sub-Step 1: added memory search step after feature name; renumbered subsequent steps.

---

## [1.1.0] — 2026-02-21

### Added
- **Master Scope Mapping** (Planning): Single source of truth for which A.C. is tackled in which iteration; MECE, no redundant Deferred lists.
- **Standardized A.C. IDs** (Holy Trinity): Naming convention across Requirements, Design, Planning (Verb-ACn, SustainAdv-ACn, EffAdv-ACn, ScalAdv-ACn, Noun-ACn, SustainAdj-ACn, EffAdj-ACn, ScalAdj-ACn).
- **Status flow (solo User):** ⚪ Pending → 🔴 To Do → 🔵 Draft Completed (by the Agent) → 🟢 Reviewed/Tested (by the User); 🟠 Stuck = off-ramp.
- **Design §4:** Optional guidance on requesting Resources/Budget from the User (when to ask, what to specify, approval gate).
- **Document flow:** Explicit chain Req → Design → Planning → Execution Matrix in README and Manifesto.
- **Utility Belt & When to use which:** Manifesto lists /state-a, /state-b, /ship, /debug, /remember and when to use each.
- **New venture checklist:** README: clone → open in Cursor → /state-a → /state-b.
- **Archive clarification:** README states docs/ai/archive/ is historical only; live docs are requirements/, design/, planning/.
- **Company board sync:** Planning README maps template statuses to Scrumban (TODO, READY TO DO, DRAFT COMPLETED, REVIEWED/TESTED, STUCK).
- **Ship ↔ Planning:** Ship command considers updating planning doc (e.g. task 🟢 Reviewed/Tested) before proposing commit.
- **Debug ↔ Holy Trinity:** Debug command notes task ID and A.C. from Planning when relevant for traceability.
- **.gitignore:** .DS_Store ignored.
- **Ambient flow rule** (`.cursor/rules/ambient-flow.mdc`): When user requests a new feature/add-on without /state-a or /state-b, nudge to /state-a, help populate requirements/design/planning from their request, get approval before any execution.

### Changed
- State B and execute-micro-task use `docs/ai/planning/README.md` (Execution Matrix, Iteration Sequencing); A.C. resolved from Master Scope Mapping.
- State A (strategy-mapping) Sub-Step 4: populate Master Scope Mapping from Requirements Phase 3 A.C. IDs.
- Planning §3 (Resource & Budget Tracker): note to update Hard Limit after User approval per Design §4.

---

## [1.0.0] — Initial

- 2-State Engine (State A: Strategy & Planning; State B: Execute One Micro-Task).
- Holy Trinity: requirements, design, planning templates in docs/ai/.
- Utility Belt: /state-a, /state-b, /ship, /debug, /remember.
- Effective Execution Manifesto; dev-lifecycle skill and references.
# Changelog — LTC Master Template

All notable changes to the Master Template (this repo) are documented here. Ventures clone a snapshot; this log helps you see what changed in the template over time. **When you update the Master Template, add an entry with date and change.**

---

## [1.3.0] — 2026-02-24

### Added
- **Glossary** in `docs/ai/frameworks/effective-system-design.md`: 20+ terms (UDO, UBS, Verb, Noun, A.C., MECE, Holy Trinity, etc.) with plain-English definitions. Referenced from README.
- **Approval language guide** in Manifesto: table mapping every approval situation to the exact phrase the User should type.
- **`/help` command:** Decision tree — "What do I run?" with all commands, approval phrases, and first-time instructions.
- **Worked example walkthrough** (`docs/ai/examples/walkthrough.md`): End-to-end habit tracker example showing /state-a (4 sub-steps with sample output) through first /state-b task execution and approval.
- **Recovery Protocol** in Manifesto: table covering undo approval, revert bad code, redo State A, agent gone off rails, undo entire iteration, context window issues.
- **Context Preservation rule** (`.cursor/rules/context-preservation.mdc`, `alwaysApply: true`): Session start re-hydration (agent reads planning doc + handoff doc); periodic checkpoint nudge (after 3 approved tasks); pre-ship handoff reminder; cross-device continuity protocol; planning doc as single source of truth over chat memory.
- **Multi-feature dashboard** in `/status`: when multiple `feature-*.md` files exist, outputs a summary table of all features before the detailed report.
- **`/review` command:** Iteration retrospective — gathers all evidence from a completed iteration, lists validated A.C., gaps/risks, and prompts the User to confirm UDO still holds before advancing. Usable at iteration boundaries, mid-iteration, or before handoff.
- **Guided mode for State A:** strategy-mapping now asks "Are you familiar with the framework, or would you like guided mode with examples?" before the Causal Map. Lowers the entry barrier for beginners.

### Changed
- README: added `/help`, `/review`, guided mode mention, context preservation, approval phrases quick reference, walkthrough link, and updated new venture checklist.
- strategy-mapping Sub-Step 1: added guided mode check (step 2), renumbered subsequent steps.
- Manifesto: added Recovery Protocol and User approval phrases sections.

---

## [1.2.0] — 2026-02-20

### Added
- **`/status` command:** Read-only "where am I?" snapshot — active feature, planning doc, template version, current iteration, next task, last approved task and evidence, task counts (🟢/🔵/🔴/🟠/⚪), next actions. Use when resuming (e.g. new computer).
- **Iteration transition gate (State B):** Before executing a task in a *new* iteration (e.g. first task of Iteration 2), the agent HARD STOPS and asks the User to confirm "Proceed to Iteration N+1" or "Re-plan". Ensures current iteration is validated before advancing.
- **Memory search at start of State A:** In strategy-mapping Sub-Step 1, after feature name is confirmed, the agent searches `@ai-devkit/memory` for principles/rules/learnings relevant to the feature or domain and presents findings to the User before the Causal Map.
- **Anti-pattern rule** (`.cursor/rules/anti-patterns.mdc`, `alwaysApply: true`): Hard rules — no code before design; no new dependencies without Resource Impact (Design §4); no optimize/refactor outside A.C.; no skip of evidence step in State B; no iteration jump without gate.
- **`/handoff` command:** Generates `project_handoff_status.md` in repo root with active feature, current iteration, next task ID, last approved task, modified/uncommitted files (from `git status`), and next actions for resuming.
- **Template version tracking:** `.template-version` file (e.g. 1.2.0). `/status` reports this version; use with CHANGELOG for "what changed" when syncing from master template.

### Changed
- execute-micro-task Step 1: renumbered steps; step 3 is the iteration transition gate (HARD STOP when next 🔴 is in a higher iteration than last 🟢).
- strategy-mapping Sub-Step 1: added memory search step after feature name; renumbered subsequent steps.

---

## [1.1.0] — 2026-02-21

### Added
- **Master Scope Mapping** (Planning): Single source of truth for which A.C. is tackled in which iteration; MECE, no redundant Deferred lists.
- **Standardized A.C. IDs** (Holy Trinity): Naming convention across Requirements, Design, Planning (Verb-ACn, SustainAdv-ACn, EffAdv-ACn, ScalAdv-ACn, Noun-ACn, SustainAdj-ACn, EffAdj-ACn, ScalAdj-ACn).
- **Status flow (solo User):** ⚪ Pending → 🔴 To Do → 🔵 Draft Completed (by the Agent) → 🟢 Reviewed/Tested (by the User); 🟠 Stuck = off-ramp.
- **Design §4:** Optional guidance on requesting Resources/Budget from the User (when to ask, what to specify, approval gate).
- **Document flow:** Explicit chain Req → Design → Planning → Execution Matrix in README and Manifesto.
- **Utility Belt & When to use which:** Manifesto lists /state-a, /state-b, /ship, /debug, /remember and when to use each.
- **New venture checklist:** README: clone → open in Cursor → /state-a → /state-b.
- **Archive clarification:** README states docs/ai/archive/ is historical only; live docs are requirements/, design/, planning/.
- **Company board sync:** Planning README maps template statuses to Scrumban (TODO, READY TO DO, DRAFT COMPLETED, REVIEWED/TESTED, STUCK).
- **Ship ↔ Planning:** Ship command considers updating planning doc (e.g. task 🟢 Reviewed/Tested) before proposing commit.
- **Debug ↔ Holy Trinity:** Debug command notes task ID and A.C. from Planning when relevant for traceability.
- **.gitignore:** .DS_Store ignored.
- **Ambient flow rule** (`.cursor/rules/ambient-flow.mdc`): When user requests a new feature/add-on without /state-a or /state-b, nudge to /state-a, help populate requirements/design/planning from their request, get approval before any execution.

### Changed
- State B and execute-micro-task use `docs/ai/planning/README.md` (Execution Matrix, Iteration Sequencing); A.C. resolved from Master Scope Mapping.
- State A (strategy-mapping) Sub-Step 4: populate Master Scope Mapping from Requirements Phase 3 A.C. IDs.
- Planning §3 (Resource & Budget Tracker): note to update Hard Limit after User approval per Design §4.

---

## [1.0.0] — Initial

- 2-State Engine (State A: Strategy & Planning; State B: Execute One Micro-Task).
- Holy Trinity: requirements, design, planning templates in docs/ai/.
- Utility Belt: /state-a, /state-b, /ship, /debug, /remember.
- Effective Execution Manifesto; dev-lifecycle skill and references.
