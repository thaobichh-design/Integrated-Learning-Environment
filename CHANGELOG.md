# Changelog — Integrated-Learning-Environment (ILE)

This project uses the **engine and brain** from [my-ai-devkit-templates](https://github.com/chrislongnguyen/my-ai-devkit-templates). Template updates are brought in manually; ILE-specific changes are documented here. **Template changelog (what was brought in) is below.**

---

## Template 1.1.0 (brought in 2026-02-21)

*Source: my-ai-devkit-templates CHANGELOG [1.1.0] — 2026-02-21*

### Added
- **Master Scope Mapping** (Planning): Single source of truth for which A.C. is tackled in which iteration; MECE, no redundant Deferred lists.
- **Standardized A.C. IDs** (Holy Trinity): Naming convention across Requirements, Design, Planning (Verb-ACn, SustainAdv-ACn, EffAdv-ACn, ScalAdv-ACn, Noun-ACn, SustainAdj-ACn, EffAdj-ACn, ScalAdj-ACn).
- **Status flow (solo Founder):** ⚪ Pending → 🔴 To Do → 🔵 Draft Completed (by the Agent) → 🟢 Reviewed/Tested (by the User); 🟠 Stuck = off-ramp.
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

## Session handoff (2026-02-21)

**What was done this session:**
- Linked project folder to GitHub repo [Integrated-Learning-Environment](https://github.com/chrislongnguyen/Integrated-Learning-Environment); initial push.
- Brought in latest template (my-ai-devkit-templates 1.1.0) from local `~/Documents/my-ai-devkit-templates`: `.cursor/` (commands, rules, skills, mcp), `docs/ai/` READMEs, Manifesto, frameworks; README, CHANGELOG.
- Updated feature docs to new template: Requirements Phase 3 with A.C. IDs (Verb-AC1.., SustainAdv-AC1.., etc.); Design §3 (attributes mapped to A.C. IDs and iterations), §4 (Resource Impact + Requesting Resources/Budget); Planning §1.2 Master Scope Mapping as two tables (Table A by iteration, Table B one row per A.C. with requirement, iteration, evidence, status).

**What to do when you continue:**
- Tell the Agent: *"We're on the ILE project. State A is complete (Causal Map, System Design, User's Requirements, 4-Iteration Roadmap approved). Planning uses the two-table Master Scope Mapping (Table A by iteration, Table B by A.C.). Next: run `/state-b` to execute the first task (T-101) from the planning doc, or continue from where we left off."*
- First uncompleted task: **T-101** (Define and document the minimal ILE flow; confirm with User that this is the desired wrapper). All planning tasks are still 🔴 To Do.
- To ship pending work: run `/ship` and approve the commit message.
