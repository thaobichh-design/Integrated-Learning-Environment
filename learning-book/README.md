# Learning Book (ILE)

One Learning Book per COE Area. This structure validates SustainAdv-AC1: same path → same logical place.

**Cross-references:** Full tree map (6 Chapters, 6 Topics, 7 pages, D/E per member) → `docs/ai/implementation/learning-book-tree-map.md` | Flow → `ile-minimal-flow.md` | Entry→Template → `entry-point-to-template-mapping.md`

## Minimal Structure (Iteration 1 stub — T-102)

*This folder is a minimal stub. The full company structure (Area → 6 Chapters → 6 Topics → Personal Learning Area per member → 7 pages) is in `learning-book-tree-map.md`.*

```
[COE]_[Area]_[Subject]/
├── A. Subject Roadmap & Level Specifications/
├── B. Capture Facts & Data/
├── C. Organise Information/
│   ├── 0. Overview & Summary/
│   ├── 1. UBS/   (Ultimate Blocking System)
│   ├── 2. UDS/   (Ultimate Driving System)
│   ├── 3. EPS/   (Effective Principle System)
│   ├── 4. UES/   (Ultimate Effective System)
│   └── 5. EOP/   (Effective Operating Procedure)
├── D. Distill Understanding/
└── E. Express Expertise/
```

## Example

`COE_DS/` = COE Data Science (COE_DS = short for [COE DS]; Data Science is an Area. EFF = Effectiveness is another Area).

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
