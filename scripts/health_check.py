#!/usr/bin/env python3
# T-407: ILE system health check (SustainAdj-AC4).
# Validates: config/ile.yaml and config/coe-map.yaml (parseable + schema);
# templates for all page types; learning-book structure; A exists for at least one subject; ile-*.mdc rules present.
# Run from repo root. Exit 0 if healthy, 1 if any issue. Output: "system is healthy" or enumerated issues.

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ILE_CONFIG = REPO_ROOT / "config" / "ile.yaml"
COE_MAP_CONFIG = REPO_ROOT / "config" / "coe-map.yaml"
CURSOR_RULES = REPO_ROOT / ".cursor" / "rules"
REQUIRED_TEMPLATES = [
    "A-subject-roadmap-and-level-specifications.md",
    "B-captured-facts-and-information.md",
    "page-0-overview-and-summary.md",
    "page-1-ultimate-blockers.md",
    "page-2-ultimate-drivers.md",
    "page-3-principles.md",
    "page-4-components.md",
    "page-5-steps-to-overcome.md",
    "page-7-topic-distilled-understanding.md",
]


def main() -> int:
    issues: list[str] = []

    # 1. config/ile.yaml — parseable and schema-valid
    ile_ok, ile_issues = check_ile_yaml()
    issues.extend(ile_issues)

    # 2. config/coe-map.yaml — parseable and schema-valid
    coe_ok, coe_issues = check_coe_map_yaml()
    issues.extend(coe_issues)

    # Paths from ile.yaml if parseable, else defaults
    templates_path = REPO_ROOT / "templates"
    learning_book_root = REPO_ROOT / "learning-book"
    if ILE_CONFIG.is_file():
        try:
            import yaml
            with open(ILE_CONFIG) as f:
                cfg = yaml.safe_load(f)
            if isinstance(cfg, dict):
                templates_path = REPO_ROOT / cfg.get("templates_path", "templates")
                learning_book_root = REPO_ROOT / cfg.get("learning_book_root", "learning-book")
        except Exception:
            pass

    # 3. Templates exist for all page types
    for name in REQUIRED_TEMPLATES:
        if not (templates_path / name).is_file():
            issues.append(f"Missing template: {templates_path / name}")

    # 4. Learning-book structure passes check-learning-book-structure.sh
    script = REPO_ROOT / "scripts" / "check-learning-book-structure.sh"
    if script.is_file():
        try:
            rel_root = learning_book_root.relative_to(REPO_ROOT)
        except ValueError:
            rel_root = "learning-book"
        result = subprocess.run(
            [str(script), str(rel_root)],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            msg = (result.stdout or "").strip() or (result.stderr or "").strip() or "check-learning-book-structure.sh failed"
            issues.append(f"Learning-book structure: {msg}")
    else:
        issues.append(f"Missing script: {script}")

    # 5. A exists for at least one subject
    a_found = False
    if learning_book_root.is_dir():
        for area_dir in learning_book_root.iterdir():
            if not area_dir.is_dir():
                continue
            a_dir = area_dir / "A. Subject Roadmap & Level Specifications"
            if a_dir.is_dir() and any(a_dir.glob("*.md")):
                a_found = True
                break
    if not a_found:
        issues.append("A (Subject Roadmap & Level Specifications) with at least one .md not found for any subject under learning-book")

    # 6. Rules .cursor/rules/ile-*.mdc present
    if CURSOR_RULES.is_dir():
        ile_rules = list(CURSOR_RULES.glob("ile-*.mdc"))
        if not ile_rules:
            issues.append("No .cursor/rules/ile-*.mdc rules found")
    else:
        issues.append(f"Missing rules directory: {CURSOR_RULES}")

    if issues:
        for i in issues:
            print(i)
        return 1
    print("system is healthy")
    return 0


def check_ile_yaml() -> tuple[bool, list[str]]:
    issues: list[str] = []
    if not ILE_CONFIG.is_file():
        issues.append(f"config/ile.yaml: file not found")
        return False, issues
    try:
        import yaml
    except ImportError:
        issues.append("config/ile.yaml: parseable but schema check skipped (install PyYAML for full validation)")
        return True, issues
    try:
        with open(ILE_CONFIG) as f:
            cfg = yaml.safe_load(f)
    except Exception as e:
        issues.append(f"config/ile.yaml: not parseable — {e}")
        return False, issues
    if not isinstance(cfg, dict):
        issues.append("config/ile.yaml: invalid structure (expected mapping)")
        return False, issues
    required = ["coe_map_path", "templates_path", "learning_book_root"]
    for key in required:
        if key not in cfg:
            issues.append(f"config/ile.yaml: missing required key '{key}'")
        elif not isinstance(cfg[key], str):
            issues.append(f"config/ile.yaml: key '{key}' must be a string")
    return len(issues) == 0, issues


def check_coe_map_yaml() -> tuple[bool, list[str]]:
    issues: list[str] = []
    if not COE_MAP_CONFIG.is_file():
        issues.append("config/coe-map.yaml: file not found")
        return False, issues
    try:
        import yaml
    except ImportError:
        issues.append("config/coe-map.yaml: parseable but schema check skipped (install PyYAML for full validation)")
        return True, issues
    try:
        with open(COE_MAP_CONFIG) as f:
            cfg = yaml.safe_load(f)
    except Exception as e:
        issues.append(f"config/coe-map.yaml: not parseable — {e}")
        return False, issues
    if not isinstance(cfg, dict):
        issues.append("config/coe-map.yaml: invalid structure (expected mapping)")
        return False, issues
    # coe: id, name
    if "coe" not in cfg:
        issues.append("config/coe-map.yaml: missing required key 'coe'")
    else:
        coe = cfg["coe"]
        if not isinstance(coe, dict):
            issues.append("config/coe-map.yaml: 'coe' must be a mapping")
        else:
            for k in ("id", "name"):
                if k not in coe:
                    issues.append(f"config/coe-map.yaml: coe missing required key '{k}'")
    # areas: list of { id, name, chapters: [ { id, name, topics: [ { id, name, topic_members_learning_area, personal_learning_areas } ] } ] }
    if "areas" not in cfg:
        issues.append("config/coe-map.yaml: missing required key 'areas'")
    elif not isinstance(cfg["areas"], list):
        issues.append("config/coe-map.yaml: 'areas' must be a list")
    else:
        for i, area in enumerate(cfg["areas"]):
            if not isinstance(area, dict):
                issues.append(f"config/coe-map.yaml: areas[{i}] must be a mapping")
                continue
            for k in ("id", "name", "chapters"):
                if k not in area:
                    issues.append(f"config/coe-map.yaml: areas[{i}] missing required key '{k}'")
            if "chapters" in area and isinstance(area["chapters"], list):
                for j, ch in enumerate(area["chapters"]):
                    if not isinstance(ch, dict):
                        issues.append(f"config/coe-map.yaml: areas[{i}].chapters[{j}] must be a mapping")
                        continue
                    for k in ("id", "name", "topics"):
                        if k not in ch:
                            issues.append(f"config/coe-map.yaml: areas[{i}].chapters[{j}] missing required key '{k}'")
                    if "topics" in ch and isinstance(ch["topics"], list):
                        for kk, topic in enumerate(ch["topics"]):
                            if not isinstance(topic, dict):
                                issues.append(f"config/coe-map.yaml: areas[{i}].chapters[{j}].topics[{kk}] must be a mapping")
                                continue
                            for tk in ("id", "name", "topic_members_learning_area", "personal_learning_areas"):
                                if tk not in topic:
                                    issues.append(f"config/coe-map.yaml: areas[{i}].chapters[{j}].topics[{kk}] missing required key '{tk}'")
    return len(issues) == 0, issues


if __name__ == "__main__":
    sys.exit(main())
