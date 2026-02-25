# D. Distilled Understanding — Template spec (XLSX canonical)

**Source of truth:** `templates/D-distilled-understanding-full.xlsx`

The Founder has manually fixed the workbook. The Agent must treat this file as the canonical template and must not regenerate structure from PDF/MD unless explicitly requested.

**Optional read-only duplicate:** `templates/D-distilled-understanding-full.json` (same content as xlsx; keys = sheet names, values = arrays of row arrays).

---

## 1. Canonical workbook contract

### Required sheets
- `PDF_RAW_TABLE` (canonical full table data)
- `Page-0`
- `Page-1`
- `Page-2`
- `Page-3`
- `Page-4`
- `Page-5`
- `Page-6`
- `PAGE_MAPPING_INDEX`
- `ROW_MARKER_INDEX`
- `README_AGENT`

### Safety rules (must follow)
- Never mutate columns, headers, or sheet names automatically.
- Never infer new columns from markdown.
- If any mapping is ambiguous, stop and ask the Founder.
- Preserve source traceability using `SOURCE_RAW_ROW` and `MARKER_COL_INDEX_0_BASED`.

---

## 2. Agent read order

When the Agent needs this template, read in this order:

1. `README_AGENT`
2. `PAGE_MAPPING_INDEX`
3. `Page-0` … `Page-6`
4. `ROW_MARKER_INDEX` (for diagnostics)
5. `PDF_RAW_TABLE` (canonical fallback)

---

## 3. Mapping semantics (page 0–5 and page 6)

The page sheets are already normalized from the full table and should be used directly.

- **Page-0:** rows whose sub-topic marker is `0.*`
- **Page-1:** rows whose sub-topic marker is `X.1`
- **Page-2:** rows whose sub-topic marker is `X.2`
- **Page-3:** rows whose sub-topic marker is `X.3`
- **Page-4:** rows whose sub-topic marker is `X.4`
- **Page-5:** rows whose sub-topic marker is `X.5` or `X.6`
- **Page-6:** rows whose sub-topic marker is `X.0` to `X.6` (topic distilled slice)

Where `X` is the topic family (e.g. 1, 2, 3, 4, 5).

---

## 4. Template alignment with existing page files

Use these markdown templates only as output format contracts:
- `templates/page-1-ultimate-blockers.md`
- `templates/page-2-ultimate-drivers.md`
- `templates/page-3-principles.md`
- `templates/page-4-components.md`
- `templates/page-5-steps-to-overcome.md`
- `templates/page-7-topic-distilled-understanding.md`

The data source must remain the XLSX sheets above.

---

## 5. Deterministic execution checklist

- [ ] Read `templates/D-distilled-understanding-full.xlsx` first.
- [ ] Use `Page-0`…`Page-6` as structured inputs.
- [ ] Keep `SOURCE_RAW_ROW` references intact in any transformed output.
- [ ] Do not add/drop columns without Founder approval.
- [ ] If a row cannot be mapped safely, mark as blocked and ask the Founder.
