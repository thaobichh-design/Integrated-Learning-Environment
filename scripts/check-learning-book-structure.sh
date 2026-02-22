#!/usr/bin/env bash
# T-102: Check that Learning Book structure matches expected layout (SustainAdv-AC1).
# Exit 0 if valid; exit 1 if invalid.

set -e
ROOT="${1:-learning-book}"
REQUIRED=(
  "A. Subject Roadmap & Level Specifications"
  "B. Capture Facts & Data"
  "C. Organise Information"
  "D. Distill Understanding"
  "E. Express Expertise"
)

for area in "$ROOT"/*/; do
  [ -d "$area" ] || continue
  for name in "${REQUIRED[@]}"; do
    path="$area$name"
    if [ ! -d "$path" ]; then
      echo "FAIL: missing $path"
      exit 1
    fi
  done
  echo "OK: $area"
done

if [ ! -d "$ROOT" ] || [ -z "$(ls -A "$ROOT" 2>/dev/null)" ]; then
  echo "FAIL: no COE Area found under $ROOT"
  exit 1
fi

echo "PASS: Learning Book structure valid"
