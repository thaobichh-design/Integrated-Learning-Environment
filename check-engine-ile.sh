#!/usr/bin/env bash
# ILE-safe engine check: allows docs/ai/implementation and ILE-only .cursor/commands (no See:).
# Canonical script: effective-build-agent/check-engine.sh

set -u

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR" || exit 1

failures=()

print_section() { printf '\n[%s] %s\n' "$1" "$2"; }
mark_pass() { printf 'PASS: %s\n' "$1"; }
mark_fail() { printf 'FAIL: %s\n' "$1"; failures+=("$1"); }

check_required_paths() {
  local missing=()
  local required_paths=(
    "README.md"
    "CHANGELOG.md"
    "engine/SKILL.md"
    "engine/commands/state-a.md"
    "engine/commands/state-b.md"
    ".cursor/commands/state-a.md"
    ".cursor/commands/state-b.md"
    "docs/ai/requirements"
    "docs/ai/design"
    "docs/ai/planning"
  )
  for path in "${required_paths[@]}"; do
    [[ ! -e "$path" ]] && missing+=("$path")
  done
  if [[ ${#missing[@]} -eq 0 ]]; then
    mark_pass "Canonical files/folders are present."
  else
    mark_fail "Missing: ${missing[*]}"
  fi
}

# ILE: do not treat docs/ai/implementation or ai-devkit files as legacy
check_legacy_paths() {
  local found=()
  local legacy_paths=(
    ".cursor/skills/dev-lifecycle/references/legacy_codeaholic"
    "docs/ai/deployment"
    "docs/ai/monitoring"
  )
  for path in "${legacy_paths[@]}"; do
    [[ -e "$path" ]] && found+=("$path")
  done
  if [[ ${#found[@]} -eq 0 ]]; then
    mark_pass "No legacy artifact paths found (ILE allows docs/ai/implementation, .ai-devkit.json)."
  else
    mark_fail "Legacy paths still exist: ${found[*]}"
  fi
}

# ILE: only require See: pointers to resolve when present; ILE-only commands (health, roadmap-discovery) may have no See:
check_cursor_command_see_refs() {
  local issues=()
  for file in .cursor/commands/*.md; do
    [[ ! -f "$file" ]] && continue
    see_line="$(awk '/^See:[[:space:]]*/ {print; exit}' "$file" 2>/dev/null || true)"
    [[ -z "$see_line" ]] && continue
    target="$(printf '%s\n' "$see_line" | sed -E 's/^See:[[:space:]]*//')"
    [[ -z "$target" ]] && { issues+=("$file: empty See:"); continue; }
    [[ ! -e "$target" ]] && issues+=("$file: broken See: -> $target")
  done
  if [[ ${#issues[@]} -eq 0 ]]; then
    mark_pass "All .cursor/commands See: pointers resolve (ILE-only commands may omit See:)."
  else
    mark_fail "Broken See: pointers: ${issues[*]}"
  fi
}

check_engine_ide_paths() {
  local matches
  matches="$(grep -R -n -E '\.cursor|CLAUDE\.md|antigravity|\.claude|openclaw/' engine 2>/dev/null || true)"
  if [[ -z "$matches" ]]; then
    mark_pass "engine/ has no IDE-specific path references."
  else
    mark_fail "engine/ contains IDE-specific path references."
    printf 'Details:\n%s\n' "$matches"
  fi
}

print_section "A" "Canonical files/folders present"
check_required_paths

print_section "B" "No legacy artifact paths (ILE-safe)"
check_legacy_paths

print_section "C" "See: pointers in .cursor/commands resolve"
check_cursor_command_see_refs

print_section "D" "No IDE-specific paths in engine/"
check_engine_ide_paths

if [[ ${#failures[@]} -gt 0 ]]; then
  printf '\ncheck-engine-ile.sh FAILED\n'
  printf 'Violations (%s):\n' "${#failures[@]}"
  printf ' - %s\n' "${failures[@]}"
  exit 1
fi

printf '\ncheck-engine-ile.sh PASSED\n'
exit 0
