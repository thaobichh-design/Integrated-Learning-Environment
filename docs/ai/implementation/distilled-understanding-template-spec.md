# D. Distilled Understanding — Template spec

**Source of truth:** `templates/D-distilled-understanding-full.md` (canonical markdown for the full subject-level D. Distilled Understanding table).

**Regenerating from PDF:** To avoid broken columns/rows or merged cells, generate the canonical from the original PDF (or ClickUp export PDF) using the repo script:

```bash
pip install -r scripts/requirements-pdf.txt
python scripts/pdf_table_to_md.py /path/to/D-distilled-understanding.pdf -o templates/D-distilled-understanding-full.md
```

Use `--strategy text` if the PDF has no grid lines and table detection fails. Use `--no-intro` if the first page is all table.

This spec documents structure and mapping so the Learning Book and Page 7 template stay aligned with the canonical template without omission.

---

## 1. Canonical template

- **File:** `templates/D-distilled-understanding-full.md`
- **Scope:** One **subject** (e.g. Effective Data Science). One table covers all 6 core topics and their sub-topics.
- **Banner:** Title `[OWNER]_SUBJECT NAME - D. DISTILLED UNDERSTANDING`, intro text (7 components EU, EA, EO, EP, EOE, EOT, EOP; Effective Principles; table purpose).

---

## 2. Table structure

### 2.1 Top-level columns (7)

| # | Column | Content |
|---|--------|--------|
| 1 | **DISTILLED UNDERSTANDING** | Row label (e.g. EFFECTIVE + NAME OF SUBJECT) |
| 2 | **6 CORE TOPICS** | Topic / sub-topic labels (0, 1–UBS, 2–UDS, 3–EP, 4–EOE, 5–EOT, 5–EOP) |
| 3 | **DESCRIPTION OF THE TOPIC & KEY TOPIC QUESTIONS** | Topic description and Basic/Advanced questions |
| 4 | **30 CORE SUB-TOPICS** | Sub-topic label (e.g. 1.0, 1.1, …, 1.6) |
| 5 | **14 CORE SUB-TOPIC QUESTIONS…** | OVERVIEW + SUCCESS (7) + FAILURE (6) |
| 6 | (empty) | — |
| 7 | **LEARNER'S NOTES** | What else? / Others / Now What? Now How? |

### 2.2 Content columns (14 + 3)

- **OVERVIEW (1):** What is it for? Why is it important? (Relevance)
- **SUCCESS (7):** What is it? (Introduction) | How does it work successfully? (Success Actions) | What ultimately cause it to work successfully? (Ultimate Drivers) | How do the ultimate drivers cause it to work successfully? (Success Mechanism) | What principles are the ultimate drivers based on? (Success Principles) | What environmental conditions do the ultimate drivers require to work? (Success Environment) | What tool(s) do ultimate drivers require to work? (Success Tools)
- **FAILURE (6):** How can it fail? (Failure Actions) | What ultimately cause it to fail? (Ultimate Blockers) | How do the ultimate blockers cause it to fail? (Failure Mechanism) | What principles are the ultimate blockers based on? (Failure Principles) | What environmental conditions do the ultimate blockers require to work? (Failure Environments) | What tool(s) the ultimate blockers require to work? (Failure Tools)
- **LEARNER'S NOTES (3):** What to do if it fails? (What else?) | Other Questions (Others) | Next Steps to Take (Now What? Now How?)

---

## 3. Row structure (6 core topics → sub-topics)

| Core topic | Label | Sub-topic rows | Page (per-topic book) |
|------------|--------|----------------|------------------------|
| 0 | Overview & Summary | 0 (Subject, EO, EA) | Page 0 |
| 1 | UBS (Ultimate Blocking System) | 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6 | Page 0 → 1.0; Page 1 → 1.1; …; Page 6 → 1.6 |
| 2 | UDS (Ultimate Driving System) | 2.0–2.6 | Page 0–6 (within UDS topic) |
| 3 | EP (Effective Principles) | 3.0–3.5 | Page 0–5 (within EP topic) |
| 4 | EOE (Effective Operating Environment) | 4.0–4.5 | Page 0–5 (within EOE topic) |
| 5 | EOT (Effective Operating Tools) | 4.0–4.5 (EOT rows in canonical) | Page 0–5 (within EOT topic) |
| 5 | EOP (Effective Operating Procedure) | 5.0–5.5 | Page 0–5 (within EOP topic) |

---

## 4. Page → block mapping (within one topic)

For a **topic file** (e.g. "1. UBS"), content from each page maps to one sub-topic row in the distilled table:

| Page | Block (sub-topic row) | Content focus |
|------|------------------------|---------------|
| 0 | X.0 | Overview & Summary of the topic |
| 1 | X.1 | Ultimate Blockers (or equivalent) |
| 2 | X.2 | Ultimate Drivers |
| 3 | X.3 | Core Values & Principles |
| 4 | X.4 | Environment (or Components) |
| 5 | X.5 | Tools (or Procedure summary) |
| 6 | X.6 | Steps to Overcome / Procedure (UBS/UDS only) |

**Rule:** All content from pages 0–5 (and 6 where applicable) for a topic maps into exactly one block (X.0–X.6) in the subject’s D. Distilled Understanding table.

---

## 5. Page 7 (Topic Distilled Understanding)

- **Template:** `templates/page-7-topic-distilled-understanding.md`
- **Use:** When `(chapter, topic, page=7)` → load this template.
- **Meaning:** Page 7 holds the **topic-level slice** of the full D. Distilled Understanding table: one core topic’s sub-rows (e.g. for topic 1 UBS: rows 1.0, 1.1, …, 1.6) with the same 14+3 column structure.
- **Canonical alignment:** Column headers and row labels must match `templates/D-distilled-understanding-full.md`. Page 7 does not add or drop columns; it shows one topic’s block of rows.

---

## 6. Checklist for no omission

- [ ] Banner and intro text match canonical.
- [ ] Table has OVERVIEW | SUCCESS (7) | FAILURE (6) | LEARNER'S NOTES (3).
- [ ] Row labels match canonical (1.0–1.6 for UBS; 2.0–2.6 for UDS; etc.).
- [ ] Page 7 template references `templates/D-distilled-understanding-full.md` and uses the same column set.
- [ ] When generating or filling D. Distilled Understanding, every page 0–6 for a topic is mapped to the correct block X.0–X.6.
