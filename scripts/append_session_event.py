#!/usr/bin/env python3
# T-412: Append one session event to logs/ile-session-events.jsonl (ScalAdv-AC5, Noun-AC10).
# Usage: python3 scripts/append_session_event.py <event> [--subject SUBJECT] [--phase PHASE] [--entry-point ENTRY_POINT]
# Event: session_start | entry_point_selected | chunk_completed | session_end

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LOG_FILE = REPO_ROOT / "logs" / "ile-session-events.jsonl"
VALID_EVENTS = ("session_start", "entry_point_selected", "chunk_completed", "session_end")


def main() -> int:
    parser = argparse.ArgumentParser(description="Append one ILE session event to JSONL log (T-412)")
    parser.add_argument("event", choices=VALID_EVENTS, help="Event type")
    parser.add_argument("--subject", default=None, help="Subject e.g. COE_DS")
    parser.add_argument("--phase", default=None, help="Phase B | C | D")
    parser.add_argument("--entry-point", dest="entry_point", default=None, help="Entry point e.g. Chapter 1 UBS, Topic 0")
    args = parser.parse_args()

    payload = {
        "event": args.event,
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    if args.subject:
        payload["subject"] = args.subject
    if args.phase:
        payload["phase"] = args.phase
    if args.entry_point:
        payload["entry_point"] = args.entry_point

    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(payload, ensure_ascii=False) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
