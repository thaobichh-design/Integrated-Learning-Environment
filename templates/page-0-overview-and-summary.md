# Template: Page 0 — Overview & Summary

*Page type: Overview & Summary (Phase C. Organise Information). Use for any Topic's Page 0.*

---

## Purpose

Page 0 is the **entry point** for the Topic. It gives a single high-level view of the entire subject of that Topic before any deep-dive begins.

---

## Row Structure

### Topic 0 (Root Overview)
- **1 row only**
- Row label: `Effective {Subject Name}` — e.g., `Effective AI Orchestration`
- All 16 columns filled at overview/surface depth. Do not go deep — deeper pages will cover that.

### Topics 1–5 (Deep-Dive Topics)
- **DUPLICATE the parent page — do not regenerate**
  - Topic 1 Page 0 = copy of Topic 0 Page 1 (UBS row)
  - Topic 2 Page 0 = copy of Topic 0 Page 2 (UDS row)
  - Topic 3 Page 0 = copy of Topic 0 Page 3 (EPS row)
  - Topic 4 Page 0 = copy of Topic 0 Page 4 (UES row)
  - Topic 5 Page 0 = copy of Topic 0 Page 5 (EOP row)
- Rename the file only. No content generation needed. This saves tokens and ensures continuity.

---

## Derivation Rules

| Column | Source |
|---|---|
| Col 10 · UBS | Becomes the row label for this Topic's Page 1 (UBS page) |
| Col 4 · UDS | Becomes the row label for this Topic's Page 2 (UDS page) |
| Col 6 · EPS | Seeds the principles for Page 3 |
| Col 7+8 · UES | Seeds the components/tools for Page 4 |
| Col 3 · EOP | Seeds the steps for Page 5 |

---

## Format (STRICT — pure markdown only)

```markdown
# Topic {X}. {Topic Name} — Page 0: Overview & Summary
*Phase C. Organise Information | Topic: {X}. {Topic Name} | Page: 0. Overview & Summary*
*Subject: AI Orchestration / Engineering | UDO: Build and master an OE System that any analyst/operator can use to build domain-specific UE systems.*

---

## Perspective Rule
> *All questions in cols 3–14 are answered from the row subject's own perspective. Identify the row subject type (Effective System / UDS / UBS) before filling cols 4 and 10. The direction of 'works' and 'fails' inverts depending on type.*

## Column Key

| # | Group | Question |
|---|---|---|
| 1 | INTRODUCTION | What is the row subject for? Why does it matter to the Learner? (Relevance) |
| 2 | INTRODUCTION | What is it precisely — and what is it NOT? (Precise Definition) |
| 3 | SUCCESS | How does the row subject operate when functioning as designed? *(UBS row: how does it block? UDS row: how does it drive?)* (Success Actions) |
| 4 | SUCCESS | What ultimately causes the row subject to function as designed? *(UBS row → UBS.UD: drives the blocker — works AGAINST Learner. UDS row → UDS.UD: drives the driver — works FOR Learner.)* (UDS) |
| 5 | SUCCESS | How does col 4 (UDS) cause the row subject to function as designed? (Success Mechanism) |
| 6 | SUCCESS | What principles is the UDS based on? (Success EPS) |
| 7 | SUCCESS | What tools do the ultimate drivers require? (Success Tools — UES) |
| 8 | SUCCESS | What environmental conditions do the ultimate drivers require? (Success Environment — UES) |
| 9 | FAILURE | How can the row subject fail to function as designed? *(UBS row: how does the blocker get disabled? UDS row: how does the driver get blocked?)* (Failure Actions) |
| 10 | FAILURE | What ultimately causes the row subject to fail to function as designed? *(UBS row → UBS.UB: disables the blocker — works FOR Learner. UDS row → UDS.UB: blocks the driver — works AGAINST Learner.)* (UBS) |
| 11 | FAILURE | How does col 10 (UBS) cause the row subject to fail? (Failure Mechanism) |
| 12 | FAILURE | What principles are the failure causes based on? (Failure EPS) |
| 13 | FAILURE | What tools do the failure causes require? (Failure Tools — UES) |
| 14 | FAILURE | What environmental conditions do the failure causes require? (Failure Environment — UES) |
| 15 | LEARNER'S NOTE | If the row subject fails as designed, what should the Learner do? (What Else?) |
| 16 | LEARNER'S NOTE | Next Steps to Take (Now What? Now How?) |

---

## Table

| Row | 1 · Relevance | 2 · Precise Definition | 3 · Success Actions | 4 · UDS | 5 · Success Mechanism | 6 · Success EPS | 7 · Success Tools (UES) | 8 · Success Environment (UES) | 9 · Failure Actions | 10 · UBS | 11 · Failure Mechanism | 12 · Failure EPS | 13 · Failure Tools (UES) | 14 · Failure Environment (UES) | 15 · What Else? | 16 · Next Steps |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Effective {Subject Name}** | | | | | | | | | | | | | | | | |
```

---

## Rules

- **Do not add more than 1 row for Topic 0 Page 0.** Overview depth only.
- **Do not generate for Topics 1–5 Page 0.** Copy the file instead.
- Col 4 (UDS) and Col 10 (UBS) in this row become the seed for Pages 1 and 2 respectively.
