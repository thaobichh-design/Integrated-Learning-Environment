---
phase: implementation
title: ILE A (Subject Roadmap) Template Structure — Proof, Rubrics, Level→Scope (T-414)
description: Defines the canonical A template structure for proof landing zone, rubrics per level, and Level→Phase C scope. Subject-agnostic; used by T-305 (self-check), T-306 (rubric walk-through), and T-415 (Agent reads Level→scope).
feature: integrated-learning-environment
task: T-414
---

# ILE A Template Structure: Proof, Rubrics, Level→Scope

*T-414 defines the canonical A (Subject Roadmap & Level Specifications) template structure so that self-check (T-305), rubric walk-through (T-306), and level-scope-driven Agent behaviour (T-415) work for any subject without ILE code changes. This document explains what each section is, why it matters, and how it's used.*

**Cross-references:** Template → `templates/A-subject-roadmap-and-level-specifications.md` | Self-check uses → T-305 `ile-self-check-before-practice.md` | Rubric uses → T-306 `ile-rubric-walk-through-proof-recording.md` | Agent reads scope → T-415 (pending) | A example (COE_AI_ORCH) → `learning-book/COE_AI_ORCH/A. Subject Roadmap & Level Specifications/`

---

**Acceptance Criteria:** Noun-AC14, SustainAdj-AC6, ScalAdv-AC6 (partial)
**Dependencies:** T-305 (references A structure), T-306 (references A structure), T-415 (reads Level→scope from A)

---

## 1. PURPOSE

A (Subject Roadmap & Level Specifications) is the **source of truth** for a subject's learning path, requirements, and level progression. It answers:
- "What does each level require?" (Level Specifications)
- "How do I know if I've passed?" (Rubrics, Credentials)
- "Where do I find evidence of completion?" (Proof Landing Zone)
- "What chapters/topics/pages complete this level?" (Level → Phase C Scope)
- "What's my current level and progress?" (Level Completion Checklist, Session Log)

**Why three new sections (Rubrics, Level→Scope, Proof Landing Zone)?**
- **Rubrics:** Enable T-305 (self-check) and T-306 (rubric walk-through) to validate credentials deterministically
- **Level→Scope:** Enable T-415 to read which content belongs to which level, so Agent can suggest sequence without hard-coded level→topic map in ILE
- **Proof Landing Zone:** Provide a standard place to record evidence so proof capture is in-conversation byproduct, not a separate step

---

## 2. THE THREE NEW SECTIONS

### 2.1 Rubrics (per Level)

**What:** Pass/fail criteria per credential per level.

**Format:**
```
| Level | Credential | Pass Criteria | Fail Criteria |
|-------|-----------|---------------|---------------|
| L1 | Credential 1 | script runs, retrieves data, responds | script missing, doesn't run, no tool call |
| L1 | Credential 2 | screenshot shows agent output + tool | no screenshot, tool not visible |
| L2 | Credential 1 | 2-agent team with observable delegation | only 1 agent, no coordinator |
```

**How Agent uses it:**
- **T-305 (self-check before practice):** Agent presents criteria to Learner before practice starts so they know the standard
- **T-306 (rubric walk-through after practice):** Agent walks through each credential, validates evidence against criteria, marks ✓ PASS / ✗ FAIL
- Both use the **same criteria** (no special rules for Agent vs external assessor)

**How to populate:**
1. Look at "Subject-Specific Requirements & Credentials" section (below in A)
2. For each level, each credential:
   - **Pass Criteria:** What success looks like (reference the requirement, add specific markers)
   - **Fail Criteria:** What doesn't pass (opposite of pass, or common gaps)

**Example (from COE_AI_ORCH L1):**
```
| L1 | Working Python script (`my_first_agent.py`) | Script runs, creates Agno Agent with YFinance tool, retrieves live AAPL price, responds to query | Script missing, doesn't run, no tool call, tool fails |
```

---

### 2.2 Level → Phase C Scope (detailed)

**What:** Detailed mapping of which chapters/topics/pages from Phase C (Organise Information) belong to each level.

**Format:**
```
| Level | Chapters/Topics Required | Pages within Each | Notes |
|-------|--------------------------|-------------------|-------|
| L1 | Chapter 0. Overview; Chapter 1. UBS | Pages 0–2 (Overview, Blockers, Drivers) | Foundation |
| L2 | Chapter 1. UBS (full); Chapter 2. UDS | Pages 0–2 | Hierarchy + drivers |
| L3 | Chapter 2. UDS (full); Chapter 3. EPS | Pages 0–3 | Deeper layers + principles |
```

**Difference from "Links to Learning Book (per Level)":**
- **Links to Learning Book:** Brief, high-level; tells Learner "start with Chapter 0 and 1"
- **Level→Phase C Scope:** Detailed, granular; tells Agent "these specific pages complete this level"

**How Agent uses it:**
- **T-415 (Agent reads Level→scope from A):** Agent reads this section to know exactly which content belongs to each level
- **Without hard-coded map:** Agent doesn't have `if level==L1 then chapters = [0,1]` in code; instead, Agent reads A
- **Flexibility:** Each subject's A can define its own Level→scope; no ILE code change needed

**How to populate:**
1. Look at approved Phase C pages for your subject
2. Group pages by level (which pages did the Learner complete to reach L1? L2? etc.)
3. Link pages to corresponding chapters/topics in the Phase C folder structure

**Example (from COE_AI_ORCH):**
```
| L1 | Chapter 0. Overview; Chapter 1. UBS | Pages 0–1 (Overview + Blockers) | Learner understands Capability Gap |
| L2 | Chapter 1. UBS (full); Chapter 2. UDS | Pages 1–2 (Blockers, Drivers) | Learner understands UBS.UB.*, UDS.UD.* |
```

---

### 2.3 Proof Landing Zone (per Level)

**What:** Standard location where evidence for each level is stored or linked.

**Format:**
```
| Level | Credential 1 Evidence | Credential 2 Evidence | Credential 3 Evidence |
|-------|----------------------|----------------------|----------------------|
| L1 | `evidence/L1-agent.py` | `evidence/L1-screenshot.png` | *conversation transcript* |
| L2 | `evidence/L2-team.py` | `evidence/L2-conv-log.txt` | *session memory test* |
```

**Evidence types:**
- **Code:** Path relative to learning-book root (e.g., `evidence/L1-agent.py`)
- **File:** Same (e.g., `evidence/screenshot.png`)
- **External:** URL or link (e.g., Git commit, ClickUp task)
- **Inline:** Short text (e.g., "Verbal explanation on 2026-03-01 in Cursor chat")

**How Agent uses it:**
- **T-306 (rubric walk-through):** Learner brings evidence → Agent validates against rubric criteria → Agent records link in this table
- **Proof capture in-conversation:** As part of the conversation, Agent proposes the table update (e.g., "I'll record your script at `evidence/L1-agent.py`"). Learner approves. Agent writes to A. No separate copy-paste step.

**How external assessor uses it:**
- Same location, same format
- Assessor reads A → sees proof landing zone → verifies all links → checks evidence against rubrics
- No ambiguity: "Where is the proof?" → "A, Proof Landing Zone, L2, Credential 1"

**How to populate:**
- **Before practice:** Leave empty or note placeholder (e.g., "TBD")
- **During rubric walk-through (T-306):** Learner and Agent agree on location → Agent records link
- **After completion:** All evidence is linked in this table; Level Completion Checklist row shows ✅ (all 3 credentials met)

---

## 3. RELATIONSHIP TO OTHER A SECTIONS

### Existing sections (unchanged)

| Section | Purpose | Used by |
|---------|---------|---------|
| **Learner Progress Tracker** | Resume point; current level, target, next entry point | Agent (session start) |
| **Level Completion Checklist** | Did Learner complete this level? (Y/N, date, evidence) | Agent, Learner (progress) |
| **Gap Analysis** | What's missing between current and target? | Agent (suggest next steps) |
| **Level Specifications (L1–L7)** | Compact table of Requirements + Credentials per level | Agent, Learner (see standard) |
| **Links to Learning Book** | High-level mapping of level → chapters | Agent, Learner (start learning) |
| **Session Log** | Activity log for pickup | Agent (resume session) |
| **Phase C Organise — state** | Page-by-page work state (approved pages, decisions, causal seeds) | Agent (learning content generation) |
| **Subject-Specific Requirements & Credentials** | Detailed Requirements + Credentials subsections per level | Agent, Learner (level details) |

### New sections (T-414)

| Section | Purpose | Used by |
|---------|---------|---------|
| **Rubrics (per Level)** | Pass/fail criteria per credential | T-305 (self-check), T-306 (rubric walk-through), external assessor |
| **Level→Phase C Scope (detailed)** | Which pages complete each level | T-415 (Agent reads and suggests sequence) |
| **Proof Landing Zone (per Level)** | Where evidence is stored/linked | T-306 (record proof), external assessor (verify) |

### How they work together

**Example workflow:**
1. **Learner at L1:** Agent reads A → shows "Links to Learning Book" → suggests "Chapter 0 Overview + Chapter 1 UBS Pages 0–1"
2. **Learner completes Phase C pages:** A → "Current State (Phase C)" → "Approved Pages (in order)" updated
3. **Learner ready for L1 practice:** Agent reads A → "Level→Phase C Scope" → confirms "All L1 pages approved ✓"
4. **Agent offers self-check (T-305):** Agent reads "Level Specifications" + "Organise content" → asks 5–10 questions
5. **Learner does L1 practice:** Solo work (outside ILE)
6. **Learner returns with evidence:** Agent offers rubric walk-through (T-306)
7. **Rubric walk-through:** Agent reads "Rubrics (per Level)" → walks through each credential → validates evidence → records links in "Proof Landing Zone"
8. **Completion:** A → "Level Completion Checklist" row for L1 updated (✅ all credentials met, date, proof links) + "Proof Landing Zone" populated with evidence

---

## 4. SUBJECT-AGNOSTIC DESIGN

This structure is **subject-agnostic**: the template is the same for all subjects (COE_AI_ORCH, COE_Data Science, etc.), but the **content** varies per subject.

**Example: COE_AI_ORCH vs COE_Data Science**

Both have:
- Level Specifications (L1–L7)
- Rubrics (per Level)
- Level→Phase C Scope (per Level)
- Proof Landing Zone (per Level)

But content is different:

**COE_AI_ORCH L1 Rubrics:**
```
| L1 | Credential 1 | Working Python script with Agno Agent + YFinance tool | Script missing or doesn't use tools |
```

**COE_Data Science L1 Rubrics (hypothetical):**
```
| L1 | Credential 1 | Can write Python function that loads CSV and computes basic statistics | Cannot write function or doesn't handle CSV |
```

**Same structure, different content.** Agent and Learner use the same template and procedure for both.

---

## 5. IMPLEMENTATION NOTES

### 5.1 Populate the template

When creating a new A for a subject:

1. **Copy the template:** `templates/A-subject-roadmap-and-level-specifications.md`
2. **Fill existing sections:** Learner Progress Tracker, Level Completion Checklist, Level Specifications, Links to Learning Book, Subject-Specific Requirements & Credentials
3. **Fill new sections (T-414):**
   - **Rubrics (per Level):** Derive from Credentials; add Pass/Fail criteria for each
   - **Level→Phase C Scope (detailed):** Map your subject's Phase C chapters/topics to levels
   - **Proof Landing Zone (per Level):** Leave empty initially; fill during rubric walk-through (T-306)

### 5.2 Agent reads A sections

Agent should prioritise sections in this order:

| Priority | Section | Used by | When |
|----------|---------|---------|------|
| 1 | Learner Progress Tracker | Session start | Resume level, current entry point |
| 2 | Level Completion Checklist | Session start | Where is Learner in the journey? |
| 3 | Level Specifications | Self-check (T-305) | What are requirements for this level? |
| 4 | Rubrics (per Level) | Rubric walk-through (T-306) | Walk through each credential |
| 5 | Level→Phase C Scope (detailed) | Suggest sequence (T-415) | Which content is needed for this level? |
| 6 | Proof Landing Zone (per Level) | Record proof (T-306) | Where to record evidence? |
| 7 | Session Log | Resume pickup | Activity log |
| 8 | Phase C Organise — state | Generate content (Learning) | Which pages are approved? |

### 5.3 Example: COE_AI_ORCH A

The actual COE_AI_ORCH A (in `learning-book/COE_AI_ORCH/A. Subject Roadmap...`) demonstrates all three new sections:

- **Rubrics:** Defined per level (based on COE_AI_ORCH credentials)
- **Level→Phase C Scope:** Maps Learner's approved Phase C pages to levels
- **Proof Landing Zone:** Populated after Learner completes L1, L2, etc. practice

Refer to this as a reference implementation for other subjects.

---

## 6. SUCCESS CRITERIA (A.C.)

**Noun-AC14:**
✅ A supports proof landing zone and rubrics per level (pass/fail per credential), usable by Agent and future external assessor.

**SustainAdj-AC6:**
✅ A template (or defined structure) supports proof landing zone, rubrics per level, and Level→Phase C scope so new subjects can adopt same structure without changing ILE code.

**ScalAdv-AC6 (partial):**
✅ Level → Phase C scope is defined per subject in A; Agent can read and use it to suggest order and inform the Learner; no hard-coded level→topic map in ILE.

---

## 7. NEXT STEPS

- **T-414 (this task):** Template structure defined ✅
- **T-415 (next):** Agent behaviour for reading Level→scope from A and suggesting sequence
- **T-305, T-306 (approved):** Both now reference A template sections defined in T-414

---

_Last updated: 2026-03-01 (T-414 draft)_
_Status: Ready for review_
