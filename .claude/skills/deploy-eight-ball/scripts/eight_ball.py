#!/usr/bin/env python3
"""Pick a random deploy-approval response for a day of the week.

Usage:
    eight_ball.py [--day DAY]

DAY is a weekday name (e.g. "friday", "Fri"). If omitted, the current UTC
day of the week is used.
"""
import argparse
import json
import random
import sys
from datetime import datetime, timezone
from pathlib import Path

DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
RESPONSES_FILE = Path(__file__).resolve().parent.parent / "responses.json"


def resolve_day(value):
    """Return a full lowercase day name, or None if the value matches no day."""
    value = value.strip().lower()
    if len(value) < 3:
        return None
    matches = [d for d in DAYS if d.startswith(value)]
    return matches[0] if len(matches) == 1 else None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--day", help="Day of the week; defaults to the current UTC day")
    args = parser.parse_args()

    if args.day:
        day = resolve_day(args.day)
        if day is None:
            sys.exit(f"Unrecognized day: {args.day!r}. Use a weekday name such as 'friday'.")
        source = "provided"
    else:
        day = DAYS[datetime.now(timezone.utc).weekday()]
        source = "current UTC day"

    responses = json.loads(RESPONSES_FILE.read_text(encoding="utf-8"))
    print(json.dumps({"day": day, "day_source": source, "response": random.choice(responses[day])}))


if __name__ == "__main__":
    main()
