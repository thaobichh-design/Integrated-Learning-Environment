#!/usr/bin/env python3
"""
Rebuild templates/D-distilled-understanding-full.md from the PDF content.
Table: 22 columns. No blank lines between table rows.
"""
import os

# Normalize: PDF uses Unicode ligatures
def n(s):
    if not s:
        return s
    return s.replace("\u0065\u0066\u0066", "eff").replace("eﬀ", "eff").replace("eﬃ", "effi").replace("ﬁ", "fi").replace("ﬂ", "fl").strip()

# Empty cells for topic-only rows (cols 4-21)
EMPTY = ""
def empty_cols(n):
    return [EMPTY] * n

# 22 columns: 0=DU, 1=6 CORE TOPICS, 2=DESCRIPTION, 3=30 CORE SUB-TOPICS,
# 4-18 = 14 sub-questions (Overview 4-10, Failure 11-17, 18=What to do, 19=Other, 20=Next Steps?), 21=LEARNER'S NOTES
def row(c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21):
    return [str(x) if x is not None else "" for x in [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21]]

def esc(c):
    """Escape pipe for markdown cell."""
    return (c or "").replace("|", "\\|")

def md_row(cells):
    return "| " + " | ".join(esc(c) for c in cells) + " |"

# --- INTRO (from template, matches PDF meaning) ---
INTRO = """[OWNER]_SUBJECT NAME - D. DISTILLED UNDERSTANDING
DISTILLED UNDERSTANDING
In order to achieve the desired outcomes in the subject, the doer/user/learner must have an effective system to enable them to perform the right actions. This effective system has 7 keys components:
i. The Effective Doer/User (i.e, the Subject's "EU")
ii. The Effective User's Effective Actions (i.e, the Subject's "EA")
iii. The Desired Outcomes of the Effective User's Effective Actions (i.e, the Subject's "EO")
iv. The Effective Principles of the Effective User's Effective Actions (i.e, the Subject's "EP")
v. The Effective Operating Environment of the Effective User's Effective Actions (i.e, the Subject's "EOE")
vi. The Effective Operating Tools used in the Effective User's Effective Actions (i.e, the Subject's "EOT")
vii. The Effective Operating Procedure of the Effective User's Effective Actions (i.e, the Subject's "EOP")
The Effective Principles are critical to ensure success of the effective system. It is the foundation on which the system operates. In order to be effective, these principles must perform the two goals well:

1. Minimize failure risks by disable/avoid the main blockers (UBS) and root blockers (the drivers of UBS or the blockers of the UDS)
2. Optimize the desired output by enable/utilize the main drivers (UDS) and root drivers (the drivers of UDS or the blockers of UBS)

The following table provide details of the effective system. It facilitates a comprehensive diagnosis and allows the user to design the effective system to achieve their desired outcomes.
DISTILLED 6 CORE TOPICS DESCRIPTION OF THE 30 CORE SUB-TOPICS 14 CORE SUB-TOPIC QUESTIONS, TYPICAL ANSWERS & EXPLANATIONS LEARNER'S NOTES
UNDERSTANDING TOPIC & KEY TOPIC (Borrowing the relevant Topics' Basic Questions, (Advanced Questions & Guide for Learner after learning this sub-
QUESTIONS Advanced Questions are nice to have but not necessary) topic)
OVERVIEW SUCCESS FAILURE
What is it for? What is it? How does it work What ultimately How do the ultimate drivers What principles are the What environmental conditions do What How can it fail? What ultimately How do the ultimate blockers What principles are the What environmental conditions do What What Other Questions Next Steps to
Why is it important? successfully? cause it to work cause it to work successfully? ultimate drivers based on? the ultimate drivers require to tool(s) cause it to fail? cause it to fail? ultimate blockers based on? the ultimate blockers require to tool(s) to do Take

"""

# Table header rows (from template - same structure)
HEADER_ROW1 = "| DISTILLED UNDERSTANDING     | 6 CORE TOPICS                                                                                                                                                                                                                                                                                                                                                                                                                            | DESCRIPTION OF THE TOPIC & KEY TOPIC QUESTIONS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 30 CORE SUB-TOPICS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 14 CORE SUB-TOPIC QUESTIONS, TYPICAL ANSWERS & EXPLANATIONS (Borrowing the relevant Topics' Basic Questions, Advanced Questions are nice to have but not necessary)     |                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                      |                                                                   |                                                                                |                                                                         |                                                                                              |                                                                   |                                    |                                                       |                                                                    |                                                                          |                                                                                                |                                                                     |                              | LEARNER'S NOTES (Advanced Questions & Guide for Learner after learning this sub- topic) |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |"
SEP_ROW    = "| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------ | ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ---------------------------------- | ----------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ---------------------------- | --------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |"
SUBH1      = "|                             |                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | OVERVIEW                                                                                                                                                                |                                                                                                                                                                                                           | SUCCESS                                                                                                                                                                                                                                                              |                                                                   |                                                                                |                                                                         |                                                                                              |                                                                   | FAILURE                            |                                                       |                                                                    |                                                                          |                                                                                                |                                                                     |                              |                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |"
SUBH2      = "|                             |                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | What is it for? Why is it important? (Relevance)                                                                                                                        | What is it? (Introduction)                                                                                                                                                                                | How does it work successfully? (Success Actions)                                                                                                                                                                                                                     | What ultimately cause it to work successfully? (Ultimate Drivers) | How do the ultimate drivers cause it to work successfully? (Success Mechanism) | What principles are the ultimate drivers based on? (Success Principles) | What environmental conditions do the ultimate drivers require to work? (Success Environment) | What tool(s) do ultimate drivers require to work? (Success Tools) | How can it fail? (Failure Actions) | What ultimately cause it to fail? (Ultimate Blockers) | How do the ultimate blockers cause it to fail? (Failure Mechanism) | What principles are the ultimate blockers based on? (Failure Principles) | What environmental conditions do the ultimate blockers require to work? (Failure Environments) | What tool(s) the ultimate blockers require to work? (Failure Tools) |                              | What to do if it fails? (What else?)                                                    | Other Questions (Others)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Next Steps to Take (Now What? Now How?)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |"

# Build data rows from PDF content (exact wording from PDF, normalized)
E = EMPTY
SAME = "(Same with the above)"
SUBJECT_PLACEHOLDER = "(EFFECTIVE + NAME OF SUBJECT )"

# Section 0
r0_core = "0. OVERVIEW & SUMMARY OF " + SUBJECT_PLACEHOLDER + " i.e., • Why is the Subject important? • What is it? What is it not? • How does it work in general? How can it fail?"
r0_desc = "Like the Preface, Foreword of Introduction section of a book, this topic covers a brief introduction of the Subject, its relevance in our lives, and how it works Basic Questions: 1. What is it for? Why is it important? 2. What is the Subject? What is it not? 3. How does it work in general? How can it fail?"
r0_sub  = "0. OVERVIEW & SUMMARY OF " + SUBJECT_PLACEHOLDER + " (Subject, EO, EA) i.e., • Why is the Subject important? What is it for? • What is it? What is it not? • How does it work in general? How can it fail?"
r0_notes = 'Effective Operating Environment ("EOE"): 1. Sustainability - Minimize Failure Risks: 2. Sustainability - Produce Desired Outcomes: 3. Efficiency - Minimize Failure Risks: 4. Efficiency - Produce Desired Outcomes: 5. Scalability - Minimize Failure Risks: 6. Scalability - Produce Desired Outcomes: Effective Operating Environment ("EOE"): 1. Sustainability - Minimize Failure Risks: 2. Sustainability - Produce Desired Outcomes: 3. Efficiency - Minimize Failure Risks: 4. Efficiency - Produce Desired Outcomes: 5. Scalability - Minimize Failure Risks: 6. Scalability - Produce Desired Outcomes: Effective Operating Tools ("EOT"): 1. Sustainability - Minimize Failure Risks: 2. Sustainability - Produce Desired Outcomes: 3. Efficiency - Minimize Failure Risks: 4. Efficiency - Produce Desired Outcomes: 5. Scalability - Minimize Failure Risks: 6. Scalability - Produce Desired Outcomes: '
r0_notes2 = 'Effective Operating Procedure ("EOP"): 1. Sustainability - Minimize Failure Risks: 2. Sustainability - Produce Desired Outcomes: 3. Efficiency - Minimize Failure Risks: 4. Efficiency - Produce Desired Outcomes: 5. Scalability - Minimize Failure Risks: 6. Scalability - Produce Desired Outcomes:'

data_rows = [
    row("EFFECTIVE + NAME OF SUBJECT", r0_core, r0_desc, r0_sub,
        "EO:", "Subject:", "EA:", "UDS:", "UDS.Actions:", "UDS.Principles:", "UDS.Environment:", "UDS.Tools:",
        "Subject.FailedActions:", "UBS:", "UBS.Actions:", "UBS.Principles:", "UBS.Environment:", "UBS.Tools:", E, E, E,
        r0_notes + r0_notes2),
]

# 1. ULTIMATE BLOCKING SYSTEM
ubs_core = '1. ULTIMATE BLOCKING SYSTEM ("UBS") OF ' + SUBJECT_PLACEHOLDER + ' i.e., • What ultimately (i.e., directly & mainly) determines the failure (i.e., the "Ultimate Blocking System" or the "UBS", and its components "Ultimate Blockers") of the Subject? • How does the Ultimate Blocking System of the Subject work? How can it possibly fail? • Why does the Ultimate Blocking System of the Subject work? Why can it possibly fail?'
ubs_desc = "This topic is a detailed discussion of the Subject's blockers of effectiveness: Basic Questions: 1. What ultimately (i.e., directly & mainly) determines the failure (i.e., the \"Ultimate Blocking System\", or the \"UBS\") of the Subject? 2. How does the Ultimate Blocking System work in general (i.e., the \"UBS.Actions\") ? How does it prevent the Subject to be effective? How can it fail to do so? 3. What cause the Ultimate Blocking System to work effectively (i.e., the \"UBS.UD\")? What may cause it to possibly fail (i.e., the \"UBS.UB\")? 4. Why does the Ultimate Blocking System work effectively? Why can it possibly fail? Advanced Questions: (To Study 1 Layer Deeper) 5. What are the governing principles that best enable the Ultimate Blocking System to become the ultimate one (i.e., the \"UBS.Principles\")? 6. What is the environment that fully incorporate all the UBS.Principles (i.e., the \"UBS.Environment\")? 7. What are the tools that fully incorporate all the UBS.Principles (i.e., the \"UBS.Tools\")? 8. How can we best overcome the Ultimate Blocking System to achieve the desired effectiveness in this Subject (i.e., the \"UBS.Procedure\")?"

data_rows.append(row(E, ubs_core, ubs_desc, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E))

# 1.0 - 1.6
def ubs_row(sub, outcomes, intro, actions, ud, ud_a, ud_p, ud_e, ud_t, failed, ub, ub_a, ub_p, ub_e, ub_t):
    return row(E, E, E, sub, outcomes, intro, actions, ud, ud_a, ud_p, ud_e, ud_t, failed, ub, ub_a, ub_p, ub_e, ub_t, E, E, E, E)

data_rows.append(ubs_row(
    '1.0. OVERVIEW & SUMMARY OF THE SUBJECT\'S ULTIMATE BLOCKING SYSTEM ("UBS", "UBS.OUTCOMES" & "UBS.ACTIONS") (Why Important? What is it? How does it work in general?)',
    "UBS.Outcomes:", "UBS: " + SAME, "UBS.Actions: " + SAME, "UBS.UD:", "UBS.UD.Actions:", "UBS.UD.Principles:", "UBS.UD.Environment:", "UBS.UD.Tools:",
    "UBS.FailedActions:", "UBS.UB:", "UBS.UB.Actions:", "UBS.UB.Principles:", "UBS.UB.Environment:", "UBS.UB.Tools:"))
data_rows.append(ubs_row(
    '1.1. ULTIMATE BLOCKERS OF THE SUBJECT\'S ULTIMATE BLOCKING SYSTEM ("UBS.UB") (What prevents it from working effectively?)',
    "UBS.UB.Outcomes:", "UBS.UB: " + SAME, "UBS.UB.Actions: " + SAME, "UBS.UB.UD:", "UBS.UB.UD.Actions:", "UBS.UB.UD.Principles:", "UBS.UB.UD.Environment:", "UBS.UB.UD.Tools:",
    "UBS.UB.FailedActions:", "UBS.UB.UB:", "UBS.UB.UB.Actions:", "UBS.UB.UB.Principles:", "UBS.UB.UB.Environment:", "UBS.UB.UB.Tools:"))
data_rows.append(ubs_row(
    '1.2. ULTIMATE DRIVERS OF THE SUBJECT\'S ULTIMATE BLOCKING SYSTEM ("UBS.UD") (What makes it work effectively?)',
    "UBS.UD.Outcomes:", "UBS.UD: " + SAME, "UBS.UD.Actions: " + SAME, "UBS.UD.UD:", "UBS.UD.UD.Actions:", "UBS.UD.UD.Principles:", "UBS.UD.UD.Environment:", "UBS.UD.UD.Tools:",
    "UBS.UD.FailedActions:", "UBS.UD.UB:", "UBS.UD.UB.Actions:", "UBS.UD.UB.Principles:", "UBS.UD.UB.Environment:", "UBS.UD.UB.Tools:"))
data_rows.append(ubs_row(
    '1.3. CORE VALUES AND PRINCIPLES OF THE SUBJECT\'S ULTIMATE BLOCKING SYSTEM ("UBS.PRINCIPLES") (Why does it work effectively?)',
    "UBS.Principles.Outcomes:", "UBS.Principles: " + SAME, "UBS.Principles.Actions:", "UBS.Principles.UD:", "UBS.Principles.UD.Actions:", "UBS.Principles.UD.Principles:", "UBS.Principles.UD.Environment:", "UBS.Principles.UD.Tools:",
    "UBS.Principles.FailedActions:", "UBS.Principles.UB:", "UBS.Principles.UB.Actions:", "UBS.Principles.UB.Principles:", "UBS.Principles.UB.Environment:", "UBS.Principles.UB.Tools:"))
data_rows.append(ubs_row(
    '1.4. ENVIRONMENT OF THE SUBJECT\'S ULTIMATE BLOCKING SYSTEM ("UBS.ENVIRONMENT") (Now What?)',
    "UBS.Environment.Outcomes:", "UBS.Environment: " + SAME, "UBS.Environment.Actions:", "UBS.Environment.UD:", "UBS.Environment.UD.Actions:", "UBS.Environment.UD.Principles:", "UBS.Environment.UD.Environment:", "UBS.Environment.UD.Tools:",
    "UBS.Environment.FailedActions:", "UBS.Environment.UB:", "UBS.Environment.UB.Actions:", "UBS.Environment.UB.Principles:", "UBS.Environment.UB.Environment:", "UBS.Environment.UB.Tools:"))
data_rows.append(ubs_row(
    '1.5. TOOLS OF THE SUBJECT\'S ULTIMATE BLOCKING SYSTEM ("UBS.TOOLS") (Now What?)',
    "UBS.Tools.Outcomes:", "UBS.Tools: " + SAME, "UBS.Tools.Actions:", "UBS.Tools.UD:", "UBS.Tools.UD.Actions:", "UBS.Tools.UD.Principles:", "UBS.Tools.UD.Environment:", "UBS.Tools.UD.Tools:",
    "UBS.Tools.FailedActions:", "UBS.Tools.UB:", "UBS.Tools.UB.Actions:", "UBS.Tools.UB.Principles:", "UBS.Tools.UB.Environment:", "UBS.Tools.UB.Tools:"))
data_rows.append(ubs_row(
    '1.6. STEPS TO OVERCOME THE SUBJECT\'S ULTIMATE BLOCKING SYSTEM ("UBS.PROCEDURE") (Now How?)',
    "UBS.Procedure.Outcomes:", "UBS.Procedure: " + SAME, "UBS.Procedure.Actions:", "UBS.Procedure.UD:", "UBS.Procedure.UD.Actions:", "UBS.Procedure.UD.Principles:", "UBS.Procedure.UD.Environment:", "UBS.Procedure.UD.Tools:",
    "UBS.Procedure.FailedActions:", "UBS.Procedure.UB:", "UBS.Procedure.UB.Actions:", "UBS.Procedure.UB.Principles:", "UBS.Procedure.UB.Environment:", "UBS.Procedure.UB.Tools:"))

# 2. ULTIMATE DRIVING SYSTEM
uds_core = '2. ULTIMATE DRIVING SYSTEM ("UDS") OF ' + SUBJECT_PLACEHOLDER + ' i.e., • What ultimately (i.e., directly & mainly) determines the success (i.e., the "Ultimate Driving System" or the "UDS", and its components "Ultimate Drivers") of the Subject? • How does the Ultimate Driving System of the Subject work? How can it possibly fail? • Why does the Ultimate Driving System of the Subject work? Why can it possibly fail?'
uds_desc = 'This topic is a detailed discussion of the Subject\'s drivers of effectiveness: Basic Questions: 1. What ultimately (i.e., directly & mainly) determines the success (i.e., the "Ultimate Driving System", or the "UDS") of the Subject? 2. How does the Ultimate Driving System work in general (i.e., the "UDS.Actions")? How does it enable the Subject to be effective? How can it possibly fail to do so? 3. What cause the Ultimate Blocking System to work effectively (i.e., the "UDS.UD")? What may cause it to possibly fail (i.e., the "UDS.UB")? 4. Why does the Ultimate Blocking System work effectively? Why can it possibly fail? Advanced Questions: (To Study 1 Layer Deeper) 5. What are the governing principles that best enable the Ultimate Driving System to become the ultimate one (i.e., the "UDS.Principles")? 6. What is the environment that fully incorporate all the UDS.Principles (i.e., the "UDS.Environment")? 7. What are the tools that fully incorporate all the UDS.Principles (i.e., the "UDS.Tools")? 8. How can we best exploit the Ultimate Driving System to achieve the desired effectiveness in this Subject(i.e., the "UDS.Procedure")?'

data_rows.append(row(E, uds_core, uds_desc, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E))

def uds_row(sub, outcomes, intro, actions, ud, ud_a, ud_p, ud_e, ud_t, failed, ub, ub_a, ub_p, ub_e, ub_t):
    return row(E, E, E, sub, outcomes, intro, actions, ud, ud_a, ud_p, ud_e, ud_t, failed, ub, ub_a, ub_p, ub_e, ub_t, E, E, E, E)

data_rows.append(uds_row(
    '2.0. OVERVIEW & SUMMARY OF THE SUBJECT\'S ULTIMATE DRIVING SYSTEM ("UDS", "UDS.OUTCOMES" & "UDS.ACTIONS") (Why Important? What is it? How does it work in general?)',
    "UDS.Outcomes:", "UDS: " + SAME, "UDS.Actions: " + SAME, "UDS.UD:", "UDS.UD.Actions:", "UDS.UD.Principles:", "UDS.UD.Environment:", "UDS.UD.Tools:",
    "UDS.FailedActions:", "UDS.UB:", "UDS.UB.Actions:", "UDS.UB.Principles:", "UDS.UB.Environment:", "UDS.UB.Tools:"))
data_rows.append(uds_row(
    '2.1. ULTIMATE BLOCKERS OF THE SUBJECT\'S ULTIMATE DRIVING SYSTEM ("UDS.UB") (What prevents it from working effectively?)',
    "UDS.UB.Outcomes:", "UDS.UB: " + SAME, "UDS.UB.Actions: " + SAME, "UDS.UB.UD:", "UDS.UB.UD.Actions:", "UDS.UB.UD.Principles:", "UDS.UB.UD.Environment:", "UDS.UB.UD.Tools:",
    "UDS.UB.FailedActions:", "UDS.UB.UB:", "UDS.UB.UB.Actions:", "UDS.UB.UB.Principles:", "UDS.UB.UB.Environment:", "UDS.UB.UB.Tools:"))
data_rows.append(uds_row(
    '2.2. ULTIMATE DRIVERS OF THE SUBJECT\'S ULTIMATE DRIVING SYSTEM ("UDS.UD") (What makes it work effectively?)',
    "UDS.UD.Outcomes:", "UDS.UD: " + SAME, "UDS.UD.Actions: " + SAME, "UDS.UD.UD:", "UDS.UD.UD.Actions:", "UDS.UD.UD.Principles:", "UDS.UD.UD.Environment:", "UDS.UD.UD.Tools:",
    "UDS.UD.FailedActions:", "UDS.UD.UB:", "UDS.UD.UB.Actions:", "UDS.UD.UB.Principles:", "UDS.UD.UB.Environment:", "UDS.UD.UB.Tools:"))
data_rows.append(uds_row(
    '2.3. CORE VALUES AND PRINCIPLES OF THE SUBJECT\'S ULTIMATE DRIVING SYSTEM ("UDS.PRINCIPLES") (Why does it work effectively?)',
    "UDS.Principles.Outcomes:", "UDS.Principles: " + SAME, "UDS.Principles.Actions:", "UDS.Principles.UD:", "UDS.Principles.UD.Actions:", "UDS.Principles.UD.Principles:", "UDS.Principles.UD.Environment:", "UDS.Principles.UD.Tools:",
    "UDS.Principles.FailedActions:", "UDS.Principles.UB:", "UDS.Principles.UB.Actions:", "UDS.Principles.UB.Principles:", "UDS.Principles.UB.Environment:", "UDS.Principles.UB.Tools:"))
data_rows.append(uds_row(
    '2.4. ENVIRONMENT OF THE SUBJECT\'S ULTIMATE DRIVING SYSTEM ("UDS.ENVIRONMENT") (Now What?)',
    "UDS.Environment.Outcomes:", "UDS.Environment: " + SAME, "UDS.Environment.Actions:", "UDS.Environment.UD:", "UDS.Environment.UD.Actions:", "UDS.Environment.UD.Principles:", "UDS.Environment.UD.Environment:", "UDS.Environment.UD.Tools:",
    "UDS.Environment.FailedActions:", "UDS.Environment.UB:", "UDS.Environment.UB.Actions:", "UDS.Environment.UB.Principles:", "UDS.Environment.UB.Environment:", "UDS.Environment.UB.Tools:"))
data_rows.append(uds_row(
    '2.5. TOOLS OF THE SUBJECT\'S ULTIMATE DRIVING SYSTEM ("UDS.TOOLS") (Now What?)',
    "UDS.Tools.Outcomes:", "UDS.Tools: " + SAME, "UDS.Tools.Actions:", "UDS.Tools.UD:", "UDS.Tools.UD.Actions:", "UDS.Tools.UD.Principles:", "UDS.Tools.UD.Environment:", "UDS.Tools.UD.Tools:",
    "UDS.Tools.FailedActions:", "UDS.Tools.UB:", "UDS.Tools.UB.Actions:", "UDS.Tools.UB.Principles:", "UDS.Tools.UB.Environment:", "UDS.Tools.UB.Tools:"))
data_rows.append(uds_row(
    '2.6. STEPS TO UTILIZE THE SUBJECT\'S ULTIMATE DRIVING SYSTEM ("UDS.PROCEDURE") (Now How?)',
    "UDS.Procedure.Outcomes:", "UDS.Procedure: " + SAME, "UDS.Procedure.Actions:", "UDS.Procedure.UD:", "UDS.Procedure.UD.Actions:", "UDS.Procedure.UD.Principles:", "UDS.Procedure.UD.Environment:", "UDS.Procedure.UD.Tools:",
    "UDS.Procedure.FailedActions:", "UDS.Procedure.UB:", "UDS.Procedure.UB.Actions:", "UDS.Procedure.UB.Principles:", "UDS.Procedure.UB.Environment:", "UDS.Procedure.UB.Tools:"))

# 3. EFFECTIVE PRINCIPLES
ep_core = '3. EFFECTIVE PRINCIPLES ("EP") OF ' + SUBJECT_PLACEHOLDER + ' i.e., • Why does the Subject work effectively? Why does it not work effectively? • What are Effective Principles that enable the Subject to best align with its Ultimate Driving System or best overcome its Ultimate Blocking System? • How and why do the Effective Principles work? How and why can they fail to do so?'
ep_desc = 'This is a detailed discussion on the 3 core values of effectiveness (i.e., sustainability, efficiency, and scalability), and their resulting effective principles (i.e., the "Effective Principles", or the "EP") that are relevant to the Subject. These Effective Principles govern the effectiveness of this Subject because they are based on the Ultimate Driving System or the Ultimate Blocking System of the Subject. The key questions in this topics are: Basic Questions:'

data_rows.append(row(E, ep_core, ep_desc, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E))

# 3.0 has long EP / Learner notes - from PDF
ep_30_sub = '3.0. OVERVIEW & SUMMARY OF THE SUBJECT\'S EFFECTIVE EFFECTIVE PRINCIPLE SYSTEM ("EP", "EP.OUTCOMES" & "EP.ACTIONS") (Why Important? What is it? How does it work in general?)'
ep_30_notes = 'EP: 1. Sustainability - Minimize Failure Risks: a. Disable the Root Failure Principles (UBS.UD.Principles + UBS.UD.UD.Principles + UBS.UB.UB.Principles + UDS.UB.Principles + UDS.UB.UD.Principles + UBS.UD.UB.Principles), and b. Disable the Main Failure Principles (UBS.Principles) 2. Sustainability - Produce Desired Outcomes:'
data_rows.append(row(E, E, E, ep_30_sub,
    "EP.Outcomes:", "EP: 1. Sustainability - Minimize Failure Risks: 2. Sustainability - Produce Desired Outcomes: 3. Efficiency - Minimize Failure Risks: 4. Efficiency - Produce Desired Outcomes: 5. Scalability - Minimize Failure Risks: 6. Scalability - Produce Desired Outcomes: ",
    "EP.Actions:", "EP.UD:", "EP.UD.Actions:", "EP.UD.Principles:", "EP.UD.Environment:", "EP.UD.Tools:",
    "EP.FailedActions:", "EP.UB:", "EP.UB.Actions:", "EP.UB.Principles:", "EP.UB.Environment:", "EP.UB.Tools:", E, E, E, ep_30_notes))

def ep_row(sub, outcomes, intro, actions, ud, ud_a, ud_p, ud_e, ud_t, failed, ub, ub_a, ub_p, ub_e, ub_t):
    return row(E, E, E, sub, outcomes, intro, actions, ud, ud_a, ud_p, ud_e, ud_t, failed, ub, ub_a, ub_p, ub_e, ub_t, E, E, E, E)

data_rows.append(ep_row(
    '3.1. ULTIMATE BLOCKERS OF THE SUBJECT\'S EFFECTIVE PRINCIPLE SYSTEM ("EP.UB") (What prevents it from working effectively?)',
    "EP.UB.Outcomes:", "EP.UB: " + SAME, "EP.UB.Actions: " + SAME, "EP.UB.UD:", "EP.UB.UD.Actions:", "EP.UB.UD.Principles:", "EP.UB.UD.Environment:", "EP.UB.UD.Tools:",
    "EP.UB.FailedActions:", "EP.UB.UB:", "EP.UB.UB.Actions:", "EP.UB.UB.Principles:", "EP.UB.UB.Environment:", "EP.UB.UB.Tools:"))
data_rows.append(ep_row(
    '3.2. ULTIMATE DRIVERS OF THE SUBJECT\'S EFFECTIVE PRINCIPLE SYSTEM ("EP.UD") (What makes it work effectively?)',
    "EP.UD.Outcomes:", "EP.UD: " + SAME, "EP.UD.Actions: " + SAME, "EP.UD.UD:", "EP.UD.UD.Actions:", "EP.UD.UD.Principles:", "EP.UD.UD.Environment:", "EP.UD.UD.Tools:",
    "EP.UD.FailedActions:", "EP.UD.UB:", "EP.UD.UB.Actions:", "EP.UD.UB.Principles:", "EP.UD.UB.Environment:", "EP.UD.UB.Tools:"))
data_rows.append(ep_row(
    '3.3. CORE VALUES & PRINCIPLES OF THE SUBJECT\'S EFFECTIVE PRINCIPLE SYSTEM ("EP.PRINCIPLES") (Why does it work effectively?)',
    "EP.Principles.Outcomes:", "EP.Principles:", "EP.Principles.Actions:", "EP.Principles.UD:", "EP.Principles.UD.Actions:", "EP.Principles.UD.Principles:", "EP.Principles.UD.Environment:", "EP.Principles.UD.Tools:",
    "EP.Principles.FailedActions:", "EP.Principles.UB:", "EP.Principles.UB.Actions:", "EP.Principles.UB.Principles:", "EP.Principles.UB.Environment:", "EP.Principles.UB.Tools:"))
data_rows.append(ep_row(
    '3.4. ENVIRONMENT OF THE SUBJECT\'S EFFECTIVE PRINCIPLES ("EP.ENVIRONMENT") (Now What?)',
    "EP.Environment.Outcomes:", "EP.Environment: " + SAME, "EP.Environment.Actions:", "EP.Environment.UD:", "EP.Environment.UD.Actions:", "EP.Environment.UD.Principles:", "EP.Environment.UD.Environment:", "EP.Environment.UD.Tools:",
    "EP.Environment.FailedActions:", "EP.Environment.UB:", "EP.Environment.UB.Actions:", "EP.Environment.UB.Principles:", "EP.Environment.UB.Environment:", "EP.Environment.UB.Tools:"))
data_rows.append(ep_row(
    '3.4. TOOLS OF THE SUBJECT\'S EFFECTIVE PRINCIPLE SYSTEM ("EP.TOOLS") (Now What?)',
    "EP.Tools.Outcomes:", "EP.Tools: " + SAME, "EP.Tools.Actions:", "EP.Tools.UD:", "EP.Tools.UD.Actions:", "EP.Tools.UD.Principles:", "EP.Tools.UD.Environment:", "EP.Tools.UD.Tools:",
    "EP.Tools.FailedActions:", "EP.Tools.UB:", "EP.Tools.UB.Actions:", "EP.Tools.UB.Principles:", "EP.Tools.UB.Environment:", "EP.Tools.UB.Tools:"))
data_rows.append(ep_row(
    '3.5. STEPS TO APPLY THE SUBJECT\'S EFFECTIVE PRINCIPLE SYSTEM ("EP.PROCEDURE") (Now How?)',
    "EP.Procedure.Outcomes:", "EP.Procedure: " + SAME, "EP.Procedure.Actions:", "EP.Procedure.UD:", "EP.Procedure.UD.Actions:", "EP.Procedure.UD.Principles:", "EP.Procedure.UD.Environment:", "EP.Procedure.UD.Tools:",
    "EP.Procedure.FailedActions:", "EP.Procedure.UB:", "EP.Procedure.UB.Actions:", "EP.Procedure.UB.Principles:", "EP.Procedure.UB.Environment:", "EP.Procedure.UB.Tools:"))

# 4. EOE
eoe_core = '4. EFFECTIVE OPERATING ENVIRONMENT ("EOE") OF ' + SUBJECT_PLACEHOLDER + ' i.e., Detailed discussion of an environment that best follows the desired Effective Principle System of the Subject:'
data_rows.append(row(E, eoe_core, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E))

def eoe_row(sub, outcomes, intro, actions, ud, ud_a, ud_p, ud_e, ud_t, failed, ub, ub_a, ub_p, ub_e, ub_t):
    return row(E, E, E, sub, outcomes, intro, actions, ud, ud_a, ud_p, ud_e, ud_t, failed, ub, ub_a, ub_p, ub_e, ub_t, E, E, E, E)

data_rows.append(eoe_row(
    '4.0. OVERVIEW & SUMMARY OF THE SUBJECT\'S EFFECTIVE OPERATING ENVIRONMENT ("EOE", "EOE.OUTCOMES" & "EOE.ACTIONS") (Why Important? What is it? How does it work general?)',
    "EOE.Outcomes:", "EOE: " + SAME, "EOE.Actions: " + SAME, "EOE.UD:", "EOE.UD.Actions:", "EOE.UD.Principles:", "EOE.UD.Environment:", "EOE.UD.Tools:",
    "EOE.FailedActions:", "EOE.UB:", "EOE.UB.Actions:", "EOE.UB.Principles:", "EOE.UB.Environment:", "EOE.UB.Tools:"))
for label, code in [
    ("4.1. ULTIMATE BLOCKERS", "EOE.UB"),
    ("4.2. ULTIMATE DRIVERS", "EOE.UD"),
    ("4.3. CORE VALUES & PRINCIPLES", "EOE.PRINCIPLES"),
    ("4.4. ENVIRONMENT", "EOE.ENVIRONMENT"),
    ("4.4. TOOLS", "EOE.TOOLS"),
    ("4.5. STEPS TO APPLY", "EOE.PROCEDURE"),
]:
    sub = f'{label} OF THE SUBJECT\'S EFFECTIVE OPERATING ENVIRONMENT ("{code}")' + (" (Now What?)" if "TOOLS" in label or "ENVIRONMENT" in label else " (What prevents it from working effectively?)" if "BLOCKERS" in label else " (What makes it work effectively?)" if "DRIVERS" in label else " (Why does it work effectively?)" if "PRINCIPLES" in label else " (Now How?)")
    data_rows.append(eoe_row(sub, f"{code}.Outcomes:" if "OVERVIEW" not in label else "EOE.Outcomes:", f"{code}: " + SAME, f"{code}.Actions: " + SAME,
        f"{code}.UD:", f"{code}.UD.Actions:", f"{code}.UD.Principles:", f"{code}.UD.Environment:", f"{code}.UD.Tools:",
        f"{code}.FailedActions:", f"{code}.UB:", f"{code}.UB.Actions:", f"{code}.UB.Principles:", f"{code}.UB.Environment:", f"{code}.UB.Tools:"))

# Fix 4.1-4.5 sub labels
data_rows[-6] = eoe_row(
    '4.1. ULTIMATE BLOCKERS OF THE SUBJECT\'S EFFECTIVE OPERATING ENVIRONMENT ("EOE.UB") (What prevents it from working effectively?)',
    "EOE.UB.Outcomes:", "EOE.UB: " + SAME, "EOE.UB.Actions: " + SAME, "EOE.UB.UD:", "EOE.UB.UD.Actions:", "EOE.UB.UD.Principles:", "EOE.UB.UD.Environment:", "EOE.UB.UD.Tools:",
    "EOE.UB.FailedActions:", "EOE.UB.UB:", "EOE.UB.UB.Actions:", "EOE.UB.UB.Principles:", "EOE.UB.UB.Environment:", "EOE.UB.UB.Tools:")
data_rows[-5] = eoe_row(
    '4.2. ULTIMATE DRIVERS OF THE SUBJECT\'S EFFECTIVE OPERATING ENVIRONMENT ("EOE.UD") (What makes it work effectively?)',
    "EOE.UD.Outcomes:", "EOE.UD: " + SAME, "EOE.UD.Actions: " + SAME, "EOE.UD.UD:", "EOE.UD.UD.Actions:", "EOE.UD.UD.Principles:", "EOE.UD.UD.Environment:", "EOE.UD.UD.Tools:",
    "EOE.UD.FailedActions:", "EOE.UD.UB:", "EOE.UD.UB.Actions:", "EOE.UD.UB.Principles:", "EOE.UD.UB.Environment:", "EOE.UD.UB.Tools:")
data_rows[-4] = eoe_row(
    '4.3. CORE VALUES & PRINCIPLES OF THE SUBJECT\'S EFFECTIVE OPERATING ENVIRONMENT ("EOE.PRINCIPLES") (Why does it work effectively?)',
    "EOE.Principles.Outcomes:", "EOE.Principles: " + SAME, "EOE.Principles.Actions:", "EOE.Principles.UD:", "EOE.Principles.UD.Actions:", "EOE.Principles.UD.Principles:", "EOE.Principles.UD.Environment:", "EOE.Principles.UD.Tools:",
    "EOE.Principles.FailedActions:", "EOE.Principles.UB:", "EOE.Principles.UB.Actions:", "EOE.Principles.UB.Principles:", "EOE.Principles.UB.Environment:", "EOE.Principles.UB.Tools:")
data_rows[-3] = eoe_row(
    '4.4. ENVIRONMENT OF THE SUBJECT\'S EFFECTIVE OPERATING ENVIRONMENT ("EOE.ENVIRONMENT") (Now What?)',
    "EOE.Environment.Outcomes:", "EOE.Environment: " + SAME, "EOE.Environment.Actions:", "EOE.Environment.UD:", "EOE.Environment.UD.Actions:", "EOE.Environment.UD.Principles:", "EOE.Environment.UD.Environment:", "EOE.Environment.UD.Tools:",
    "EOE.Environment.FailedActions:", "EOE.Environment.UB:", "EOE.Environment.UB.Actions:", "EOE.Environment.UB.Principles:", "EOE.Environment.UB.Environment:", "EOE.Environment.UB.Tools:")
data_rows[-2] = eoe_row(
    '4.4. TOOLS OF THE SUBJECT\'S EFFECTIVE OPERATING ENVIRONMENT ("EOE.TOOLS") (Now What?)',
    "EOE.Tools.Outcomes:", "EOE.Tools: " + SAME, "EOE.Tools.Actions:", "EOE.Tools.UD:", "EOE.Tools.UD.Actions:", "EOE.Tools.UD.Principles:", "EOE.Tools.UD.Environment:", "EOE.Tools.UD.Tools:",
    "EOE.Tools.FailedActions:", "EOE.Tools.UB:", "EOE.Tools.UB.Actions:", "EOE.Tools.UB.Principles:", "EOE.Tools.UB.Environment:", "EOE.Tools.UB.Tools:")
data_rows[-1] = eoe_row(
    '4.5. STEPS TO APPLY THE SUBJECT\'S EFFECTIVE OPERATING ENVIRONMENT ("EOE.PROCEDURE") (Now How?)',
    "EOE.Procedure.Outcomes:", "EOE.Procedure: " + SAME, "EOE.Procedure.Actions:", "EOE.Procedure.UD:", "EOE.Procedure.UD.Actions:", "EOE.Procedure.UD.Principles:", "EOE.Procedure.UD.Environment:", "EOE.Procedure.UD.Tools:",
    "EOE.Procedure.FailedActions:", "EOE.Procedure.UB:", "EOE.Procedure.UB.Actions:", "EOE.Procedure.UB.Principles:", "EOE.Procedure.UB.Environment:", "EOE.Procedure.UB.Tools:")

# 5. EOT
eot_core = '5. EFFECTIVE OPERATING TOOLS (EOT) OF ' + SUBJECT_PLACEHOLDER + ' i.e., Detailed discussion of a system and its components that best follows the desired Effective Principle System of the Subject:'
data_rows.append(row(E, eot_core, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E))

def eot_row(sub, outcomes, intro, actions, ud, ud_a, ud_p, ud_e, ud_t, failed, ub, ub_a, ub_p, ub_e, ub_t):
    return row(E, E, E, sub, outcomes, intro, actions, ud, ud_a, ud_p, ud_e, ud_t, failed, ub, ub_a, ub_p, ub_e, ub_t, E, E, E, E)

# EOT uses 5.0 -> 5.5 in PDF but labels say 4.0-4.5 in PDF; we use 5.0-5.5 for EOT
for t in [
    ('5.0. OVERVIEW & SUMMARY OF THE SUBJECT\'S EFFECTIVE OPERATING TOOLS ("EOT", "EOT.OUTCOMES" & "EOT.ACTIONS") (Why Important? What is it? How does it work general?)', "EOT"),
    ('5.1. ULTIMATE BLOCKERS OF THE SUBJECT\'S EFFECTIVE OPERATING TOOLS ("EOT.UB") (What prevents it from working effectively?)', "EOT.UB"),
    ('5.2. ULTIMATE DRIVERS OF THE SUBJECT\'S EFFECTIVE OPERATING TOOLS ("EOT.UD") (What makes it work effectively?)', "EOT.UD"),
    ('5.3. CORE VALUES & PRINCIPLES OF THE SUBJECT\'S EFFECTIVE OPERATING TOOLS ("EOT.PRINCIPLES") (Why does it work effectively?)', "EOT.Principles"),
    ('5.4. ENVIRONMENT OF THE SUBJECT\'S EFFECTIVE OPERATING TOOLS ("EOT.ENVIRONMENT") (Now What?)', "EOT.Environment"),
    ('5.4. TOOLS OF THE SUBJECT\'S EFFECTIVE OPERATING TOOLS ("EOT.TOOLS") (Now What?)', "EOT.Tools"),
    ('5.5. STEPS TO APPLY THE SUBJECT\'S EFFECTIVE OPERATING TOOLS ("EOT.PROCEDURE") (Now How?)', "EOT.Procedure"),
]:
    sub, code = t
    data_rows.append(eot_row(sub, f"{code}.Outcomes:", f"{code}: " + SAME, f"{code}.Actions: " + SAME,
        f"{code}.UD:", f"{code}.UD.Actions:", f"{code}.UD.Principles:", f"{code}.UD.Environment:", f"{code}.UD.Tools:",
        f"{code}.FailedActions:", f"{code}.UB:", f"{code}.UB.Actions:", f"{code}.UB.Principles:", f"{code}.UB.Environment:", f"{code}.UB.Tools:"))

# 5. EOP
eop_core = '5. EFFECTIVE OPERATING PROCEDURE ("EOP") OF ' + SUBJECT_PLACEHOLDER + ' Detailed discussions of the steps to operate the Subject\'s Effective Operating Environment and Effective Operating Tools introduced in the previous topic:'
data_rows.append(row(E, eop_core, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E))

for t in [
    ('5.0. OVERVIEW & SUMMARY OF THE SUBJECT\'S EFFECTIVE OPERATING PROCEDURE ("EOP", "EOP.OUTCOMES" & "EOP.ACTIONS") (Why Important? What is it? How does it work general?)', "EOP"),
    ('5.1. ULTIMATE BLOCKERS OF THE SUBJECT\'S EFFECTIVE OPERATING PROCEDURE ("EOP.UB") (What prevents it from working effectively?)', "EOP.UB"),
    ('5.2. ULTIMATE DRIVERS OF THE SUBJECT\'S EFFECTIVE OPERATING PROCEDURE ("EOP.UD") (What makes it work effectively?)', "EOP.UD"),
    ('5.3. CORE VALUES & PRINCIPLES OF THE SUBJECT\'S EFFECTIVE OPERATING PROCEDURE ("EOP.PRINCIPLES") (Why does it work effectively?)', "EOP.Principles"),
    ('5.4. ENVIRONMENT OF THE SUBJECT\'S EFFECTIVE OPERATING PROCEDURE ("EOP.ENVIRONMENT") (Now What?)', "EOP.Environment"),
    ('5.4. COMPONENTS OF THE SUBJECT\'S EFFECTIVE OPERATING PROCEDURE (Now What?)', "EOP.Tools"),
    ('5.5. STEPS TO APPLY THE SUBJECT\'S EFFECTIVE OPERATING PROCEDURE (Now How?)', "EOP.Procedure"),
]:
    sub, code = t
    data_rows.append(eot_row(sub, f"{code}.Outcomes:", f"{code}: " + SAME, f"{code}.Actions: " + SAME,
        f"{code}.UD:", f"{code}.UD.Actions:", f"{code}.UD.Principles:", f"{code}.UD.Environment:", f"{code}.UD.Tools:",
        f"{code}.FailedActions:", f"{code}.UB:", f"{code}.UB.Actions:", f"{code}.UB.Principles:", f"{code}.UB.Environment:", f"{code}.UB.Tools:"))

# Ensure every row has exactly 22 columns
for i, r in enumerate(data_rows):
    if len(r) != 22:
        raise SystemExit(f"Row {i} has {len(r)} columns, expected 22")

# Write output
base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out_path = os.path.join(base, "templates", "D-distilled-understanding-full.md")
with open(out_path, "w") as f:
    f.write(INTRO)
    f.write(HEADER_ROW1 + "\n")
    f.write(SEP_ROW + "\n")
    f.write(SUBH1 + "\n")
    f.write(SUBH2 + "\n")
    for r in data_rows:
        f.write(md_row(r) + "\n")
print("Wrote", out_path, "with", len(data_rows), "data rows")
