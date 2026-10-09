# claude-skill-magic-eight-ball
A sample Claude skill that emulates a magic eight ball for deployment approvals, using lists of responses keyed to the day of the week.

This is a spike to prove the technical feasibility of a system. The skill running at all is the proof.

## Usage

Ask Claude whether something should be deployed, or invoke the skill by name:

```
/deploy-eight-ball should we ship the billing fix?
/deploy-eight-ball what about Friday?
```

If you name a day of the week, that day's responses are used. Otherwise the current UTC day of the week is used.

Example verdict for Friday: *"Not on read-only Friday."*

## Layout

```
.claude/skills/deploy-eight-ball/
├── SKILL.md                  # skill definition and instructions for Claude
├── responses.json            # responses for each day of the week
└── scripts/eight_ball.py     # picks a random response for a day
```

- `responses.json` has at least 3 responses per day, and no response is repeated across days. Edit it to add or change responses.
- `eight_ball.py` does the random selection so the result doesn't depend on the model. It can be run directly:

  ```
  python .claude/skills/deploy-eight-ball/scripts/eight_ball.py [--day friday]
  ```

## Requirements

Python 3 (`python` or `python3` on the path).
