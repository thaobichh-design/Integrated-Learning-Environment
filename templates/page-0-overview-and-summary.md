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

## Column Key

| # | Group | Question |
|---|---|---|
| 1 | INTRODUCTION | What is it for? Why is it important? (Relevance) |
| 2 | INTRODUCTION | What is it? (Introduction) |
| 3 | SUCCESS | How does it work successfully? (Effective Operating Procedure) |
| 4 | SUCCESS | What ultimately causes it to work successfully? (Ultimate Driving System) |
| 5 | SUCCESS | How does the UDS cause it to work successfully? (Success Mechanism) |
| 6 | SUCCESS | What principles is the UDS based on? (Effective Principle System) |
| 7 | SUCCESS | What tools do the ultimate drivers require? (Ultimate Effective System) |
| 8 | SUCCESS | What environmental conditions do the ultimate drivers require? (Ultimate Effective System) |
| 9 | FAILURE | How can it fail? (Failure Actions) |
| 10 | FAILURE | What ultimately causes it to fail? (Ultimate Blocking System) |
| 11 | FAILURE | How does the UBS cause it to fail? (Failure Mechanism) |
| 12 | FAILURE | What principles are the blockers based on? (Risky Principles) |
| 13 | FAILURE | What tools do the blockers require? (Risky Tools) |
| 14 | FAILURE | What environmental conditions do the blockers require? (Risky Environments) |
| 15 | LEARNER'S NOTE | What to do if it fails? (What else?) |
| 16 | LEARNER'S NOTE | Next Steps to Take (Now What? Now How?) |

---

## Table

| Row | 1 · Relevance | 2 · Introduction | 3 · EOP | 4 · UDS | 5 · Success Mechanism | 6 · EPS | 7 · Tools (UES) | 8 · Environment (UES) | 9 · Failure Actions | 10 · UBS | 11 · Failure Mechanism | 12 · Risky Principles | 13 · Risky Tools | 14 · Risky Environment | 15 · What Else? | 16 · Next Steps |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Effective {Subject Name}** | | | | | | | | | | | | | | | | |
```

---

## Rules

- **Do not add more than 1 row for Topic 0 Page 0.** Overview depth only.
- **Do not generate for Topics 1–5 Page 0.** Copy the file instead.
- Col 4 (UDS) and Col 10 (UBS) in this row become the seed for Pages 1 and 2 respectively.
