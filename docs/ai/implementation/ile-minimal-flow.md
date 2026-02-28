---
phase: implementation
title: ILE Minimal Flow (T-101)
description: Minimal ILE flow in the current IDE—phase B/C/D (Capture, Organise, Distill) → entry points → template load → conversation → doc update. A (Roadmap) as checking point. Maps 1:1 to EOP steps 1–8 (contract). Aligned with T-201 persistent memory and I2 contract (Iteration 2).
feature: integrated-learning-environment
task: T-101
---

# Minimal ILE Flow in Current IDE (Cursor)

*One workspace: chat (Cursor Chat) + structural document (Learning Book Markdown repo). User does not switch app. This flow validates desirability of the Wrapper before building the Effective Core. In Iteration 2 it maps 1:1 to the full EOP (steps 1–8) and is used together with the ILE Effective Learning Contract and T-201 persistent memory.*

**Cross-references:** Contract (EPS + full EOP + Strategy) → `docs/ai/implementation/ile-effective-learning-contract.md` | Persistent memory (A + Learning Book; contract Option B/A) → `docs/ai/implementation/ile-persistent-memory.md` | Rule (all EOP steps, gates) → `.cursor/rules/ile-effective-learning.mdc` | Structure → `docs/ai/implementation/learning-book-tree-map.md` | Entry→Template → `docs/ai/implementation/entry-point-to-template-mapping.md` | A Template → `templates/A-subject-roadmap-and-level-specifications.md` | Folder layout → `learning-book/README.md`

---

## A. Subject Roadmap & Level Specifications as the Checking Point

**A is the canonical checkpoint for learning state.** The Agent reads A at session start and writes to A at session end (or on phase/entry switch). This replaces reliance on ephemeral chat history for context. This flow maps 1:1 to EOP steps 1–8; for the full sequence (including Step 2 pre-session checklist and mandatory gates), see `docs/ai/implementation/ile-effective-learning-contract.md`.

| A Section | Role | When Agent Uses It |
|-----------|------|--------------------|
| **Learner Progress Tracker** | Current Level, Target Level, Last Session, Last Entry Point, Next Recommended Entry Point | Session start (orient); session end (update) |
| **Level Completion Checklist** | Per-level: Met, Evidence link, Date | Session start (gaps); session end (if level changed) |
| **Gap Analysis** | Current vs Target gaps by level | Session start (priorities) |
| **Links to Learning Book (per Level)** | Level → Chapters/Topics mapping | Suggest entry points based on current level |
| **Session Log** | Date, Entry Point, Progress | Session start (resume context); session end (append row) |
| **Phase C: Approved Pages** | Ordered list of Phase C pages with status (Approved / Generated pending approval) | Session start (orient for Phase C); Step 7 (update after approval) |
| **Phase C: Decisions Log** | Date, Scope, Decision (terminology, structure, corrections) | Session start (reference); Step 7 (append when decision made) |
| **Phase C: Current state / Next action** | Last approved page path; next action (e.g. generate T1.P5) | Session start (read before Phase C work); Step 7 (update after approval) |
| **Phase C: Causal Seeds** | From page, Col, Content, Seeds into (derivation chain) | Session start (reference when generating); Step 7 (extend when new seeds uncovered) |

**Checkpoint protocol:**
- **Session start:** Agent reads A → Learner Progress Tracker + Session Log + Level Completion Checklist. If A contains "Phase C Organise — state" (Approved Pages, Current state), read that section and the last approved page file before orienting. Uses this to orient: "You were at L2, working on Chapter 1 UBS Topic 0. Next suggested: …"
- **Fallbacks:** If A is missing for the chosen subject → offer roadmap discovery. If A exists but Phase C state sections are empty and the subject has Phase C content → ask "Which page are we on?" and orient from Learning Book file list or Session Log.
- **Before phase/entry switch:** Agent prompts to save; writes current progress to the active doc and (optionally) appends to A's Session Log; if Phase C, update Approved Pages, Decisions log, Current state.
- **Session end:** Agent appends to A's Session Log (Date, Entry Point, Progress); updates Learner Progress Tracker if level changed; if Phase C, update Phase C state sections in A.

---

## Agent Persistent Memory: How Start/Resume Preserves Context

**UDS.UB risk:** Linear, chronological chat interfaces suffer from context collapse; users repeat themselves. The ILE avoids this by making the **structural document (Learning Book) the persistent memory**, not the chat.

### What Counts as Persistent Memory

| Source | Contents | Persistence |
|--------|----------|-------------|
| **A. Subject Roadmap & Level Specifications** | Learner Progress Tracker, Session Log, Level Completion Checklist, Gap Analysis, Links to Learning Book | File-based; survives sessions |
| **Learning Book Markdown** | B/C/D/E content per entry point | File-based; survives sessions |
| **ILE Effective Learning Contract** | Minimal EPS + full EOP + ILE Strategy. Option B: MCP digest key `ile:contract`; Option A: load `ile-effective-learning-contract.md` at session start. | Per `ile-persistent-memory.md` §3 |
| **Project rules / Cursor memory** | Principles, conventions, ILE rules (e.g. `.cursor/rules/ile-effective-learning.mdc`, `ile-session-memory.mdc`) | Optional; cross-session if configured |

### Session Start (Resume)

In ILE context the full sequence is **EOP Step 1 (Open)** → **Step 2 (Pre-session checklist:** principles, environment, tools; Learner confirms or defers) → **Step 3 (Resume**, below). Do not proceed to Step 3 without Step 2 confirm/defer (see contract).

1. Agent reads A for the chosen subject.
2. From **Learner Progress Tracker:** Current Level, Target Level, Last Session, Last Entry Point, Next Recommended Entry Point.
3. From **Session Log:** Last N rows (recent history).
4. **For Phase C Organise:** If A contains a "Phase C Organise — state" section (Approved Pages, Current state, Last approved page), read that section and then read the **last approved page file** (path in A) before orienting. Do not start generating or reviewing the next page until both are read.
5. Agent orients: *"You're at L2. Last session YYYY-MM-DD: Chapter 1 UBS Topic 0—[progress note]. Next suggested: complete Topic 0 or move to Topic 1."*
6. User chooses: resume where left off or pick another entry point.

**Fallbacks:** If A is missing → offer roadmap discovery. If A exists but Phase C state is empty and the subject has Phase C content → ask "Which page are we on?" and rebuild state from Learning Book or Session Log.

### Session Resume Without Chat History

The Agent does **not** rely on prior chat. It re-reads A + the active entry point's file. Context is reconstructed from the document, not from chat scroll. This satisfies **EffAdv-AC2** (resume without re-entering context) and **Noun-AC2** (persistent memory tied to subject/Learning Book).

---

## Mid-Session Context: Handling Long Sessions (1M+ Tokens)

**UDS.UB:** Long sessions (1M+ tokens) cause context collapse in linear chat; hierarchical structure is lost and users repeat context. The ILE addresses this via **hierarchy over chronology** and **scoped context**.

### Principle: Hierarchy Over Chronology

- **Chat is ephemeral.** It scrolls; older turns may be dropped from the context window.
- **The document is the source of truth.** The Learning Book (and A) persists. The Agent can always re-read the doc to recover context.

### Scoped Context Strategy

| Scope | What Agent Loads | Typical Size |
|-------|------------------|--------------|
| **Current entry point** | Template + that section's content (e.g. Chapter 1 UBS Topic 0) | Bounded (one file/section) |
| **A (checkpoint)** | Learner Progress Tracker, Session Log, Links to Learning Book | Small (one file) |
| **Full chat history** | Not required | — |

The Agent scopes to **one entry point at a time**. It loads: (1) the template for that entry, (2) the current content of that section, (3) A (or the relevant A sections). This stays within a manageable context window—not 1M tokens.

### Checkpointing During Long Sessions

| Action | Purpose |
|--------|---------|
| **Periodic write to doc** | As the conversation progresses, Agent writes outcomes to the structural Markdown. The doc becomes the checkpoint. |
| **Session progress note** | For long sessions, Agent periodically appends a row to A's Session Log (or a "session checkpoint" note). Next turn: Agent reads that note instead of full chat history. |
| **Entry-point switch** | Before switch, Agent commits current progress to the doc and (optionally) updates A. New entry point = fresh scoped context. |

### Recovery From Context Collapse

If the context window is exceeded or chat history is lost:
1. Agent re-reads **A** (Learner Progress Tracker, Session Log).
2. Agent re-reads the **current entry point's file** (the section being worked on).
3. Agent reconstructs: "You're working on Chapter 1 UBS Topic 0. Last Session Log note: [X]. Current doc state: [Y]. Continuing from here."

**Result:** The user does not repeat context. The hierarchical structure (doc) survives; the chat is transient.

---

## Flow variants

### Session start: New book vs Resume

In ILE context the full sequence is **EOP Step 1 (Open)** → **Step 2 (Pre-session checklist)** per contract → then route below. Do not proceed to Resume without Step 2 confirm/defer.

- **Explicit choice:** At session start, Agent asks: "Start a new subject?" or "Resume [Subject]?" to route into (a) or (b).
- **Initial check:** Always verify A (Subject Roadmap) exists and is readable for the chosen subject; if not, treat as new book and **run Roadmap Discovery** first (see below).

### (a) Entirely new book

- **A. Subject Roadmap first:** Populate or complete A before any B/C/D/E work. A defines L1–L7 (Requirements, Credentials), Learner Progress Tracker, Level Completion Checklist, Session Log, Links to Learning Book.
- **Roadmap Discovery:** When A is missing, the Agent offers to run **Roadmap Discovery** per `docs/ai/implementation/ile-roadmap-discovery.md`: a structured interview (like PM Problem Discovery / User's Requirements) so the curriculum and level specs fit the individual—context, goal (desired outcome), learning habits, current level and gaps, curriculum fit. The Agent guides the Learner through each block, proposes content for A, and writes only with Learner approval. Command: `/roadmap-discovery` or "run roadmap discovery."
- **A as checking point:** Use A as the reference for level-appropriate entry points; Agent suggests next steps based on Learner Progress Tracker (Current Level, Target Level, Next Recommended Entry Point).
- **Session-end checkpoint:** After each session, Agent appends to A's Session Log (Date, Entry Point, Progress) and updates Learner Progress Tracker if level changed (e.g. L1.2 → L1.3).
- **Entry choice:** When A exists, Agent uses Learner Progress Tracker + Links to Learning Book to suggest entry points; user can still choose any entry point.

### (b) Picking up an already-learning subject

- **Resume logic:** On "Resume [Subject]," Agent reads A: Learner Progress Tracker (Last Session, Last Entry Point, Current Level, Next Recommended Entry Point) + Session Log (last N rows).
- **A as anchor (T-303):** Agent **surfaces in chat**: current mastery level and relevant A content (e.g. level requirements for current level, next-step recommendations). Example: "You were at L2, Last Entry Point: Chapter 1 UBS Topic 0. At L2 for this subject: [brief requirement from A]. Next recommended: complete UBS or move to UDS." See `ile-phase-and-entry-points.md` §4.
- **Optional prompt:** "Resume where you left off ([last entry]) or pick another entry point?"

## Core flow (maps to EOP steps 1–8)

This core flow corresponds to **EOP steps 1–8** (see `ile-effective-learning-contract.md`). **Step 2 (Pre-session)** and **Step 7 (Checkpoint)** are mandatory gates: no proceed to Resume without Step 2 confirm/defer; no switch entry/phase or end session without Step 7 approval. RACI: no A write or entry/phase switch without Learner approval.

| EOP step | This flow |
|----------|-----------|
| 1 Open | User opens Cursor workspace with Learning Book repo; confirm A exists for subject. |
| 2 Pre-session | Agent states 3 principles + environment + tools checklists; Learner confirms or defers. (Must complete before Step 3.) |
| 3 Resume | Below: Start or resume session. |
| 4 Phase | Choose phase (B/C/D). |
| 5 Entry | Select entry point; Agent loads template. |
| 6 Learn | Learning conversation. |
| 7 Checkpoint | Before switch or exit: approve save → Agent updates A (Session Log, Progress Tracker). |
| 8+ Repeat | Next entry/phase or end; next time start at Step 3. |

**Operational steps:**

1. **Start or resume session** — User opens Cursor workspace with Learning Book repo. Chooses subject: COE → Area → Chapter → Topic (or creates new). Session context scoped to that subject. *(EOP 3; Verb-AC1)*

2. **Choose phase** — Agent asks: "Which phase? B. Capture Facts & Data | C. Organise Information | D. Distill Understanding." User chooses one. Agent presents entry points from the Learning Map for that phase per **`docs/ai/implementation/ile-phase-and-entry-points.md`** (6 chapters × 6 topics; informed by Subject Roadmap (A) and current level where available). *(EOP 4; Verb-AC2; T-301)*

3. **Select entry point** — User selects an entry point (e.g. Chapter 1 UBS, Topic 0. Overview). Agent loads the correct template per `entry-point-to-template-mapping.md` and scopes conversation and document context to that entry. *(EOP 5; Verb-AC3)*

4. **Learning conversation** — User and Agent conduct hierarchical Q&A (active recall, deep questioning) within the template. Later: structural Markdown is updated in real time as a byproduct. *(EOP 6; Concept: flow only; real-time update in Iteration 2.)*

5. **Progress / next** — User can switch entry point or phase at any time; progress is retained or committed before switch. **EOP Step 7 (Checkpoint) required before switch or exit:** Prompt to save or confirm; Learner approves; Agent appends to A's Session Log and updates Learner Progress Tracker if level changed. *(EOP 7, 8+)*

## Learning as a tree (entry points and levels)

- **No rigid level→entry mapping:** The COE Effective Learning Template is set up like a tree: the more you know about a subject, the more branches and leaves (entry points, sub-topics) the book can have. One can branch out a book on a subject indefinitely. It is not required—and can be difficult—to map "Overview = L1–L2, UBS = L2–L3" etc.; the structure is open-ended.
- **A as checking point:** A (Subject Roadmap) defines what L1–L7 mean (Requirements, Credentials) and holds Learner Progress Tracker, Level Completion Checklist, Session Log, Links to Learning Book. The Agent uses A to *suggest* where to focus next (e.g. "at L2, consider deepening UBS or starting UDS"); entry points are nodes in a growing tree, not fixed level buckets.
- **Level granularity:** A's Learner Progress Tracker and Session Log can use sub-levels (e.g. L1.1, L1.2) for incremental progress within a level.

## Mapping personal Learning Book ↔ company COE on ClickUp (scale)

- **Design consideration (Iteration 4):** Mapping the hierarchical structure of a personal Learning Book to the company's COE space on ClickUp—and vice versa—at scale (hundreds or thousands of pages) is **feasible but non-trivial**.
- **What makes it easier:** (1) A **defined schema** on both sides: Learning Book = COE → Area → Chapter → Topic → phases/sections; ClickUp = COE → Chapter → Topic → Topic Members' Learning Area → each member's Personal Learning Area. The **company-side hierarchy is the single source of truth in `config/coe-map.yaml`** (T-411; see `ile-coe-map.md`). (2) **Stable identifiers**: consistent paths, naming, or IDs so that "this section in the Book" maps to "this location in ClickUp" by rule, not by free text. (3) **Config-driven mapping**: COE map (Design §2.3) holds the hierarchy and user→location rules; sync is incremental (e.g. by subject, by last-updated) to avoid scanning entire books every time.
- **What makes it harder:** Many pages, ad hoc naming, or structural drift (e.g. new sections in the Book with no corresponding ClickUp place). Mitigation: enforce the same structure (templates, hierarchy) in the Book so the mapping rule stays deterministic; sync only changed or new nodes.

## Environment

| Component | Current IDE (Cursor) |
|-----------|----------------------|
| Chat | Cursor Chat (or AntiGravity) |
| Structural document | Learning Book Markdown in same workspace (open folder or file tree) |
| User action | Conversational: state phase, pick entry point, conduct Q&A |
| No | Separate app for docs; manual copy-paste from chat to doc |

## T-302: Zero-friction capture and retain-on-switch

**Task T-302** ensures: (1) updates to Markdown occur only as a **byproduct of the conversation** per `ile-conversation-to-doc-mapping.md`—no separate copy-paste (EffAdv-AC3, EffAdj-AC1, EffAdj-AC2); (2) on **entry/phase switch**, EOP Step 7 (Checkpoint) is required and progress is **committed to the doc (and A)** before switch so the user does not lose in-progress context (EffAdj-AC3).

**Evidence:** `.cursor/rules/ile-learning-book.mdc` § Before entry/phase switch (T-302); `ile-effective-learning-contract.md` § Step 7 and mandatory gates; this flow § Core flow (Step 7, Entry-point switch).

## T-304: Engagement light (completion moment + progress summary)

**Task T-304** ensures: (1) after each **chunk** (one component or one entry point completed—e.g. Learner approves a write for one component/section), the Agent delivers a **completion moment** (explicit confirmation; optional lightweight reward); (2) when appropriate (e.g. after a completion moment, or when the Learner asks), the Agent surfaces a **progress summary in chat** (e.g. "X of Y completed for this phase"). Agent behavior only; no new UI; no mandatory steps (EffAdj-AC5).

**Chunk:** One component (one page/section within a topic) or one entry point (one topic) for which the Learner has approved an update and the Agent has written to the doc.

**Completion moment:** One short sentence in chat after the write is confirmed (e.g. "✓ [Component/entry] updated. Chunk complete." or "Done. Another component here, or switch entry point?"). Optional: lightweight positive reinforcement (e.g. "Nice progress.").

**Progress summary:** When appropriate (after a completion moment, or when the Learner asks "how am I doing?"), state in chat how much is completed for the current phase (e.g. "This phase: you've completed [N] entry points (or components)." or "X of Y completed for this phase."). Data source: A's Session Log + current phase entry-point list; infer from Session Log how many distinct entry points (or components) have been worked on/completed this phase. If A or Session Log is missing, infer from conversation (e.g. "You've completed [current entry] and [N] others this session.").

**Evidence:** `.cursor/rules/ile-learning-book.mdc` § Completion moment and progress summary (T-304). Verb-AC9, Verb-AC10, EffAdv-AC4, EffAdj-AC4, EffAdj-AC5, Noun-AC11.

## What this validates

- **Desirability / Hook:** User wants to learn-and-capture in one environment with no chat→docs handoff.
- **UDO Resolution:** The flow (phase → entry points → template load → conversation → doc update) is the desired wrapper; the root blocker (manual paste) is addressed by design (doc update as byproduct in later iterations).
- **UDS.UB Resolution:** Linear, chronological chat that suffers from context collapse is addressed by (1) A as the checking point (persistent, file-based); (2) hierarchy over chronology (doc is source of truth, chat is ephemeral); (3) scoped context (one entry point at a time); (4) checkpointing to A's Session Log and the Learning Book during long sessions.
- **Iteration 2 alignment:** Flow maps 1:1 to full EOP (steps 1–8) per contract; T-201 persistent memory (A + Learning Book; contract Option B/A) and `.cursor/rules/ile-effective-learning.mdc` enforce gates and RACI.

## User confirmation

*Does this flow represent the desired ILE wrapper? Reply "Approved" to mark T-101 🟢 Reviewed/Tested and proceed to T-102.*
