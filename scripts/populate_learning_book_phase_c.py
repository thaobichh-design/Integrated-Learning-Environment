#!/usr/bin/env python3
"""Pre-populate Phase C (Organise Information) with full 7-page topic files.

Generates 36 topic files (6 chapters × 6 topics) under learning-book/{subject}/C. Organise Information/.
Each file contains all 7 page sections (Page 0–5 + Page 7) from the canonical templates so the user
can start learning at any entry point without waiting for file creation.

Usage:
  python scripts/populate_learning_book_phase_c.py [subject] [--templates PATH] [--learning-book PATH]
  Default subject: COE_DS. Paths default to repo root (templates/, learning-book/).

Requires: no extra deps. Run from repo root or set paths.
"""

import argparse
import re
from pathlib import Path


# From learning-book-tree-map.md: chapter folder names and topic display names
CHAPTER_FOLDERS = [
    "0. Overview & Summary",
    "1. UBS",
    "2. UDS",
    "3. EPS",
    "4. UES",
    "5. EOP",
]

TOPIC_NAMES = [
    "Overview & Summary",
    "Ultimate Blockers",
    "Ultimate Drivers",
    "Principles",
    "Components",
    "Steps to Overcome",
]

# Page id -> (display name, template filename)
PAGES = [
    (0, "Overview & Summary", "0-overview-and-summary.md"),
    (1, "Ultimate Blockers", "page-1-ultimate-blockers.md"),
    (2, "Ultimate Drivers", "page-2-ultimate-drivers.md"),
    (3, "Principles", "page-3-principles.md"),
    (4, "Components", "page-4-components.md"),
    (5, "Steps to Overcome", "page-5-steps-to-overcome.md"),
    (7, "Topic Distilled Understanding", "page-7-topic-distilled-understanding.md"),
]


def template_body(content: str) -> str:
    """Extract body from template: from first '## ' to end (keeps Target table format + table)."""
    lines = content.splitlines()
    start = 0
    for i, line in enumerate(lines):
        if line.strip().startswith("## "):
            start = i
            break
    return "\n".join(lines[start:]).strip()


def load_templates(templates_root: Path) -> dict[int, str]:
    """Load each page template and return {page_id: body}."""
    out = {}
    for page_id, _name, filename in PAGES:
        path = templates_root / filename
        if not path.exists():
            raise FileNotFoundError(f"Template not found: {path}")
        body = template_body(path.read_text(encoding="utf-8"))
        out[page_id] = body
    return out


def build_topic_file(
    ch: int,
    topic: int,
    chapter_folder: str,
    topic_name: str,
    templates: dict[int, str],
) -> str:
    """Build full markdown content for one topic file (7 pages)."""
    title = f"{chapter_folder} - {topic}. {topic_name}"
    lines = [
        f"# {title} — Effective Data Science (Chapter {ch})",
        "",
        f"*Phase C. Organise Information | Chapter {chapter_folder} | Topic {topic}. {topic_name} | Entry point: ({ch}, {topic}).*",
        "",
        "---",
        "",
    ]
    for page_id, page_display_name, _ in PAGES:
        body = templates[page_id]
        lines.append(f"## Page {page_id}: {page_display_name}")
        lines.append("")
        lines.append(body)
        lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines).rstrip()


def main() -> None:
    ap = argparse.ArgumentParser(description="Populate Phase C with full 7-page topic files.")
    ap.add_argument("subject", nargs="?", default="COE_DS", help="Subject/area id (e.g. COE_DS)")
    ap.add_argument("--templates", type=Path, default=None, help="Templates directory (default: repo templates/)")
    ap.add_argument("--learning-book", type=Path, default=None, help="Learning book root (default: repo learning-book/)")
    args = ap.parse_args()

    repo = Path(__file__).resolve().parent.parent
    templates_root = args.templates or repo / "templates"
    lb_root = args.learning_book or repo / "learning-book"
    phase_c = lb_root / args.subject / "C. Organise Information"
    if not phase_c.is_dir():
        raise SystemExit(f"Phase C directory not found: {phase_c}")

    templates = load_templates(templates_root)
    created = 0
    for ch in range(6):
        chapter_folder = CHAPTER_FOLDERS[ch]
        chapter_dir = phase_c / chapter_folder
        chapter_dir.mkdir(parents=True, exist_ok=True)
        for topic in range(6):
            topic_name = TOPIC_NAMES[topic]
            content = build_topic_file(ch, topic, chapter_folder, topic_name, templates)
            filename = f"{chapter_folder} - {topic}. {topic_name}.md"
            out_path = chapter_dir / filename
            out_path.write_text(content, encoding="utf-8")
            created += 1
    print(f"Created {created} topic files under {phase_c}")


if __name__ == "__main__":
    main()
