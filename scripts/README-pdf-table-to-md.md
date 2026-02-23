# PDF table → Markdown

Script: **`pdf_table_to_md.py`**

Converts a PDF that contains tables into a single Markdown file with **correct pipe tables**: one cell per column, no merged cells, no missing rows. Preserves integrity of the PDF/ClickUp table.

## Install

```bash
pip install -r scripts/requirements-pdf.txt
```

## Usage

```bash
# Output: same path as PDF with .md extension
python scripts/pdf_table_to_md.py path/to/file.pdf

# Custom output path (e.g. overwrite canonical template)
python scripts/pdf_table_to_md.py path/to/D-distilled-understanding.pdf -o templates/D-distilled-understanding-full.md
```

## Options

| Option | Description |
|--------|-------------|
| `-o`, `--output` | Output .md path |
| `--no-intro` | Do not extract intro text from the first page |
| `--strategy` | Table detection: `lines` (default), `text`, or `lines_strict`. Use `text` if the PDF has no visible grid lines |

## Example: refresh D. Distilled Understanding template

From repo root:

```bash
pip install -r scripts/requirements-pdf.txt
python scripts/pdf_table_to_md.py "/Users/longhnguyen/Downloads/[OWNER]_SUBJECT NAME - D. DISTILLED UNDERSTANDING.pdf" -o templates/D-distilled-understanding-full.md
```

Replace the PDF path with your actual file path.
