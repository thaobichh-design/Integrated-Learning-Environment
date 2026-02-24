---
phase: implementation
title: ILE Configurable Hierarchy, Templates, and ClickUp Space Mapping (T-404)
description: Hierarchy, templates, and ClickUp space mapping configurable (e.g. per workspace or mode) so the ILE pattern can be applied to other ClickUp spaces and different doc template sets. ScalAdj-AC4.
feature: integrated-learning-environment
task: T-404
---

# Configurable Mapping (T-404)

**Purpose:** The ILE pattern (Capture → Organise → Distill; template-driven; sync to a defined location) can be applied to **other ClickUp spaces** and **different doc template sets**. **Hierarchy**, **templates**, and **ClickUp space mapping** are **configurable** (e.g. per workspace or mode) so the same code drives other use cases (e.g. project spaces, sales, operations) with their own templates and ClickUp structure. ScalAdj-AC4.

**Configuration file:** **`config/ile.yaml`** (canonical). Schema:

| Key | Description | Default / example |
|-----|-------------|-------------------|
| **coe_map_path** | Path to COE/hierarchy map (used by user→ClickUp mapping and sync). | `config/coe-map.yaml` |
| **templates_path** | Template root (entry-point→template resolution; phase C page templates). | `templates` |
| **learning_book_root** | Learning Book root (sync dry-run, conversation→doc mapping). | `learning-book` |
| **clickup_space_id** | Optional ClickUp Space ID or sync target (for full sync; null = not set). | `null` |
| **mode** | Optional mode name (e.g. `coe`, `sales`) for named profiles. | unset |

**Per workspace:** Use a **different config file** for a different workspace or use case. Example: copy `config/ile.yaml` to `config/ile-sales.yaml`, set `coe_map_path: config/coe-map-sales.yaml`, `templates_path: templates-sales`, and point the workspace or runner to it (e.g. env `ILE_CONFIG=config/ile-sales.yaml`). Core integration (chat + memory + doc + template load + sync) unchanged; only config changes.

**Per mode:** Set **`ILE_MODE`** (or equivalent) to a mode name (e.g. `coe`, `sales`). Loader can then read `config/ile-{mode}.yaml` if it exists, else fall back to `config/ile.yaml`. Same idea: different hierarchy/templates/space per mode without code change.

**Usage:** Scripts and Agent should read paths from `config/ile.yaml` (or from env overrides: `ILE_COE_MAP_PATH`, `ILE_TEMPLATES_PATH`, `ILE_LEARNING_BOOK_ROOT`, `ILE_CLICKUP_SPACE_ID`) so that switching config or mode switches behaviour. Current scripts accept CLI args (e.g. `learning-book_root` in dry-run); documenting that these can be sourced from config/ile.yaml or env satisfies "configurable."

**Evidence (T-404):** This doc defines the configuration model; `config/ile.yaml` is the implemented schema. Hierarchy (COE map path), templates (template root), and ClickUp space mapping (optional space ID) are configurable via that file or per-workspace/per-mode config files. ScalAdj-AC4.

**Cross-references:** Design §1.3 (configurable hierarchy, templates, space) | Requirements ScalAdj-AC4 | `ile-coe-map.md` | `entry-point-to-template-mapping.md` | `ile-sync-clickup.md` | T-401, T-402, T-403.
