# Template: Page 4 — UES (Ultimately Effective System)

*Page type: Components — the tools and environment of this Topic (Phase C. Organise Information).*

---

## Purpose

Page 4 defines the **Ultimately Effective System (UES)** for this Topic: the concrete tools and environment conditions required to implement the Principles (Page 3).

EPS (Page 3) tells you WHAT to do. UES (Page 4) tells you WITH WHAT you execute it.

Each Topic is a system on its own. Mastering the UES for a Topic means: given the right tools and environment, the Principles become executable — the UBS is overcome and the UDS is enabled.

---

## UES = Environment + Tools, in 3 Causal Layers

Components must be:
- **Logical**: Each one has a clear purpose and rationale
- **Causal**: Each layer depends on and builds from the layer below it
- **Layered (stacked)**: The 3-layer stack creates a strong foundation — you cannot skip layers
- **MECE**: Within each layer, components are mutually exclusive and collectively exhaustive

### The Universal 3-Layer Structure

Every subject has 3 causally ordered layers. The layer **names** depend on the subject — you define them based on what makes sense. The **logic** is always the same:

```
Layer 1: [FOUNDATIONAL LAYER]
  Must exist before anything else can operate.
  Everything above depends on this.
  Define the name based on the subject (e.g., Infrastructure, Physical, Legal, Biological).

Layer 2: [OPERATIONAL LAYER]
  The working environment — requires Layer 1 to function.
  Where the actual work is done.
  Define the name based on the subject (e.g., Workspace, Digital, Process, Organisational).

Layer 3: [ENHANCEMENT LAYER]
  Amplifies and optimises — requires Layers 1+2 to be useful.
  Without the layers below it, this layer cannot add value.
  Define the name based on the subject (e.g., Intelligence, Cultural, Strategic, Cognitive).
```

**Why this order is always causal:**
- You cannot operate Layer 2 without Layer 1 running.
- Layer 3 amplifies nothing without Layer 2 to operate in.
- The structure is universal — only the names change per subject.

### Subject-Specific Layer Names (defined in CLAUDE.md per subject)
For the active subject (AI Orchestration / COE_AI_ORCH), the 3 layers are:
- **Layer 1 = INFRASTRUCTURE** (Python, Agno, Anthropic API, compute)
- **Layer 2 = WORKSPACE** (Cursor, Git, ILE, ClickUp)
- **Layer 3 = INTELLIGENCE** (Claude LLM, YFinance, Exa, prompts, community)

For other subjects, define equivalent layer names before generating Page 4.

---

## Row Structure (all Topics)

- **N rows — one component per row**, ordered Layer 1 first, Layer 3 last
- Row labels: `[LAYER1_NAME].{n}`, `[LAYER2_NAME].{n}`, `[LAYER3_NAME].{n}` — sequential within each layer
- Components are specific to THIS Topic's requirements (derived from its Principles)
- Components in deeper Topics go deeper than Topic 0 (which is overview-level)

### Component count guide
- Topic 0: ~6–9 rows (2–3 per layer, overview depth)
- Topics 1–5: more specific, more detailed components for that Topic's system

---

## Causal Logic

For each component row, answer the 16 canonical questions AS IF that component is the subject:
- Col 1: Why does THIS component matter for this Topic's system?
- Col 3: How does it work (install, configure, connect)?
- Col 4: What drives this component to work well?
- Col 10: What ultimately blocks this component from working?
- Etc.

---

## Format

```markdown
# Topic {X}. {Topic Name} — Page 4: Components
*Phase C. Organise Information | Topic: {X}. {Topic Name} | Page: 4. Components*
*Subject: AI Orchestration / Engineering | UDO: ...*

---

## Column Key
[standard 16-question key]

---

## Table

| Row | 1 · Relevance | 2 · Introduction | 3 · EOP | 4 · UDS | 5 · Success Mechanism | 6 · EPS | 7 · Tools (UES) | 8 · Environment (UES) | 9 · Failure Actions | 10 · UBS | 11 · Failure Mechanism | 12 · Risky Principles | 13 · Risky Tools | 14 · Risky Environment | 15 · What Else? | 16 · Next Steps |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **[LAYER1].1** | | | | | | | | | | | | | | | | |
| **[LAYER1].2** | | | | | | | | | | | | | | | | |
| **[LAYER2].1** | | | | | | | | | | | | | | | | |
| **[LAYER3].1** | | | | | | | | | | | | | | | | |
```

---

## Rules

- Always order: Layer 1 rows first → Layer 2 rows → Layer 3 rows.
- Define the 3 layer names for your subject BEFORE generating this page (check CLAUDE.md or subject notes).
- Each component derives from the Principles in Page 3 — every component must be traceable to at least one principle.
- Components within a layer are MECE — no overlap, no gaps.
- Do not include components not required by this Topic's Principles.
- Deeper Topics = more specific/granular components than Topic 0.
