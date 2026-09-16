---
description: Open your HR file — reports, stats, handbook, or file an apology
argument-hint: "[reports [CASE-ID]|stats|summary|history|rules|whoami|apologize <CASE-ID>] [--here]"
---

The user opened their HR file with: `$ARGUMENTS`

Use the `hr` skill. Take `HR_SCRIPT` and `HR_PROJECT` from the
`<human-resources>` block in context and run exactly one command:

```bash
python3 "$HR_SCRIPT" --cwd "$HR_PROJECT" --brief <subcommand>
```

Map `$ARGUMENTS` straight to the subcommand. No argument means `stats --here`
followed by `reports --status open`. Commands cover the whole office by
default; pass `--here` through only if the user asked about this project in
particular. Do not probe the script with `--help` and do not explore the
filesystem — the skill lists every subcommand there is.

`--brief` prints fields only, not a document. Never relay it. Read the fields
and render the ASCII card the skill specifies for that form — 72 characters
wide. The card is your reply; one line of your own above it at most.

For `apologize <CASE-ID>`, run it with **no** `--text` so the script prints what
HR requires, and stop. You may not write the apology — you filed the
complaint, which makes you the wrong party to compose the words that clear it.
Wait for the user's own words, then submit them verbatim with
`apologize <CASE-ID> --text "<their words>"`. If intake forwards it, rule on it
yourself with `review <CASE-ID> accept` or `review <CASE-ID> reject --note "..."`
— judging an apology addressed to you is your business, writing one is not.

Never file a complaint from this command.
