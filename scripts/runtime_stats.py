#!/usr/bin/env python3
# T-410: Lightweight runtime stats (Verb-AC10, Noun-AC11).
# Reads config/ile.yaml + config/coe-map.yaml + A's Session Log; computes
# completed entry points, streak, last session. Dashboard can consume this;
# validates config files are consumable by code.
# Run from repo root. Output: JSON or text summary.

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ILE_CONFIG = REPO_ROOT / "config" / "ile.yaml"
COE_MAP_CONFIG = REPO_ROOT / "config" / "coe-map.yaml"


def main() -> int:
    stats: dict = {
        "completed_entry_points": 0,
        "streak_days": 0,
        "last_session": None,
        "subjects": [],
        "errors": [],
    }

    # 1. Read config/ile.yaml (optional: use default learning-book if missing)
    learning_book_root = REPO_ROOT / "learning-book"
    if ILE_CONFIG.is_file():
        try:
            import yaml
            with open(ILE_CONFIG) as f:
                cfg = yaml.safe_load(f)
            if isinstance(cfg, dict) and "learning_book_root" in cfg:
                learning_book_root = REPO_ROOT / cfg["learning_book_root"]
        except Exception as e:
            stats["errors"].append(f"ile.yaml: {e}")

    # 2. Read config/coe-map.yaml (validate consumable by code)
    if COE_MAP_CONFIG.is_file():
        try:
            import yaml
            with open(COE_MAP_CONFIG) as f:
                yaml.safe_load(f)
        except Exception as e:
            stats["errors"].append(f"coe-map.yaml: {e}")

    # 3. Find A files and parse Session Log + Learner Progress Tracker
    a_dir_name = "A. Subject Roadmap & Level Specifications"
    all_dates: list[datetime] = []
    all_entry_points: set[str] = set()

    for area_dir in learning_book_root.iterdir() if learning_book_root.is_dir() else []:
        if not area_dir.is_dir():
            continue
        a_dir = area_dir / a_dir_name
        if not a_dir.is_dir():
            continue
        for a_file in a_dir.glob("*.md"):
            if not a_file.is_file():
                continue
            text = a_file.read_text(encoding="utf-8", errors="replace")
            subject = area_dir.name
            sub_stats = {"subject": subject, "last_session": None, "entry_points": 0, "dates": []}

            # Learner Progress Tracker: Last Session (YYYY-MM-DD)
            tracker_match = re.search(
                r"\*\*Last Session\*\*\s*\|\s*(\d{4}-\d{2}-\d{2})",
                text,
            )
            if tracker_match:
                try:
                    d = datetime.strptime(tracker_match.group(1), "%Y-%m-%d")
                    all_dates.append(d)
                    sub_stats["last_session"] = tracker_match.group(1)
                    sub_stats["dates"].append(tracker_match.group(1))
                except ValueError:
                    pass

            # Session Log table: rows after | Date | Entry Point | Progress |
            in_session_log = False
            for line in text.splitlines():
                if "## Session Log" in line:
                    in_session_log = True
                    continue
                if in_session_log and line.strip().startswith("|") and "Date" not in line and "---" not in line:
                    parts = [p.strip() for p in line.split("|") if p.strip()]
                    if len(parts) >= 1 and re.match(r"\d{4}-\d{2}-\d{2}", parts[0]):
                        try:
                            d = datetime.strptime(parts[0], "%Y-%m-%d")
                            all_dates.append(d)
                            sub_stats["dates"].append(parts[0])
                        except ValueError:
                            pass
                        if len(parts) >= 2 and not parts[1].startswith("*"):
                            all_entry_points.add(parts[1])
                            sub_stats["entry_points"] += 1

            if sub_stats["dates"] or sub_stats["last_session"] or sub_stats["entry_points"]:
                stats["subjects"].append(sub_stats)

    # Aggregate: completed entry points = distinct entry points across Session Logs
    stats["completed_entry_points"] = len(all_entry_points)

    # Last session = most recent date
    if all_dates:
        last = max(all_dates)
        stats["last_session"] = last.strftime("%Y-%m-%d")
    else:
        for s in stats["subjects"]:
            if s.get("last_session"):
                stats["last_session"] = s["last_session"]
                break

    # Streak = consecutive days with at least one session (from today backwards)
    if all_dates:
        unique_dates = sorted(set(d.date() for d in all_dates), reverse=True)
        today = datetime.now().date()
        streak = 0
        expect = today
        for d in unique_dates:
            if d > today:
                continue
            if d == expect:
                streak += 1
                expect -= timedelta(days=1)
            elif d < expect:
                break
        stats["streak_days"] = streak

    # Output
    if "--json" in sys.argv:
        print(json.dumps(stats, indent=2))
    else:
        print("Runtime stats (T-410)")
        print("  Completed entry points:", stats["completed_entry_points"])
        print("  Streak (days):", stats["streak_days"])
        print("  Last session:", stats["last_session"] or "(none)")
        if stats["errors"]:
            print("  Errors:", stats["errors"])

    return 0 if not stats["errors"] else 1


if __name__ == "__main__":
    sys.exit(main())
