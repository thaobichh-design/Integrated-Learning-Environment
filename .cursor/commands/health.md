---
description: Run ILE system health check (T-407, SustainAdj-AC4).
---

# UTILITY: HEALTH (System health check)

**Purpose:** Validate in one pass that the ILE is set up correctly before a learning session (T-407, SustainAdj-AC4).

**Action:** Run the health check script from the repo root and report the output to the User.

1. **Execute:** `python3 scripts/health_check.py` (from project root).
2. **Report:** Output is either **"system is healthy"** or an enumerated list of issues (config parse/schema, templates, learning-book structure, A exists, rules present).
3. **Do not modify** any config or files; this is read-only validation.

**Reference:** `docs/ai/implementation/` — config schema: `ile-configurable-mapping.md`, `ile-coe-map.md`; structure: `scripts/check-learning-book-structure.sh`; templates: `entry-point-to-template-mapping.md` § Page-type resolution.
