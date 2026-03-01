---
phase: implementation
title: ILE Rubric Walk-Through & Proof Recording (T-306)
description: Procedure and Agent behaviour for walking through level rubrics when User returns from practice; Agent helps record evidence in proof landing zone and updates Level Completion Checklist. Verb-AC12, EffAdv-AC5, EffAdj-AC6.
feature: integrated-learning-environment
task: T-306
---

# ILE Rubric Walk-Through & Proof Recording

*When the User returns from level practice and claims completion, the Agent offers an optional rubric walk-through (Agent-assisted self-check). The Agent guides the Learner through each Credential for that level, checks evidence against pass/fail criteria, and helps record evidence in the proof landing zone (A). Proof capture happens in-conversation as a byproduct; no separate export or copy-paste step. The Learner always chooses: accept feedback, revisit, or resubmit.*

**Cross-references:** Flow → `docs/ai/implementation/ile-minimal-flow.md` | Self-check before → T-305 `ile-self-check-before-practice.md` | A (checkpoint) → `ile-minimal-flow.md` § A. Subject Roadmap | A template (proof/rubrics/scope) → T-414 (pending) | Rule → `.cursor/rules/ile-learning-book.mdc`

---

**Acceptance Criteria:** Verb-AC12, EffAdv-AC5, EffAdj-AC6
**Dependencies:** T-305 (self-check before practice), T-414 (A template: proof landing zone & rubrics — pending, but T-306 references and assumes structure)

---

## 1. PURPOSE

**What is a rubric walk-through?**
A rubric walk-through is an optional, Agent-guided review that validates whether a Learner's practice work meets the level's pass/fail criteria. It happens AFTER practice, when the Learner brings evidence and claims completion.

**Data sources:**
1. **Subject Roadmap (A):** Level Credentials (deterministic proof artefacts) + Pass/Fail Criteria (per credential)
2. **Learner's evidence:** Code, screenshots, artefacts, conversation logs, or explanations brought by the Learner

**Why it matters:**
- Validates completion against explicit criteria (no ambiguity: "Did I pass?")
- Helps Learner understand what "done" means
- Records proof deterministically for future assessors (e.g., external reviewer, auditor)
- Builds confidence: "I did this. It meets criteria. I can move to the next level."
- **Optional:** Learner can accept feedback, defer, or resubmit; Agent does not block

**Who offers it:**
The Agent offers rubric walk-through based on explicit conditions (see §3 Triggers).

**Subject-agnostic procedure:**
This document describes the rubric walk-through procedure (when to offer, how to conduct, how to record). The examples (L1/L2 credentials, rubric format, example transcript) are specific to COE_AI_ORCH. **For other subjects,** the Agent must derive rubrics and credentials from that subject's **A (Subject Roadmap)**: look for a section containing Requirements and Credentials per level (the exact section name may vary per subject; for COE_AI_ORCH it's called "Level Specifications (L1–L7)" and "Subject-Specific Requirements & Credentials"). The procedure itself (credential-by-credential walk-through, evidence collection, proof recording) is subject-agnostic and applies to any subject with an A and Credentials.

---

## 2. DATA SOURCES

### 2.1 Source 1: Subject Roadmap (A) — Credentials & Rubrics

From A, the level credentials are stored in one of two equivalent formats:
- **Compact form:** A → **"Level Specifications (L1–L7)"** (table format, all levels in one view)
- **Detailed form:** A → **"Subject-Specific Requirements & Credentials"** (subsections per level with full text)

Both contain the same Requirements and Credentials; choose whichever format is clearer for the Agent.

Per level:
- **Credentials:** Deterministic proof artefacts (e.g., "Working Python script", "Screenshot", "Written standards document")
- **Pass Criteria (per credential):** What success looks like (e.g., "Script runs, retrieves live data via tool call, responds to query")
- **Fail Criteria (per credential):** What does NOT pass (e.g., "Script missing, doesn't run, no tool call visible")

**Example (L1 Credential 1):**
```
Credential: Working Python script (my_first_agent.py) that creates an Agno Agent
  and answers "What is the current price of AAPL?"

Pass criteria:
  ✓ Script file exists and is named my_first_agent.py (or similar)
  ✓ Script runs without error
  ✓ Script creates an Agno Agent with at least one tool (YFinance)
  ✓ Agent successfully retrieves live AAPL price via tool call
  ✓ Agent responds to the query with the price

Fail criteria:
  ✗ Script missing or cannot be located
  ✗ Script throws errors when run
  ✗ Agent does not use tools; just echoes input
  ✗ Tool call fails or returns stale/incorrect data
```

### 2.2 Source 2: Proof Landing Zone (in A)

From A, **Level Completion Checklist** and/or **Links to Proof** section (per level):

- **Proof landing zone:** Where evidence for each credential is stored or linked (e.g., folder path, ClickUp link, Git commit)
- **Evidence examples per credential type:**
  - Code artefact: Git repository path, file path in learning-book/evidence/
  - Screenshot: Markdown ![](path/to/screenshot.png)
  - Conversation log: Markdown code block or linked file
  - Written explanation: Link or inline text

---

## 3. TRIGGERS: WHEN TO OFFER RUBRIC WALK-THROUGH

Agent should offer rubric walk-through in these scenarios:

### 3.1 Condition A: Learner Returns from Practice & Claims Completion

**Trigger:** User says "I've done the practice" or "Here's my work" or "I'm ready for review" after completing a level's practice.

**Agent action:**
- Accept the claim
- Determine target level from context (stated by User, or inferred from A's Current Level)
- Offer: "Great! I can walk through the Level X rubric to validate your work against the criteria. This is optional; I can provide feedback, or you can submit as-is. What would you prefer?"
- Do not assume; let User accept, defer, or skip

**Example:**
```
User: "I've built my first agent. It retrieves AAPL price and I have screenshots. Ready to check if it's done?"

Agent: "Excellent! I can walk through the Level 1 rubric to check your work against the pass criteria for each credential. This helps ensure you're ready for Level 2. Want me to do that, or prefer to submit as-is?"
```

### 3.2 Condition B: User Explicitly Asks for Feedback

**Trigger:** User says "Can you review my work?" or "Check if this meets the criteria" or "Does this pass?"

**Agent action:**
- Accept the request
- Determine target level and credential(s) from context
- Proceed to rubric walk-through (§4 Procedure)

### 3.3 Condition C: Agent Detects Completion & Suggests

**Trigger:** User has completed practice for a level; Agent can detect this from context (e.g., "I've built the Investment Team and deployed it").

**Agent action:**
- Suggest: "You've completed Level X practice! Would you like a rubric walk-through so we can validate your work before you move to Level Y?"
- Wait for User response

---

## 4. RUBRIC WALK-THROUGH PROCEDURE

### 4.1 Agent Preparation

Before starting, the Agent should:
1. **Read A (Subject Roadmap)** to find the target level's Credentials and Pass/Fail Criteria
   - Use either "Level Specifications (L1–L7)" table OR "Subject-Specific Requirements & Credentials" subsections; both are equivalent
2. **Scan Proof Landing Zone** in A to see where evidence should be recorded
3. **Determine credential count** for this level (typically 3 per level; see A)
4. **Prepare pass/fail checklist** for each credential

### 4.2 Walk-Through Flow

**Step 1: Confirm target level and scope**
```
"Let's walk through the Level 2 rubric. You should have evidence for 3 credentials:
  1. Working 2-agent Team script with observable Coordinator delegation
  2. Conversation log showing Agent A → Coordinator → Agent B handoff
  3. Session memory test: follow-up question references prior context

Do you have these, or would you like to revisit any?"
```

**Step 2: Walk through each credential (one at a time)**

For each credential:

1. **Present the credential and pass criteria:**
   ```
   "Credential 1: Working 2-agent Team script with observable Coordinator delegation

   Pass criteria:
     ✓ Script file exists and is runnable (Python 3.9+)
     ✓ Script creates 2 agents (Research Analyst, Risk Analyst)
     ✓ Coordinator mode is configured (observable in code)
     ✓ When run, Coordinator delegates to agents and shows handoff in output

   Do you have this?"
   ```

2. **Listen to User's response:**
   - If User says "Yes, here it is" → ask to show the evidence (code, screenshot, path)
   - If User says "Not quite" or "I didn't do this" → identify the gap

3. **Validate evidence (if provided):**
   - Ask User to share code or screenshot (e.g., "Can you show me the Coordinator line in your code?")
   - Verify against pass criteria: ✓ all points met, or ✗ some points missing
   - If ✓ **PASS**: Mark credential as passing. "✓ Credential 1 passes all criteria."
   - If ✗ **FAIL**: Identify which criteria are missing. "I see you have the script and 2 agents, but I don't see observable Coordinator delegation. Let's look at..."

4. **Record outcome:**
   - **Pass:** Note the evidence (e.g., "my_first_agent.py at path X")
   - **Fail:** Note what's missing and ask: "Want to revisit this and resubmit, or move forward with the other credentials?"

**Step 3: Summarize across all credentials**

After walking through all credentials:
```
"Here's what I see:
  ✓ Credential 1: PASS (code shows 2-agent Team + observable delegation)
  ✓ Credential 2: PASS (conversation log shows Agent A → Coordinator → Agent B)
  ✗ Credential 3: FAIL (session memory test missing; you didn't test follow-up with prior context)

Result: 2 of 3 credentials pass.

Options:
  A. PASS (submit as-is with feedback): You can move to Level 3 practice now. I recommend revisiting Credential 3 once you're ready.
  B. REVISIT (fix Credential 3): Spend 20 minutes adding a session memory test, then resubmit.
  C. DEFER (no decision now): Take time to think, and we'll revisit when you're ready.

What's your choice?"
```

**Step 4: Record proof & update A (§6 below)**

Once the Learner chooses (Pass, Revisit, or Defer), update A with the result.

---

## 5. AGENT BEHAVIOUR (MANDATORY RULES)

1. **Optional, non-blocking:**
   - Agent offers rubric walk-through; User accepts, defers, or skips.
   - If User says "Don't need a review, I'm moving to Level 3," Agent does not block.

2. **Grounded in A:**
   - All credentials and pass/fail criteria come from A (Subject-Specific Requirements & Credentials).
   - Do not invent criteria; use A as source of truth.

3. **Diagnostic + summative:**
   - **Diagnostic:** Check if evidence meets criteria (not punitive).
   - **Summative:** Validate completion (evidence of learning).

4. **Tone:**
   - Supportive, expert, collaborative ("We're checking that you've got solid foundations for the next level").
   - Not judgmental ("You didn't pass" → "Credential 3 needs a bit more work; let's see what's missing").

5. **Credential by credential:**
   - Walk through one credential at a time.
   - Listen to User's evidence; validate against criteria.
   - Record the outcome for each.

6. **Transparency on pass/fail:**
   - State clearly: "This credential passes all criteria" or "This credential is missing [X]; we need to revisit."
   - Explain WHY (link to criteria) so Learner understands.

7. **Learner chooses next step:**
   - After walk-through, present options: Pass & move forward, Revisit & resubmit, or Defer.
   - Do not prescribe; Learner decides.

---

## 6. PROOF RECORDING: HOW TO UPDATE A

When the rubric walk-through is complete and the Learner chooses a path, the Agent updates A:

### 6.1 Update Level Completion Checklist (in A)

**Location:** A → "Level Completion Checklist" section

**Action:** Update the row for the target level:

| Level | Met | Evidence | Date |
|-------|-----|----------|------|
| L2 | 🟡 | Credentials 1, 2 PASS; Credential 3 revisiting | 2026-03-01 |

- **Met:** ✅ (all 3 credentials pass), 🟡 (partial: some pass, some revisit), 🔲 (not yet)
- **Evidence:** Brief summary (e.g., "2-agent Team code in repo/agents/; Conversation log in proof/; Session memory test pending")
- **Date:** Date of rubric walk-through

### 6.2 Update Proof Landing Zone (in A or separate section)

**Location:** A → new section "Proof Landing Zone (per Level)" or added to "Level Completion Checklist"

**Action:** Record evidence for each credential:

```
## L2 Proof Landing Zone

**Credential 1: 2-agent Team script**
- Location: `learning-book/COE_AI_ORCH/evidence/L2-team-agents.py`
- Status: ✅ PASS (2026-03-01)
- Notes: Research Analyst + Risk Analyst with Coordinator; observable delegation in output

**Credential 2: Conversation log**
- Location: `learning-book/COE_AI_ORCH/evidence/L2-conversation-log.txt`
- Status: ✅ PASS (2026-03-01)
- Notes: Shows Agent A → Coordinator → Agent B handoff; clear message passing

**Credential 3: Session memory test**
- Location: pending
- Status: 🟡 REVISIT (2026-03-01)
- Notes: Test not yet added; Learner to revisit and resubmit follow-up question interaction
```

### 6.3 Update Session Log (in A)

**Location:** A → "Session Log" section

**Action:** Append a new row:

| Date | Entry Point | Progress |
|------|-------------|----------|
| 2026-03-01 | L2 Rubric Walk-Through | Credential 1, 2 PASS; Credential 3 revisiting. Learner chose to revisit before Level 3. |

---

## 7. EXAMPLE SESSION TRANSCRIPT

### Scenario: Learner at L2, completed practice, returns with code and conversation log

**User:** "I've built my 2-agent Team and tested it. I have the code and a conversation log. Can you check if it's done?"

**Agent:** "Excellent! Let me walk through the Level 2 rubric to validate your work against the credentials. You should have evidence for 3 things:
1. Working 2-agent Team script with observable Coordinator delegation
2. Conversation log showing Agent A → Coordinator → Agent B handoff
3. Session memory test: follow-up question references prior context

Do you have all three, or are you stronger in some areas?"

**User:** "I have the code and the conversation log. I didn't do a formal session memory test, but my Team does use memory—I can show you."

**Agent:** "Good to know. Let's walk through each credential and see.

**Credential 1: 2-agent Team script with observable Coordinator delegation**

Pass criteria:
  ✓ Script file exists and is runnable
  ✓ Creates 2 agents (Research Analyst, Risk Analyst)
  ✓ Coordinator mode configured
  ✓ When run, shows delegation and handoff

Can you share your script path or the key lines? I'd like to verify the Coordinator setup."

**User:** "Sure. It's in my repo at agents/investment_team.py. The Coordinator is configured with `mode='coordinator'` and both agents are registered."

**Agent:** *(reviews the code)* "Perfect. ✓ **Credential 1 PASSES** all criteria. I see the 2 agents, the Coordinator mode, and in your output log I can see the delegation happening. Great work."

**Credential 2: Conversation log showing Agent A → Coordinator → Agent B handoff**

Pass criteria:
  ✓ Conversation log exists and is readable
  ✓ Shows at least one instance of Agent A output → Coordinator delegation decision → Agent B input
  ✓ Shows that Coordinator chose the right agent for the task

Can you show me the conversation log?"

**User:** *(shares conversation log)* "Here's the log. You can see the Research Analyst responds, then the Coordinator decides to delegate to Risk Analyst."

**Agent:** *(reviews the log)* "✓ **Credential 2 PASSES**. Crystal clear handoff. Coordinator makes a deliberate decision ('Delegating research to Risk Analyst for validation'), and Agent B gets the prior context and responds."

**Credential 3: Session memory test (follow-up question references prior context)**

Pass criteria:
  ✓ You ask a follow-up question in a second turn
  ✓ Agent(s) reference prior context from turn 1 (e.g., 'Your earlier research showed...')
  ✓ Proof: screenshot or log showing this interaction

You mentioned your Team uses memory, but didn't do a formal test. Can you do a quick test now, or would you prefer to revisit this later?"

**User:** "I can do a quick test. Let me run a follow-up query and see if the Team references the earlier context."

*(User runs a follow-up; the Team correctly references prior research)*

**Agent:** "Perfect! ✓ **Credential 3 PASSES**. The Team remembered the earlier findings and applied them in the follow-up response."

**Summary:**
```
✓ Credential 1: PASS
✓ Credential 2: PASS
✓ Credential 3: PASS (with quick test just now)

Result: All 3 credentials pass. You're ready for Level 3 practice!

What's next?
  A. Move to Level 3 practice (I'll help you set up Workflow with Parallel/Condition/Loop)
  B. Spend more time on Level 2 (optional; you've met the criteria)
  C. Defer decision (take a break, revisit when ready)
```
```

**User:** "Let's go to Level 3!"

**Agent:** "Great! Before we start, would you like a self-check for Level 3? I can help you see if you're ready for the learning content, or we can jump straight in."

*(Handoff to Phase C entry point for Level 3; update A with completion result)*

---

## 8. EDGE CASES & HANDLING

| Scenario | Agent Action |
|----------|--------------|
| User says "Skip review, submit as-is" | Do not block. Accept the submission. Record in A with status 🟡 (unvalidated). |
| Learner has partial evidence (e.g., code + screenshot, but no conversation log) | Walk through each credential with what they have. Mark: ✓ PASS, 🟡 PARTIAL, ✗ REVISIT. Offer path forward. |
| Learner's evidence doesn't clearly meet criteria | Ask clarifying questions. If still unclear, mark REVISIT and suggest specific improvements. |
| Learner disputes a criteria (e.g., "That's not what pass means") | Explain: "This criteria comes from A. If you believe A is wrong, we can propose changes to the Level Specifications, but for now this is the standard." (Escalate to A update only if User asks.) |
| User passes some credentials but wants to defer others | Accept. Record status per credential. Mark Level as 🟡 (partial). Suggest next steps. |
| User fails all credentials | Encourage: "This is normal on first practice. Let me help you understand what's needed." Walk through each failure and point to learning content (Phase C) that covers the gap. |
| User asks "Is this the same rubric a future assessor would use?" | Say "Yes. This rubric comes from A and is the standard for this level. An external assessor would use the same criteria." This is the "same-criteria principle": Agent and assessor use identical rubrics. |

---

## 9. RELATIONSHIP TO T-305 (SELF-CHECK BEFORE PRACTICE)

| When | What | Who | Purpose |
|------|------|-----|---------|
| **Before practice** | Self-check (T-305) | Agent offers; User opts in | Diagnostic: assess readiness; identify knowledge gaps |
| **During practice** | Practice (User's work) | Learner (solo or with Agent help) | Active learning: build, code, test, experiment |
| **After practice** | Rubric walk-through (T-306) | Agent guides; Learner brings evidence | Summative: validate completion; record proof |

- **T-305** = "Am I ready to practice?"
- **T-306** = "Did I do it well? Does it meet criteria?"

Both are optional; neither blocks the Learner. Learner always chooses the next step.

---

## 10. IMPLEMENTATION NOTES

### 10.1 Integration with `.cursor/rules/ile-learning-book.mdc`

**Note:** The rule already instructs the Agent to follow this document. The section below is an optional summary for the rule file:

```markdown
## § Rubric walk-through & proof recording (T-306)

**Trigger:** User returns from practice and claims completion, OR explicitly asks for review/feedback.

**Procedure:**
1. Confirm target level and credential count
2. Walk through each credential (one at a time):
   - Present credential + pass criteria
   - Listen to User's evidence
   - Validate against criteria
   - Record ✓ PASS, 🟡 PARTIAL, or ✗ REVISIT
3. Summarize and present options: Pass & move forward, Revisit & resubmit, Defer
4. Update A: Level Completion Checklist + Proof Landing Zone + Session Log

**Tone:** Supportive, collaborative, expert.

**Criteria source:** A, "Subject-Specific Requirements & Credentials" (same criteria Agent and future assessor use).

**Full procedure:** `docs/ai/implementation/ile-rubric-walk-through-proof-recording.md`
```

### 10.2 Relationship to T-414 (A Template: Proof Landing Zone & Rubrics)

T-306 assumes that A has a defined structure for:
1. **Proof Landing Zone:** Where evidence for each level is stored or linked
2. **Rubrics:** Pass/fail criteria per credential (same criteria used by Agent and future assessor)

T-414 (pending, Iteration 4) will define this A template structure. **T-306 does not wait for T-414**; T-306 documents the procedure using the assumed structure. When T-414 is approved, both T-305 and T-306 can reference the exact A sections and template.

### 10.3 Proof Capture In-Conversation

Key principle: **Proof capture is a byproduct of the conversation.** The Agent does not ask the Learner to "export proof" or "save evidence separately." Instead:

1. During rubric walk-through, User shares evidence (code snippet, screenshot path, conversation log)
2. Agent reviews it (in-conversation)
3. Agent proposes an update to A (Proof Landing Zone) with the evidence location/link
4. User approves; Agent writes to A
5. Result: Proof is recorded; no separate copy-paste step

---

## 11. SUCCESS CRITERIA (A.C.)

**Verb-AC12:**
✅ User can have Agent walk through level rubric when practice is complete; Agent helps record evidence in proof landing zone and update Level Completion Checklist.

**EffAdv-AC5:**
✅ User can complete rubric walk-through in-conversation without leaving the ILE; Agent guides and helps record evidence so proof capture is a byproduct of conversation.

**EffAdj-AC6 (partial):**
✅ Rubric walk-through is optional and does not block; Agent suggests and helps when Learner opts in.

---

_Last updated: 2026-03-01 (T-306 draft)_
_Status: Ready for review_
