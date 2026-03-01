---
phase: implementation
title: ILE Agent Reads Level→Scope & Gates from A (T-415)
description: Procedure and Agent behaviour for reading Level→Phase C Scope from A and using it to suggest sequence and validate gates. No hard-coded level→topic map in ILE. Noun-AC15, ScalAdv-AC6 (final).
feature: integrated-learning-environment
task: T-415
---

# ILE Agent Reads Level→Scope & Gates from A

_When the Learner completes Phase C pages or requests level progression, the Agent reads Level→Phase C Scope from A (Subject Roadmap) to: (1) validate prerequisites (gates), (2) suggest next steps (sequence), (3) guide level-appropriate learning. No hard-coded level→chapter map in ILE code; all scope is per-subject, defined in A._

**Cross-references:** A template structure → T-414 `ile-a-template-structure.md` | Self-check uses scope → T-305 `ile-self-check-before-practice.md` | Rubric uses scope → T-306 `ile-rubric-walk-through-proof-recording.md` | Rule → `.cursor/rules/ile-learning-book.mdc` | A example → `learning-book/COE_TECH_LONG_N_AI_ORCHESTRATION/[COE TECH]_[LONG N.]_AI ORCHESTRATION - A. Subject Roadmap & Level Specifications/`

---

**Acceptance Criteria:** Noun-AC15, ScalAdv-AC6 (final)
**Dependencies:** T-414 (A structure defined), T-305 & T-306 (approved)

---

## 1. PURPOSE

**What is Level→Scope?**
A mapping in A that specifies: for each level L1–L7, which chapters/topics/pages from Phase C (Organise Information) must be completed.

**Example (COE_TECH_LONG_N_AI_ORCHESTRATION):**

```
L1: Chapter 0. Overview (pages 0–1) + Chapter 1. UBS (pages 0–1)
L2: Chapter 1. UBS (pages 0–2) + Chapter 2. UDS (pages 0–2)
L3: Chapter 2. UDS (pages 0–3) + Chapter 3. EPS (pages 0–3)
```

**What does Agent do with it?**

1. **Read** Level→Scope from A
2. **Check** which pages Learner has completed (from A → Approved Pages)
3. **Validate** whether all L_n pages are done before allowing L_n practice
4. **Suggest** next steps: "Complete L1 pages first, then L1 practice"
5. **No code changes:** Scope is subject-specific, in A; Agent doesn't hard-code level→chapter rules

**Why it matters:**

- **Scalability (ScalAdv-AC6):** Any new subject can define its own scope in A; Agent uses same procedure
- **Clarity (Noun-AC15):** Agent can explicitly state: "Complete these X pages to finish Level Y"
- **Flexibility:** Each subject's progression is different; A is the authority, not code

---

## 2. DATA SOURCES

### 2.1 Source: A (Subject Roadmap) — Level → Phase C Scope (detailed)

From A, section **"Level → Phase C Scope (detailed)"**:

| Level | Chapters/Topics Required  | Pages within Each     | Notes               |
| ----- | ------------------------- | --------------------- | ------------------- |
| L1    | Ch 0 Overview; Ch 1 UBS   | Pages 0–1 per chapter | Foundation          |
| L2    | Ch 1 UBS (full); Ch 2 UDS | Pages 0–2 per chapter | Hierarchy + drivers |
| …     | …                         | …                     | …                   |

**Agent reads this table to know:** "For this subject, L2 requires pages 1.0–1.2 and 2.0–2.2"

### 2.2 Companion Source: A → Approved Pages (in order)

From A, section **"Phase C Organise — state" → "Approved Pages (in order)"**:

| #   | File                                                                                           | Status      |
| --- | ---------------------------------------------------------------------------------------------- | ----------- |
| 1   | C. Organise Information/0. Overview & Summary/0. Overview & Summary - 0. Overview & Summary.md | ✅ APPROVED |
| …   | …                                                                                              | …           |

**Agent cross-references:** "Learner has approved pages 1, 2, 3. Are these enough for L2? Let me check Level→Scope..."

---

## 3. AGENT PROCEDURE: READ SCOPE & VALIDATE

### 3.1 Trigger: When to Check Level→Scope

Agent should check Level→Scope in these scenarios:

**Trigger A: Phase C page just approved**

- User approves a page (e.g., T1.P5 approved)
- Agent detects: User has completed a page
- Agent action: Read A → Level→Scope → check if all L_n pages are done

**Trigger B: Learner requests level progression**

- User says "I'm ready for L2 practice" or "Can I start Level 2?"
- Agent action: Read A → Level→Scope → check if all L1 pages approved → allow or suggest prerequisite

**Trigger C: Session start (optional)**

- Agent reads A to understand Learner's progression
- Agent action: "You've completed L1 scope (pages 0.0, 0.1, 1.0, 1.1). Next: L1 practice."

**Trigger D: Agent suggests next step**

- After Learner completes L1 practice
- Agent action: "Ready for L2? First, complete L2 pages (Chapter 1 Pages 2–5, Chapter 2 Pages 0–2)"

### 3.2 Agent Decision Logic

**Pseudocode:**

```
when page_approved:
  current_level = A.Learner_Progress_Tracker.current_level
  next_level = current_level + 1

  # Read scope for next level
  required_pages = A.Level_Phase_C_Scope[next_level]

  # Check which are approved
  approved_pages = A.Phase_C_Organise_state.Approved_Pages

  # Compare
  if approved_pages contains all required_pages:
    suggest("You've completed L{next_level} scope! Ready for L{next_level} practice?")
  else:
    missing = required_pages - approved_pages
    suggest("L{next_level} requires: {required_pages}. You've done: {approved_pages}. Still need: {missing}.")

when learner_requests_level_practice(target_level):
  required_pages = A.Level_Phase_C_Scope[target_level]
  approved_pages = A.Phase_C_Organise_state.Approved_Pages

  if approved_pages contains all required_pages:
    allow_practice = true
    suggest("All {target_level} pages approved ✓. Ready for {target_level} practice!")
  else:
    allow_practice = false
    missing = required_pages - approved_pages
    suggest("Not yet. L{target_level} requires: {missing}. Complete those pages first, then practice.")
```

**Key principle:** Agent reads from A, not hard-coded rules in ILE code.

---

## 4. AGENT BEHAVIOUR (MANDATORY RULES)

1. **Read A first:**
   - Agent reads A → "Level → Phase C Scope (detailed)" → "Approved Pages" → derives current state
   - Every session start, before suggesting level progression

2. **Explicit about scope:**
   - When suggesting: name the chapters/topics/pages explicitly
   - Example: "L2 requires Chapter 1 UBS (pages 0–2) + Chapter 2 UDS (pages 0–2). You've done pages 1.0, 1.1. Still need: 1.2, 2.0, 2.1, 2.2"

3. **Gates are soft, not hard:**
   - Agent validates gates and suggests prerequisites, but does not block Learner
   - If Learner insists: "Proceed to L2 practice if you like, but L1 scope isn't complete. Ready?"
   - Learner chooses; Agent informs

4. **Subject-agnostic:**
   - Same procedure works for any subject (COE_TECH_LONG_N_AI_ORCHESTRATION, COE_Data Science, etc.)
   - Each subject's A defines its own Level→Scope; Agent reads from that subject's A

5. **Transparency:**
   - Always cite the source: "According to A → Level→Scope, L2 requires..."
   - Let Learner see the mapping

---

## 5. EXAMPLE: COE_TECH_LONG_N_AI_ORCHESTRATION PROGRESSION

### Scenario 1: Phase C page completion

**User approves T1.P5 (final page of L1 scope).**

**A state before:**

- Approved Pages: T0.P0–P5, T1.P0–P4 (11 pages)
- Current Level: L1

**User action:** Approves T1.P5

**Agent reads A:**

- Level→Scope: L1 requires pages 0.0, 0.1, 1.0, 1.1 (all approved ✓)
- Approved Pages: now includes T1.P5
- Next level: L2

**Agent suggests:**

```
"✅ T1.P5 approved!

You've now completed all Level 1 scope:
  ✓ Chapter 0. Overview (pages 0–1)
  ✓ Chapter 1. UBS (pages 0–1)

Ready for Level 1 practice? Once you do L1 practice, we can move to Level 2 learning.

Or, want to continue with learning first? Your choice."
```

### Scenario 2: Learner returns from L1 practice

**User says:** "I've done L1 practice. Ready for L2?"

**Agent reads A:**

- Level→Scope: L2 requires pages 1.0–1.2, 2.0–2.2
- Approved Pages: T0.P0–P5, T1.P0–P5 (all L1 done ✓)
- Missing for L2: T1.P2, T1.P3, T1.P4, T1.P5, T2.P0–P5

**Agent suggests:**

```
"Great! L1 practice done ✓

For Level 2, you'll need:
  • Chapter 1. UBS (pages 2–5) — all 3 causal layers + principles + components + steps
  • Chapter 2. UDS (pages 0–2) — overview, blockers, drivers of Hierarchical Decomposition

These pages take deeper dives into the UBS and introduce the UDS system.

Want to start L2 learning?"
```

### Scenario 3: Learner requests level progression mid-way

**User says:** "Can I jump to L3? I'm ready."

**Agent reads A:**

- Level→Scope: L3 requires all of Ch 2 (pages 0–3) + all of Ch 3 (pages 0–3)
- Approved Pages: T0.P0–P5, T1.P0–P5 (only L1 scope)
- Current Level: L1

**Agent responds:**

```
"Not yet. Here's why:

L3 requires:
  • Chapter 2. UDS (all 4 pages: 0–3)
  • Chapter 3. EPS (all 4 pages: 0–3)

You haven't done L2 yet:
  • Chapter 1. UBS (missing pages 2–5)
  • Chapter 2. UDS (missing pages 0–2)

Learn L2 first, then practice, then L2 scope will be complete and L3 will unlock.

Ready for L2 learning?"
```

**Note:** Agent does not block; Learner could skip if they insist. But Agent has made clear the recommendation and the scope definition from A.

---

## 6. IMPLEMENTATION NOTES

### 6.1 Integration with `.cursor/rules/ile-learning-book.mdc`

Add new section § Agent reads Level→scope and gates from A:

```markdown
## § Agent reads Level→scope and gates from A (T-415)

**Trigger:** When Phase C page is approved, when Learner requests level progression, or at session start.

**Procedure:**

1. Read A → "Level → Phase C Scope (detailed)" to get scope for target level
2. Read A → "Phase C Organise — state" → "Approved Pages" to see what Learner has done
3. Compare: Are all required pages approved?
4. If YES → Suggest progression: "L_n scope complete ✓. Ready for L_n practice?"
5. If NO → Show gap: "L_n requires [list]. You've done [done]. Missing: [missing]."

**Gate validation:**

- Gates are **soft**: Agent suggests prerequisites but does not block
- Learner can choose to proceed or revisit
- Agent cites A as source: "According to A → Level→Scope..."

**No hard-coded map:** All scope comes from A. Same procedure works for any subject.

**Full procedure:** `docs/ai/implementation/ile-agent-reads-level-scope-gates.md`
```

### 6.2 Session Walkthrough Example

See §7 below for a concrete transcript showing Agent reading scope and guiding Learner.

### 6.3 Subject-Agnostic Design

This procedure is identical for all subjects. Only the A content varies:

| Subject                          | A Section: Level→Scope                               |
| -------------------------------- | ---------------------------------------------------- |
| COE_TECH_LONG_N_AI_ORCHESTRATION | L1: Ch 0–1 (pages 0–1); L2: Ch 1–2 (pages 0–2); etc. |
| COE_Data Science (hypothetical)  | L1: Ch 0–1 (pages 0–1); L2: Ch 1–2 (pages 0–3); etc. |

Agent reads from whatever A is active; no code changes needed.

---

## 7. EXAMPLE SESSION TRANSCRIPT

### Setup

- Learner has completed L1 learning (pages 0.0, 0.1, 1.0, 1.1 approved)
- Just completed L1 practice (solo, outside ILE)
- Returns to ILE asking about L2

### Transcript

**Learner:** "I've finished Level 1 learning and done the practice. What's next?"

**Agent:** "Excellent! Let me check your progress.

[Reads A → Level→Scope]

You've completed all Level 1 scope:
✓ Chapter 0. Overview & Summary (pages 0–1)
✓ Chapter 1. UBS (pages 0–1)
✓ Level 1 practice done ✓

**Next:** Level 2 learning.

For Level 2, you'll learn Chapter 1. UBS (deeper — pages 2–5 add causal layers) and Chapter 2. UDS (new topic — the root driver for hierarchical thinking).

Here's the full L2 scope:
• Chapter 1. UBS: Pages 2–5 (Drivers, Principles, Components, Steps)
• Chapter 2. UDS: Pages 0–2 (Overview, Blockers, Drivers)

Ready to start Level 2 learning?"

**Learner:** "What if I just do the practice now instead of all this learning?"

**Agent:** "I wouldn't recommend it. Here's why:

Level 2 practice is more complex — you'll need to understand:

1. The 3 causal layers of the Capability Gap (UBS.UB, UBS.UB.UB, UBS.UB.UD) — that's Chapter 1 pages 2–5
2. The root driver for Hierarchical Thinking (UDS.UD and its layers) — that's Chapter 2 pages 0–2

Without that foundation, L2 practice will be confusing.

My suggestion: Do L2 learning first (pages above). Then L2 practice will make sense. Then you'll be ready for L3.

What do you say — shall we start Chapter 1 Page 2 (Drivers)?

Or, if you want to jump ahead, I won't stop you. But I'm warning you it'll be harder."

**Learner:** "OK, let's do the learning properly. Start me with Chapter 1 Page 2."

**Agent:** "Great decision. Chapter 1. UBS — Page 2: Ultimate Drivers.

[Loads template, starts learning conversation]"

---

## 8. EDGE CASES & HANDLING

| Scenario                                                               | Agent Action                                                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Learner says "I'm done with L1, skip L2 learning, give me L2 practice" | Agent states scope requirement: "L2 practice needs L2 learning first (pages X, Y, Z). I can't give you practice without those. Options: (A) Learn L2 first, then practice; (B) Do practice anyway and learn as you go (harder); (C) Defer both." Learner chooses. |
| A section "Level→Scope" is missing or empty                            | Agent falls back: "I don't have your subject's level scope defined in A yet. Let's populate it together. What pages did you complete for L1?"                                                                                                                     |
| New subject (e.g., COE_Data Science) has no A yet                      | Agent waits for A to be created. Then reads scope from that A. No code change.                                                                                                                                                                                    |
| Learner disputes scope (e.g., "Why does L2 require page 2.1?")         | Agent: "That's defined in A → Level→Scope. If you think it's wrong, we can propose a change to A. But for now, A is the standard."                                                                                                                                |
| Learner completed pages out of order (e.g., did 1.2 before 1.0)        | Agent checks: approved_pages includes [0.0, 0.1, 1.0, 1.1, 1.2]. Scope requires [0.0, 0.1, 1.0, 1.1]. ✓ All required pages are approved. Agent allows progression. (Order doesn't matter; presence matters.)                                                      |

---

## 9. SUCCESS CRITERIA (A.C.)

**Noun-AC15:**
✅ Agent can read from A Level → Phase C scope and gates and use them to suggest order and inform the Learner.

**ScalAdv-AC6 (final):**
✅ Level → Phase C scope and order/gates defined per subject in A; Agent reads A and suggests sequence and gates; ILE does not hard-code level→topic map.

---

## 10. COMPLETION NOTES

**T-415 (this task)** completes:

- Noun-AC15: Agent behaviour for reading scope from A ✓
- ScalAdv-AC6: No hard-coded map in ILE; scope per-subject in A ✓

**After T-415 approval:**

- ✅ **All Iteration 4 tasks complete** (core + extension)
- ✅ **All 48 A.C. delivered** (Iterations 1–4)
- ✅ **ILE design & requirements complete** → Ready for State B (implementation/execution)

---

_Last updated: 2026-03-01 (T-415 draft)_
_Status: Ready for review_
