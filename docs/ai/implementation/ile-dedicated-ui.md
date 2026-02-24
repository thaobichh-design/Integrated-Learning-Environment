---
phase: implementation
title: ILE Dedicated UI — Progress, Entry Points, Stats (T-405)
description: Optional dedicated UI for progress, entry points, and stats (e.g. Duolingo-style dashboard) as an optional entry point; in-conversation progress remains sufficient for minimum engagement. Noun-AC12.
feature: integrated-learning-environment
task: T-405
---

# Dedicated UI (T-405)

**Purpose:** The ILE may provide a **dedicated UI** for progress, entry points, and stats (e.g. Duolingo-style dashboard) as an **optional entry point**. In-conversation progress (T-304: completion moment + progress summary in chat) remains **sufficient for minimum engagement**; the dedicated UI is additive and optional to consume. Noun-AC12.

**Scope (when implemented):**

| Section | Content |
|--------|---------|
| **Progress** | Summary of completed entry points / components per phase; level (L1–L7) and Subject Roadmap (A) alignment; optional "X of Y completed for this phase". Data source: A + Session Log (same as in-conversation). |
| **Entry points** | List of entry points per phase (B/C/D), informed by Learning Map and A; user can click to start a session at that entry. Same data as Agent-presented list; optional visual map (e.g. tree or checklist). |
| **Stats (optional)** | T-406: streaks, achievements, completed entry points, daily return. Optional to show; can be stubbed as placeholder. |

---

## How it works

**Today (minimum):** Progress and entry points live **in conversation**. You ask the Agent for phase and entry points; the Agent shows a list in chat and, after you complete work, gives a progress summary (e.g. "3 of 36 completed for this phase"). That stays the default and is enough for minimum engagement.

**With the dedicated UI (optional):** You get a **second way** to see the same information — a **page** (the dashboard) you can open in a browser or in Cursor’s Simple Browser. On that page you’d see:
- **Progress** — e.g. "Phase C: 3 of 36 entry points completed", your level (L1–L7), alignment with Subject Roadmap (A).
- **Entry points** — The same list the Agent would show (by phase B/C/D), informed by the Learning Map and A; you could **click** one to “start here” (when implemented, that could open chat with that entry pre-selected or deep-link into the workspace).
- **Stats (optional)** — Streaks, daily return, achievements (T-406), if implemented.

**Data:** The dashboard would read the **same sources** as the Agent: **A (Subject Roadmap)** and **Session Log** (what’s completed per phase/entry). No separate backend required — it’s another view over the same Learning Book + A + Session Log.

**Flow:** You can (1) use only chat, or (2) open the dashboard when you want a visual overview, then go back to chat to work. The dashboard is an **optional entry point** — you’re never forced to use it.

**Learn with chat + dashboard open (intended use):** **Yes.** The intended flow is **side-by-side**: you **converse with Cursor in chat** (learn, complete entry points, get completion moments) and **keep the dashboard open** (e.g. in Cursor’s Simple Browser or a browser tab) to see how learning is progressing. You learn in chat; the dashboard is a **companion view** for visibility — e.g. “Phase C: 3 of 36 completed” updating as you finish work in chat. Today the stub is static (no live data); when implemented, the dashboard would read A + Session Log and refresh (e.g. on reload or a simple poll) so it reflects what you’ve completed in chat.

**When can you see the UI?** **Now.** Open the stub to see the placeholder layout:
- **In Cursor:** Open **Simple Browser** (Command Palette → “Simple Browser: Show”) and open the file: `file:///.../docs/ai/implementation/ile-dashboard-stub.html` (use your repo path), or right‑click `ile-dashboard-stub.html` → “Reveal in Finder” then open in your system browser.
- **In a browser:** Open `docs/ai/implementation/ile-dashboard-stub.html` from your repo (e.g. drag the file into the browser, or File → Open File and select it).

You’ll see the placeholder sections (Progress, Entry points, Stats). They don’t show real data yet; full implementation would wire the dashboard to A + Session Log so it updates as you learn in chat.

**Stub today:** The HTML stub (`ile-dashboard-stub.html`) is only placeholder sections; it doesn’t read real data yet. Full implementation would wire it to A + Session Log (and optionally T-406 stats) and make entry points clickable.

---

**Constraint:** No mandatory steps. The user can ignore the dedicated UI and use only chat (phase choice → entry points in chat → template load → conversation → progress summary in chat). The UI is an **alternative entry point**, not a requirement.

**Stub (T-405):** A **minimal HTML stub** is provided as the optional entry point: **`docs/ai/implementation/ile-dashboard-stub.html`**. Open in a browser to see placeholder sections (Progress, Entry points, Stats). It is not wired to live data; it demonstrates the intended layout and that a dedicated UI exists as an optional entry point. Full implementation would read from A + Session Log (and optionally T-406 stats) and render real progress and entry points.

**Evidence (T-405):** This doc defines the UI spec; the HTML stub is the stubbed optional entry point. Noun-AC12: "Dedicated UI for progress/entry points/stats implemented or stubbed."

**Cross-references:** Design §1.5 I4 Engagement full | Requirements Noun-AC12, Verb-AC10, Noun-AC11 | T-304 (in-conversation progress) | T-406 (stats/achievements/streaks) | `ile-phase-and-entry-points.md` (entry points).
