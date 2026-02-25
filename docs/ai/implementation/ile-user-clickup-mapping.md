---
phase: implementation
title: ILE User → ClickUp Location Mapping (T-402)
description: Defines how the ILE maps a single user's learning to that user's respective location on ClickUp (Topic → Personal Learning Area). Noun-AC7.
feature: integrated-learning-environment
task: T-402
---

# User → ClickUp Mapping (T-402)

**Purpose:** The ILE **can map** a single user's learning to **that user's respective location on ClickUp** (correct Topic → that user's Personal Learning Area). Noun-AC7. Consumed by T-403 (sync).

**Inputs:** `user_id`, `area_id`, `chapter_id`, `topic_id` (e.g. `LONG_N`, `COE_DS`, `1`, `0`).

**Procedure:**

1. **Read COE map:** Load `config/coe-map.yaml` (see `ile-coe-map.md`).
2. **Lookup:** Find the area by `area_id`, then the chapter by `chapter_id`, then the topic by `topic_id`. Read `personal_learning_areas[user_id]` for that topic.
3. **Output:**
   - If `personal_learning_areas[user_id]` is set (e.g. a ClickUp list/folder ID or URL), that is the user's ClickUp location for that topic → **use it**.
   - Else **fallback:** Use the **canonical PLA name** per `learning-book-tree-map.md` § Naming Convention (Personal Learning Area):  
     `[COE AREA]_[MEMBER]_[CHAPTER ID]. [CHAPTER NAME] - [TOPIC ID]. [TOPIC NAME] - Personal Learning Area`.  
     Example: `[COE DS]_[LONG N.]_1. DATA SCIENCE UBS - 0. OVERVIEW & SUMMARY - Personal Learning Area`. Sync (T-403) or ClickUp API can resolve this name to the actual folder/item.

**Script:** `scripts/resolve-user-clickup-location.sh` implements the mapping: given (user_id, area_id, chapter_id, topic_id), it prints the canonical PLA name (and, when config contains ClickUp IDs, can be extended to print that ID). Run from repo root:  
`./scripts/resolve-user-clickup-location.sh <user_id> <area_id> <chapter_id> <topic_id>`.

**Evidence (T-402):** This doc defines the procedure; `config/coe-map.yaml` holds per-topic `personal_learning_areas` keyed by user; the script produces deterministic output for (user, area, chapter, topic). Noun-AC7.

---

## Risks & edge cases

*Approach 2: Success = efficient and scalable management of failure risks. These risks affect mapping and sync (T-403); they should be validated or mitigated before/during sync.*

| Risk | Description | Mitigation / behaviour |
|------|-------------|------------------------|
| **Structural mismatch** | Company ClickUp does **not** have the expected hierarchy (Area → Chapter → Topic → Topic Members' Learning Area → Personal Learning Area; hierarchy defined in **`config/coe-map.yaml`**, see `ile-coe-map.md`) or is missing folders that match the user's Learning Book tree. | **Pre-sync check (T-403):** Validate that the target location exists in ClickUp (by ID or by resolving canonical PLA name). If not: **fail safe** — do not write to a wrong place; report "Target PLA not found for (area, chapter, topic); ensure ClickUp structure matches COE map" and optionally list expected path. Rely on a **test Space** first so production COE is not corrupted. |
| **Naming / identity errors** | Identifiers are wrong or inconsistent: typo in `user_id`, `area_id`, or config; different naming convention in ClickUp (e.g. "COE DS" vs "COE_DS"); canonical name does not match any ClickUp folder. | **Deterministic IDs:** Prefer ClickUp list/folder **IDs** in `personal_learning_areas[user_id]` over name resolution when available. **Validation:** Mapping script or sync step should validate that (user_id, area_id, chapter_id, topic_id) exist in `config/coe-map.yaml` before resolving; unknown ids → clear error (e.g. "area_id X not in coe-map"). **Convention:** Document canonical PLA naming in one place (`learning-book-tree-map.md`) and use it consistently; any name-based lookup in ClickUp must be explicit (e.g. "match by name" vs "match by ID"). |
| **User not in config** | `personal_learning_areas` has no entry for this user for this topic; or user is new and not in the COE map at all. | **Fallback:** Use **canonical PLA name** (current behaviour). Sync (T-403) can attempt to create the PLA by that name in the correct parent, or report "No PLA for user X at (area, chapter, topic); add to coe-map or create in ClickUp first." Do not guess a different user's location. |
| **Missing Area / Chapter / Topic in config** | Learning Book has an Area, Chapter, or Topic that is not present in `config/coe-map.yaml` (e.g. new subject or new chapter). | **Lookup fails:** Resolve only (area, chapter, topic) that exist in the COE map. If a Learning Book path has no corresponding entry in coe-map → report "No COE map entry for (area, chapter, topic); add to config/coe-map.yaml or skip sync for this node." Do not invent a ClickUp location. |
| **ClickUp structure drift** | ClickUp folders/lists were renamed, moved, or deleted; IDs in config point to removed items. | **T-403:** Sync step should verify target (e.g. GET by ID) before write. If ID invalid or missing → report and optionally fall back to "create by canonical name" in the correct parent, or require operator to update coe-map with new IDs. |
| **Page-level mismatch** | User's Learning Book has a **Page** (e.g. Page 7 Topic Distilled Understanding) but ClickUp PLA structure does not have a matching page/section. | **Scope of T-402:** Mapping is Topic → PLA (one location per topic). Page-level mapping (which page within the PLA) is a separate concern for T-403 (e.g. sync doc content to a specific ClickUp doc or section). If ClickUp PLA has no matching page structure, T-403 should define behaviour (e.g. single doc per PLA, or create sub-items by page). Document in T-403. |

**Summary:** The mapping (T-402) produces a **deterministic** target (canonical name or config ID). Sync (T-403) must **validate** that the target exists (or explicitly create it by convention) and **fail safe** (no write to wrong or unknown location). Use a dedicated **test ClickUp Space** to validate structure and naming before touching production COE. **T-403 implementation:** See `ile-sync-clickup.md` for pre-sync validation, dry-run mode, and fail-safe error behaviour.

**Cross-references:** Design §2.3 COE map | Requirements Noun-AC7, Noun-AC8 | `ile-coe-map.md` | `ile-sync-clickup.md` § Pre-sync validation & fail-safe behaviour | `learning-book-tree-map.md` § Naming Convention | T-401, T-403 | `ile-minimal-flow.md` § Mapping personal Learning Book ↔ company COE.
