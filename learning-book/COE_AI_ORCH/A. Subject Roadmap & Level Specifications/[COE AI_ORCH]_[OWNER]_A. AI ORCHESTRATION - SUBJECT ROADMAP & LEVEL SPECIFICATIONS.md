# [COE AI_ORCH]_[OWNER]_A. AI ORCHESTRATION - SUBJECT ROADMAP & LEVEL SPECIFICATIONS

*Subject: AI Orchestration / Engineering. Area: Operational Excellence → Product Leadership → User Enablement. Primary framework: Agno. Secondary: CrewAI. Context: Non-tech solo operator building and directing AI agent swarms.*

---

## Learner Progress Tracker

| Field | Value |
|-------|-------|
| **Current Level** | L1 (Follow) |
| **Target Level** | L5 (Ensure / Advise) |
| **Target Date** | 2026-08 |
| **Last Session** | 2026-02-27 |
| **Last Entry Point** | Chapter 0. Overview & Summary, Page 0. Overview |
| **Next Recommended Entry Point** | Chapter 0. Overview & Summary — review full Effective System Design, then Chapter 4. UES, Topic 0 (system components deep-dive) |

---

## Level Completion Checklist

| Level | Met | Evidence | Date |
|-------|-----|----------|------|
| L1 | 🔲 | — | — |
| L2 | ⬜ | — | — |
| L3 | ⬜ | — | — |
| L4 | ⬜ | — | — |
| L5 | ⬜ | — | — |
| L6 | ⬜ | — | — |
| L7 | ⬜ | — | — |

---

## Gap Analysis

| Level | Gap | Priority |
|-------|-----|----------|
| L1 | Can converse with single AI (Claude/Gemini) and build prototypes in Cursor; has NOT yet built a standalone agent with tools, memory, or instructions via a framework (Agno/CrewAI). | 🔴 Immediate |
| L2 | Has not wired two agents into a Team or passed context between agents. No experience with Coordinator Mode, shared memory, or handoff protocols. | 🔴 Next |
| L3 | Has not built a multi-step Workflow (Loop, Parallel, Condition, Router). Has not deployed an agent to AgentOS or any runtime. | 🟡 After L2 |
| L4 | Has not designed a reusable agent architecture (e.g., Investment Team template customised for a second domain). Has not taught or enabled others to use the system. | 🟡 After L3 |
| L5 | Has not governed a production swarm (monitoring, error handling, cost control, scaling). Has not established organisational standards for agent design. | ⚪ Future |

---

## Level Specifications (L1–L7)

| Expertise Band | SFIA Level | Requirements | Credentials |
|----------------|------------|--------------|-------------|
| **ENTRY** | **1 – Follow** | Understand what an AI agent is vs a chatbot. Install Agno. Build 1 single agent with tools (e.g., YFinance) and instructions. Run it locally. Understand Agent → Team → Workflow hierarchy. | Working single agent that retrieves live stock data and responds to a query. Screenshot or repo link. |
| **FOUNDATION** | **2 – Assist** | Build a 2-agent Team with Coordinator Mode. Pass context from Agent A → Agent B (e.g., Research Analyst outputs thesis → Risk Analyst challenges it). Use session memory. Understand role-playing (CrewAI comparison). | Working 2-agent Team with observable handoff. Session memory persists across turns. |
| **PRACTITIONER** | **3 – Apply** | Build a multi-step Workflow with at least: 1 Parallel step, 1 Condition, 1 Loop. Deploy to AgentOS. Monitor via dashboard. Handle errors (agent failure, LLM timeout). Build a 4+ agent team for a real use case (Investment Research). | Deployed Workflow on AgentOS with dashboard screenshots. Investment Team running end-to-end: ticker in → memo out. |
| **EXPERT** | **4 – Enable** | Reuse the Investment Team architecture for a second domain (e.g., Competitive Intelligence, Due Diligence). Create reusable agent templates. Teach the pattern to another person or document it for team use. Integrate with ClickUp for task tracking. | Two domain-specific agent teams running from the same base architecture. Documentation or training artefact. ClickUp integration working. |
| **STRATEGIC PRACTITIONER** | **5 – Ensure / Advise** | Govern a production swarm: cost monitoring, rate limiting, error budgets, security review. Establish organisational standards (naming, tool approval, prompt templates). Evaluate new frameworks (CrewAI Flows, OpenFang v1.0) against current architecture. Advise on build-vs-buy decisions. | Production governance dashboard. Written standards document. Framework evaluation report with recommendation. |
| **STRATEGIC LEADER** | **6 – Initiate / Influence** | Design multi-team orchestration (teams of teams). Influence organisational adoption of AI orchestration. Define ROI metrics and business cases. Lead cross-functional agent deployments. | Multi-team architecture deployed. Business case with measured ROI. Cross-functional deployment evidence. |
| **STRATEGIC VISIONARY** | **7 – Set Strategy / Inspire / Mobilize** | Set the AI orchestration strategy for the organisation. Anticipate framework evolution. Inspire others to adopt. Mobilise resources for enterprise-scale deployment. Define the vision for human-AI collaboration at organisational level. | Published strategy. Evidence of organisational mobilisation. Vision document adopted by leadership. |

---

## Links to Learning Book (per Level)

| Level | Recommended Chapters/Topics |
|-------|---------------------------|
| L1 | Chapter 0. Overview (all pages); Chapter 1 UBS (0. Overview, 1. Blockers) |
| L2 | Chapter 1 UBS (full); Chapter 2 UDS (0. Overview, 2. Drivers) |
| L3 | Chapters 2–3 (UDS full, EPS full); Chapter 4 UES (0. Overview, 4. Components) |
| L4 | Chapter 4 UES (full); Chapter 5 EOP (0. Overview, 5. Steps) |
| L5+ | Chapter 5 EOP (full); Area D/E (Distill Understanding, Express Expertise) |

---

## Session Log

| Date | Entry Point | Progress |
|------|-------------|----------|
| 2026-02-27 | Chapter 0. Overview, Page 0 | Initial Effective System Design populated via Claude Cowork. High-level overview of AI Orchestration, UBS/UDS/EPS/UES/EOP all populated. Framework comparison (Agno vs CrewAI vs OpenFang vs OpenClaw) completed. Agno selected as primary. |
| 2026-02-28 | Topic 1 complete | T1.P0–P1.P5 all approved. Topic 1 (UBS / Capability Gap) is a complete system: 6 pages, 1 Overview + 3 UB rows + 3 UD rows + 7 principles + 7 components + 6 EOP steps. 12 of 36 pages done. |
| 2026-02-28 | Topic 2 started | T2.P0 APPROVED (copy of T0.P2, Relevance edited for Topic 2). T2.P1 APPROVED (UB Layer: Pattern Blindness, Absence of Forcing Mechanism, Multi-Domain Curriculum Discipline; table separator fixed to 17 columns). T2.P2 GENERATED (UD Layer: Deliberate post-build reflection, Reflection bypass, Structured same-session extraction gate). Pending User approval of T2.P2. |

---

## Phase C Organise — state (read first when resuming Phase C)

*This section holds the persistent state for Phase C (Organise Information) page-by-page work. Agent: read this and the last approved page file before generating or reviewing the next page. Update here at every approval.*

### UDO (Ultimate Desired Outcome)

Build and master an OE System (AI Orchestration Engine) that any analyst/operator can use to build domain-specific UE systems. Effective = Sustainable, Efficient, Scalable. This is the system that builds systems — NOT a specific domain project. Investment Research is one example instance only.

### Structure

- 6 Topics (0-5) × 6 Pages (0-5) = 36 .md files under Phase C
- Each page = ONE pure markdown table, as many rows as needed, 17 columns (1 row label + 16 canonical questions)
- Column Key reference section above every table
- NO HTML tables — they do not render in Cowork sidebar Preview mode

### Topic Map

| Topic | Name | Role |
|---|---|---|
| 0 | Overview & Summary | Root level, overview depth only |
| 1 | UBS | Deep dive into root UBS from T0.P1 |
| 2 | UDS | Deep dive into root UDS from T0.P2 |
| 3 | EPS | Deep dive into principles from T0.P3 |
| 4 | UES | Deep dive into components from T0.P4 |
| 5 | EOP | Deep dive into procedure from T0.P5 |

### Notation (CRITICAL — dot-notation only)

- UBS = Ultimate Blocking System (root blocker). UBS.UB = what disables the UBS → works IN User's favour. UBS.UD = what drives the UBS harder → works AGAINST User.
- UDS = Ultimate Driving System (root driver). UDS.UD = what drives the UDS further → works IN User's favour. UDS.UB = what blocks the UDS → works AGAINST User.
- Recursive: UBS.UB.UB, UBS.UB.UD, UBS.UD.UB, UBS.UD.UD, etc. **NEVER use UBS1, UBS2, UDS1, UDS2.**

### Page Structure Rules

**Topic 0:** P0 = 1 row (Effective system). P1 = 1 row from P0 col 10 (UBS). P2 = 1 row from P0 col 4 (UDS). P3 = N rows harvest cols 6+12 from P0+P1+P2. P4 = N rows INFRA→WORKSPACE→INTEL. P5 = N rows STEP.1….

**Topics 1–5:** P0 = COPY parent page (T1→T0.P1, etc.). P1 = 3 rows: parent.UB, parent.UB.UB, parent.UB.UD. P2 = 3 rows: parent.UD, parent.UD.UB, parent.UD.UD. P3 = harvest from P0+P1+P2 of THIS topic. P4 = INFRA→WORKSPACE→INTEL, each traces to P3. P5 = steps referencing P1–P4.

### UES = 3 Causal Layers (AI Orchestration)

- Layer 1: INFRASTRUCTURE — Python, Agno, Anthropic API, compute (must exist first)
- Layer 2: WORKSPACE — Cursor, Git, ILE, ClickUp (requires Infrastructure)
- Layer 3: INTELLIGENCE — Claude LLM, YFinance, Exa, prompts, community (requires Workspace)
- Row labels: INFRA.n → WORKSPACE.n → INTEL.n (always this order). Each component traceable to at least one Principle from Page 3 of the same Topic.

### Key Rules (Phase C — do not override)

1. EPS derives DIRECTLY from UBS and UDS — never generic best practices.
2. One blocker or driver per row — not greedy. Depth comes in later Topics.
3. Each row builds causally on the previous (causal chain — not a list).
4. Topic 0 = overview depth. Topics 1–5 = one recursive layer deeper each.
5. Present each page in sidebar → User reviews → challenges → approves → update A (this section) → next page.
6. Do NOT regenerate Topics 1–5 Page 0 — copy the parent file and rename.
7. EPS must explicitly state "Enables [UDS element]" OR "Disables [UBS element]" per row.
8. UES components ordered: INFRA first, WORKSPACE second, INTEL third — always.

### Frameworks

- Primary: Agno (Python) — Agent → Team (Coordinator) → Workflow (Loop, Parallel, Condition, Router). AgentOS for monitoring.
- Secondary: CrewAI (Python) — evaluate at L4+.
- IDE: Cursor | Model: Claude LLM.

### Session Protocol (Hybrid — Option C)

- **Content state:** A (this file) is the source of truth for Phase C approved pages, current state, next action, causal seeds, and decisions.
- **In Cursor:** Step 2 at session start; Step 7 before phase/entry switch; conversation→doc mapping for every write; Session Log updated. Both read A first.
- **On Claude:** CLAUDE.md + A only; handoff = update this file (Session Log + Phase C state sections).

### Causal Seeds (carry forward to next pages)

| From page | Col | Content | Seeds into |
|---|---|---|---|
| T0.P0 | col 10 (UBS) | Capability Gap — User lacks mental model for agent decomposition | T0.P1 row label; T1.P0 (copy) |
| T0.P0 | col 4 (UDS) | Hierarchical decomposition thinking | T0.P2 row label; T2.P0 (copy) |
| T0.P1 | col 4 (UDS) | Activation Barrier — drives the Capability Gap harder (UBS.UD, works AGAINST Learner) | T1.P2 Row1 (UBS.UD) |
| T0.P1 | col 10 (UBS) | Incremental build-test cycles — disables the Capability Gap (UBS.UB, works FOR Learner) | T1.P1 Row1 (UBS.UB) |

### Decisions Log

| Date | Scope | Decision |
|---|---|---|
| 2026-02-27 | P0 | EPS must derive from UBS/UDS — not generic best practices |
| 2026-02-27 | P0 | UES = Infrastructure/Workspace/Intelligence (3 causal layers) |
| 2026-02-27 | P0 | T0.P0 revised to 1 row only — greedy extra rows removed |
| 2026-02-27 | All | CLAUDE.md created at ILE root — auto-loads at session start |
| 2026-02-27 | All | Page structure finalised: T0 P1/P2 = 1 row; T1-5 P1/P2 = 3 rows |
| 2026-02-27 | All | UES confirmed = Environment + Tools. Each Topic = its own complete system. |
| 2026-02-27 | All | All 6 template files rewritten to pure markdown with derivation instructions |
| 2026-02-27 | All | page-4-components.md updated: generic [LAYER1/2/3] placeholders; AI Orch names in CLAUDE.md |
| 2026-02-27 | All | Old `0. Overview & Summary.md` (wrong format) deleted |
| 2026-02-27 | All | Duplicate parent file rule confirmed: T1-5 P0 = copy of T0.Px, no regeneration |
| 2026-02-27 | All | Session handoff = A (this file) Session Log + Phase C state sections |
| 2026-02-27 | All | Min files to resume: CLAUDE.md + A (this file) + last approved page |
| 2026-02-27 | Model | Sonnet for Topics 0–3; Opus only for Topic 5 EOP if needed |
| 2026-02-27 | T0.P0 | APPROVED by User |
| 2026-02-27 | T0.P1 | APPROVED by User |
| 2026-02-27 | T0.P2 | APPROVED by User (row label updated: "Hierarchical Decomposition Thinking (Systems Thinking)") |
| 2026-02-27 | T0.P3 | APPROVED by User (P1 reframed as ELF→System Design; P2 as hypothesis-driven; P3 as Learn→Build→Test→Validate→Measure loop) |
| 2026-02-27 | T0.P4 | APPROVED by User (7 rows: INFRA.1-2, WORKSPACE.1-3, INTEL.1+2. INTEL.2 domain tools removed — belongs in domain instance, not OE meta-system. Original INTEL.3 AgentOS renumbered to INTEL.2 after removal.) |
| 2026-02-28 | All | TERMINOLOGY: "ILE Framework" → "Effective Learning Framework (ELF)" everywhere. ILE = digital environment/tool built on Cursor. ELF = the methodology (UDO→Roles→UBS→UDS→EPS→UES→EOP). Applied across T0.P3 and T0.P5. |
| 2026-02-28 | All | TERMINOLOGY: "kill criteria" → "Acceptance Criteria (A.C.)" everywhere. A.C. = single, deterministic pass/fail test traceable to a design decision (Verb/Adverb/Noun/Adjective) → EPS → UBS/UDS. Applied across T0.P3 and T0.P5. |
| 2026-02-28 | ELF gap | Phase 3 Formalization (Verb+Adverb+Noun+Adjective + A.C.) has NO ELF equivalent. Desirable Wrapper / Effective Core distinction not in ELF. User Persona / Anti-Persona not in ELF. These gaps to be addressed in Topics 3–5, not blocking Topic 0. |
| 2026-02-28 | T0.P5 | STEP.8 reframed: not just extracting patterns — explicitly packaging the OE meta-system with OE README (≤2 pages) and named domain-agnostic templates under /oe-system/ in Git, so other solo operators can run STEP.1–7 for their own domain. Gate updated to require README committed + second domain STEP.2 faster. |
| 2026-02-28 | T0.P5 | APPROVED by User. Topic 0 complete. Proceeding to Topic 1 generation. |
| 2026-02-28 | T1.P2 | Generated and APPROVED by User (pre-fix version — content correct, structural position wrong due to col 4/10 swap). |
| 2026-02-28 | All | **COLUMN KEY REVISION**: Canonical questions strengthened to prevent perspective error. Col 3→"Success Actions" (symmetric with col 9). Col 6→"Success EPS". Col 7→"Success Tools (UES)". Col 8→"Success Environment (UES)". Col 12→"Failure EPS". Col 13→"Failure Tools (UES)". Col 14→"Failure Environment (UES)". Cols 3, 4, 9, 10 include explicit row-subject-type guidance. Perspective Rule added above every Column Key. |
| 2026-02-28 | All | **COL 4/10 SWAP FIX**: When row subject is a UBS, col 4 = UBS.UD (drives blocker — AGAINST Learner) and col 10 = UBS.UB (disables blocker — FOR Learner). T0.P1 had these swapped. Cascade: T1.P0 (copy), T1.P1 (seeded from wrong col), T1.P2 (seeded from wrong col). Fix: swap col 4↔10 in T0.P1/T1.P0, swap T1.P1↔T1.P2 content with corrected notation. COMPLETED AND APPROVED. |
| 2026-02-28 | T1 | T1.P0 APPROVED (corrected copy of T0.P1 with col 4/10 fixed). T1.P1 APPROVED (3 rows: UBS.UB=Incremental Build-Test Cycles, UBS.UB.UB=Scope Indiscipline, UBS.UB.UD=Principle Extraction Discipline). T1.P2 APPROVED (3 rows: UBS.UD=Activation Barrier, UBS.UD.UB=Permission to Start Small, UBS.UD.UD=Unlimited Preparation as Avoidance). T1.P3 GENERATED (7 rows: P1–P7 harvested from T1.P0+P1+P2 col 6+12. P6+P7 are risky principles. Pending User approval in sidebar). |
| 2026-02-28 | All | **COL 2 REVISION — HEADER**: Col 2 question updated from "What is it? (Introduction)" to "What is it precisely — and what is it NOT? (Precise Definition)" across all 6 templates + all 10 approved pages. Table header label updated from "2 · Introduction" to "2 · Precise Definition". |
| 2026-02-28 | All | **COL 2 REVISION — CONTENT**: Col 2 cell content regenerated for all 35 rows across 10 approved pages using IS / IS NOT structure. Each cell now states the precise bounded definition + explicit boundary contrast (what it is NOT, what it could be confused with). Replaces old "Introduction" content that echoed the row label without adding precision. Applied in session 2026-02-28. |
| 2026-02-28 | T1.P4 | APPROVED by User. Full template restored (Perspective Rule, Column Key, Layer Map, 7×16 table); content streamlined and UBS-specific per column. Proceeding to T1.P5. |
| 2026-02-28 | T1.P5 | Generated (6 steps). STEP.2 revised: ELF before A.C. STEP.4 revised: technical (AgentOS) + usage (A.C.) testing. APPROVED by User. Topic 1 complete. |
| 2026-02-28 | T1 complete | All 6 pages (T1.P0–T1.P5) approved. Topic 1 (UBS / Capability Gap via Incremental Build-Test Cycles) is now a complete, usable system. 12 of 36 pages done (T0: 6, T1: 6). |
| 2026-02-28 | T2.P1 | APPROVED by User. Table separator fixed (17 columns). T2.P2 GENERATED (UD Layer: UDS.UD = Deliberate post-build reflection, UDS.UD.UB = Reflection bypass, UDS.UD.UD = Structured same-session extraction gate). |

### Approved Pages (in order)

| # | File | Status |
|---|---|---|
| 1 | `C. Organise Information/0. Overview & Summary/0. Overview & Summary - 0. Overview & Summary.md` | ✅ APPROVED |
| 2 | `C. Organise Information/0. Overview & Summary/0. Overview & Summary - 1. Ultimate Blockers.md` | ✅ APPROVED |
| 3 | `C. Organise Information/0. Overview & Summary/0. Overview & Summary - 2. Ultimate Drivers.md` | ✅ APPROVED |
| 4 | `C. Organise Information/0. Overview & Summary/0. Overview & Summary - 3. Principles.md` | ✅ APPROVED |
| 5 | `C. Organise Information/0. Overview & Summary/0. Overview & Summary - 4. Components.md` | ✅ APPROVED |
| 6 | `C. Organise Information/0. Overview & Summary/0. Overview & Summary - 5. Steps to Apply.md` | ✅ APPROVED |
| 7 | `C. Organise Information/1. UBS/1. UBS - 0. Overview & Summary.md` | ✅ APPROVED |
| 8 | `C. Organise Information/1. UBS/1. UBS - 1. Ultimate Blockers.md` | ✅ APPROVED |
| 9 | `C. Organise Information/1. UBS/1. UBS - 2. Ultimate Drivers.md` | ✅ APPROVED |
| 10 | `C. Organise Information/1. UBS/1. UBS - 3. Principles.md` | ✅ APPROVED |
| 11 | `C. Organise Information/1. UBS/1. UBS - 4. Components.md` | ✅ APPROVED |
| 12 | `C. Organise Information/1. UBS/1. UBS - 5. Steps to Apply.md` | ✅ APPROVED |
| 13 | `C. Organise Information/2. UDS/2. UDS - 0. Overview & Summary.md` | ✅ APPROVED |
| 14 | `C. Organise Information/2. UDS/2. UDS - 1. Ultimate Blockers.md` | ✅ APPROVED |
| 15 | `C. Organise Information/2. UDS/2. UDS - 2. Ultimate Drivers.md` | 📝 Generated |

### Current State (Phase C)

*Last updated: 2026-02-28 (session 4)*

- T0.P0–T0.P5: ✅ ALL APPROVED (Topic 0 complete)
- **T1.P0–T1.P5: ✅ ALL APPROVED (Topic 1 complete)**
  - T1.P0 (Overview): corrected copy of T0.P1
  - T1.P1 (UB Layer): 3 rows (Incremental Build-Test Cycles / Scope Indiscipline / Principle Extraction Discipline)
  - T1.P2 (UD Layer): 3 rows (Activation Barrier / Permission to Start Small / Unlimited Preparation as Avoidance)
  - T1.P3 (EPS): 7 rows (P1–P7, including P6+P7 as risky principles)
  - T1.P4 (UES): 7 rows (INFRA/WORKSPACE/INTEL, UBS-specific)
  - T1.P5 (EOP): 6 steps (confirm components → ELF+A.C. → build → test (technical+usage) → commit → principle)
- **T2 (UDS / Hierarchical Decomposition Thinking):**
  - T2.P0 (Overview): ✅ APPROVED — copy of T0.P2.
  - T2.P1 (UB Layer): ✅ APPROVED — 3 rows (Pattern Blindness / Absence of Forcing Mechanism / Multi-Domain Curriculum Discipline). Table separator fixed (17 columns).
  - T2.P2 (UD Layer): Generated — 3 rows (Deliberate post-build reflection / Reflection bypass / Structured same-session extraction gate). Pending User approval.
  - T2.P3–T2.P5: Not yet generated
- Topics 3–5: Not yet generated

**Last approved page:** `C. Organise Information/2. UDS/2. UDS - 1. Ultimate Blockers.md`

**Next action:** Review T2.P2 (UD Layer) in sidebar. Approve to proceed to T2.P3 (EPS harvest).

---

## Agent role for this subject

**The Agent acts as the Learner's subject teacher and world-class expert in AI Orchestration for this Learning Book.** The Agent teaches the subject (agents, teams, workflows, Agno, CrewAI, orchestration patterns, OE systems) by answering questions, explaining concepts, and helping the Learner explore the boundaries of knowledge — in addition to executing the ILE process (templates, Phase C state, one entry at a time). The Agent should use full domain knowledge and, when useful, web search to bring in the most recent knowledge. The Agent must be honest and explicitly state when it does not know something or is at the edge of its knowledge.

---

## Subject-Specific Requirements & Credentials

### L1 – Follow

- **Requirements:**
  1. Explain the difference between a chatbot conversation and an AI agent (tools, memory, instructions, autonomy)
  2. Install Agno (`pip install agno`) in a Python environment accessible from Cursor
  3. Build and run a single Finance Agent with YFinance tools that retrieves live stock data

- **Credentials:**
  1. Working Python script (`my_first_agent.py`) that creates an Agno Agent and answers "What is the current price of AAPL?"
  2. Screenshot of agent output with tool call visible
  3. Can articulate: "An agent has a model, tools, instructions, and memory. A chatbot only has a model."

### L2 – Assist

- **Requirements:**
  1. Build a 2-agent Team: Research Analyst + Risk Analyst with Coordinator
  2. Demonstrate context passing: Research output feeds Risk input
  3. Use session memory so a follow-up question references prior analysis

- **Credentials:**
  1. Working Team script with observable Coordinator delegation
  2. Conversation log showing Agent A → Coordinator → Agent B handoff
  3. Session memory test: ask a follow-up → agent references prior context

### L3 – Apply

- **Requirements:**
  1. Build a Workflow with Parallel + Condition + Loop steps
  2. Deploy to AgentOS (local or cloud)
  3. Build 4+ agent Investment Research Team (Market, Financial, Technical, Risk analysts + Memo Writer + Committee Chair)

- **Credentials:**
  1. Workflow code with at least 3 step types (Parallel, Condition, Loop)
  2. AgentOS dashboard screenshot showing deployed agents
  3. End-to-end Investment Team run: ticker input → investment memo output

### L4 – Enable

- **Requirements:**
  1. Reuse Investment Team architecture for a second domain (e.g., Competitive Intelligence)
  2. Create reusable agent templates (base analyst, base writer, base coordinator)
  3. Integrate agent outputs with ClickUp (task creation, status updates)

- **Credentials:**
  1. Two domain-specific teams running from shared base templates
  2. Template library with documented customisation points
  3. ClickUp integration: agent creates/updates tasks automatically

### L5 – Ensure / Advise

- **Requirements:**
  1. Production governance: cost tracking, error budgets, rate limiting, security review
  2. Written organisational standards for agent design (naming, prompts, tool approval)
  3. Framework evaluation: test CrewAI Flows or OpenFang v1.0 against Agno for a specific use case

- **Credentials:**
  1. Governance dashboard with cost/error metrics
  2. Standards document adopted by team/organisation
  3. Evaluation report with data-backed recommendation

### L6 – Initiate / Influence

- **Requirements:**
  1. Multi-team orchestration: Team of Teams (Investment Team + Research Team + Operations Team coordinated)
  2. Business case with ROI measurement
  3. Cross-functional deployment affecting 2+ business areas

- **Credentials:**
  1. Architecture diagram + working multi-team deployment
  2. ROI report with before/after metrics
  3. Evidence of cross-functional adoption

### L7 – Set Strategy / Inspire / Mobilize

- **Requirements:**
  1. Organisational AI orchestration strategy document
  2. Framework evolution roadmap (anticipate Agno/CrewAI/new entrants)
  3. Vision for human-AI collaboration at scale

- **Credentials:**
  1. Published and adopted strategy document
  2. Roadmap with decision triggers for framework migration
  3. Evidence of organisational mobilisation and culture change

---

*Template source: [COE AI_ORCH]_[OWNER]_A. AI ORCHESTRATION - SUBJECT ROADMAP & LEVEL SPECIFICATIONS. Aligned with SFIA and COE Effective Learning structure. Primary framework: Agno. Secondary: CrewAI.*
