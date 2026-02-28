---
phase: implementation
title: ILE Persistent Memory (T-201)
description: Contract and wiring for Agent store/recall of context tied to subject/Learning Book. Noun-AC2.
feature: integrated-learning-environment
task: T-201
---

# ILE Persistent Memory — Contract & Wiring

*Persistent memory is available to the Agent and tied to the current subject/Learning Book so context is preserved across sessions (Noun-AC2).*

## 1. Canonical source: file-based (A + Learning Book)

The **primary** persistent memory is file-based and already wired:

- **A. Subject Roadmap & Level Specifications** — Learner Progress Tracker, Session Log, Level Completion Checklist, Gap Analysis.
- **Learning Book Markdown** — B/C/D/E content per entry point.

The Agent reads A at session start and writes to A at session end (see `ile-minimal-flow.md`). No MCP is required for context preservation; A + Learning Book suffice.

## 2. Optional: MCP for fast resume

When **MCP** (e.g. `@ai-devkit/memory`) is available, the Agent may use it to store/recall a **lightweight session pointer** so resume does not require re-reading the whole Book. MCP is configured in `.cursor/mcp.json` as `ai-devkit-memory`.

### 2.0 MCP tool reference (single source of truth)

Use these **exact** identifiers when calling MCP from the Agent. If the store tool returns `UNKNOWN_TOOL`, the name the server registers may differ; check Cursor's MCP/Tools list for the ai-devkit-memory server and update this section with the exact tool name shown there.

| Purpose | MCP server identifier | MCP tool name |
|---------|------------------------|---------------|
| Store knowledge | `project-0-Integrated-Learning-Environment-ai-devkit-memory` | `memory_storeKnowledge` |
| Search knowledge | `project-0-Integrated-Learning-Environment-ai-devkit-memory` | `memory_searchKnowledge` |
| Update knowledge | `project-0-Integrated-Learning-Environment-ai-devkit-memory` | `memory_updateKnowledge` |

**Agent usage:** Call `call_mcp_tool` with `server` = server identifier and `toolName` = tool name. Arguments for store: `title` (required), `content` (required), optional `tags`, optional `scope`. If the call returns `UNKNOWN_TOOL`, use the file-based fallback (see `/remember` command and §2.2).

All ILE session context MUST be keyed by subject or Learning Book path so context is tied to the current subject/Learning Book.

| Key pattern | Contents | When to store | When to recall |
|-------------|----------|---------------|-----------------|
| `ile:session:{subject}` | `{ "subject": "<Area or subject id>", "last_entry_point": "<e.g. Chapter 1 UBS Topic 0>", "last_session_date": "YYYY-MM-DD", "learning_book_path": "<relative path to learning-book/COE_XX>" }` | Session end; before phase/entry switch | Session start (resume) |

- **subject** — Current subject or Area (e.g. `COE_DS`, `Data Science`).
- **last_entry_point** — Last entry point the user worked on (e.g. Chapter 1 UBS, Topic 0).
- **last_session_date** — Date of last session (YYYY-MM-DD).
- **learning_book_path** — Path to the Learning Book root for this subject (e.g. `learning-book/COE_DS`).

### 2.2 MCP API usage

- **Store:** Call MCP with server `project-0-Integrated-Learning-Environment-ai-devkit-memory` and tool `memory_storeKnowledge` (see §2.0); pass title and content that includes the JSON above; tag with `ile`, `session`, and the subject so recall can filter by key/tag.
- **Recall:** Query memory by tag/key (e.g. `ile`, `session`, subject) to retrieve the most recent session context for this subject.

If the MCP server does not support keyed recall, the Agent MUST use **A** (read Learner Progress Tracker and Session Log) as the source of truth for resume. MCP is an optimization, not a requirement.

## 3. Principles and EOP (contract) — Option B primary, Option A fallback

The Agent must have the **ILE Effective Learning Contract** (minimal EPS + full EOP + ILE Strategy) in scope at ILE session start so it follows all EOP steps (1–8), gates, and RACI. Two options:

| Option | When | What | Key / Path |
|--------|------|------|------------|
| **Option B (Preferred)** | MCP available | Store a **digest** of the contract (minimal EPS + full EOP in compact form + ILE Strategy checklist). Recall at session start so the Agent has Principles and full EOP in scope with minimal tokens. | MCP key/tag: `ile:contract` or `ile:effective-learning-contract` |
| **Option A (Fallback)** | MCP unavailable or recall fails | Load the full contract doc at session start so the Agent has EPS + EOP + Strategy in context. | `docs/ai/implementation/ile-effective-learning-contract.md` |

**Digest contents (Option B):** Minimal EPS (3 principles); full EOP (RACI + all 8 steps with Required Input, Desired Output, Agent/Learner DOS-DON'TS, mandatory gates); ILE Strategy checklist. Store after any contract update; recall at ILE session start.

**Recommendation:** Use Option B when MCP is configured for reliability and token savings; fall back to Option A otherwise. The rule `.cursor/rules/ile-effective-learning.mdc` instructs the Agent to recall (Option B) or load (Option A) at session start and to follow all EOP steps 1–8.

## 4. Wiring summary

| Layer | What | Where |
|-------|------|--------|
| **Primary** | Session context (current level, last entry point, session log) | A (Subject Roadmap) — read/write at session start/end |
| **Optional** | Lightweight session pointer for fast resume | MCP store tool `memory_storeKnowledge` (§2.0) / recall, keyed by `ile:session:{subject}` |
| **Contract** | EPS + full EOP + Strategy at session start | Option B: MCP digest key `ile:contract`; Option A: `docs/ai/implementation/ile-effective-learning-contract.md` |
| **Rule** | Agent behavior for store/recall at session boundaries | `.cursor/rules/ile-session-memory.mdc` |
| **Rule** | Agent behavior for contract + all EOP steps 1–8 | `.cursor/rules/ile-effective-learning.mdc` |

Context is **preserved across sessions** because (1) A and the Learning Book are on disk, and (2) optionally MCP holds a small pointer keyed by subject. The Agent is instructed (via rule) to use this at session start and session end.

## 4. Evidence for Noun-AC2

- **Persistent memory available to the Agent:** File-based (A + Learning Book) always; MCP when configured (`.cursor/mcp.json`).
- **Tied to current subject/Learning Book:** Keys use `{subject}` and `learning_book_path`; A is per-subject; Learning Book is per Area.
- **Context preserved across sessions:** Agent reads A (and optionally MCP) at session start; Agent writes to A (and optionally MCP) at session end. See `ile-minimal-flow.md` and `.cursor/rules/ile-session-memory.mdc`.
