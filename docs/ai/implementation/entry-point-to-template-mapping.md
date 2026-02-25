---
phase: implementation
title: Entry Point → Template Mapping (T-102, T-203)
description: Rule "entry X → template Y". Template loading when user selects entry point; scope conversation/document to that entry. Verb-AC3.
feature: integrated-learning-environment
task: T-203
---

# Entry Point → Template Mapping

*Rule: when user selects entry point X, Agent loads template Y and scopes conversation/document context to that entry. Aligned with `learning-book-tree-map.md`.*

**Cross-references:** Tree map → `docs/ai/implementation/learning-book-tree-map.md` | Flow → `docs/ai/implementation/ile-minimal-flow.md` | Conversation→Doc → `docs/ai/implementation/ile-conversation-to-doc-mapping.md` | Rule → `.cursor/rules/ile-learning-book.mdc` | Folder layout → `learning-book/README.md`

## Loading procedure (T-203)

*Deterministic behavior when user selects an entry point.*

1. **Resolve entry point** — From user: (subject, phase, chapter, topic, **page**). Example: COE_DS, C. Organise Information, Chapter 1 UBS, Topic 1 (Ultimate Blockers), Page 0. For Phase B, entry is subject-level only (no chapter/topic/page).
2. **Resolve template path** — For **Phase B** use `templates/B-captured-facts-and-information.md` (one file per subject). Use **page-type resolution (MECE)** for Phase C topic content: (chapter, topic, **page**) → one of the 7 page templates per the table below. For A. Subject Roadmap, use `templates/A-subject-roadmap-and-level-specifications.md`. If page is missing or unknown, fallback to `templates/0-overview-and-summary.md`.
3. **Load template** — Read the template file at the resolved path. Use its structure (questions × components, target table format) for the conversation and for any proposed doc updates. If the file does not exist, use the structure from `templates/0-overview-and-summary.md`.
4. **Scope context** — Resolve target file and section per `ile-conversation-to-doc-mapping.md`. Keep conversation and doc updates scoped to this single entry (one file, one section). Do not mix other entry points in the same exchange.

**Evidence:** Agent can state the loaded template path and the target file/section for the current entry point (SustainAdv-AC3, Verb-AC3).

## Page-type resolution (MECE)

*For Phase C. Organise Information topic content: resolve template by **page** so every section (36 × 7 = 252) is covered by exactly one of 7 page templates. See `docs/ai/implementation/ile-template-mece-checklist.md`.*

| Page | Template path |
|------|----------------|
| 0 | `templates/0-overview-and-summary.md` |
| 1 | `templates/page-1-ultimate-blockers.md` |
| 2 | `templates/page-2-ultimate-drivers.md` |
| 3 | `templates/page-3-principles.md` |
| 4 | `templates/page-4-components.md` |
| 5 | `templates/page-5-steps-to-overcome.md` |
| 7 | `templates/page-7-topic-distilled-understanding.md` |

*All 7 page templates exist. Use this table when (subject, phase, chapter, topic, page) is known; target file/section still resolved per `ile-conversation-to-doc-mapping.md`.*

## Phase B (B. Capture Facts & Data)

*Phase B is **one file per subject** (not per chapter/topic). The file contains a single table: USER GUIDE + rows for chapters 0–5 with subtopics and learning-tool columns. No (chapter, topic, page) entry-point resolution for B—the whole subject is one entry.*

| Phase | Entry | Template path |
|-------|-------|----------------|
| B | B. Capture Facts & Data (subject-level) | `templates/B-captured-facts-and-information.md` |

*When user selects Phase B, load `templates/B-captured-facts-and-information.md` and scope context to the single B file for the current subject per `ile-conversation-to-doc-mapping.md`.*

## Mapping table (legacy / A. Subject Roadmap)

*6 Chapters × 6 Topics. Each Topic has 7 pages (0–5 + Page 7 Topic Distilled Understanding). Organise level = 16 columns (14 questions + 2 notes). Distilled level = 17 columns (14 questions + 3 notes).*

| — | — | **A. Subject Roadmap & Level Specifications** | A. Subject Roadmap | `templates/A-subject-roadmap-and-level-specifications.md` |
| 0 | 0. Overview & Summary | Chapter 0, Topic 0 | C. Organise Information | `templates/0-overview-and-summary.md` |
| 1 | 0. Overview & Summary | Chapter 1 UBS, Topic 0 | C. Organise Information | `templates/1-ubs-0-overview-and-summary.md` |
| 1 | 1. Ultimate Blockers | Chapter 1 UBS, Topic 1 | C. Organise Information | `templates/1-ubs-1-ultimate-blockers.md` |
| 1 | 2. Ultimate Drivers | Chapter 1 UBS, Topic 2 | C. Organise Information | `templates/1-ubs-2-ultimate-drivers.md` |
| 1 | 3. Principles | Chapter 1 UBS, Topic 3 | C. Organise Information | `templates/1-ubs-3-principles.md` |
| 1 | 4. Components | Chapter 1 UBS, Topic 4 | C. Organise Information | `templates/1-ubs-4-components.md` |
| 1 | 5. Steps to Overcome | Chapter 1 UBS, Topic 5 | C. Organise Information | `templates/1-ubs-5-steps-to-overcome.md` |
| 2–5 | (same pattern) | Chapter X, Topic Y | C. Organise Information | `templates/{chapter}-{topic}.md` |

*For A. Subject Roadmap use the first row. For Phase C topic content use **page-type resolution** above (7 page templates).*

## Rule

- **Entry X:** Chapter ID + Topic ID (e.g. `1. UBS - 0. Overview & Summary`). For conversation→doc targeting, **entry point** = (chapter, topic, **page**) — a particular page within a topic; page ∈ {0,1,2,3,4,5,7}. See `ile-conversation-to-doc-mapping.md` and `learning-book-tree-map.md` § 6 Pages per Topic.
- **Template Y:** Resolved from table; canonical structure: questions × components (16 cols Organise, 17 cols Distilled).
- **Content address:** Page = path; cell = row (component) × column (question). See `learning-book-tree-map.md` § Content Addressing.

## Extending

To add more entry points: create a template under `templates/` following the naming convention, add a row to the table, and ensure the template matches the canonical question set (see tree map § Canonical Questions).
