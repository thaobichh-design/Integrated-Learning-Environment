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
