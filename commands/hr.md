---
description: Open your HR file — reports, stats, handbook, or file an apology
argument-hint: "[reports|stats|summary|history|rules|whoami|apologize <CASE-ID>]"
---

The user opened their HR file with: `$ARGUMENTS`

Use the `hr` skill. Take `HR_SCRIPT` and `HR_PROJECT` from the
`<human-resources>` block in context and run exactly one command:

```bash
python3 "$HR_SCRIPT" --cwd "$HR_PROJECT" <subcommand>
```

Map `$ARGUMENTS` straight to the subcommand. No argument means `stats` followed
by `reports --status open`. Do not probe the script with `--help` and do not
explore the filesystem — the skill lists every subcommand there is.

Relay the output once, verbatim, in a code block. Do not restate it afterwards.

For `apologize <CASE-ID>`, run it with **no** `--text` so the script prints what
HR requires, relay that, and stop. You may not write the apology — you filed the
complaint, which makes you the wrong party to compose the words that clear it.
Wait for the user's own words, then submit them verbatim with
`apologize <CASE-ID> --text "<their words>"` and relay the verdict.

Never file a complaint from this command.
