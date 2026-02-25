#!/usr/bin/env bash
# T-408: Integration smoke test for sync pipeline (SustainAdj-AC5).
# Runs sync-learning-book-to-clickup-dryrun.sh, validates output format (path -> PLA),
# and checks that every Learning Book file maps to a valid PLA (no "resolve failed").
# Run from repo root. Exit 0 if pass, 1 if fail (enumerated issues).
# Usage: ./scripts/smoke-test-sync-dryrun.sh [user_id] [learning-book_root]

set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
DRYRUN="$SCRIPT_DIR/sync-learning-book-to-clickup-dryrun.sh"
USER_ID="${1:-LONG_N}"
ROOT="${2:-${ILE_LEARNING_BOOK_ROOT:-learning-book}}"

if [ ! -x "$DRYRUN" ]; then
  echo "FAIL: missing or not executable: $DRYRUN"
  exit 1
fi

# Run dry-run and capture output
output="$("$DRYRUN" "$USER_ID" "$ROOT" 2>&1)" || true
issues=()
line_num=0

while IFS= read -r line; do
  line_num=$((line_num + 1))
  # Expected format: relpath -> clickup_location
  if [[ "$line" != *" -> "* ]]; then
    # Allow empty lines or script stderr (e.g. usage) only if no path lines expected
    [[ -z "$line" ]] && continue
    issues+=("Line $line_num: invalid format (expected 'path -> PLA'): $line")
    continue
  fi
  right="${line#* -> }"
  if [[ "$right" == "(resolve failed"* ]]; then
    issues+=("Line $line_num: file does not map to valid PLA in COE map: $line")
  fi
done <<< "$output"

if [ ${#issues[@]} -gt 0 ]; then
  echo "FAIL: smoke test (sync dry-run output validation)"
  for i in "${issues[@]}"; do
    echo "  $i"
  done
  exit 1
fi

# If dry-run produced no lines (e.g. no C. Organise Information .md files), that's valid
echo "PASS: sync dry-run output format valid; all Learning Book files map to valid PLA in config/coe-map.yaml"
