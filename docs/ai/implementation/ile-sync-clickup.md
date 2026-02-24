---
phase: implementation
title: ILE Sync Learning Book → ClickUp (T-403)
description: Sync (or stub) of the user's Book to the company's ClickUp in the correct place using the COE map and user mapping. Noun-AC8. De-risking: pre-sync validation, dry-run, fail-safe errors.
feature: integrated-learning-environment
task: T-403
---

# Sync Learning Book → ClickUp (T-403)

**Purpose:** The ILE supports (or will support) **syncing** the user's learning from their Book **to the company's ClickUp** in the correct place, using the COE map and user mapping. Noun-AC8. ScalAdv-AC4.

**Inputs:** User's Learning Book path(s) (e.g. `learning-book/COE_DS/...`), `user_id`, and optionally a scope (e.g. one file, one topic, or full Area). **Output:** Content written to the correct ClickUp location (that user's PLA for the corresponding area/chapter/topic), or a clear report when sync is skipped or failed.

**Dependencies:** T-401 (COE map), T-402 (user→ClickUp mapping). Sync uses `config/coe-map.yaml` and the mapping procedure in `ile-user-clickup-mapping.md` to resolve (user, area, chapter, topic) → target ClickUp location.

---

## Pre-sync validation & fail-safe behaviour

*Aligned with **`ile-user-clickup-mapping.md` § Risks & edge cases**. Sync must not write to a wrong or unknown location.*

| Step | What to do | On failure |
|------|------------|------------|
| **1. Resolve target** | For each Learning Book path to sync, derive (area_id, chapter_id, topic_id) from the path; resolve (user_id, area_id, chapter_id, topic_id) → ClickUp location via T-402 (script or procedure). | If (area, chapter, topic) not in `config/coe-map.yaml`: **stop** for that node; report: *"No COE map entry for (area, chapter, topic); add to config/coe-map.yaml or skip sync for this node."* Do not invent a location. |
| **2. Validate target exists (when ClickUp API available)** | Before writing, verify the target location exists in ClickUp (e.g. GET by ID from `personal_learning_areas[user_id]`, or resolve canonical PLA name to a folder/list). | If target not found: **fail safe** — do not write; report: *"Target PLA not found for (area, chapter, topic); ensure ClickUp structure matches COE map."* Optionally list the expected canonical path. Use a **test Space** first so production COE is not corrupted. |
| **3. Id drift** | If using a stored ClickUp ID, verify it still exists (e.g. GET by ID). | If ID invalid or missing: report and optionally fall back to "create by canonical name" in the correct parent, or require operator to update coe-map with new IDs. |

**Dry-run mode:** Sync implementation **must** support a **dry-run** (or equivalent): compute all (Learning Book path → ClickUp location) and **log or return** the list **without** performing any ClickUp API write. This allows validation of mapping and structure with minimal risk.

**Clear error messages:** Every failure path above must produce a **deterministic, actionable message** (e.g. "Target PLA not found for COE_DS / 1 / 0; expected: [COE DS]_[LONG N.]_1. DATA SCIENCE UBS - 0. OVERVIEW & SUMMARY - Personal Learning Area"). No silent skip and no write to a guessed location.

---

## Page-level behaviour

*From `ile-user-clickup-mapping.md` § Risks: Page-level mismatch.*

Mapping (T-402) is **Topic → PLA** (one location per topic). **Page-level** (e.g. Page 0–5, Page 7 within a topic) is a sync policy choice:

- **Option A:** One ClickUp doc per PLA (topic); all pages in that topic merged or appended into that doc.
- **Option B:** One ClickUp doc (or sub-item) per page within the PLA; structure must exist in ClickUp or be created by convention.

T-403 implementation (or stub) should **document** which option is used. If ClickUp PLA has no matching page structure, do not guess; either create by convention (e.g. sections or sub-items) or report and sync at topic level only.

---

## Stub vs full implementation

- **Stub:** Document this procedure and the validation steps above; provide a script or command that performs **dry-run only** (resolve paths → list of (source path, target ClickUp location) with no API call). Evidence for Noun-AC8: "Sync to ClickUp implemented or stubbed; correct place per COE/User mapping."
- **Full:** Implement actual ClickUp API calls (create/update doc or folder) after pre-sync validation and optional dry-run; respect rate limits and user approval (per contract: "on approval, sync to ClickUp if configured").

**Stub implementation (T-403):** **Dry-run script:** `scripts/sync-learning-book-to-clickup-dryrun.sh` — takes `user_id` and optional `learning-book_root` (default `learning-book`), discovers topic `.md` files under phase C (Organise Information), derives (area_id, chapter_id, topic_id) from each path, resolves to ClickUp PLA via `scripts/resolve-user-clickup-location.sh`, and prints `source_path -> clickup_pla_name` with **no ClickUp API call**. Run from repo root: `./scripts/sync-learning-book-to-clickup-dryrun.sh <user_id> [learning-book_root]`.

**Page-level (stub):** Option A — one ClickUp doc per PLA (topic); page-level sync (which page within the PLA) is deferred to full implementation.

---

**Cross-references:** Design §2.3 COE map | Requirements Noun-AC8, ScalAdv-AC4 | `ile-coe-map.md` | `ile-user-clickup-mapping.md` § Procedure & § Risks & edge cases | T-401, T-402 | `ile-effective-learning-contract.md` (sync on approval).
