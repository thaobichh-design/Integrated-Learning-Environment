---
phase: implementation
title: Entry Point → Template Mapping (T-102)
description: Rule "entry X → template Y". One stub template; deterministic mapping for Verb-AC3.
feature: integrated-learning-environment
task: T-102
---

# Entry Point → Template Mapping

*Rule: when user selects entry point X, Agent loads template Y. Aligned with `learning-book-tree-map.md`.*

**Cross-references:** Tree map → `docs/ai/implementation/learning-book-tree-map.md` | Flow → `docs/ai/implementation/ile-minimal-flow.md` | Folder layout → `learning-book/README.md`

## Mapping table

*6 Chapters × 6 Topics. Each Topic has 7 pages (0–5 + Page 7 Topic Distilled Understanding). Organise level = 16 columns (14 questions + 2 notes). Distilled level = 17 columns (14 questions + 3 notes).*

| — | — | **A. Subject Roadmap & Level Specifications** | A. Capture / Define | `templates/A-subject-roadmap-and-level-specifications.md` |
| 0 | 0. Overview & Summary | Chapter 0, Topic 0 | B. Organise | `templates/0-overview-and-summary.md` |
| 1 | 0. Overview & Summary | Chapter 1 UBS, Topic 0 | B. Organise | `templates/1-ubs-0-overview-and-summary.md` |
| 1 | 1. Ultimate Blockers | Chapter 1 UBS, Topic 1 | B. Organise | `templates/1-ubs-1-ultimate-blockers.md` |
| 1 | 2. Ultimate Drivers | Chapter 1 UBS, Topic 2 | B. Organise | `templates/1-ubs-2-ultimate-drivers.md` |
| 1 | 3. Principles | Chapter 1 UBS, Topic 3 | B. Organise | `templates/1-ubs-3-principles.md` |
| 1 | 4. Components | Chapter 1 UBS, Topic 4 | B. Organise | `templates/1-ubs-4-components.md` |
| 1 | 5. Steps to Overcome | Chapter 1 UBS, Topic 5 | B. Organise | `templates/1-ubs-5-steps-to-overcome.md` |
| 2–5 | (same pattern) | Chapter X, Topic Y | B. Organise | `templates/{chapter}-{topic}.md` |

*Stub: `templates/0-overview-and-summary.md` exists (T-102). Remaining templates to be added per tree map.*

## Rule

- **Entry X:** Chapter ID + Topic ID (e.g. `1. UBS - 0. Overview & Summary`)
- **Template Y:** Resolved from table; canonical structure: questions × components (16 cols Organise, 17 cols Distilled).
- **Content address:** Page = path; cell = row (component) × column (question). See `learning-book-tree-map.md` § Content Addressing.

## Extending

To add more entry points: create a template under `templates/` following the naming convention, add a row to the table, and ensure the template matches the canonical question set (see tree map § Canonical Questions).
