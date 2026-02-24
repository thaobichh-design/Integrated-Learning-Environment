---
phase: implementation
title: ILE Roadmap Discovery — Populate A (Subject Roadmap) via Learner Interview
description: Procedure for the Agent to guide the Learner through a structured interview (like PM Problem Discovery / User's Requirements) so A. Subject Roadmap & Level Specifications is populated to fit the individual—context, goal, habits, level aspirations, gaps.
feature: integrated-learning-environment
---

# Roadmap Discovery: Populate A via Learner Interview

**Purpose:** A (Subject Roadmap & Level Specifications) is the **starting point for every session** (resume or new). When A is missing or the Learner wants to (re)define their roadmap, the Agent acts like an **expert teacher / Product Manager** interviewing the Learner—in the same spirit as **Problem Discovery** and **User's Requirements**—so the curriculum, roadmap, and level specs are **best fitted to the individual**.

**When to run:**
- **A is missing** (Learner starts a completely new Area) → offer Roadmap Discovery before phase/entry-point flow.
- **Learner asks** to (re)define, (re)populate, or refresh their roadmap → run Roadmap Discovery (full or by section).

**Output:** A populated (or updated) from `templates/A-subject-roadmap-and-level-specifications.md`, with Learner Progress Tracker, Level Specifications (L1–L7), Links to Learning Book, Session Log, and optionally Gap Analysis and Level Completion Checklist—all informed by the Learner's own context, goal, and habits.

**Cross-references:** A template → `templates/A-subject-roadmap-and-level-specifications.md` | Flow (new book) → `ile-minimal-flow.md` § (a) Entirely new book | Problem Discovery framing → `docs/ai/frameworks/effective-system-design.md` Phase 1, `docs/ai/requirements/README.md` Phase 1.

---

## 1. Interview blocks (mirror Problem Discovery)

Conduct **one block at a time**. Ask clarifying questions; propose or write into A as the Learner answers; **confirm with the Learner** before moving to the next block. Do not rush; the goal is a roadmap that fits *them*.

| Block | Goal (PM analogue) | What to discover | Maps to A section(s) |
|-------|--------------------|------------------|----------------------|
| **1. Context** | Who is the Learner in this subject? | Why this subject? Current role, experience, prior learning (formal or informal). What do they already use this for? | Level Specifications (which levels matter); Links to Learning Book (which chapters/topics matter for their role). |
| **2. Goal (Learning UDO)** | What is the desired outcome? | Desired outcome for *this* subject: e.g. "Reach L3 Apply for my role," "Biological mastery L1→L7," "Pass a certification by [date]." Target level and target date. | **Learner Progress Tracker:** Target Level, Target Date; **Level Specifications** (requirements/credentials for that level). |
| **3. Learning habits** | How does the Learner learn? | How often (sessions per week), how long (chunk size), preferred style (chunks vs long sessions), constraints (time, energy, focus). What tends to block or support them? | **Session Log** expectations; how Agent suggests **Next Recommended Entry Point** (chunk-friendly); optional note in A or in session behavior. |
| **4. Current level & gaps** | Where are they now vs where they want to be? | Self-assessed current level (L1–L7 or sub-level). Gaps between current and target: what's missing? What do they already know in this subject? | **Learner Progress Tracker:** Current Level; **Gap Analysis**; **Level Completion Checklist** (what's met, what's not). |
| **5. Curriculum fit** | Which content maps to which level for *them*? | Which chapters/topics matter most for their role or target level? (Optional: use standard Links to Learning Book first; refine with Learner.) | **Links to Learning Book (per Level):** Level → Recommended Chapters/Topics. |
| **6. Level specifications (L1–L7)** | What does each level mean for this subject? | For the subject and the Learner's context: what are the **requirements** and **credentials** at each level (at least for levels they care about)? Agent can propose from SFIA + subject; Learner confirms or edits. | **Level Specifications (L1–L7):** Requirements, Credentials per level. **Subject-Specific Requirements & Credentials** section. |

---

## 2. Example questions (by block)

Use these as a scaffold; adapt to the subject and the Learner's answers.

**Block 1 — Context**
- "Why this subject? What's your current role or how do you use it today?"
- "What prior learning or experience do you have in this area (formal or informal)?"

**Block 2 — Goal (Learning UDO)**
- "What's your desired outcome for this subject? (e.g. reach a certain level for your role, pass a certification, master the full ladder L1→L7.)"
- "What target level and time frame do you have in mind (e.g. L3 by end of year)?"

**Block 3 — Learning habits**
- "How often can you dedicate time to this (e.g. sessions per week)? How long are your typical sessions?"
- "Do you prefer short, focused chunks or longer deep-dive sessions? What usually gets in the way of learning (time, energy, focus)?"

**Block 4 — Current level & gaps**
- "Where would you place yourself today in this subject (L1–L7 or sub-level)?"
- "What are the main gaps between where you are and where you want to be?"

**Block 5 — Curriculum fit**
- "Which chapters or topics matter most for your role or target level? (I can suggest a default mapping; you can adjust.)"

**Block 6 — Level specifications**
- "For this subject, what should 'L2' or 'L3' mean in practice—requirements and credentials? (I can propose from SFIA + subject; you confirm or edit.)"

---

## 3. Agent behavior

1. **Create A from template** if the file does not exist: use `templates/A-subject-roadmap-and-level-specifications.md` and write to the correct path per Learning Book structure (e.g. `learning-book/{subject}/A. Subject Roadmap & Level Specifications/` or per `learning-book/README.md`).
2. **Run blocks in order** (1 → 6). For each block: ask 1–2 questions, listen, then **propose concrete text or table rows** for the relevant A section(s). Wait for Learner approval before writing and before moving on.
3. **Do not invent** requirements or credentials; propose from SFIA + subject context and let the Learner confirm or edit.
4. **Blocks 5 and 6 — if the Learner cannot populate:** The Agent populates on their behalf from (a) standard/default content (e.g. template default Links to Learning Book; SFIA + subject for Level Specifications) and (b) what was learned in blocks 1–4 (e.g. target level, role, context). Then the Learner confirms or edits.
5. **RACI:** The Learner is accountable for their roadmap; the Agent proposes and writes only with explicit approval (e.g. "Approve?", "Confirm?").
6. **Session Log:** After Discovery, optionally add an initial Session Log row: "Roadmap Discovery completed; A populated."

---

## 4. When Discovery is done

- **New book:** Proceed to normal flow: phase choice → entry points → template load → learning conversation (per `ile-minimal-flow.md`).
- **Refresh:** If the Learner only wanted to update part of A, return to the flow at the appropriate step (e.g. surface updated level and recommendations per T-303).

---

## 5. Command and rule

- **Command:** User can invoke **`/roadmap-discovery`** (or "run roadmap discovery") to start or resume the interview. Agent loads this doc and runs the procedure.
- **Rule:** When A is missing at session start, the Agent offers to run Roadmap Discovery per this doc before offering phase/entry points. When the Learner asks to (re)define or (re)populate the roadmap, the Agent follows this doc.

*Evidence: A is the starting point for every session; curriculum and level specs are fitted to the individual via structured discovery, analogous to PM Problem Discovery and User's Requirements.*
