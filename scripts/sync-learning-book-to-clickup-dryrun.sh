#!/usr/bin/env bash
# T-403: Dry-run only — list Learning Book path → ClickUp PLA location. No ClickUp API calls (Noun-AC8 stub).
# T-404: learning_book_root configurable via ILE_LEARNING_BOOK_ROOT or config/ile.yaml (learning_book_root).
# Run from repo root: ./scripts/sync-learning-book-to-clickup-dryrun.sh <user_id> [learning-book_root]
# Example: ./scripts/sync-learning-book-to-clickup-dryrun.sh LONG_N learning-book

set -e
if [ $# -lt 1 ]; then
  echo "Usage: $0 <user_id> [learning-book_root]" >&2
  echo "Example: $0 LONG_N learning-book" >&2
  echo "Env: ILE_LEARNING_BOOK_ROOT overrides default learning-book when [learning-book_root] omitted." >&2
  exit 1
fi
USER_ID="$1"
ROOT="${2:-${ILE_LEARNING_BOOK_ROOT:-learning-book}}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
RESOLVE_SCRIPT="$SCRIPT_DIR/resolve-user-clickup-location.sh"

if [ ! -d "$REPO_ROOT/$ROOT" ]; then
  echo "No COE map entry or missing root: $ROOT (expected under $REPO_ROOT)" >&2
  exit 1
fi

# Find topic .md files under phase C (Organise Information) per learning-book structure
find "$REPO_ROOT/$ROOT" -type f -name "*.md" \
  -path "*C. Organise Information*" \
  ! -path "*/README.md" \
  ! -path "*A. Subject Roadmap*" \
  2>/dev/null | sort | while read -r abspath; do
  relpath="${abspath#$REPO_ROOT/}"
  # Parse: learning-book/COE_DS/C. Organise Information/1. UBS/1. UBS - 0. Overview & Summary.md
  # area = second path component, chapter = first number in folder name, topic = first number in filename (after " - " or leading)
  area_id=""
  chapter_id=""
  topic_id=""
  rest="$relpath"
  # Strip leading learning-book/ or ROOT/
  rest="${rest#$ROOT/}"
  # First component = area_id
  area_id="${rest%%/*}"
  rest="${rest#*/}"
  # Skip "C. Organise Information"
  rest="${rest#*/}"
  # Next = chapter folder (e.g. "1. UBS" or "0. Overview & Summary")
  chapter_folder="${rest%%/*}"
  rest="${rest#*/}"
  # Chapter id = leading digits from folder name
  chapter_id="${chapter_folder%%[!0-9]*}"
  [ -z "$chapter_id" ] && chapter_id="0"
  # Rest is filename (e.g. "1. UBS - 0. Overview & Summary.md")
  filename="${rest##*/}"
  # Topic id: "X. ... - Y. ..." -> Y; "0. Overview & Summary.md" -> 0
  if [[ "$filename" =~ -\ ([0-9])\. ]]; then
    topic_id="${BASH_REMATCH[1]}"
  else
    topic_id="${filename%%[!0-9]*}"
    [ -z "$topic_id" ] && topic_id="0"
  fi
  clickup_loc="$("$RESOLVE_SCRIPT" "$USER_ID" "$area_id" "$chapter_id" "$topic_id" 2>/dev/null)" || clickup_loc="(resolve failed for $area_id $chapter_id $topic_id)"
  echo "$relpath -> $clickup_loc"
done
