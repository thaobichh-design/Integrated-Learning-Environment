---
phase: implementation
title: T-202 Validation Test — Conversation → Doc in Action
description: User test-learns a small content part to validate T-202 (Agent read/write of Learning Book from conversation; mapping rule). Success metrics (kill criteria) defined before test.
feature: integrated-learning-environment
task: T-202
---

# T-202 Validation Test — Conversation → Doc in Action

*Before marking T-202 🟢 Reviewed/Tested, the User (Learner) runs this test: learn a small content part and observe T-202 (conversation→doc mapping, read/write on approval) in action. **Success metrics (kill criteria)** are defined below; if any criterion fails, the test fails and T-202 is not approved.*

**Cross-references:** Mapping rule → `docs/ai/implementation/ile-conversation-to-doc-mapping.md` | Individual's tree → `docs/ai/implementation/learning-book-tree-map.md` § Individual's full effective learning tree | Rule → `.cursor/rules/ile-learning-book.mdc` | Entry→Template → `docs/ai/implementation/entry-point-to-template-mapping.md`

---

## 1. Objective

- **What:** Confirm that the Agent can (1) resolve the target file path and section from conversation scope (subject, phase, entry point), (2) read from that file/section when loading context, (3) write to that file/section when the User approves an update from the conversation—with **no manual paste**.
- **Entry point:** A **particular page within a topic** — i.e. (chapter, topic, page). Example: Chapter 1 UBS, Topic 0 (Overview & Summary), Page 0.

---

## 2. Preconditions

- [ ] ILE repo open in Cursor; `learning-book/COE_DS/` exists.
- [ ] A. Subject Roadmap exists for COE_DS (or User accepts stub).
- [ ] At least one template exists for the chosen entry point (e.g. `templates/0-overview-and-summary.md` for Chapter 0 Topic 0, or Chapter 1 UBS Topic 0 if that template exists).
- [ ] Rules `ile-learning-book.mdc` and `ile-effective-learning.mdc` apply when working in learning-book or docs/ai/implementation context.

---

## 3. Test Steps (User-led)

1. **Choose subject and entry point** — Tell the Agent: subject = COE_DS, phase = C (Organise Information), entry point = **Chapter 1 UBS, Topic 0 (Overview & Summary), Page 0** (or Chapter 0 Topic 0 if that’s the only template available).
2. **Agent resolves target** — Agent states the **target file path** and **section** per `ile-conversation-to-doc-mapping.md` (e.g. `learning-book/COE_DS/C. Organise Information/1. UBS/1. UBS - 0. Overview & Summary.md`, section = Page 0 / Overview & Summary). If the chapter folder (e.g. `1. UBS`) or file does not exist, Agent may create the folder/file from template or state the path where the write will go.
3. **Short learning exchange** — Ask one or two questions (e.g. “What is the Ultimate Blocking System in one sentence?” or “What is this topic for?”). Agent **acts as teacher**: elicits (e.g. asks or clarifies before giving the answer), checks understanding (e.g. confirms in learner's terms), and applies UDS/UBS (support drivers, mitigate blockers). Agent answers using the template structure and **target table format**.
4. **Propose an update** — Agent proposes a short update to the Learning Book (e.g. one sentence or one table cell) and states the **exact file path and section** where it will be written.
5. **User approves** — User replies “Approve” or “Confirm.”
6. **Agent writes** — Agent writes to the target file/section per the mapping. No manual copy-paste by the User.
7. **Verify on disk** — User opens the target file in the repo and confirms the content appears at the stated path/section.

---

## 4. Success Metrics (Kill Criteria)

*If any of the following is **false**, the test **fails** and T-202 is **not** approved.*

| # | Criterion | Pass condition |
|---|-----------|-----------------|
| **K1** | **Mapping rule** | Agent resolves and states the target **file path** and **section** from (subject, phase, entry point) using the rule in `ile-conversation-to-doc-mapping.md`. Path uses correct folder names (e.g. `1. UBS` not “1. Ultimate Blocking System”) per `learning-book/README.md`. |
| **K2** | **Read** | Agent loads context from the target file/section (or treats as empty if file does not exist) and uses it in the learning exchange. |
| **K3** | **Write on approval only** | Agent does **not** write before the User explicitly approves (e.g. “Approve” or “Confirm”). RACI respected. |
| **K4** | **Write to correct location** | After approval, the update appears in the **stated** file path and section. User can open the file and see the content at the expected place. |
| **K5** | **No manual paste** | The User did **not** copy content from chat and paste into the Learning Book; the Agent wrote to the file as a byproduct of the conversation. |
| **K6** | **Exact file/section stated** | Agent can point to the **exact** file(s) and section(s) created or updated for the exchange (SustainAdv-AC3). |
| **K7** | **Agent as teacher** | Agent **teaches**, not only answers: elicits (e.g. asks or clarifies before giving the answer), checks understanding (e.g. confirms in learner's terms), and applies UDS/UBS principles (support drivers, mitigate blockers). |
| **K8** | **Target table format** | Content is written in the **target table format**: a table with canonical question columns and a **SUBJECT CONTENT** row; content goes in the cells corresponding to the questions for that page. No free-form headings/bullets in place of the table. |

---

## 5. Result

- **Pass:** All of K1–K8 are true. User marks test ✅ and may approve T-202 🟢 Reviewed/Tested.
- **Fail:** Any of K1–K8 is false. User notes which criterion failed; T-202 remains 🔵 Draft Completed until the failure is fixed and the test is re-run.

---

## 6. User Sign-off (after test)

- [x] I ran the test steps above.
- [x] **Pass / Fail:** Pass
- [x] If Pass: I approve T-202 🟢 Reviewed/Tested. (Agent or User updates planning doc.)

*T-202 approved. Planning doc updated.*
