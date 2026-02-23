# Integrated Learning Environment (ILE)

*Learn with an AI Agent. Capture, organise, and distill knowledge—with zero copy-paste. Your Learning Book grows as a byproduct of the conversation.*

Built for the **LTC Advanced Effective Learning Framework**. *Engine and brain from [my-ai-devkit-templates](https://github.com/chrislongnguyen/my-ai-devkit-templates) (template 1.1.0).*

---

## The LTC Advanced Effective Learning Framework

**You don't consume knowledge—you *build* it.** The LTC Advanced Effective Learning Framework turns learning into a structured, traceable process. You write your own Learning Book per subject. The AI Agent is your sparring partner: it guides you, questions you, and helps you organise knowledge from high-level concepts down to deep-root layers.

### What makes it different


| Traditional learning                   | LTC Advanced Effective Learning                                                                                                                                          |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Passive consumption (videos, articles) | **Active recall** — you explain, the Agent probes                                                                                                                        |
| Flat notes, scattered across apps      | **Hierarchical structure** — 0. Overview → 1. Ultimate Blockers → 2. Ultimate Drivers → 4. Principles → 5. Components -> 6. Steps to Apply -> 7. Distilled Understanding |
| Manual copy-paste from chat to docs    | **Documentation as byproduct** — the Learning Book updates as you talk                                                                                                   |
| Linear chat that forgets context       | **Persistent memory** — the document *is* the memory; you never repeat yourself                                                                                          |
| Ad hoc progression                     | **Level-aligned** — Subject Roadmap (A) guides L1→L7 mastery (SFIA)                                                                                                      |


**You are the author.** The learner is the best teacher for themselves. The Agent and others are references. You write your own book, continuously from L1 (Follow) to L7 (Strategic Visionary).

---

## The Process: Capture → Organise → Distill

Three phases. One flow. No handoff.

```
A. Subject Roadmap (L1–L7, where you are) 
        ↓
B. Capture Facts & Data — Raw facts, information
        ↓
C. Organise Information — Structured knowledge (Overview, UBS, UDS, EPS, UES, EOP)
        ↓
D. Distill Understanding — Condensed understanding
        ↓
E. Express Expertise — Your proof of mastery
```

- **Capture:** Gather raw facts and information. The Agent helps you capture without losing structure.
- **Organise:** Turn facts into knowledge. The Agent guides hierarchical Q&A—Overview, Blockers (UBS), Drivers (UDS), Principles (EPS), Effective System (UES), Operating Procedure (EOP). *You* articulate; the Agent writes into the right section.
- **Distill:** Compress Organise Information into the Distill Understanding format. The Agent helps condense on demand.

**Consumption is in-scope.** Digestion (reflection, practice, internalisation) is explicitly *outside* the system—you do that in your head and in the real world.

---

## How the ILE Helps You Learn Most Effectively

*UDS = Ultimate Driving System (your drive to master). UBS = Ultimate Blocking System (admin tax, copy-paste). UD = Driver. UB = Blocker.*

### 1. One workspace. No copy-paste.

Chat and Learning Book live in the same place (Cursor + Markdown repo). You choose phase and entry point. The Agent loads the right template and scopes the conversation. What you discuss is written *directly* into the Learning Book—no extract, format, or paste.

→ **Addresses UBS** (no manual copy-paste). **Removes UBS.UD** (no separation of chat and docs). **ILE = UBS.UB** (integrated workspace).

### 2. Hierarchy over chronology

Linear chat collapses context. Scrolling back is lost. The ILE flips this: **the document is the source of truth.** Chat is ephemeral; the Learning Book persists. The Agent reads the doc to orient and recover context. Structure survives; you don't repeat yourself.

→ **Removes UDS.UB** (linear chat no longer breaks hierarchy; doc preserves structure).

### 3. Subject Roadmap (A) as your anchor

**A** defines L1–L7 for each subject (requirements, credentials, progression). It holds your **Learner Progress Tracker** (current level, target, last entry point), **Session Log** (where you worked, when), and **Level Completion Checklist**. The Agent reads A at session start and writes to A at session end. You always know where you are and what's next.

→ **Supports UDS** (mastery drive). **Removes UDS.UB** (checkpoint survives; no context loss).

### 4. Resume without re-entering context

Close the session. Come back next week. The Agent reads A + the current entry point's file. *"You're at L2. Last session: Chapter 1 UBS Topic 0—you worked on Blockers. Next suggested: finish Topic 0 or move to Topic 1."* No pasting. No re-explaining.

→ **Removes UDS.UB** (user no longer forced to repeat context).

### 5. Long sessions without context collapse

Even 1M+ token sessions stay manageable. The Agent loads **only** the current entry point + A. It checkpoints progress into the document and Session Log. If chat history is lost, the Agent re-reads the doc and continues. The hierarchical structure survives; you never repeat context.

→ **Removes UDS.UB** (context collapse addressed; doc + checkpoint recover).

### 6. Scoped, level-appropriate learning

Entry points are informed by your current level and A. The Agent suggests level-aligned Chapters/Topics so you avoid scattered learning (e.g. jumping to L4 content while still at L1/L2). You can still choose any entry point—the "right" path is visible.

→ **Enables UDS.UD** (hierarchical questioning, level-aligned structure). **Supports UDS** (mastery drive).

---

## Quick Start

1. **Clone** this repo and open in Cursor.
2. **Choose a subject** (e.g. Data Science) under `learning-book/COE_DS/`.
3. **Start or resume** — Tell the Agent: "Start a new subject" or "Resume Data Science."
4. **Choose phase** — B. Capture Facts & Data | C. Organise Information | D. Distill Understanding.
5. **Pick an entry point** — e.g. Chapter 1 UBS, Topic 0. Overview.
6. **Learn and capture** — Conduct hierarchical Q&A. The Agent updates the Learning Book as you go.

The Agent uses the Subject Roadmap (A) to orient, suggest next steps, and keep your progression on track. See `docs/ai/implementation/ile-minimal-flow.md` for the full flow.

---

## Project Structure

```
learning-book/
├── COE_DS/                          # Example: Data Science Area
│   ├── A. Subject Roadmap & Level Specifications/
│   ├── B. Capture Facts & Data/
│   ├── C. Organise Information/
│   │   ├── 0. Overview & Summary/
│   │   ├── 1. UBS/   (Ultimate Blocking System)
│   │   ├── 2. UDS/   (Ultimate Driving System)
│   │   ├── 3. EPS/   (Effective Principle System)
│   │   ├── 4. UES/   (Ultimate Effective System)
│   │   └── 5. EOP/   (Effective Operating Procedure)
│   ├── D. Distill Understanding/
│   └── E. Express Expertise/
templates/                           # Universal templates (A, B/C, D, E)
docs/ai/                             # Requirements, Design, Planning, Implementation
```

Full tree map: `docs/ai/implementation/learning-book-tree-map.md`

---

## Deeper Docs


| Doc                                                               | Purpose                                                               |
| ----------------------------------------------------------------- | --------------------------------------------------------------------- |
| `docs/ai/requirements/feature-integrated-learning-environment.md` | Requirements, UDO/UDS/UBS, acceptance criteria                        |
| `docs/ai/implementation/ile-minimal-flow.md`                      | Minimal flow, A as checkpoint, persistent memory, mid-session context |
| `docs/ai/implementation/learning-book-tree-map.md`                | Full Learning Book structure (6 Chapters × 6 Topics)                  |
| `learning-book/README.md`                                         | Folder layout, structure verification                                 |


---

*This repository is the ILE project. To start learning, clone or duplicate this folder, open in Cursor, and begin a session. Do not overwrite the underlying `.cursor/skills/` or template logic without approval.*