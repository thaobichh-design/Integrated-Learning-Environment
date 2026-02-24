---
phase: implementation
title: ILE Phase Choice & Entry Points from Learning Map (T-301)
description: Procedure: offer phase (B | C | D), present entry points from Learning Map for chosen phase, informed by Subject Roadmap (A) and current level. Verb-AC2, Noun-AC5, Noun-AC9.
feature: integrated-learning-environment
task: T-301
---

# Phase Choice & Entry Points (Learning Map)

*When the user is in ILE context (session start or "choose phase"), the Agent (1) offers phase choice **B. Capture Facts & Data | C. Organise Information | D. Distill Understanding**, (2) presents **entry points** from the Learning Map for the chosen phase, (3) informs the list by **Subject Roadmap (A)** (current level, next recommended entry point, last session) where A is available. User then selects an entry point → Agent loads template per `entry-point-to-template-mapping.md` (T-203).*

**Cross-references:** Flow → `docs/ai/implementation/ile-minimal-flow.md` | Tree map → `docs/ai/implementation/learning-book-tree-map.md` | Entry→Template → `docs/ai/implementation/entry-point-to-template-mapping.md` | Conversation→Doc → `docs/ai/implementation/ile-conversation-to-doc-mapping.md` | A (checkpoint) → `ile-minimal-flow.md` § A. Subject Roadmap | Rule → `.cursor/rules/ile-learning-book.mdc`, `.cursor/rules/ile-session-memory.mdc`

---

## 1. Phase choice (EOP Step 4)

Present exactly three options. Do not offer A (checking point only) or E (Express Expertise) in this step unless the User explicitly asks.

| Phase | Label |
|-------|--------|
| **B** | B. Capture Facts & Data |
| **C** | C. Organise Information |
| **D** | D. Distill Understanding |

**Agent behavior:** Ask: *"Which phase? **B.** Capture Facts & Data | **C.** Organise Information | **D.** Distill Understanding."* Wait for User to choose one. Then proceed to §2.

---

## 2. Learning Map: entry points per phase

The **Learning Map** for phases B, C, and D has the **same structure**: 6 chapters × 6 topics per chapter. Each (chapter, topic) is one **topic-level entry point**; each topic has 7 **pages** (0–5 + Page 7) for granular work. For presenting the list, use **topic-level** entry points (chapter + topic); when the user selects one, default to **Page 0** unless they specify a page, then load template per `entry-point-to-template-mapping.md`.

### 2.1 Chapters (same for B, C, D)

| Chapter ID | Chapter name (short) |
|------------|----------------------|
| 0 | 0. Overview & Summary |
| 1 | 1. UBS (Ultimate Blocking System) |
| 2 | 2. UDS (Ultimate Driving System) |
| 3 | 3. EPS (Effective Principle System) |
| 4 | 4. UES (Ultimate Effective System) |
| 5 | 5. EOP (Effective Operating Procedure) |

### 2.2 Topics per chapter (same 6 per chapter)

| Topic ID | Topic name (Chapter 1 UBS example) | Topic name (Chapter 2 UDS: "Steps to Utilize") |
|----------|------------------------------------|--------------------------------------------------|
| 0 | 0. Overview & Summary | 0. Overview & Summary |
| 1 | 1. Ultimate Blockers | 1. Ultimate Blockers |
| 2 | 2. Ultimate Drivers | 2. Ultimate Drivers |
| 3 | 3. Principles | 3. Principles |
| 4 | 4. Components | 4. Components |
| 5 | 5. Steps to Overcome | 5. Steps to Utilize |

*For other chapters, use the same topic names; only Chapter 2 uses "Steps to Utilize" instead of "Steps to Overcome" for topic 5.*

### 2.3 Deriving the list for chosen phase

- **Phase B:** Entry points = 6 chapters × 6 topics = 36 (chapter name + topic name per tree map).
- **Phase C:** Same 36 entry points (C. Organise Information, same chapter/topic structure).
- **Phase D:** Same 36 entry points (D. Distill Understanding, same chapter/topic structure).

**Folder layout (Individual Learning Book):** `learning-book/{subject}/{phase_folder}/{chapter_folder}/` with one file per topic. Phase folder: B → `B. Capture Facts & Data`, C → `C. Organise Information`, D → `D. Distill Understanding`. Chapter folder: 0 → `0. Overview & Summary`, 1 → `1. UBS`, 2 → `2. UDS`, 3 → `3. EPS`, 4 → `4. UES`, 5 → `5. EOP`. See `learning-book-tree-map.md` § Individual tree and `learning-book/README.md`.

**Presenting:** Group by chapter. Example for Phase C: *"**Chapter 0.** Overview & Summary: Topic 0 Overview, Topic 1 Ultimate Blockers, … Topic 5 Steps to Overcome. **Chapter 1.** UBS: Topic 0 Overview, … Topic 5 Steps to Overcome. … **Chapter 5.** EOP: …"* Or list as a short table: Chapter | Topic 0 | Topic 1 | … | Topic 5. User selects one (chapter + topic) → then Agent loads template for (chapter, topic, page 0) unless user specifies a page.

---

## 3. Informed by Subject Roadmap (A)

When **A. Subject Roadmap & Level Specifications** exists for the subject, read it **before** presenting the entry-point list and use it to **inform** (order, suggest, or annotate) the list. Do not require A to present the list; if A is missing, present the full Learning Map for the chosen phase.

### 3.1 What to read from A

| A section | Use |
|-----------|-----|
| **Learner Progress Tracker** | Current Level, Target Level, Last Session, **Last Entry Point**, **Next Recommended Entry Point** |
| **Session Log** | Last N rows (last entry point, progress note) |
| **Links to Learning Book (per Level)** | Optional: level → chapters/topics mapping for level-appropriate suggestions |
| **Gap Analysis** | Optional: current vs target gaps to prioritise entry points |

### 3.2 How to inform the list

1. **Suggest first:** If A has "Next Recommended Entry Point", show it at the top: *"Suggested next: Chapter X, Topic Y (from your roadmap)."*
2. **Resume:** If A has "Last Entry Point" or Session Log last row, call it out: *"Last worked on: Chapter X, Topic Y. Resume there or pick another."*
3. **Level-appropriate:** If A defines level requirements or "Links to Learning Book" per level, optionally reorder or annotate entry points (e.g. "at L2, these are level-appropriate: …"). User can still choose any entry point.
4. **Full list:** After suggestions, present the full list (or by chapter) so the user can pick any entry point.

**Evidence:** Agent can state that entry points were derived from the Learning Map (tree map) and, when A exists, that the list was informed by Learner Progress Tracker / Session Log / Next Recommended Entry Point.

---

## 4. T-303: Surfacing current level and A content (Noun-AC9)

When **A. Subject Roadmap & Level Specifications** exists, the Agent must **surface in chat** (state explicitly) so the user can see and respect level-appropriate progression:

1. **Current mastery level** — From A's **Learner Progress Tracker**: state Current Level (and optionally Target Level, Last Session, Last Entry Point) in one sentence (e.g. *"Your current level: L2. Last worked on: Chapter 1 UBS, Topic 0. Overview."*).
2. **Relevant A content** — From A, state in one or two sentences:
   - **Level requirements:** If A's **Level Specifications (L1–L7)** or **Level Completion Checklist** is populated, mention the requirement(s) for the user's current or target level (e.g. *"At L2 for this subject: [brief requirement from A]."*).
   - **Next-step recommendations:** From **Next Recommended Entry Point**, **Gap Analysis**, or **Links to Learning Book (per Level)** — state the suggested next step (e.g. *"Next recommended: Chapter 1 UBS Topic 1, or complete UBS before moving to UDS."*).

**When to surface:** (a) At **session start or resume** (after reading A, before phase choice or entry-point list). (b) When **presenting entry points** (before or with the list: state level + recommendations, then present the list). If A is missing, skip surfacing and present the full Learning Map for the chosen phase.

**Evidence (T-303):** Agent states in chat current mastery level and relevant A content (level requirements and/or next-step recommendations) so the user can consciously respect level-appropriate progression. Noun-AC9.

---

## 5. Procedure summary (Agent checklist)

1. **Phase choice** — Ask: "Which phase? B. Capture | C. Organise | D. Distill." User picks one.
2. **Optional: read A** — For the current subject, if A exists, read Learner Progress Tracker, Session Log, Next Recommended Entry Point (and optionally Links to Learning Book, Gap Analysis).
3. **Build list** — Learning Map for chosen phase: 6 chapters × 6 topics; use §2.1 and §2.2 for names.
4. **Present** — If A informed: **surface** current level and relevant A content per §4 (T-303); show suggested next and/or last worked on first; then present full list (grouped by chapter) or a concise table. User selects (chapter, topic) [and optionally page].
5. **Load template** — Per `entry-point-to-template-mapping.md`: resolve entry point (chapter, topic, page default 0), load template, scope context. Then learning conversation (T-302, T-203).

---

## 6. Deterministic evidence (T-301, T-303)

- **Verb-AC2:** User can choose phase (B/C/D) and see entry points from the Learning Map for that phase, informed by A.
- **Noun-AC5:** Entry points are derived from the Learning Map; when A exists, they are informed by current level and Next Recommended Entry Point.
- **Noun-AC9 (T-303):** When A exists, the Agent surfaces in chat: current mastery level and relevant A content (level requirements, next-step recommendations) so the user can respect level-appropriate progression. See §4.

*Implementation: this doc + rule reference so the Agent follows the procedure in ILE context.*
