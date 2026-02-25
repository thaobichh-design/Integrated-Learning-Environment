---
phase: implementation
title: ILE Session Recording for Analytics (T-412)
description: Append structured events (session start, entry point selected, chunk completed, session end) to a simple JSON log. Lightest path to ScalAdv-AC5 / Noun-AC10 without a full analytics platform.
feature: integrated-learning-environment
task: T-412
---

# Session Recording (T-412)

**Purpose:** When a learning session happens, the ILE appends **structured events** to a simple JSON log so the product owner (or operator) can obtain usage data for Descriptive, Diagnostic, Predictive, and Prescriptive analytics (ScalAdv-AC5, Noun-AC10). No full analytics platform is required; the log is the minimal data collection mechanism.

**Log file:** **`logs/ile-session-events.jsonl`** (one JSON object per line; JSONL). The `logs/` directory is created on first write. Add `logs/` to `.gitignore` so usage data is not committed.

**Event types and when to append:**

| Event | When to append |
|-------|----------------|
| **session_start** | When the Agent has oriented the user at session start (EOP Step 3 Resume or equivalent). |
| **entry_point_selected** | When the user has selected an entry point and the Agent has loaded the template / scoped context. |
| **chunk_completed** | When the user has approved a write and the Agent has written to the Learning Book for one component or entry point (completion moment). |
| **session_end** | When the user ends the session or switches phase/entry after Step 7 Checkpoint (progress committed, A updated if applicable). |

**Schema (one JSON object per line):**

- **event** (string, required): `session_start` | `entry_point_selected` | `chunk_completed` | `session_end`
- **timestamp** (string, required): ISO 8601 (e.g. `2025-02-24T10:30:00Z`)
- **subject** (string, optional): e.g. `COE_DS`
- **entry_point** (string, optional): e.g. `Chapter 1 UBS, Topic 0` (for entry_point_selected, chunk_completed)
- **phase** (string, optional): `B` | `C` | `D` (for entry_point_selected, chunk_completed)

Example lines:

```json
{"event":"session_start","timestamp":"2025-02-24T10:00:00Z","subject":"COE_DS"}
{"event":"entry_point_selected","timestamp":"2025-02-24T10:05:00Z","subject":"COE_DS","phase":"C","entry_point":"Chapter 1 UBS, Topic 1"}
{"event":"chunk_completed","timestamp":"2025-02-24T10:15:00Z","subject":"COE_DS","phase":"C","entry_point":"Chapter 1 UBS, Topic 1"}
{"event":"session_end","timestamp":"2025-02-24T10:30:00Z","subject":"COE_DS"}
```

**Who appends:** The Agent, when operating in ILE context (session start, entry point selected, chunk completed, session end), appends one line to the log. The Agent may use **`scripts/append_session_event.py`** to ensure consistent format and path, or write the JSON line directly per this schema.

**Script:** `scripts/append_session_event.py` — accepts event type and optional `--subject`, `--phase`, `--entry-point`; appends a single JSON object (with timestamp) to `logs/ile-session-events.jsonl`. Run from repo root.

**Rule:** `.cursor/rules/ile-session-memory.mdc` § Session recording (T-412): at the four moments above, append to the session event log per this doc (or invoke the script).

**Evidence (T-412):** This doc defines the event schema and log path; the script and rule implement the lightest path to usage data for analytics. ScalAdv-AC5, Noun-AC10.

**Cross-references:** Design § Usage analytics (I4) | Requirements ScalAdv-AC5, Noun-AC10 | `ile-session-memory.mdc` § Session recording.
