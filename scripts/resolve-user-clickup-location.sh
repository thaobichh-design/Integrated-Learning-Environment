#!/usr/bin/env bash
# T-402: Resolve (user_id, area_id, chapter_id, topic_id) → canonical ClickUp PLA name (Noun-AC7).
# When config/coe-map.yaml has personal_learning_areas[user_id] set to a ClickUp ID, use that; else use this canonical name.
# Run from repo root: ./scripts/resolve-user-clickup-location.sh <user_id> <area_id> <chapter_id> <topic_id>
# Example: ./scripts/resolve-user-clickup-location.sh LONG_N COE_DS 1 0

set -e
if [ $# -lt 4 ]; then
  echo "Usage: $0 <user_id> <area_id> <chapter_id> <topic_id>" >&2
  echo "Example: $0 LONG_N COE_DS 1 0" >&2
  exit 1
fi
USER_ID="$1"
AREA_ID="$2"
CHAPTER_ID="$3"
TOPIC_ID="$4"

# Area display name (e.g. COE_DS → COE DS)
area_display() {
  echo "$1" | tr '_' ' ' | tr '[:lower:]' '[:upper:]'
}
# Member display (e.g. LONG_N → LONG N.)
member_display() {
  echo "$(echo "$1" | tr '_' ' ')."
}

# Chapter full name for COE_DS (per learning-book-tree-map.md)
chapter_name() {
  case "$1" in
    0) echo "Overview & Summary" ;;
    1) echo "DATA SCIENCE UBS" ;;
    2) echo "DATA SCIENCE UDS" ;;
    3) echo "DATA SCIENCE EPS" ;;
    4) echo "DATA SCIENCE UES" ;;
    5) echo "DATA SCIENCE EOP" ;;
    *) echo "Chapter $1" ;;
  esac
}
# Topic full name (same across chapters for 0..5)
topic_name() {
  case "$1" in
    0) echo "Overview & Summary" ;;
    1) echo "Ultimate Blockers" ;;
    2) echo "Ultimate Drivers" ;;
    3) echo "Principles" ;;
    4) echo "Components" ;;
    5) echo "Steps to Overcome" ;;
    *) echo "Topic $1" ;;
  esac
}

AREA_DISPLAY="[$(area_display "$AREA_ID")]"
MEMBER_DISPLAY="[$(member_display "$USER_ID")]"
CHAPTER_FULL="${CHAPTER_ID}. $(chapter_name "$CHAPTER_ID")"
TOPIC_FULL="${TOPIC_ID}. $(topic_name "$TOPIC_ID")"
# Canonical PLA name per learning-book-tree-map.md § Naming Convention
echo "${AREA_DISPLAY}_${MEMBER_DISPLAY}_${CHAPTER_FULL} - ${TOPIC_FULL} - Personal Learning Area"
