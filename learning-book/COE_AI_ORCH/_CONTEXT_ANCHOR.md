# COE_AI_ORCH — Context Anchor (Persistent Memory)
*Last updated: 2026-02-27 | Read this file at the start of every continuation session.*

---

## UDO
Build and master an OE System (AI Orchestration Engine) that any analyst/operator can use to build domain-specific UE systems. Effective = Sustainable, Efficient, Scalable. This is the system that builds systems — NOT a specific domain project.

## Structure
- 6 Topics (0-5) × 6 Pages (0-5) = 36 .md files
- Each page = ONE markdown table, as many rows as needed, 17 columns (1 label + 16 canonical questions)
- Pure markdown tables only (no HTML — doesn't render in Cowork sidebar)
- Column Key reference section above each table

## Topic Map
- 0. Overview & Summary — root level, overview depth
- 1. UBS — deep dive into the root UBS from Topic 0
- 2. UDS — deep dive into the root UDS from Topic 0
- 3. EPS — deep dive into the principles from Topic 0
- 4. UES — deep dive into the components/tools from Topic 0
- 5. EOP — deep dive into the procedure from Topic 0

## Notation
- UBS.UB = blocker that disables the UBS (works IN User's favour)
- UBS.UD = driver that drives UBS harder (works AGAINST User)
- UDS.UD = driver that enables UDS further (works IN User's favour)
- UDS.UB = blocker that blocks the UDS (works AGAINST User)
- Recursive: UBS.UB.UB, UBS.UB.UD, UBS.UD.UB, UBS.UD.UD, etc.
- DO NOT use UBS1, UBS2, UDS1, UDS2 — always dot-notation

## Page Structure Rules (Finalised 2026-02-27)

### Topic 0 (Overview & Summary)
| Page | Rows | Row label | Derives from |
|---|---|---|---|
| P0 Overview | 1 | Effective AI Orchestration | Root — no parent |
| P1 UBS | 1 | root UBS | P0 col 10 · UBS |
| P2 UDS | 1 | root UDS | P0 col 4 · UDS |
| P3 EPS | N (one per principle) | P1, P2, P3 ... | Harvest from P0+P1+P2 cols 6+12 |
| P4 UES | N (one per component) | INFRA.n, WORKSPACE.n, INTEL.n | Derives from P3 principles |
| P5 EOP | N (one per step) | STEP.1, STEP.2 ... | Links to P1+P2+P3+P4 |

### Topics 1–5 (Deep-Dive — same 6-page pattern)
| Page | Rows | Rule |
|---|---|---|
| P0 Overview | 1 (duplicate) | COPY parent page, do not regenerate. T1→T0.P1, T2→T0.P2, T3→T0.P3, T4→T0.P4, T5→T0.P5 |
| P1 UB layer | 3 | Row1=parent.UB (P0 col10), Row2=parent.UB.UB (Row1 col10), Row3=parent.UB.UD (Row1 col4) |
| P2 UD layer | 3 | Row1=parent.UD (P0 col4), Row2=parent.UD.UB (Row1 col10), Row3=parent.UD.UD (Row1 col4) |
| P3 EPS | N | Harvest all principles from P0+P1+P2 of THIS topic |
| P4 UES | N | Layered components for THIS topic (INFRA→WORKSPACE→INTEL) |
| P5 EOP | N | Sequential steps for THIS topic. Each links to P1/P2/P3/P4. |

## UES = 3 Causal Layers (Finalised)
- Infrastructure → Workspace → Intelligence (cannot skip layers)
- Row labels: INFRA.n, WORKSPACE.n, INTEL.n
- Each component must trace to at least one Principle from P3

## Key Rules (from User corrections)
1. EPS must derive DIRECTLY from UBS and UDS — not generic best practices
2. One blocker or driver per row — not greedy
3. Each row builds causally on the previous
4. Page 0 = overview level. Deeper topics go deeper. Do not front-load.
5. Present each page in sidebar → user reviews → challenges → approves → next page
6. Do NOT regenerate Topic 1-5 Page 0 — duplicate the file

## Frameworks
- Primary: Agno (Python)
- Secondary: CrewAI (Python) — evaluate at L4+
- IDE: Cursor | Model: Claude LLM

## Decisions Log
| Date | Scope | Decision |
|---|---|---|
| 2026-02-27 | P0 | Rewrite: EPS must derive from UBS/UDS not best practices |
| 2026-02-27 | P0 | Rewrite: UES = Infrastructure/Workspace/Intelligence causal layers |
| 2026-02-27 | P0 | Rewrite: One UBS.UB, UBS.UD, UDS.UD, UDS.UB only — was greedy |
| 2026-02-27 | All | CLAUDE.md created — auto-loads at session start |
| 2026-02-27 | All | Page structure rules finalised: T0 P1/P2 = 1 row; T1-5 P1/P2 = 3 rows |
| 2026-02-27 | All | UES confirmed = Environment + Tools. Each Topic = its own complete system. |
| 2026-02-27 | All | All 6 template files updated to pure markdown with correct derivation instructions |
| 2026-02-27 | T0.P0 | Page 0 revised to 1 row. UBS.UB/UD and UDS.UD/UB rows removed (too greedy for P0). |

## Current State
- CLAUDE.md: ✅ COMPLETE
- All 6 template files: ✅ UPDATED
- Topic 0, Page 0: ⏳ PENDING USER APPROVAL (revised, 1 row, pure markdown)
- Topic 0, Pages 1-5: ❌ Need rewrite to correct structure
- Topics 1-5: ❌ Not yet generated
- **Next action: User approves T0.P0 → generate T0.P1 (1 row UBS) → T0.P2 (1 row UDS) → T0.P3 → T0.P4 → T0.P5 → then Topics 1-5**
