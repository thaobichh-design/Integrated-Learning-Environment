---
phase: implementation
title: ILE Self-Check Before Practice (T-305)
description: Procedure and Agent behaviour for offering comprehensive self-check before level practice. Verb-AC11, EffAdj-AC6. Optional diagnostic gate; subject-agnostic pattern sourced from A.
feature: integrated-learning-environment
task: T-305
---

# ILE Self-Check Before Practice

_When the User has completed all Phase C pages for a target level (A → Approved Pages shows all required pages), or when the User explicitly asks, the Agent offers an optional comprehensive self-check. The self-check uses Subject Roadmap (A) and completed Learning Book content to diagnose readiness for level practice. The Learner always chooses whether to self-check, revisit content, or proceed directly to practice. This is a diagnostic gate, not a blocker._

**Cross-references:** Flow → `docs/ai/implementation/ile-minimal-flow.md` | Tree map → `docs/ai/implementation/learning-book-tree-map.md` | A (checkpoint) → `ile-minimal-flow.md` § A. Subject Roadmap | Rubric flow → T-306 `ile-rubric-walk-through-proof-recording.md` | Rule → `.cursor/rules/ile-learning-book.mdc`

---

**Acceptance Criteria:** Verb-AC11, EffAdj-AC6
**Dependencies:** T-304 (completion moment), A (Subject Roadmap)

---

## 1. PURPOSE

**What is a self-check?**
A self-check is an optional, Agent-guided review that helps the Learner assess readiness for level practice. It uses two sources:

1. **Subject Roadmap (A):** The Level Requirements and Credentials for the target level
2. **Learning Book (Organise content):** The completed chapters/topics/pages for that level

**Why it matters:**

- Reduces anxiety ("Am I ready to practice?")
- Provides concrete, level-appropriate questions
- Identifies knowledge gaps before practice
- **Optional:** Learner can skip or defer; Agent does not block or require

**Who offers it:**
The Agent offers self-check based on explicit conditions (see §3 Triggers).

**Subject-agnostic procedure:**
This document describes the self-check procedure (when to offer, how to conduct, tone). The examples (L1/L2/L3 questions, example transcript in §7) are specific to COE_AI_ORCH. **For other subjects,** the Agent must derive conceptual questions and scope from that subject's **A (Subject Roadmap)**: the Level Requirements, Credentials, and "Links to Learning Book (per Level)" table. The procedure itself (Socratic questioning, gap identification, optional gate) is subject-agnostic and applies to any subject with an A and Organise content (Phase C).

---

## 2. DATA SOURCES

### 2.1 Source 1: Subject Roadmap (A)

From A, **Level Specifications** section:

- **Level Requirements:** What the Learner must understand and do (e.g., "Understand what an AI agent is; build 1 single agent with tools")
- **Credentials:** Deterministic proof artefacts (e.g., "Working Python script; screenshot; verbal explanation")
- **Links to Learning Book (per Level):** Which chapters/topics/pages belong to this level (e.g., L1 = Chapter 0 Overview + Chapter 1 UBS Pages 0–1)

### 2.2 Source 2: Learning Book (Organise Content — Phase C)

From the Learning Book, **Phase C (Organise Information)** for the level:

- **Pages completed:** Which pages are marked approved in A's Approved Pages section
- **Key concepts per page:**
  - Page 0 (Overview): "What is the row subject and why does it matter?"
  - Page 1 (UBS): Root blockers and causal layers
  - Page 2 (UDS): Root drivers and causal layers
  - Page 3 (EPS): Principles that enable UDS / disable UBS
  - Page 4 (UES): Components (tools, environment) per layer
  - Page 5 (EOP): Steps to apply/practice

---

## 3. TRIGGERS: WHEN TO OFFER SELF-CHECK

Agent should offer self-check in these scenarios (in order of precedence):

### 3.1 Condition A: Level Scope Complete

**Trigger:** User has approved all Phase C pages for the level.

**How to detect:**

1. Read A, section **"Links to Learning Book (per Level)"** (table: Level | Recommended Chapters/Topics) to find what pages belong to the target level (e.g., L1 = Chapter 0 Overview + Chapter 1 UBS Pages 0–1).
2. Read A, section **"Phase C Organise — state"** → subsection **"Approved Pages (in order)"** and/or **"Current State (Phase C)"** to see which pages are marked ✅ APPROVED.
3. Check: does every page in "Links to Learning Book (per Level)" for level L appear as approved? If yes → **Level scope complete** for level L.

**Agent action:**

- Detect the condition (scan A using the sections above)
- Suggest: "You've completed all Level X learning content. Would you like a self-check before you start level practice?"
- Do not assume; let User accept, defer, or skip

**Example:**

```
"✅ You've approved all Phase C pages for Level 1 (Chapter 0 Overview + Chapter 1 UBS pages 0–1).

Ready for a self-check before Level 1 practice? This is optional; I can guide you through a quick checklist so you know where you stand. You can also skip this and go straight to practice. What works for you?"
```

### 3.2 Condition B: User Explicitly Asks

**Trigger:** User says "Can you give me a self-check?" or "Help me prepare for L2 practice" or similar.

**Agent action:**

- Accept the request
- Determine target level from context (e.g., "L2" stated, or infer from A's Current Level)
- Proceed to self-check flow (§4)

### 3.3 Condition C: Return from Practice (Rubric Walk-Through)

**Trigger:** User returns from practice and claims completion (e.g., "I've done the practice; here's my work").

**Agent action:**

- This is NOT self-check before practice; it's rubric walk-through (T-306)
- Separate flow (§5 below)

---

## 4. SELF-CHECK PROCEDURE (BEFORE PRACTICE)

A comprehensive self-check covers all Level Requirements from A and key concepts from each completed Organise page for that level; 5–10 questions is a minimum to achieve this.

### 4.1 Agent Preparation

Before starting, the Agent should:

1. **Read A (Subject Roadmap)** to find the target level's Requirements, Credentials, and Links to Learning Book
2. **Scan Approved Pages** in A to see which content is complete
3. **Identify gaps:** What was supposed to be complete but isn't? (A shows expected pages; if not marked approved, mark as gap)
4. **Prepare questions:** Derive from the completed pages and level requirements

### 4.2 Self-Check Flow

**Step 1: Confirm target level**

```
"Just to confirm: are you preparing for Level 1, Level 2, or another level?"
```

**Step 2: Present the level's Requirements**
From A, state the Requirements in plain language:

```
"Level 2 requires:
  1. Build a 2-agent Team with Coordinator Mode
  2. Demonstrate context passing (Agent A → Agent B)
  3. Use session memory for follow-up questions

Let's check your understanding of these. Ready?"
```

**Step 3: Ask conceptual questions** (5–10 questions, Socratic style)

Derive questions from the **learning content for that level** (A → Links to Learning Book). Examples:

**For L1 (based on Chapter 0 Overview + Chapter 1 UBS):**

- "What's the difference between a chatbot and an agent?"
- "If an agent has a blocker (e.g., Capability Gap), how does the learner overcome it?"
- "What's the single most important principle for starting an agent project?"

**For L2 (based on Chapter 1 UBS full + Chapter 2 UDS):**

- "Why would you build a 2-agent Team instead of one big agent?"
- "How does a Coordinator decide which agent to delegate to?"
- "In Chapter 2, what's the root driver for Hierarchical Decomposition?"

**For L3 (based on Chapter 2 UDS full + Chapter 3 EPS):**

- "What's the difference between a Team and a Workflow?"
- "When would you use a Loop vs. a Parallel step in a Workflow?"
- "Name one principle from Chapter 3 that applies to Workflow design."

**Format:** Ask one question at a time. Listen to the answer. If it shows understanding, move on. If it shows a gap, offer to revisit that chapter.

Example exchange:

```
Agent: "In Chapter 1, we identified the root blocker to building agents. Do you remember what it was?"

User: "Uh... capability gap?"

Agent: "Exactly — the learner lacks a mental model for how agents work. In Chapter 1 Page 1 (Ultimate Blockers), you found three causal layers. Can you name one of them?"

User: "I'm fuzzy on that."

Agent: "No problem. That's a gap we can close. Let me know if you'd like to spend 10 minutes re-reading T1.P1 (Ultimate Blockers) before you practice, or if you'd like to jump into practice and learn by doing."
```

**Step 4: Identify gaps**
As questions are asked, the Agent notes:

- ✅ Clear understanding
- 🟡 Fuzzy but directional
- ❌ Missing or incorrect

Tally at the end: "You showed clear understanding of [3 topics], fuzzy on [1 topic], and we skipped [1 topic]. Here's what I'd recommend..."

**Step 5: Recommendation & consent**

```
"Based on this self-check, I see two paths:

Option A (Skip & Practice): Jump into Level X practice now. You'll learn by doing, and I'll help you debug if you hit blockers.

Option B (Revisit & Strengthen): Spend 30 minutes re-reading [Chapter/Page] to shore up the fuzzy areas, then practice.

Which feels right to you?"
```

**Do not prescribe.** Learner chooses.

### 4.3 Optional: Gap Closure Loop

If the Learner chooses to revisit content:

1. **Identify the page:** "Let's re-read Chapter X Page Y. I'll help you understand the key concepts."
2. **Quick review:** Ask the Learner to summarize the page's main ideas in 1–2 sentences.
3. **Clarify:** Answer questions; fill gaps.
4. **Re-check:** Ask 1–2 follow-up questions to confirm the gap is closed.
5. **Resume self-check:** Go back to §4.2 Step 3 for any remaining unanswered questions.

---

## 5. AGENT BEHAVIOUR (MANDATORY RULES)

1. **Optional, not mandatory:**
   - Agent offers; User accepts, defers, or skips.
   - If User says "Skip self-check, let's go straight to practice," Agent does not block.

2. **Grounded in A and Learning Book:**
   - All questions derive from completed pages (A → Approved Pages).
   - Do not ask about content the Learner hasn't read.
   - Reference page labels and column names (e.g., "In T1.P1, column 4 asked...").

3. **Tone:**
   - Supportive, not judgmental ("This is normal; let's close the gap").
   - Expert (the Agent is a subject matter expert in AI Orchestration).
   - Socratic (ask, listen, clarify; don't lecture).

4. **Clarity on next step:**
   - At the end, state clearly: "You're ready for Level X practice" OR "I recommend closing [gap] first" OR "Let's revisit [page] and then re-check."
   - Always end with Learner's choice: "What would you like to do?"

---

## 6. PROOF OF COMPLETION

When self-check is complete, the Agent should:

1. **Update A (Subject Roadmap)** → Session Log with one line:

   ```
   | [Date] | Self-check L[X] | Completed; gaps: [list if any]; recommend: [path]. Ready for L[X] practice. |
   ```

2. **Optional: Update Level Completion Checklist** → mark progress:
   - If all gaps closed: "Self-check PASS ✅"
   - If gaps remain but Learner proceeding: "Self-check PASS (with gaps) 🟡"

3. **No blocker:** Learner can proceed to practice regardless of outcome.

---

## 7. EXAMPLE SESSION TRANSCRIPT

### Scenario: User at L1, all Chapter 0 + 1 content approved, ready to practice

**User:** "I've finished reading Chapter 0 and Chapter 1. I'm ready to build my first agent. How do I know if I'm ready?"

**Agent:** "Great progress! You've completed all the learning content for Level 1 (Chapter 0 Overview + Chapter 1 UBS Pages 0–1). I can give you a quick self-check to make sure the concepts stuck, or we can jump straight into practice. What would you prefer?"

**User:** "Let's do the self-check. I want to feel confident."

**Agent:** "Perfect. Here are the Level 1 requirements:

1. Explain the difference between a chatbot and an agent
2. Install Agno in Python
3. Build and run a Finance Agent with YFinance that retrieves live stock data

Let me ask you a few questions to see where you stand.

**First question:** In Chapter 0, we introduced the concept of an agent. What do you remember about what makes an agent different from a chatbot?"

**User:** "An agent can use tools and has memory, whereas a chatbot is just a conversation model."

**Agent:** "Excellent. Exactly right — agents have tools, memory, and instructions. Chatbots are just a model. ✅

**Next question:** In Chapter 1 (UBS / Capability Gap), we explored the root blocker that stops people from building agents. What was that blocker?"

**User:** "Um... I think it was that people don't have a mental model for how agents work?"

**Agent:** "Right direction. The root blocker is **Capability Gap** — the learner lacks a mental model for agent decomposition. In Page 1 (Ultimate Blockers), we found three layers to that gap. Do you remember any of them?"

**User:** "I read it, but I'm fuzzy."

**Agent:** "That's normal. Those three layers were:

1. **Scope Indiscipline** (UBS.UB.UB) — learner doesn't define what the agent should do
2. **Principle Extraction Discipline** (UBS.UB.UD) — learner extracts principles from builds so they can apply them next time
3. **Permission to Start Small** (UBS.UD.UB) — learner needs permission to build tiny agents first, not big ones

The key insight: you overcome the Capability Gap by building small incremental agents, testing each one, and extracting patterns. Not by reading. By doing.

Does that ring a bell from Chapter 1?"

**User:** "Ah, yes! I remember now. Start small, test, extract."

**Agent:** "Perfect. ✅ That's the core of L1 practice.

**Last question:** In Chapter 1 Page 3 (Principles), we harvested principles that help you build agents. Can you name one principle and explain what it enables?"

**User:** "Hmm, I don't remember the exact list."

**Agent:** "That's okay. The principles included things like 'Build → Test → Validate → Measure' and 'Learn before you build scope.' These principles come directly from Chapter 1's blockers and drivers. The point is: when you're building your agent, follow these patterns instead of trial-and-error.

Here's what I'm seeing: You understand the concept of agents vs. chatbots (✅), you get the Capability Gap idea (✅), but the specific principles and causal layers are fuzzy (🟡).

Two options:

1. **Skip & Practice:** Jump into building your first agent now. You'll remember the principles as you code, and I'll be here to help.
2. **Revisit & Strengthen:** Spend 15 minutes re-reading Chapter 1 Page 3 (Principles) + Page 1 (Blockers), and we can do another quick mini-check.

What feels right?"

**User:** "Let's just jump into practice. I learn better by doing."

**Agent:** "Perfect. That's actually the L1 principle in action: learn by building. ✅

Let's start Level 1 Practice:

1. Install Agno: `pip install agno`
2. Create a new file: `my_first_agent.py`
3. Build a Finance Agent with YFinance that retrieves live stock data

I'll walk you through it step-by-step. Let's go!"

---

## 8. EDGE CASES & HANDLING

| Scenario                                                           | Agent Action                                                                                                                       |
| ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| User says "Skip self-check, go straight to practice"               | Do not block. Proceed to practice. Optional.                                                                                       |
| User requests self-check but hasn't completed any learning content | Offer gap-closure path: "Let me point you to the key pages for Level X. Once you've read those, we can do the self-check."         |
| User completes self-check but has multiple gaps                    | State gaps clearly. Recommend revisit. Do not block practice. Learner chooses.                                                     |
| User passes self-check but still fails practice                    | This is normal. Practice reveals deeper gaps. Use practice failure as a trigger for T-306 (rubric walk-through).                   |
| Self-check is offered but User asks "What is this?"                | Explain: "A self-check is a quick optional quiz to see if you're ready for practice. It's not graded; it just helps us find gaps." |

---

## 9. RELATIONSHIP TO T-306 (RUBRIC WALK-THROUGH)

| When                | What                        | Who runs it                           | Purpose                           |
| ------------------- | --------------------------- | ------------------------------------- | --------------------------------- |
| **Before practice** | Self-check (T-305)          | Agent offers optionally               | Assess readiness; identify gaps   |
| **After practice**  | Rubric walk-through (T-306) | Agent guides; Learner shares evidence | Validate completion; record proof |

- **T-305** is **diagnostic** (are you ready?).
- **T-306** is **summative** (did you do it? does it meet criteria?).

Both are optional; neither blocks the Learner.

---

## 10. IMPLEMENTATION NOTES

### 10.1 Integration with `.cursor/rules/ile-learning-book.mdc`

**Note:** The rule already instructs the Agent to follow this document (`ile-self-check-before-practice.md`). The section below is an optional short summary that could be added to the rule file if desired (e.g., as a quick reference alongside the full document link). It is not a replacement for this full documentation; it is supplementary.

Optional summary section for the rule:

```markdown
## § Self-check before practice (T-305)

**Trigger:** When User has completed all Phase C pages for a level (A → "Phase C Organise — state" → "Approved Pages (in order)" shows all pages for that level), OR User explicitly asks for self-check.

**Procedure:**

1. Confirm target level
2. Present Level Requirements from A
3. Ask 5–10 conceptual questions derived from completed pages
4. Identify gaps
5. Recommend: proceed to practice, or revisit content first
6. Learner chooses; Agent does not block

**Tone:** Supportive, expert, Socratic.

**Update A after completion:** Append Session Log with self-check summary.

**Full procedure:** `docs/ai/implementation/ile-self-check-before-practice.md`
```

### 10.2 Update to `ile-minimal-flow.md`

Self-check fits into the flow at a new step:

**Flow (updated):**

1. **Session start/resume:** Read A; identify current level
2. **Phase choice:** B (Capture) | C (Organise) | D (Distill)
3. **Entry point:** User selects from Learning Map
4. **Template load:** Correct template loaded; context scoped
5. **Conversation → doc:** Learning conversation; Markdown updated in real-time
6. **Completion:** User and Agent confirm chunk done
7. **Engagement:** Clear completion moment + optional progress summary
8. **[NEW] Self-check before practice (optional):** If User has finished all content for a level, offer self-check
9. **Switch or exit:** Before switching entry point/phase or exiting, commit draft to doc; update A Session Log

---

## 11. SUCCESS CRITERIA (A.C.)

**Verb-AC11:**
✅ User can request a comprehensive self-check from the Agent; the Agent offers it based on A and the Organise content for that level. Self-check is optional.

**EffAdj-AC6:**
✅ Self-check is optional and does not block the Learner; the Agent suggests and helps when the Learner opts in.

---

This document is the T-305 deliverable and the deterministic evidence for planning Table B (Verb-AC11, EffAdj-AC6).
_Last updated: 2026-03-01 (T-305 draft)_
_Status: Ready for review_
