#!/usr/bin/env python3
"""
Convert a PDF containing tables into a Markdown file that preserves:
- Every column and row (no merging; one cell per pipe-delimited column)
- Cell content (newlines → <br>; pipes escaped)

Usage:
  python scripts/pdf_table_to_md.py path/to/file.pdf
  python scripts/pdf_table_to_md.py path/to/file.pdf -o output.md

Requires: pip install pdfplumber
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def escape_cell(text: str | None) -> str:
    """Prepare cell text for markdown: escape | and newlines."""
    if text is None:
        return ""
    s = str(text).strip()
    s = s.replace("|", "\\|")
    s = s.replace("\n", "<br>").replace("\r", "")
    return s


def normalize_table(rows: list[list[str | None]]) -> list[list[str]]:
    """Ensure every row has the same number of columns (fill with empty string)."""
    if not rows:
        return []
    max_cols = max(len(r) for r in rows)
    out = []
    for row in rows:
        padded = [escape_cell(c) for c in row]
        while len(padded) < max_cols:
            padded.append("")
        out.append(padded[:max_cols])
    return out


def table_to_md(rows: list[list[str]]) -> str:
    """Turn a list of rows (same length) into a markdown pipe table."""
    if not rows:
        return ""
    ncols = len(rows[0])
    lines = []
    for i, row in enumerate(rows):
        # Ensure row length
        r = (row + [""] * ncols)[:ncols]
        lines.append("| " + " | ".join(r) + " |")
        if i == 0:
            lines.append("| " + " | ".join("---" for _ in range(ncols)) + " |")
    return "\n".join(lines)


def extract_text_before_tables(page) -> str:
    """Get body text that appears before the first table (e.g. title, intro)."""
    try:
        return (page.extract_text() or "").strip()
    except Exception:
        return ""


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convert PDF tables to a single Markdown file preserving columns and rows."
    )
    parser.add_argument(
        "pdf_path",
        type=Path,
        help="Path to the PDF file",
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=None,
        help="Output .md path (default: same name as PDF with .md)",
    )
    parser.add_argument(
        "--no-intro",
        action="store_true",
        help="Do not extract intro text from first page",
    )
    parser.add_argument(
        "--strategy",
        choices=["lines", "text", "lines_strict"],
        default="lines",
        help="Table detection: lines (default), text, or lines_strict",
    )
    args = parser.parse_args()

    pdf_path = args.pdf_path.resolve()
    if not pdf_path.is_file():
        print(f"Error: not a file: {pdf_path}", file=sys.stderr)
        return 1

    out_path = args.output
    if out_path is None:
        out_path = pdf_path.with_suffix(".md")
    out_path = out_path.resolve()

    try:
        import pdfplumber
    except ImportError:
        print("Error: pdfplumber is required. Run: pip install pdfplumber", file=sys.stderr)
        return 1

    table_settings = {
        "vertical_strategy": args.strategy,
        "horizontal_strategy": args.strategy,
        "snap_tolerance": 4,
        "join_tolerance": 4,
    }

    parts: list[str] = []
    first_page_intro_done = False

    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            tables = page.extract_tables(table_settings=table_settings)

            # Optional: intro text from first page only (before first table)
            if not args.no_intro and page_num == 1 and tables:
                intro = extract_text_before_tables(page)
                if intro:
                    # Heuristic: keep only lines that look like title/intro (short, before table content)
                    intro_lines = intro.split("\n")[:20]
                    intro_trim = "\n".join(l for l in intro_lines if len(l.strip()) > 0)
                    if intro_trim and len(intro_trim) < 4000:
                        parts.append(intro_trim)
                        parts.append("")
            if not tables:
                continue

            for table in tables:
                if not table:
                    continue
                normalized = normalize_table(table)
                if normalized:
                    parts.append(table_to_md(normalized))
                    parts.append("")

    if not parts:
        print("Warning: no content extracted.", file=sys.stderr)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(parts).strip() + "\n", encoding="utf-8")
    print(f"Wrote: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
