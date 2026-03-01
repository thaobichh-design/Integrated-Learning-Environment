# Template: Page 3 — EPS (Effective Principle System)

_Page type: Principles — the governing rules of this Topic (Phase C. Organise Information)._

---

## Naming (Learning Book)

When creating or updating a page under a subject, **all** phase folders, topic folders, and page files must use the **subject prefix** so the structure matches the company ClickUp COE naming and sync works.

- **Prefix:** `[COE AREA]_[MEMBER]_SUBJECT NAME - ` (e.g. `[COE TECH]_[LONG N.]_AI ORCHESTRATION - `).
- **This page type** → file name: `{PREFIX}{Chapter} - {Page}.md` (e.g. `{PREFIX}1. UBS - 3. Principles.md`).
- **Full rule:** `docs/ai/implementation/ile-learning-book-naming-convention.md`.

---

## Purpose

Page 3 **consolidates all principles already embedded in Pages 0, 1, and 2** of this same Topic into one place. It does NOT generate new principles — it harvests them. Each principle either enables a UDS element or disables a UBS element from this Topic. State explicitly which.

---

## S/E/Sc Labeling (MANDATORY)

**Every principle must be labeled with its Effectiveness pillar.** This bucketing happens during ELF — not later during ESD. The label tells the agent which pillar this principle serves when translated into Adverb A.C.s.

- **P[n](S)** — Sustainability principle: governs correct, safe, risk-managed operation. Primarily disables UBS elements.
- **P[n](E)** — Efficiency principle: governs fast, lean, frugal operation. Primarily enables UDS elements via speed/resource optimization.
- **P[n](Sc)** — Scalability principle: governs repeatable, comparable, growth-capable operation. Primarily enables UDS elements at recursive depth.

**How to determine the pillar:**

- Ask: "Does this principle prevent failure/harm (S), reduce waste/time (E), or enable growth/repeatability (Sc)?"
- If a principle spans two pillars, assign it to the _higher-priority_ pillar (S > E > Sc) — Sustainability always wins.
- The pillar label goes in the row label: `P1(S)`, `P2(E)`, `P3(Sc)`, etc.

---

## Row Structure (all Topics)

- **N rows — one principle per row**
- Rows are collected from:
  - Page 0: col 6 (EPS from success side) + col 12 (Risky Principles from failure side)
  - Page 1: col 6 + col 12 from each row
  - Page 2: col 6 + col 12 from each row
- Row labels: `P1(S)`, `P2(E)`, `P3(Sc)` ... (sequential, with S/E/Sc pillar label)
- Each principle must explicitly state: **"Enables [UDS element]"** OR **"Disables [UBS element]"**

### Principle count guide

- Topic 0: ~2–4 principles (overview depth — sparse, not greedy)
- Topics 1–5: ~4–8 principles (deeper layers uncovered = more principles derivable)

### Pillar distribution guide

- At overview depth (Topic 0), expect mostly (S) principles — Sustainability is the foundation.
- Deeper Topics (1–5) will surface more (E) and (Sc) principles as recursive UDS layers are uncovered.
- There is no required ratio — the distribution is driven by the UBS/UDS content, not by quota.

---

## Causal Logic

Principles are NOT generic best practices. They are **the scientific or logical laws** that explain why the UDS works and why the UBS blocks. Derive them by asking:

- "Why does this driver work? What universal principle does it operate on?"
- "Why does this blocker form? What universal principle does it exploit?"

Respect the Hierarchy of Science when identifying which layer the principle operates at:
`Sociology → Psychology → Biology → Chemistry → Physics → Mathematics → Logic → Philosophy`

---

## Format

```markdown
# Topic {X}. {Topic Name} — Page 3: Principles

_Phase C. Organise Information | Topic: {X}. {Topic Name} | Page: 3. Principles_
_Subject: AI Orchestration / Engineering | UDO: ..._

---

## Column Key

[standard 16-question key — see CLAUDE.md §6 for full Perspective Rule + revised Column Key]

---

## Table

| Row        | 1 · Relevance | 2 · Precise Definition | 3 · Success Actions | 4 · UDS | 5 · Success Mechanism | 6 · Success EPS | 7 · Success Tools (UES) | 8 · Success Environment (UES) | 9 · Failure Actions | 10 · UBS | 11 · Failure Mechanism | 12 · Failure EPS | 13 · Failure Tools (UES) | 14 · Failure Environment (UES) | 15 · What Else? | 16 · Next Steps |
| ---------- | ------------- | ---------------------- | ------------------- | ------- | --------------------- | --------------- | ----------------------- | ----------------------------- | ------------------- | -------- | ---------------------- | ---------------- | ------------------------ | ------------------------------ | --------------- | --------------- |
| **P1(S)**  |               |                        |                     |         |                       |                 |                         |                               |                     |          |                        |                  |                          |                                |                 |                 |
| **P2(S)**  |               |                        |                     |         |                       |                 |                         |                               |                     |          |                        |                  |                          |                                |                 |                 |
| **P3(E)**  |               |                        |                     |         |                       |                 |                         |                               |                     |          |                        |                  |                          |                                |                 |                 |
| **P4(Sc)** |               |                        |                     |         |                       |                 |                         |                               |                     |          |                        |                  |                          |                                |                 |                 |
```

---

## Rules

- Do NOT invent principles not derivable from Pages 0–2 of this Topic.
- Each principle row must explicitly name which UDS or UBS element it links to in col 1 (Relevance).
- **Every principle must carry a pillar label: (S), (E), or (Sc).** This is required for ESD translation.
- Principles accumulate across Topics — Topic 1 principles build on Topic 0 principles; later Topics add more.
- Do not be greedy — fewer precise principles > many vague ones.
- If a principle from a prior Topic is now better understood, it may be refined in a deeper Topic — but the pillar label must remain consistent (or be explicitly corrected with a note in A's Decisions log, in the Phase C Organise — state section).
