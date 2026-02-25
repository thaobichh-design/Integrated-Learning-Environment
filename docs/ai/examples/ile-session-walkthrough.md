# ILE Concrete Session Walkthrough (T-409)

*Step-by-step transcript of a real learning session: user input → Agent response → file changes. Onboarding reference and regression baseline. Noun-AC13.*

**Context:** Learner in Cursor with Integrated-Learning-Environment repo open. Subject: COE_DS (Data Science). A (Subject Roadmap) already exists for this subject.

---

## Step 1: User opens session and chooses to resume

**I typed:** `Resume COE_DS`

**Agent did:** Read `learning-book/COE_DS/A. Subject Roadmap & Level Specifications/` (A), oriented from Learner Progress Tracker and Session Log, then replied in chat with current level, last entry point, and next recommended entry. No file was written.

**File changed:** None.

---

## Step 2: Agent offers phase choice

**Agent said:** "Which phase? **B.** Capture Facts & Data | **C.** Organise Information | **D.** Distill Understanding."

**I typed:** `C`

**Agent did:** Listed entry points for Phase C (6 chapters × 6 topics) from the Learning Map, informed by A. No file was written.

**File changed:** None.

---

## Step 3: User selects entry point

**I typed:** `Chapter 1 UBS, Topic 1 Ultimate Blockers`

**Agent did:** Resolved entry point to (chapter 1, topic 1); loaded template `templates/page-1-ultimate-blockers.md` per entry-point-to-template-mapping; scoped conversation and document context to target file `learning-book/COE_DS/C. Organise Information/1. UBS/1. UBS - 1. Ultimate Blockers.md` and the relevant section (e.g. SUBJECT CONTENT row for one question). No file was written yet.

**File changed:** None.

---

## Step 4: Learning conversation — one Q&A

**I typed:** `What is the main blocker for me when learning data science? I think it's time management.`

**Agent did:** Elicited and proposed content (e.g. one cell for "What ultimately cause it to fail? (Ultimate Blocking System)" or similar canonical question from the template). Agent stated the target file and section and proposed a short sentence for the SUBJECT CONTENT cell.

**File changed:** None (proposal only; write only after approval).

---

## Step 5: User approves; Agent writes to Learning Book

**I typed:** `Approve`

**Agent did:** Wrote the approved content to `learning-book/COE_DS/C. Organise Information/1. UBS/1. UBS - 1. Ultimate Blockers.md` in the correct table cell (SUBJECT CONTENT row, column matching the question). Confirmed in chat: "✓ [component] updated. Chunk complete."

**File changed:** `learning-book/COE_DS/C. Organise Information/1. UBS/1. UBS - 1. Ultimate Blockers.md` — one or more table cells in the SUBJECT CONTENT row updated with the agreed text (e.g. time management as UBS).

---

## Step 6: User switches entry point (Step 7 Checkpoint)

**I typed:** `Switch to Chapter 2 UDS, Topic 0`

**Agent did:** Prompted: "Save current progress before switching? Approve to write to the doc and update A." User approved. Agent committed any in-progress content to the doc, optionally appended a row to A's Session Log (Date, Entry Point, Progress), then loaded the new entry point (Chapter 2 UDS, Topic 0) and template.

**File changed:** `learning-book/COE_DS/A. Subject Roadmap & Level Specifications/[COE DS]_[OWNER]_A. DATA SCIENCE - SUBJECT ROADMAP & LEVEL SPECIFICATIONS.md` — Session Log appended with one row (date, "1. UBS - 1. Ultimate Blockers", progress note). Optionally no A change if User deferred.

---

## Summary (regression checklist)

| Step | User input (X)        | Agent action (Y)                    | File updated (Z) | Content (W) |
|------|------------------------|-------------------------------------|------------------|------------|
| 1    | Resume COE_DS          | Read A, orient, reply               | —                | —          |
| 2    | C                      | List entry points for Phase C       | —                | —          |
| 3    | Chapter 1 UBS, Topic 1 | Load template, scope to target file | —                | —          |
| 4    | Q&A + content          | Propose text for one cell           | —                | —          |
| 5    | Approve                | Write to target file/section        | `.../1. UBS - 1. Ultimate Blockers.md` | SUBJECT CONTENT cell |
| 6    | Switch + Approve       | Commit, append A Session Log       | A (Session Log)  | One log row |

**Cross-references:** Flow → `docs/ai/implementation/ile-minimal-flow.md` | Entry→Template → `entry-point-to-template-mapping.md` | Conversation→Doc → `ile-conversation-to-doc-mapping.md` | Rule → `.cursor/rules/ile-learning-book.mdc`.
