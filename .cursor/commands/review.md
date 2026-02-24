---
description: Iteration retrospective — review all evidence before advancing. Use at iteration boundaries or any time the User wants a progress audit.
---

# UTILITY: REVIEW (Iteration Retrospective)

**PRIME DIRECTIVE:** Produce a structured evidence review of a completed (or in-progress) iteration so the User can make an informed decision about whether the UDO/UDS/UBS mapping still holds before advancing. Read-only — do not modify docs or execute tasks.

## Step 0: Determine Active Feature
Same logic as State B Step 0. Identify the active feature and its planning doc.

## Step 1: Identify the Iteration to Review
- Default: the **most recently completed iteration** (the highest iteration number where all tasks are 🟢 Reviewed/Tested).
- If the User specifies an iteration number, review that one.
- If no iteration is fully complete, review the current in-progress iteration (partial review).

## Step 2: Gather Evidence
From the planning doc (Execution Matrix + Master Scope Mapping Table B), collect:
1. **All tasks in this iteration** — ID, title, status, and the evidence from the task's "Evidence of Truth" or Table B.
2. **All A.C. validated** — which A.C. IDs from Table B are now 🟢, with their deterministic evidence.
3. **Skipped or stuck tasks** — any 🟠 Stuck tasks and why they were blocked.
4. **Unvalidated A.C.** — any A.C. assigned to this iteration (Table A) that are NOT yet 🟢.

## Step 3: Output the Retrospective

**Iteration [N]: [Name] — Review**

**Validated tasks:**

| Task | Title | A.C. Addressed | Evidence |
| :--- | :--- | :--- | :--- |
| [ID] | [title] | [A.C. IDs] | [brief evidence summary] |

**A.C. now 🟢 (validated in this iteration):**

| A.C. ID | Requirement | Evidence |
| :--- | :--- | :--- |
| [ID] | [from Requirements Phase 3] | [from Table B] |

**Gaps / Risks:**
- 🟠 Stuck tasks: [list or "None"]
- Unvalidated A.C. for this iteration: [list or "All validated"]
- Open risks or dependencies: [any blockers that surfaced during execution]

**Reflection prompt:**
> *Based on the evidence above:*
> 1. *Does the original UDO still describe what the User actually wants?* What would have to be true for the UDO to be wrong or incomplete?
> 2. *Have we discovered new Blockers (UBS) or Drivers (UDS) during this iteration?* Have we discovered new Nouns, Verbs, or Adverbs we care about (e.g. a capability that should be first-class)?
> 3. *Does the scope for the next iteration still make sense, or should we re-plan?* Any outcomes from this iteration that should change what we do in the next iteration? Re-plan = run /state-a to update requirements, design, and planning.
>
> *Reply "Proceed to Iteration N+1" to advance, "Re-plan" to run /state-a, or share your thoughts for discussion.*

## When to Run This
- **At the iteration transition gate:** The agent in `/state-b` will hard-stop at iteration boundaries. Run `/review` before deciding "Proceed" or "Re-plan."
- **Mid-iteration audit:** Run any time to see current progress within an iteration.
- **Before /handoff:** Good practice to review before handing off to another device or session.
