---
phase: implementation
title: ILE Stats, Achievements, Streaks (T-406)
description: Stats, achievements, and streaks (e.g. completed entry points, daily return) so the user can view progress and sustain motivation; optional to consume, no mandatory steps. Verb-AC10, Noun-AC11.
feature: integrated-learning-environment
task: T-406
---

# Stats, Achievements, Streaks (T-406)

**Purpose:** The ILE supports (or will support) **stats, achievements, and streaks** (e.g. completed entry points, daily return) so the user can **view progress and sustain motivation**. Optional to consume; no mandatory steps. Verb-AC10, Noun-AC11.

**Scope (when implemented):**

| Stat / concept | Description | Data source |
|----------------|-------------|-------------|
| **Completed entry points** | Count of entry points (or components) completed per phase (B/C/D) or overall. | A + Session Log (what’s completed per phase/entry). |
| **Daily return** | Whether the user had a session today (or last N days). | Session Log (session dates). |
| **Streak** | Consecutive days with at least one session (e.g. "3-day streak"). | Session Log (session dates, ordered). |
| **Achievements (optional)** | Milestones (e.g. "First entry point completed", "Phase C 50% complete"). | Derived from completed entry points + Session Log. |

**Where shown:** (1) **In-conversation** — Agent can mention progress summary (T-304) and, when implemented, optional stats (e.g. "You’re on a 3-day streak"). (2) **Dedicated UI** — Stats section in the dashboard (T-405 stub) can show completed entry points, streak, last session date.

**Constraint:** No mandatory steps. Stats are **additive and optional**; the user can ignore them. EffAdj-AC5: engagement features do not add mandatory steps.

**Stub (T-406):** Stats are **documented** here and **stubbed** in the dashboard (`ile-dashboard-stub.html` § Stats): placeholder fields (Current streak, Completed entry points, Last session). Not computed from live data yet. Full implementation would derive stats from A + Session Log (and optionally session timestamps for streaks) and surface them in-conversation and/or in the dashboard.

**Evidence (T-406):** This doc defines the stats model; the dashboard stub has a Stats section with placeholder fields. Verb-AC10, Noun-AC11: "stats/achievements/streaks implemented or stubbed; optional to consume."

**Cross-references:** Design §1.5 I4 Engagement full | Requirements Verb-AC10, Noun-AC11, EffAdj-AC5 | T-304 (progress summary in chat) | T-405 (dedicated UI) | `ile-dedicated-ui.md` § Stats (optional).
