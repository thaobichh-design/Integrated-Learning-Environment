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
