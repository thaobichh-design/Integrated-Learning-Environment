# ILE Concrete Session Walkthrough (T-409)

_Step-by-step transcript of a real learning session: user input → Agent response → file changes. Onboarding reference and regression baseline. Noun-AC13._

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

**Agent did:** Resolved entry point to (chapter 1, topic 1); loaded template `templates/page-1-ultimate-blockers.md` per entry-point-to-template-mapping; scoped conversation and document context to target file `learning-book/COE_TECH_LONG_N_AI_ORCHESTRATION/[COE TECH]_[LONG N.]_AI ORCHESTRATION - C. Organise Information/[COE TECH]_[LONG N.]_AI ORCHESTRATION - 1. UBS/[COE TECH]_[LONG N.]_AI ORCHESTRATION - 1. UBS - 1. Ultimate Blockers.md` and the relevant section (e.g. SUBJECT CONTENT row for one question). No file was written yet.

**File changed:** None.

---

## Step 4: Learning conversation — one Q&A

**I typed:** `What is the main blocker for me when learning data science? I think it's time management.`

**Agent did:** Elicited and proposed content (e.g. one cell for "What ultimately cause it to fail? (Ultimate Blocking System)" or similar canonical question from the template). Agent stated the target file and section and proposed a short sentence for the SUBJECT CONTENT cell.

**File changed:** None (proposal only; write only after approval).

---

## Step 5: User approves; Agent writes to Learning Book

**I typed:** `Approve`

**Agent did:** Wrote the approved content to `learning-book/COE_TECH_LONG_N_AI_ORCHESTRATION/[COE TECH]_[LONG N.]_AI ORCHESTRATION - C. Organise Information/[COE TECH]_[LONG N.]_AI ORCHESTRATION - 1. UBS/[COE TECH]_[LONG N.]_AI ORCHESTRATION - 1. UBS - 1. Ultimate Blockers.md` in the correct table cell (SUBJECT CONTENT row, column matching the question). Confirmed in chat: "✓ [component] updated. Chunk complete."

**File changed:** `learning-book/COE_TECH_LONG_N_AI_ORCHESTRATION/[COE TECH]_[LONG N.]_AI ORCHESTRATION - C. Organise Information/[COE TECH]_[LONG N.]_AI ORCHESTRATION - 1. UBS/[COE TECH]_[LONG N.]_AI ORCHESTRATION - 1. UBS - 1. Ultimate Blockers.md` — one or more table cells in the SUBJECT CONTENT row updated with the agreed text (e.g. time management as UBS).

---

## Step 6: User switches entry point (Step 7 Checkpoint)

**I typed:** `Switch to Chapter 2 UDS, Topic 0`

**Agent did:** Prompted: "Save current progress before switching? Approve to write to the doc and update A." User approved. Agent committed any in-progress content to the doc, optionally appended a row to A's Session Log (Date, Entry Point, Progress), then loaded the new entry point (Chapter 2 UDS, Topic 0) and template.

**File changed:** `learning-book/COE_DS/A. Subject Roadmap & Level Specifications/[COE DS]_[OWNER]_A. DATA SCIENCE - SUBJECT ROADMAP & LEVEL SPECIFICATIONS.md` — Session Log appended with one row (date, "1. UBS - 1. Ultimate Blockers", progress note). Optionally no A change if User deferred.

---

## Step 7 (Optional): Self-check before practice (T-305)

**Scenario:** Learner has completed all Phase C pages for Level 1 (A → Approved Pages shows all required pages). Agent detects this and offers a self-check.

**Agent said:** "✅ You've completed all Level 1 learning content (Chapter 0 Overview + Chapter 1 UBS pages 0–1). Would you like a self-check before you start Level 1 practice? This is optional; I can guide you through a quick checklist, or you can jump straight to practice."

**I typed:** `Yes, let's do the self-check.`

**Agent did:**

1. Confirmed target level: "Great. We're checking readiness for Level 1."
2. Presented Level Requirements from A: "Level 1 requires: (1) Explain the difference between a chatbot and an agent; (2) Install Agno; (3) Build and run a Finance Agent with YFinance."
3. Asked conceptual questions based on Chapter 0 & 1 content (e.g., "What's a key difference between an agent and a chatbot?" → User answered ✅)
4. Identified any gaps (none in this scenario)
5. Recommended: "You're ready for Level 1 practice."
6. Appended A's Session Log: "| 2026-03-01 | Self-check L1 | Completed; no gaps. Ready for L1 practice. |"

**File changed:** `learning-book/COE_DS/A. Subject Roadmap & Level Specifications/.../A. ...md` — Session Log appended with self-check result.

**No file written for learning content; self-check is diagnostic only.**

---

## Summary (regression checklist)

| Step | User input (X)                        | Agent action (Y)                                               | File updated (Z)                                                | Content (W)                                   |
| ---- | ------------------------------------- | -------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------- |
| 1    | Resume COE_DS                         | Read A, orient, reply                                          | —                                                               | —                                             |
| 2    | C                                     | List entry points for Phase C                                  | —                                                               | —                                             |
| 3    | Chapter 1 UBS, Topic 1                | Load template, scope to target file                            | —                                                               | —                                             |
| 4    | Q&A + content                         | Propose text for one cell                                      | —                                                               | —                                             |
| 5    | Approve                               | Write to target file/section                                   | `.../1. UBS - 1. Ultimate Blockers.md`                          | SUBJECT CONTENT cell                          |
| 6    | Switch + Approve                      | Commit, append A Session Log                                   | A (Session Log)                                                 | One log row                                   |
| 7    | Self-check (optional)                 | Ask 5–10 diagnostic questions; recommend                       | A (Session Log)                                                 | Self-check result                             |
| 8    | Practice complete + rubric (optional) | Walk through credentials; validate evidence; record proof      | A (Level Completion Checklist, Proof Landing Zone, Session Log) | Proof links + completion status               |
| 9    | Level progression (optional)          | Read A Level→Scope; compare approved pages; suggest next level | A (Level→Phase C Scope, Approved Pages)                         | Scope gap analysis; next level recommendation |

**Cross-references:** Flow → `docs/ai/implementation/ile-minimal-flow.md` | Self-check before → T-305 `ile-self-check-before-practice.md` | Rubric after → T-306 `ile-rubric-walk-through-proof-recording.md` | Level scope → T-415 `ile-agent-reads-level-scope-gates.md` | Entry→Template → `entry-point-to-template-mapping.md` | Conversation→Doc → `ile-conversation-to-doc-mapping.md` | Rule → `.cursor/rules/ile-learning-book.mdc`.

---

## Step 8 (Optional): Rubric walk-through & proof recording (T-306)

**Scenario:** Learner has completed Level 1 practice (built the agent, has code and screenshots). Returns with evidence and claims completion. Agent offers rubric walk-through.

**Agent said:** "Great! I can walk through the Level 1 rubric to validate your work against the pass/fail criteria. This is optional; I can provide feedback, or you can submit as-is. What works for you?"

**I typed:** `Let's do the walk-through. I want to make sure it's solid.`

**Agent did:**

1. **Confirmed level and credentials:** "Level 1 has 3 credentials: (1) Working Python script with Agno Agent; (2) Screenshot with tool call visible; (3) Can articulate the difference between agent and chatbot."
2. **Walked through each credential:**
   - **Credential 1:** Agent asked for script path. Reviewed code. Verified: script exists, runs, uses YFinance tool, retrieves AAPL price. ✓ PASS
   - **Credential 2:** Agent asked for screenshot. Reviewed it. Verified: shows Agent output + YFinance tool call visible. ✓ PASS
   - **Credential 3:** Agent asked Learner to explain. Learner said: "An agent has a model, tools, instructions, and memory. A chatbot only has a model." ✓ PASS
3. **Summarized:** "All 3 credentials pass. You're ready for Level 2 practice!"
4. **Updated A:** Agent proposed update to Level Completion Checklist (L1: ✅ all pass) and Proof Landing Zone (linked code path, screenshot, and note on explanation). Learner approved. Agent wrote to A.

**File changed:** `learning-book/COE_DS/A. Subject Roadmap & Level Specifications/.../A. ...md` — Level Completion Checklist row for L1 updated with ✅ and date; Proof Landing Zone section added with evidence links.

**No file written for learning content; proof recording updated A only.**
