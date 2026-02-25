---
phase: implementation
title: ILE COE Map — Representation of LTC COE Hierarchical Map (T-401)
description: Defines and implements the ILE's representation of the LTC COE hierarchy for sync and user→ClickUp mapping. Noun-AC6.
feature: integrated-learning-environment
task: T-401
---

# COE Map Representation (T-401)

**Purpose:** The ILE has a **defined representation** of the **LTC COE hierarchical map** so that user learning can be mapped to the correct ClickUp location (Topic → that user's Personal Learning Area). Noun-AC6. Used by T-402 (user→ClickUp mapping) and T-403 (sync).

**Single source of truth (T-411):** The canonical COE hierarchy and structure are defined **only** in **`config/coe-map.yaml`**. Other docs (design, requirements, sync, mapping, tree map) reference this file or this doc and do not re-state the full hierarchy; see T-411.

**Hierarchy (from Requirements; authoritative schema in config):**

| Level | Description |
|-------|-------------|
| **COE** | Company / COE root (e.g. LTC COE). |
| **Chapter** | Chapter within an Area (e.g. Chapter 1 UBS, Chapter 2 UDS). Same 6 chapters as Learning Map: 0. Overview & Summary, 1. UBS, 2. UDS, 3. EPS, 4. UES, 5. EOP. |
| **Topic** | Topic within a Chapter (e.g. Topic 0. Overview, Topic 1. Ultimate Blockers). 6 topics per chapter. |
| **Topic Members' Learning Area** | The container (e.g. ClickUp list or folder) that holds **each member's Personal Learning Area** for that topic. |
| **Personal Learning Area (PLA)** | One per member per topic. Where that user's learning content for that topic lives (e.g. ClickUp folder/item). Naming: `[COE AREA]_[MEMBER]_[CHAPTER] - [TOPIC] - Personal Learning Area`. |

**Individual Learning Book vs COE map:** The **Learning Book** (`learning-book/`) is one person's content (one Area, e.g. COE_DS); the **COE map** is the company-side structure (COE → Chapter → Topic → Topic Members' Learning Area → each member's PLA). Sync maps from Learning Book paths to COE map locations. See `learning-book-tree-map.md` § Company vs Individual.

**Storage:** The representation is stored as a **config or repo file** so the Agent (and future sync logic) can read it. Canonical path: **`config/coe-map.yaml`** (or `config/coe-map.json`). Schema: COE → Areas (optional) → Chapters → Topics; each Topic has a **topic_members_learning_area** (e.g. ClickUp list ID or name) and **personal_learning_areas** (member_id → ClickUp location or identifier). See `config/coe-map.yaml` for the stub.

**Usage:** T-402 will consume this map to resolve (user, subject, chapter, topic) → ClickUp location (that user's PLA for that topic). T-403 will use it to sync Learning Book content to the correct place.

**Evidence (T-401):** This doc defines the hierarchy and storage; `config/coe-map.yaml` is the implemented representation. Noun-AC6.

---

## Risks & assumptions

*The COE map is the **source of truth** for hierarchy and user→location; it does not validate that ClickUp actually has that structure. Mapping and sync risks (structural mismatch, naming errors, missing user/config, ClickUp drift, page-level mismatch) are documented and mitigated in **`ile-user-clickup-mapping.md` § Risks & edge cases** and **`ile-sync-clickup.md` § Pre-sync validation & fail-safe behaviour**. Assumption: ClickUp Space is created and maintained (by ops or template) to match the COE map; when it does not, sync must fail safe and report.*

**Cross-references:** Design §2.3 COE map | Requirements Noun-AC6, Noun-AC7, Noun-AC8 | `learning-book-tree-map.md` § Company tree | T-402, T-403 | `ile-user-clickup-mapping.md` § Risks & edge cases | `ile-sync-clickup.md`.
