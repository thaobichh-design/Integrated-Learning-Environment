---
phase: design
title: LTC Integrated Learning Environment — Design
description: System design and architecture for the Integrated Agentic Learning Workspace. State A Sub-Step 2 approved.
feature: integrated-learning-environment
---

# 1. THE SYSTEM DESIGN (Context & Bridge)
*Approved in State A Sub-Step 2. Source: `docs/ai/requirements/feature-integrated-learning-environment.md`.*
* **Subject Roadmap (A) as UDO anchor** (learning and entry-point presentation informed by current level L1–L7 so the user can respect level-appropriate progression and avoid scattered learning).
* **Principles (Why):** Hierarchy over chronology; active recall and deep questioning; single persistent context; documentation as byproduct; one environment; you are the author; consumption in-scope, digestion out-of-scope; 
* **Environment (Where):** Digital, local-first. Learning Book = Markdown repo (COE → Area → Chapter → Topic). Per subject: A. Subject Roadmap, B. Captured, B. Organised Knowledge (UBS, UDS, EPS, UES, EOP…), D. Distilled Understanding, E. Expressed Expertise. Interfaces: Cursor Chat / AntiGravity; optional later: NotebookLM-like (Audio, Infographics, Quiz) with exploration beyond given sources.
* **Tools (What):** Desirable Wrapper = integrated learning conversation (phase A/B/C, entry-point choice, template-driven). Effective Core = persistent memory + real-time Markdown update + template loading (questions × components) + Learning Map entry points.
* **SOP (How):** (1) Start area (COE → Area → Chapter → Topic); (2) Agent asks phase A/B/C and presents entry points; (3) User selects entry → template loads; (4) Learning conversation, doc updates in real time; (5) Optional distill (Phase C); (6) Progress/roadmap; (7) Digestion outside system.

### 1.1 Persistent Memory & Context Storage

| What | Where it lives | Notes |
|------|----------------|--------|
| **AEL hierarchy** (COE → Area → Chapter → Topic, phases A/B/C, components) | **Repo files** (templates, config, or `docs/ai/`) | Canonical, versioned; Agent reads when needed. Not in MCP memory. |
| **Templates** (questions × components, Distilled Table structure) | **Repo files** | Single source of truth. |
| **LTC COE map** (for ClickUp mapping) | **Repo files or config** | Defined structure. |
| **Subject learning content** (what the user has written in the Book) | **Markdown Learning Book** | Source of truth; Agent reads/writes these files. |
| **Resume / session context** (current subject, last entry point) | **Optional: MCP persistent memory** (e.g. `@ai-devkit/memory`) | Enables "where we left off" without re-reading the whole Book. |
| **First-principles / venture rules** (e.g. from `/remember`) | **MCP persistent memory** | Cross-session knowledge for the Agent. |

So: persistent memory does **not** store the full hierarchy or all templates; it **can** store subject/session pointers and high-level knowledge for continuity across sessions.

### 1.2 Subject Roadmap (A) as UDO Anchor

**A** (Subject Roadmap & Level Specifications) defines the target mastery levels (L1–L7 SFIA), requirements, and recommended learning sources per subject. It is the **UDO anchor**: learning that respects A is level-appropriate and sequenced; ignoring A leads to scattered learning (e.g. L4 content while still at L1/L2/L3). The ILE must:

* **Surface A:** Let the user see their current level and the relevant part of A (e.g. level requirements, next-step recommendations) so they can consciously respect it.
* **Inform entry points:** Use the user's current level and A to prioritise or suggest level-appropriate entry points in the Learning Map; the user can still choose any entry point.
* **Assess progress:** Use A to assess growth, identify gaps, and plan next steps (SOP step 6).

So: A is not only "where we store the roadmap" but the **reference for what the user should respect** so learning stays on track.

### 1.3 Reusability: other spaces and template sets

The ILE pattern (Capture → Organise → Distill with AI Agent; template-driven; sync to a defined location) is **generic**. The current use case (COE Learning Book, AEL templates, sync to LTC COE ClickUp space) is **one configuration**. The same setup can later be applied to:

* **Other ClickUp spaces** (e.g. project management, sales, operations — not COE), each with its own hierarchy and member/location mapping.
* **Different doc template sets** (different phases, entry points, questions × components) stored as config or repo files.

To support this, **hierarchy**, **templates**, and **ClickUp space mapping** must be **configurable** (e.g. per workspace or per "mode"), not hard-coded to COE and AEL. Then the core integration (chat + memory + real-time doc update + template load + sync) stays the same; only the config changes.

---

# 2. TECHNICAL ARCHITECTURE (The Noun)
*First pass after Sub-Step 4 (Roadmap); refined and completed in State B as we implement each iteration.*

* **Feature Noun:** ILE = IDE (or OpenClaw) + Master Effective Learning Template + integration (see requirements Phase 3).
* **Visual Map (Mermaid):** [TBD]
* **Component Mapping:** [TBD]
* **Data Models & APIs:** [TBD]

---

# 3. EFFECTIVENESS ATTRIBUTES (The Adjectives)
*How the feature attributes enable the user to reach the Effectiveness Outcomes.*

*Map each attribute below to the corresponding Requirements A.C. IDs (e.g. SustainAdj-AC1, EffAdj-AC1, ScalAdj-AC1) and to the Planning iteration where that A.C. is validated. Design defines how; Requirements and Planning define what and when.*

* **Sustainability (Risk/Safety):** Structure-faithful — SustainAdj-AC1..AC3. All writes conform to hierarchy and phase structure; template loading uses canonical component set; user can verify repo structure. *Validated in:* Iteration 2 (Working Prototype).
* **Efficiency (Speed/Utility):** Zero-friction capture — EffAdj-AC1..AC3. No copy-paste step; updates triggered by conversation; in-progress context retained on switch. *Validated in:* Iteration 3 (MVE).
* **Scalability (Growth):** Template-driven — ScalAdj-AC1..AC4. New subjects reuse template; configurable entry points/templates; optional capabilities; hierarchy/templates/space configurable for other ClickUp spaces and template sets. *Validated in:* Iteration 4 (Leadership).

---

# 4. RESOURCE IMPACT (The "Price Tag")
* **Financial Cost (OpEx):** [Estimated monthly/fixed costs — TBD when architecture is defined]
* **Build Complexity:** [Low/Medium/High — TBD]
* **ROI Sanity Check:** [Does this architecture respect the Principle of Efficiency? — TBD]

*Ongoing tracking:* See Planning §3 (Resource & Budget Tracker) for current usage vs limits.

**Requesting Resources / Budget from the User (optional):** When the design or execution requires a budget increase, new tool, or paid service:
1. **When to ask:** Before committing to a task that exceeds current limits (e.g. new API, hosting, paid tier). Do not assume; request explicit approval.
2. **What to specify:** Amount or ceiling (e.g. $X/month, Y API calls/day), purpose (which A.C. or task it serves), and alternative if the User says no.
3. **Approval gate:** Do not spend or integrate until the User approves. Record the approved limit in Planning §3 (Hard Limit) and proceed. If the User declines, adjust scope or task (e.g. mark 🟠 Stuck and propose an alternative).

---

*Last updated: Aligned with template 1.1.0. Planning: `docs/ai/planning/feature-integrated-learning-environment.md`. Full design (§2–4) refined in State B.*
