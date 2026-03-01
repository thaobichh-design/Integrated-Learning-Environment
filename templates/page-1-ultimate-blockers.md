# Template: Page 1 — UBS / UB Layer

_Page type: Ultimate Blockers — the blocking side of this Topic (Phase C. Organise Information)._

---

## Naming (Learning Book)

When creating or updating a page under a subject, **all** phase folders, topic folders, and page files must use the **subject prefix** so the structure matches the company ClickUp COE naming and sync works.

- **Prefix:** `[COE AREA]_[MEMBER]_SUBJECT NAME - ` (e.g. `[COE TECH]_[LONG N.]_AI ORCHESTRATION - `).
- **This page type** → file name: `{PREFIX}{Chapter} - {Page}.md` (e.g. `{PREFIX}1. UBS - 1. Ultimate Blockers.md`).
- **Full rule:** `docs/ai/implementation/ile-learning-book-naming-convention.md`.

---

## Purpose

Page 1 explores the **blocking layer** of this Topic. It answers: what ultimately causes this system/element to fail? Then it goes one layer deeper: what disables that blocker (UB), and what drives that blocker harder (UD)?

---

## Row Structure

### Topic 0 (Root)

- **1 row only**
- Row label: the main UBS (root blocker for the entire subject)
- Source: derived from Topic 0 Page 0, col 10 · UBS
- Do not go deeper than the root UBS here — deeper layers belong in Topic 1.

### Topics 1–5 (Deep-Dive)

- **3 rows**
- Row 1 label: `UBS: {Hierarchical Name} - {parent}.UB: {Description}` — derived from **this Topic's Page 0, col 10 · UBS**
- Row 2 label: `{parent}.UB: {Description from Row 1} - {parent}.UB.UB: {Description}` — derived from **Row 1, col 10 · UBS**
- Row 3 label: `{parent}.UB: {Description from Row 1} - {parent}.UB.UD: {Description}` — derived from **Row 1, col 4 · UDS**

### Notation guide for this page

```
Topic 1 → UBS.UB (row1), UBS.UB.UB (row2), UBS.UB.UD (row3)
Topic 2 → UDS.UB (row1), UDS.UB.UB (row2), UDS.UB.UD (row3)
Topic 3 → EPS.UB (row1), EPS.UB.UB (row2), EPS.UB.UD (row3)
Topic 4 → UES.UB (row1), UES.UB.UB (row2), UES.UB.UD (row3)
Topic 5 → EOP.UB (row1), EOP.UB.UB (row2), EOP.UB.UD (row3)
```

---

## Causal Logic

- **Row 1 (.UB)**: The single most critical blocker of the parent element. Works IN User's favour (disables the parent blocker or blocks the parent driver).
- **Row 2 (.UB.UB)**: What disables Row 1. If Row 1 gets blocked, its disabling effect disappears — works AGAINST User.
- **Row 3 (.UB.UD)**: What drives Row 1 harder. Makes Row 1 even more effective — works further IN User's favour.

Each row builds causally on the previous. **One blocker or driver per row. Never list multiples.**

---

## Principles embedded in this page

Each row's col 6 (EPS) and col 12 (Risky Principles) generate principles. These are harvested into Page 3. Do not skip those cells.

---

## Format

```markdown
# Topic {X}. {Topic Name} — Page 1: Ultimate Blockers

_Phase C. Organise Information | Topic: {X}. {Topic Name} | Page: 1. Ultimate Blockers_
_Subject: AI Orchestration / Engineering | UDO: ..._

---

## Column Key

[standard 16-question key — see CLAUDE.md §6 for full Perspective Rule + revised Column Key]

---

## Table

| Row                                                                       | 1 · Relevance | 2 · Precise Definition | 3 · Success Actions | 4 · UDS | 5 · Success Mechanism | 6 · Success EPS | 7 · Success Tools (UES) | 8 · Success Environment (UES) | 9 · Failure Actions | 10 · UBS | 11 · Failure Mechanism | 12 · Failure EPS | 13 · Failure Tools (UES) | 14 · Failure Environment (UES) | 15 · What Else? | 16 · Next Steps |
| ------------------------------------------------------------------------- | ------------- | ---------------------- | ------------------- | ------- | --------------------- | --------------- | ----------------------- | ----------------------------- | ------------------- | -------- | ---------------------- | ---------------- | ------------------------ | ------------------------------ | --------------- | --------------- |
| **UBS: {Hierarchical Name} - {parent}.UB: {Description}**                 |               |                        |                     |         |                       |                 |                         |                               |                     |          |                        |                  |                          |                                |                 |                 |
| **{parent}.UB: {Description from Row 1} - {parent}.UB.UB: {Description}** |               |                        |                     |         |                       |                 |                         |                               |                     |          |                        |                  |                          |                                |                 |                 |
| **{parent}.UB: {Description from Row 1} - {parent}.UB.UD: {Description}** |               |                        |                     |         |                       |                 |                         |                               |                     |          |                        |                  |                          |                                |                 |                 |
```

---

## Rules

- Topic 0: 1 row (root UBS only).
- Topics 1–5: 3 rows (root.UB + root.UB.UB + root.UB.UD).
- Row 1 derives from this Topic's P0, col 10.
- Rows 2–3 derive from Row 1.
- Principles in col 6 and col 12 of each row feed into Page 3.
