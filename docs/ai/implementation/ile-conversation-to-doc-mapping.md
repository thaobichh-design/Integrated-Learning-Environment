---

## phase: implementation
title: ILE Conversation → Doc Mapping (T-202)
description: Mapping rule from conversation scope (subject, phase, entry point) to Learning Book file path and section. Deterministic evidence for Verb-AC5, SustainAdv-AC2, SustainAdv-AC3, Noun-AC4.
feature: integrated-learning-environment
task: T-202

# ILE Conversation → Doc Mapping

*Rule: given the current **subject**, **phase**, and **entry point** of the learning conversation, the Agent can deterministically resolve the **target file path** and **section** in the Learning Book for read/write. Updates from the conversation are written to that file/section as a byproduct; no manual paste.*

**Entry point definition:** An **entry point** is a **particular page within a topic**. So entry point = (chapter_id, topic_id, **page**). **Layer 6 in Individual = 7 pages per topic file:** Page ∈ {0, 1, 2, 3, 4, 5, 7} per tree map § 6 Pages per Topic (0 = Overview & Summary, 1 = Ultimate Blockers, 2 = Ultimate Drivers, 3 = Principles, 4 = Components, 5 = Steps to Overcome, **7 = Topic Distilled Understanding**). Target **file** = one per (chapter, topic); target **section** = that page (component/row) within the file. **Do not rely on Phase D (D. Distill Understanding) at subject root for topic-level distilled**—when merging to company tree, Distilled Understanding is **Page 7 within each topic** (Layer 6), not Phase D at root.

**Cross-references:** Entry point → template → `docs/ai/implementation/entry-point-to-template-mapping.md` | **Individual's tree** (learning-book/ for one person) → `docs/ai/implementation/learning-book-tree-map.md` § Individual's full effective learning tree | Company tree & folder layout → `learning-book-tree-map.md` | Folder layout → `learning-book/README.md` | Flow → `docs/ai/implementation/ile-minimal-flow.md`

---

## 1. Inputs (Conversation Scope)


| Input           | Source                                                                                                                   | Example                                             |
| --------------- | ------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------- |
| **subject**     | User choice at session start / resume                                                                                    | `COE_DS`                                            |
| **phase**       | User choice (B | C | D)                                                                                                  | `C` (Organise Information)                          |
| **entry point** | User selection from Learning Map; (chapter_id, topic_id, **page**) — **page** = particular page within topic (0..5 or 7) | Chapter 1 UBS, Topic 0, Page 0 (Overview & Summary) |


---

## 2. Mapping Rule: Conversation Scope → File Path & Section

**Rule:** **Phase B:** `target_path = learning-book/{subject}/{phase_folder}/{filename}` (no chapter_folder; one file per subject). **Phase C/D:** `target_path = learning-book/{subject}/{phase_folder}/{chapter_folder}/{filename}`.


| Part               | Derivation                                                                                                                                                                                                                                               | Example                                                           |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **subject**        | Current subject (e.g. COE_DS)                                                                                                                                                                                                                            | `COE_DS`                                                          |
| **phase_folder**   | B → `B. Capture Facts & Data`; C → `C. Organise Information`; D → `D. Distill Understanding`                                                                                                                                                             | `C. Organise Information`                                         |
| **chapter_folder** | **Phase B:** none (one file at phase folder). **Phase C/D:** From entry point: 0 → `0. Overview & Summary`; 1 → `1. UBS`; 2 → `2. UDS`; 3 → `3. EPS`; 4 → `4. UES`; 5 → `5. EOP`                                                                          | `1. UBS`                                                          |
| **filename**       | **Phase B:** One file per subject: `[COE AREA]_[OWNER]_[SUBJECT TITLE] - B. CAPTURED FACTS & INFORMATION.md` (e.g. `[COE DS]_[OWNER]_DATA SCIENCE - B. CAPTURED FACTS & INFORMATION.md`). **Phase C:** One file per (chapter, topic): `[COE AREA]_[OWNER]_[CHAPTER]. [CHAPTER NAME] - [TOPIC ID]. [TOPIC NAME].md` or stub. | `1. UBS - 0. Overview & Summary.md` or stub `1-ubs-0-overview.md` |


**Section (within file) — Layer 6: 7 pages:** Each topic file in the Individual Learning Book has **exactly 7 pages** as sections: Page 0, Page 1, Page 2, Page 3, Page 4, Page 5, **Page 7: Topic Distilled Understanding**. Section = **page** within the topic (entry point's page). Do not use Phase D at subject root for topic-level distilled—Page 7 is inside each topic. Pages 0–5 and 7 map to components/rows per `learning-book-tree-map.md` § 6 Pages per Topic. Optionally, section = component (row) × question (column) for cell-level write. Agent writes to the section (page/component) that matches the current entry point and Q&A focus.

**Minimal stub (current repo):** Under `learning-book/COE_DS/`, phase folders exist; chapter subfolders under C are `0. Overview & Summary`, `1. UBS`, … (per README). If the target file does not exist, Agent creates it from the template for that entry point (per entry-point-to-template-mapping) or writes to the path once the file exists.

---

## 3. Deterministic Resolution (Algorithm)

1. **Resolve entry point** — From user selection: (chapter_id, topic_id, **page**). Page = particular page within topic (0..5 or 7). Same chapter/topic as entry-point-to-template-mapping; page identifies which section within the topic file.
2. **Resolve phase folder** — B → `B. Capture Facts & Data`; C → `C. Organise Information`; D → `D. Distill Understanding`.
3. **Resolve chapter folder** — 0 → `0. Overview & Summary`; 1 → `1. UBS`; 2 → `2. UDS`; 3 → `3. EPS`; 4 → `4. UES`; 5 → `5. EOP`. *Folder names must match `learning-book/README.md` (short form: 1. UBS, not "1. Ultimate Blocking System").*
4. **Resolve filename** — One file per (chapter, topic). Use naming from tree map or stub: e.g. `[COE DS]_[OWNER]_1. UBS - 0. Overview & Summary.md` or `1-ubs-0-overview.md`.
5. **Full path** — For Phase B: `learning-book/{subject}/B. Capture Facts & Data/{filename}`. For Phase C/D: `learning-book/{subject}/{phase_folder}/{chapter_folder}/{filename}`.
6. **Section** — **Phase B:** Section = table row (topic/subtopic) within the single B file; no page. **Phase C/D:** Section = **page** (component/row) within that topic file. Each topic file has exactly 7 pages: Page 0 = Overview & Summary, 1 = Ultimate Blockers, 2 = Ultimate Drivers, 3 = Principles, 4 = Components, 5 = Steps to Overcome, **7 = Topic Distilled Understanding**. Topic-level distilled is Page 7 within the topic, not Phase D at subject root. Agent reads/writes that section when the entry point includes that page.

---

## 4. Agent Read/Write Behavior

- **Read:** When loading context for the current entry point, Agent reads the target file (and optionally only the relevant section) per this mapping. If the file does not exist, treat as empty and use template structure for proposed content.
- **Write:** When the user approves an update from the conversation (or at a logical chunk), Agent writes to the target file/section per this mapping. Do not write to a different file/section than the one resolved from current subject + phase + entry point. One exchange (or one Q&A chunk) maps to one file and optionally one section; Agent can point to the exact file and section (SustainAdv-AC3).
- **RACI:** No write without Learner approval (per ILE Effective Learning Contract). Agent proposes; Learner approves or corrects.

---

## 5. Evidence for A.C.


| A.C. ID        | Requirement                                                                                                                                 | Evidence                                                                                                               |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Verb-AC5       | After a learning conversation, structural Markdown file(s) reflect new or updated content (no manual paste).                                | Agent writes to target file/section per this mapping when user approves; doc updated as byproduct.                     |
| SustainAdv-AC2 | Updates from conversation map to a known template (questions × components); mapping rule is explicit.                                       | This doc defines the mapping rule; template structure from entry-point-to-template-mapping and learning-book-tree-map. |
| SustainAdv-AC3 | User or Agent can point to the exact file(s) and section(s) created or updated for a given exchange.                                        | Target path and section are deterministic from subject + phase + entry point; Agent can state exact path and section.  |
| Noun-AC4       | Agent can read and write structural Markdown for current subject so conversation outcomes written into correct files/sections as byproduct. | Read: load target file/section per mapping. Write: write to target file/section per mapping on approval.               |


