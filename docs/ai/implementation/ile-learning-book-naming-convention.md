---
phase: implementation
title: ILE Learning Book Naming Convention
description: Canonical naming rule for folder, phase, topic, and page so new subjects match company ClickUp COE structure and sync works.
feature: integrated-learning-environment
---

# Learning Book Naming Convention

**Purpose:** When a new subject (Learning Book) is created, **all** folder and file names under that subject must follow this rule so that (1) the structure matches the company ClickUp COE naming, (2) sync to ClickUp (T-403) and path resolution (T-202) stay deterministic, and (3) Agents and scripts can rely on a single pattern.

**Cross-references:** Tree map → `learning-book-tree-map.md` | Entry→Template → `entry-point-to-template-mapping.md` | Conversation→Doc → `ile-conversation-to-doc-mapping.md` | COE map → `config/coe-map.yaml`, `ile-coe-map.md`

---

## 1. Subject root folder (repository path)

- **Use a slug — no square brackets.**  
  Example: `COE_TECH_LONG_N_AI_ORCHESTRATION`, `COE_DS`.  
  Rationale: brackets in paths break shells and many tools; the slug is the stable identifier for scripts and `config/coe-map.yaml` (area `id`).
- **Match the area id in `config/coe-map.yaml`** when the subject is added to the COE map (so sync can resolve `learning-book/{area_id}/` → ClickUp).

---

## 2. Display prefix (phases, topics, pages)

**Every** phase folder, topic folder, and page file under the subject root **must** use the same prefix. This is the “display” name that aligns with ClickUp COE spaces (e.g. `[COE TECH]_[LONG N.]_AI ORCHESTRATION`).

**Prefix format:**

```
[COE AREA]_[MEMBER]_SUBJECT NAME -
```

- **COE AREA** = ClickUp COE area code (e.g. `COE TECH`, `COE DS`). No space inside brackets in filenames; one space after the closing `]` before the underscore.
- **MEMBER** = Owner / learner identifier (e.g. `LONG N.`).
- **SUBJECT NAME** = Short subject title (e.g. `AI ORCHESTRATION`, `DATA SCIENCE`).
- Trailing space, hyphen, space: `-` (so the next part is clearly separated).

**Example prefix:** `[COE TECH]_[LONG N.]_AI ORCHESTRATION - `

---

## 3. Naming by level

| Level            | Pattern                                                                      | Example                                                                                |
| ---------------- | ---------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **Phase folder** | `{PREFIX}{Phase}. {Phase name}`                                              | `[COE TECH]_[LONG N.]_AI ORCHESTRATION - A. Subject Roadmap & Level Specifications`    |
|                  |                                                                              | `[COE TECH]_[LONG N.]_AI ORCHESTRATION - C. Organise Information`                      |
| **Topic folder** | `{PREFIX}{Chapter}. {Chapter name}`                                          | `[COE TECH]_[LONG N.]_AI ORCHESTRATION - 0. Overview & Summary`                        |
|                  |                                                                              | `[COE TECH]_[LONG N.]_AI ORCHESTRATION - 1. UBS`                                       |
| **Page file**    | `{PREFIX}{Chapter} - {Page}.md`                                              | `[COE TECH]_[LONG N.]_AI ORCHESTRATION - 1. UBS - 0. Overview & Summary.md`            |
|                  |                                                                              | `[COE TECH]_[LONG N.]_AI ORCHESTRATION - 2. UDS - 4. Components.md`                    |
| **A file**       | `[COE AREA]_[MEMBER]_A. SUBJECT - SUBJECT ROADMAP & LEVEL SPECIFICATIONS.md` | `[COE TECH]_[LONG N.]_A. AI ORCHESTRATION - SUBJECT ROADMAP & LEVEL SPECIFICATIONS.md` |

The **A file** lives inside the Phase A folder and uses a slightly different pattern: `A.` instead of `AI ORCHESTRATION - A.` so the document title stays readable. All other phases, topics, and pages use the same prefix as above.

---

## 4. Full structure example (one subject)

```
learning-book/COE_TECH_LONG_N_AI_ORCHESTRATION/     ← subject root (slug)
├── _CONTEXT_ANCHOR.md
├── [COE TECH]_[LONG N.]_AI ORCHESTRATION - A. Subject Roadmap & Level Specifications/
│   └── [COE TECH]_[LONG N.]_A. AI ORCHESTRATION - SUBJECT ROADMAP & LEVEL SPECIFICATIONS.md
├── [COE TECH]_[LONG N.]_AI ORCHESTRATION - B. Capture Facts & Data/
├── [COE TECH]_[LONG N.]_AI ORCHESTRATION - C. Organise Information/
│   ├── [COE TECH]_[LONG N.]_AI ORCHESTRATION - 0. Overview & Summary/
│   │   ├── [COE TECH]_[LONG N.]_AI ORCHESTRATION - 0. Overview & Summary - 0. Overview & Summary.md
│   │   ├── [COE TECH]_[LONG N.]_AI ORCHESTRATION - 0. Overview & Summary - 1. Ultimate Blockers.md
│   │   └── ... (pages 2–5)
│   ├── [COE TECH]_[LONG N.]_AI ORCHESTRATION - 1. UBS/
│   │   ├── [COE TECH]_[LONG N.]_AI ORCHESTRATION - 1. UBS - 0. Overview & Summary.md
│   │   └── ...
│   ├── [COE TECH]_[LONG N.]_AI ORCHESTRATION - 2. UDS/
│   └── ... (chapters 3, 4, 5)
├── [COE TECH]_[LONG N.]_AI ORCHESTRATION - D. Distill Understanding/
└── [COE TECH]_[LONG N.]_AI ORCHESTRATION - E. Express Expertise/
```

---

## 5. Checklist when creating a new subject

1. **Choose identifiers:** COE area code (e.g. `COE TECH`), member (e.g. `LONG N.`), subject name (e.g. `AI ORCHESTRATION`).
2. **Subject root:** Create folder with **slug** only, e.g. `COE_TECH_LONG_N_AI_ORCHESTRATION`. Add the area to `config/coe-map.yaml` with this `id` if sync will be used.
3. **Prefix:** Set `PREFIX = [COE AREA]_[MEMBER]_SUBJECT NAME - ` (with spaces as in §2).
4. **Phase folders:** Create `{PREFIX}A. Subject Roadmap & Level Specifications`, `{PREFIX}B. Capture Facts & Data`, etc.
5. **Topic folders:** Under Phase C, create `{PREFIX}0. Overview & Summary`, `{PREFIX}1. UBS`, … `{PREFIX}5. EOP`.
6. **A file:** Create `[COE AREA]_[MEMBER]_A. SUBJECT - SUBJECT ROADMAP & LEVEL SPECIFICATIONS.md` inside the Phase A folder (from `templates/A-subject-roadmap-and-level-specifications.md`).
7. **Page files:** When creating any page from templates, name the file `{PREFIX}{Chapter} - {Page}.md` (e.g. `{PREFIX}1. UBS - 3. Principles.md`). Use the templates under `templates/`; each template’s “Naming (Learning Book)” section repeats this rule.
8. **Pointers:** Update `_CONTEXT_ANCHOR.md`, `CLAUDE.md`, and any handoff/status docs with the new subject root and A file path.

---

## 6. Relation to ClickUp

Company ClickUp COE spaces use names like `[COE TECH]_TECHNOLOGY EXCELLENCE`, with sub-spaces `[COE TECH CS]`, `[COE TECH AI]`, etc. The Learning Book prefix mirrors this so that when sync (T-403) or mapping (T-402) runs, the path `learning-book/{area_id}/` and the prefixed phase/topic/page names can map to the correct ClickUp location (e.g. a future `[COE TECH AI]` sub-space for this subject).
