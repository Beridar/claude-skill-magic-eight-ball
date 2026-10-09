---
name: deploy-eight-ball
description: A magic 8 ball for deployment approvals. Use when the user asks whether something should be deployed, released, shipped, or approved for production, or explicitly asks for the deploy eight ball. Returns a random, day-of-the-week-flavored verdict.
---

# Deploy Eight Ball

Answers "should we deploy this?" with a random response that reflects the team's attitude toward deploying on a given day of the week.

## Steps

1. Determine whether the user named a day of the week (e.g. "what about Friday?", "if we ship on Tuesday"). If so, use it. If not, do not pass a day; the script defaults to the current UTC day.
2. Run the script, adding `--day <day>` only when the user provided one:

   ```
   python .claude/skills/deploy-eight-ball/scripts/eight_ball.py [--day <day>]
   ```

   Use `python3` if `python` is not available.
3. The script prints JSON with `day`, `day_source`, and `response`. Reply to the user with the `response` text verbatim, as the 8 ball's verdict. Do not pick, rewrite, or embellish the response yourself.
4. Add one short line after the verdict naming the day that was used, e.g. "(Verdict for Friday, current UTC day)". Use `day_source` to say whether the day was provided or defaulted.

## Notes

- Responses live in `responses.json`: at least 3 per day, none duplicated across days. Edit that file to add or change responses.
- If the script fails (e.g. an unrecognized day), tell the user what went wrong rather than inventing a response.
- This is for entertainment. Make clear it is not a substitute for a real change-approval process only if the user seems to be treating it as one.
