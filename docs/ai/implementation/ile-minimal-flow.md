---
phase: implementation
title: ILE Minimal Flow (T-101)
description: Minimal ILE flow in the current IDE—phase A/B/C → entry points → template load → conversation → doc update. A (Roadmap) as checking point. Deterministic evidence for Verb-AC1, Verb-AC2, Verb-AC3 (Iteration 1 Concept).
feature: integrated-learning-environment
task: T-101
---

# Minimal ILE Flow in Current IDE (Cursor)

*One workspace: chat (Cursor Chat) + structural document (Learning Book Markdown repo). User does not switch app. This flow validates desirability of the Wrapper before building the Effective Core.*

**Cross-references:** Structure → `docs/ai/implementation/learning-book-tree-map.md` | Entry→Template → `docs/ai/implementation/entry-point-to-template-mapping.md` | A Template → `templates/A-subject-roadmap-and-level-specifications.md` | Folder layout → `learning-book/README.md`

---

## A. Subject Roadmap & Level Specifications as the Checking Point

**A is the canonical checkpoint for learning state.** The Agent reads A at session start and writes to A at session end (or on phase/entry switch). This replaces reliance on ephemeral chat history for context.

| A Section | Role | When Agent Uses It |
|-----------|------|--------------------|
| **Learner Progress Tracker** | Current Level, Target Level, Last Session, Last Entry Point, Next Recommended Entry Point | Session start (orient); session end (update) |
| **Level Completion Checklist** | Per-level: Met, Evidence link, Date | Session start (gaps); session end (if level changed) |
| **Gap Analysis** | Current vs Target gaps by level | Session start (priorities) |
| **Links to Learning Book (per Level)** | Level → Chapters/Topics mapping | Suggest entry points based on current level |
| **Session Log** | Date, Entry Point, Progress | Session start (resume context); session end (append row) |

**Checkpoint protocol:**
- **Session start:** Agent reads A → Learner Progress Tracker + Session Log + Level Completion Checklist. Uses this to orient: "You were at L2, working on Chapter 1 UBS Topic 0. Next suggested: …"
- **Before phase/entry switch:** Agent prompts to save; writes current progress to the active doc and (optionally) appends to A's Session Log.
- **Session end:** Agent appends to A's Session Log (Date, Entry Point, Progress); updates Learner Progress Tracker if level changed.

---

## Agent Persistent Memory: How Start/Resume Preserves Context

**UDS.UB risk:** Linear, chronological chat interfaces suffer from context collapse; users repeat themselves. The ILE avoids this by making the **structural document (Learning Book) the persistent memory**, not the chat.

### What Counts as Persistent Memory

| Source | Contents | Persistence |
|--------|----------|-------------|
| **A. Subject Roadmap & Level Specifications** | Learner Progress Tracker, Session Log, Level Completion Checklist, Gap Analysis, Links to Learning Book | File-based; survives sessions |
| **Learning Book Markdown** | B/C/D/E content per entry point | File-based; survives sessions |
| **Project rules / Cursor memory** | Principles, conventions (e.g. `.cursor/rules`, `/remember`) | Optional; cross-session if configured |

### Session Start (Resume)

1. Agent reads A for the chosen subject.
2. From **Learner Progress Tracker:** Current Level, Target Level, Last Session, Last Entry Point, Next Recommended Entry Point.
3. From **Session Log:** Last N rows (recent history).
4. Agent orients: *"You're at L2. Last session YYYY-MM-DD: Chapter 1 UBS Topic 0—[progress note]. Next suggested: complete Topic 0 or move to Topic 1."*
5. User chooses: resume where left off or pick another entry point.

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

- **Explicit choice:** At session start, Agent asks: "Start a new subject?" or "Resume [Subject]?" to route into (a) or (b).
- **Initial check:** Always verify A (Subject Roadmap) exists and is readable for the chosen subject; if not, treat as new book and populate A first (see `templates/A-subject-roadmap-and-level-specifications.md`).

### (a) Entirely new book

- **A. Subject Roadmap first:** Populate or complete A before any B/C/D/E work. A defines L1–L7 (Requirements, Credentials), Learner Progress Tracker, Level Completion Checklist, Session Log, Links to Learning Book.
- **A as checking point:** Use A as the reference for level-appropriate entry points; Agent suggests next steps based on Learner Progress Tracker (Current Level, Target Level, Next Recommended Entry Point).
- **Session-end checkpoint:** After each session, Agent appends to A's Session Log (Date, Entry Point, Progress) and updates Learner Progress Tracker if level changed (e.g. L1.2 → L1.3).
- **Entry choice:** When A exists, Agent uses Learner Progress Tracker + Links to Learning Book to suggest entry points; user can still choose any entry point.

### (b) Picking up an already-learning subject

- **Resume logic:** On "Resume [Subject]," Agent reads A: Learner Progress Tracker (Last Session, Last Entry Point, Current Level, Next Recommended Entry Point) + Session Log (last N rows).
- **A as anchor:** Agent orients: e.g. "You were at L2, Last Entry Point: Chapter 1 UBS Topic 0. Next suggested: complete UBS or move to UDS."
- **Optional prompt:** "Resume where you left off ([last entry]) or pick another entry point?"

## Core flow (5 steps)

1. **Start or resume session** — User opens Cursor workspace with Learning Book repo. Chooses subject: COE → Area → Chapter → Topic (or creates new). Session context scoped to that subject. *(Verb-AC1)*

2. **Choose phase** — Agent asks: "Which phase? B. Capture | C. Organise | D Distill." User chooses one. Agent presents entry points from the Learning Map (6 Chapters × 6 Topics; see `learning-book-tree-map.md`) for that phase, informed by Subject Roadmap (A) and current level where available. *(Verb-AC2)*

3. **Select entry point** — User selects an entry point (e.g. Chapter 1 UBS, Topic 0. Overview). Agent loads the correct template per `entry-point-to-template-mapping.md` and scopes conversation and document context to that entry. *(Verb-AC3)*

4. **Learning conversation** — User and Agent conduct hierarchical Q&A (active recall, deep questioning) within the template. Later: structural Markdown is updated in real time as a byproduct. *(Concept: flow only; real-time update in Iteration 2.)*

5. **Progress / next** — User can switch entry point or phase at any time; progress is retained or committed before switch. Optional: distill (Phase C) when user chooses. **Validation before switch:** Prompt to save or confirm in-progress draft before changing phase or entry. **Checkpoint:** Agent appends to A's Session Log and updates Learner Progress Tracker if level changed.

## Learning as a tree (entry points and levels)

- **No rigid level→entry mapping:** The COE Effective Learning Template is set up like a tree: the more you know about a subject, the more branches and leaves (entry points, sub-topics) the book can have. One can branch out a book on a subject indefinitely. It is not required—and can be difficult—to map "Overview = L1–L2, UBS = L2–L3" etc.; the structure is open-ended.
- **A as checking point:** A (Subject Roadmap) defines what L1–L7 mean (Requirements, Credentials) and holds Learner Progress Tracker, Level Completion Checklist, Session Log, Links to Learning Book. The Agent uses A to *suggest* where to focus next (e.g. "at L2, consider deepening UBS or starting UDS"); entry points are nodes in a growing tree, not fixed level buckets.
- **Level granularity:** A's Learner Progress Tracker and Session Log can use sub-levels (e.g. L1.1, L1.2) for incremental progress within a level.

## Mapping personal Learning Book ↔ company COE on ClickUp (scale)

- **Design consideration (Iteration 4):** Mapping the hierarchical structure of a personal Learning Book to the company's COE space on ClickUp—and vice versa—at scale (hundreds or thousands of pages) is **feasible but non-trivial**.
- **What makes it easier:** (1) A **defined schema** on both sides: Learning Book = COE → Area → Chapter → Topic → phases/sections; ClickUp = COE → Chapter → Topic → Topic Members' Learning Area → each member's Personal Learning Area. (2) **Stable identifiers**: consistent paths, naming, or IDs so that "this section in the Book" maps to "this location in ClickUp" by rule, not by free text. (3) **Config-driven mapping**: COE map (Design §2.3) holds the hierarchy and user→location rules; sync is incremental (e.g. by subject, by last-updated) to avoid scanning entire books every time.
- **What makes it harder:** Many pages, ad hoc naming, or structural drift (e.g. new sections in the Book with no corresponding ClickUp place). Mitigation: enforce the same structure (templates, hierarchy) in the Book so the mapping rule stays deterministic; sync only changed or new nodes.

## Environment

| Component | Current IDE (Cursor) |
|-----------|----------------------|
| Chat | Cursor Chat (or AntiGravity) |
| Structural document | Learning Book Markdown in same workspace (open folder or file tree) |
| User action | Conversational: state phase, pick entry point, conduct Q&A |
| No | Separate app for docs; manual copy-paste from chat to doc |

## What this validates

- **Desirability / Hook:** User wants to learn-and-capture in one environment with no chat→docs handoff.
- **UDO Resolution:** The flow (phase → entry points → template load → conversation → doc update) is the desired wrapper; the root blocker (manual paste) is addressed by design (doc update as byproduct in later iterations).
- **UDS.UB Resolution:** Linear, chronological chat that suffers from context collapse is addressed by (1) A as the checking point (persistent, file-based); (2) hierarchy over chronology (doc is source of truth, chat is ephemeral); (3) scoped context (one entry point at a time); (4) checkpointing to A's Session Log and the Learning Book during long sessions.

## User confirmation

*Does this flow represent the desired ILE wrapper? Reply "Approved" to mark T-101 🟢 Reviewed/Tested and proceed to T-102.*
