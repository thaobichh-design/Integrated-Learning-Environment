#!/usr/bin/env bash
# T-102 / T-204: Check that Learning Book structure matches expected layout (SustainAdv-AC1, SustainAdj-AC3).
# Per learning-book/README.md and learning-book-tree-map.md: Area → A/B/C/D/E; under C, 6 chapters (0..5).
# Exit 0 if valid; exit 1 if invalid. Run from repo root: ./scripts/check-learning-book-structure.sh [learning-book]

set -e
ROOT="${1:-learning-book}"
REQUIRED_PHASES=(
  "A. Subject Roadmap & Level Specifications"
  "B. Capture Facts & Data"
  "C. Organise Information"
  "D. Distill Understanding"
  "E. Express Expertise"
)
REQUIRED_C_CHAPTERS=(
  "0. Overview & Summary"
  "1. UBS"
  "2. UDS"
  "3. EPS"
  "4. UES"
  "5. EOP"
)

if [ ! -d "$ROOT" ] || [ -z "$(ls -A "$ROOT" 2>/dev/null)" ]; then
  echo "FAIL: no COE Area found under $ROOT"
  exit 1
fi

for area in "$ROOT"/*/; do
  [ -d "$area" ] || continue
  for name in "${REQUIRED_PHASES[@]}"; do
    path="$area$name"
    if [ ! -d "$path" ]; then
      echo "FAIL: missing $path"
      exit 1
    fi
  done
  # T-204: under C. Organise Information, require 6 chapter folders (per README § Minimal Structure)
  C_PATH="${area}C. Organise Information"
  if [ -d "$C_PATH" ]; then
    for ch in "${REQUIRED_C_CHAPTERS[@]}"; do
      ch_path="$C_PATH/$ch"
      if [ ! -d "$ch_path" ]; then
        echo "FAIL: missing $ch_path"
        exit 1
      fi
    done
  fi
  echo "OK: $area"
done

echo "PASS: Learning Book structure valid"
