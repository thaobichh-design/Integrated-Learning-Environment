# Learning Book (ILE)

One Learning Book per COE Area. This structure validates SustainAdv-AC1: same path → same logical place.

**Naming:** All phase folders, topic folders, and page files **must** use the **subject prefix** so the structure matches the company ClickUp COE naming. Full rule: **`docs/ai/implementation/ile-learning-book-naming-convention.md`**. Summary: subject root = slug (e.g. `COE_TECH_LONG_N_AI_ORCHESTRATION`); prefix = `[COE AREA]_[MEMBER]_SUBJECT NAME - `; phases/topics/pages = `{PREFIX}A. ...`, `{PREFIX}1. UBS - 0. Overview & Summary.md`, etc.

**Cross-references:** Full tree map (6 Chapters, 6 Topics, 7 pages, D/E per member) → `docs/ai/implementation/learning-book-tree-map.md` | **Naming convention** → `docs/ai/implementation/ile-learning-book-naming-convention.md` | Flow → `ile-minimal-flow.md` | Entry→Template → `entry-point-to-template-mapping.md`

## Minimal Structure (Iteration 1 stub — T-102)

_This folder is a minimal stub. The full company structure (Area → 6 Chapters → 6 Topics → Personal Learning Area per member → 7 pages) is in `learning-book-tree-map.md`. **Folder and file names must follow the prefix rule** in `ile-learning-book-naming-convention.md`._

```
learning-book/{subject_slug}/   e.g. COE_TECH_LONG_N_AI_ORCHESTRATION
├── [COE AREA]_[MEMBER]_SUBJECT - A. Subject Roadmap & Level Specifications/
├── [COE AREA]_[MEMBER]_SUBJECT - B. Capture Facts & Data/
├── [COE AREA]_[MEMBER]_SUBJECT - C. Organise Information/
│   ├── [COE AREA]_[MEMBER]_SUBJECT - 0. Overview & Summary/
│   ├── [COE AREA]_[MEMBER]_SUBJECT - 1. UBS/   (Ultimate Blocking System)
│   ├── [COE AREA]_[MEMBER]_SUBJECT - 2. UDS/   (Ultimate Driving System)
│   ├── [COE AREA]_[MEMBER]_SUBJECT - 3. EPS/   (Effective Principle System)
│   ├── [COE AREA]_[MEMBER]_SUBJECT - 4. UES/   (Ultimate Effective System)
│   └── [COE AREA]_[MEMBER]_SUBJECT - 5. EOP/   (Effective Operating Procedure)
├── [COE AREA]_[MEMBER]_SUBJECT - D. Distill Understanding/
└── [COE AREA]_[MEMBER]_SUBJECT - E. Express Expertise/
```

## Example

`COE_TECH_LONG_N_AI_ORCHESTRATION/` = COE TECH, member LONG N., subject AI Orchestration (slug matches area id for sync). `COE_DS/` = COE Data Science. When creating a new subject, follow `ile-learning-book-naming-convention.md`.

## Full Structure (company / ClickUp)

Per `learning-book-tree-map.md`: Area → A/B/C/D/E (D and E have per-member subpages) → 6 Chapters (each with A/B/C/D/E + 6 Topics) → each Topic: Personal Learning Area per member → 7 pages (0–5 + Page 7 Topic Distilled Understanding).

## Pre-populating Phase C (all entry points)

To create all 36 topic files with full 7-page structure so you can start at any (chapter, topic, page) without waiting for creation:

```bash
python scripts/populate_learning_book_phase_c.py [subject]
```

Default subject is `COE_DS`. Each file contains Page 0–5 and Page 7 (Topic Distilled Understanding) from the canonical templates. Re-running overwrites existing topic files.

## Verification

Run `scripts/check-learning-book-structure.sh` to verify the minimal structure.
