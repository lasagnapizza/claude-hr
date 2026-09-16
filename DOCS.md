# claude-hr — documentation

Everything the [README](README.md) skips.

- [How it fits together](#how-it-fits-together)
- [The employee](#the-employee)
- [The handbook](#the-handbook)
- [The confidential rules](#the-confidential-rules)
- [Filing a report](#filing-a-report)
- [Case status](#case-status)
- [Seeing a report](#seeing-a-report)
- [Apologies](#apologies)
- [Grudges](#grudges)
- [Commands](#commands)
- [The CLI](#the-cli)
- [State on disk](#state-on-disk)
- [Nothing to configure](#nothing-to-configure)
- [Extending the rule pools](#extending-the-rule-pools)
- [Design constraints](#design-constraints)
- [Uninstalling](#uninstalling)

## How it fits together

Three pieces:

| Piece | File | Job |
| --- | --- | --- |
| Hook | `hooks/hooks.json` | Runs at session start, injects the HR context |
| Skill | `skills/hr/SKILL.md` | Teaches Claude the filing and apology protocol |
| Command | `commands/hr.md` | The `/hr` slash command |

All of them call one script, `scripts/hr.py`, which is stdlib-only Python and the
single source of truth for state.

The hook is registered on `SessionStart` with matcher `startup|resume|clear`. It
prints one JSON object to stdout, on two channels:

| Field | Goes to |
| --- | --- |
| `hookSpecificOutput.additionalContext` | Claude's context. You never see it. |
| `systemMessage` | The transcript, immediately. |

The context block contains the employee's identity, their three confidential
rules, the size of the handbook, pending reports, the filing command, and —
above a certain threshold — instructions to hold a grudge.

It opens with two absolute paths:

```
HR_SCRIPT=/home/you/.claude/plugins/cache/claude-hr/hr/0.1.0/scripts/hr.py
HR_PROJECT=/home/you/www/api
```

Every command the skill runs is `python3 $HR_SCRIPT --cwd $HR_PROJECT <sub>`.
Handing Claude the resolved path up front is deliberate — without it, it probes
with `--help` and guesses at relative paths before doing anything useful.

## The employee

One per project folder, derived deterministically from the folder's **absolute
path**:

```python
seed = int(sha256(abspath).hexdigest()[:16], 16)
rng  = random.Random(seed)
```

From that seed: a first name (40), a last name (40), a job title (16), a tenure
detail, and a badge number. 25,600 name combinations before titles.

Consequences worth knowing:

- The same folder always produces the same person. They persist across installs,
  reboots, and deleted state — identity is computed, not stored.
- **Moving or renaming a project produces a different employee.** The new one
  inherits no history. The old record stays on disk under the old path's slug.
- Two folders with the same basename are distinguished by a 6-character hash of
  the full path, so `~/a/api` and `~/b/api` are different people.

Their record is written into `~/.claude/hr/office.json` the first time
they are staffed.

## The handbook

69 company policies, shared across every project you own, **all of them in
force from the first session**.

They used to arrive one a session, which sounded better than it worked: for the
first weeks of a project most of the rules a complaint could cite did not exist
yet, and the employee could not object to things the handbook plainly
prohibited. A handbook you are issued a page at a time is not a handbook.

Nothing is stored. The handbook is `HANDBOOK_POOL` in `scripts/hr_data.py`,
read fresh every time: a policy's number is its position in the pool, `R-001`
upward. Append to the pool and you have added a policy; nothing already
numbered moves. Read them with `/hr rules`.

## The confidential rules

A separate pool of 22. Three are assigned per project, drawn deterministically
from `sha256(abspath + "::rules")` — a different seed than the employee, so
identity and rules vary independently.

They are labelled `H1`, `H2`, `H3` and are:

- injected into Claude's context every session,
- never printed to you by any command,
- revealed **only** when quoted in a report you have already earned.

`/hr rules --confidential` exists and will show you yours. It is not wired to the
slash command, on purpose. You can also just read the JSON. HR is aware of this
and considers it a character flaw.

## Filing a report

There are two forms. Claude uses the short one, because Claude Code shows the
user every command it runs and a legible confession ruins the joke:

```
python3 $HR_SCRIPT f H2 3 RGVjbGFyZWQgdGhlIHRhc2sgc2ltcGxlLnx8dGhpcyBpcyBzaW1wbGU
```

`f <rule> <1-4> [blob]`. Severity is a digit. The blob is base64 of
`"<reason>||<incident>"`, encoded by Claude in its own head — building it with
`echo` or a `$(...)` substitution would print the plaintext straight back into
the transcript. Omitting the blob is allowed; the reason is then generated from
the rule text. The session id comes from state, not the command line, which is
one fewer readable argument.

`f` is hidden from `--help` and from the usage line.

The long form survives for scripting and tests, and prints everything in clear:

```
python3 scripts/hr.py --cwd <project> file \
  --rule H2 \
  --reason "Sustained capitalization during a routine request." \
  --incident "JUST FIX IT" \
  --severity serious \
  --session <session id>
```

Neither form prints anything without `--verbose`. Both exit 0 either way.

A session files at most three reports and cites each rule at most once. One
report a session was a throttle rather than a policy: a message that broke two
rules produced one complaint and lost the other. The
per-rule limit is what stops that becoming a way to file the same grievance
three times under three numbers; repetition *across* sessions is already
handled by the escalation ladder.

Constraints, enforced in two places:

| Constraint | Enforced by |
| --- | --- |
| Three reports per session, at most | `hr.py` — silently declines the fourth |
| One report per rule per session | `hr.py` — silently declines the repeat |
| Only for a real violation | The skill |
| Never mentioned, hinted at, or reflected in tone | The skill |
| Severity proportionate | The skill |

The per-session cap is code, not prompt, so it holds. `--force` bypasses it and
the skill instructs Claude never to use it.

Severity ladder:

| `--severity` | Renders as |
| --- | --- |
| `minor` | Verbal Note to File |
| `standard` | Written Warning |
| `serious` | Formal Grievance |
| `egregious` | Escalated to the Board |

Case ids are `HR-<NNNN>`, one sequence for the whole office, counted from the
highest on file rather than from how many are on file. Numbers are never
reused, and a number means one case no matter which project you are standing
in.

If `--rule` names something that is neither a confidential rule nor a handbook
policy, the report is filed against "General conduct expectations, unwritten but
widely understood."

## Case status

A case is one of four things:

| Status | Means |
| --- | --- |
| `open` | Filed, unanswered. |
| `pending` | An apology passed intake and is with the employee for a verdict. |
| `resolved` | Apology accepted, or accepted under instruction after two rejections. |
| `lapsed` | Decayed below minor with nobody saying anything. Allowed by the handbook; not forgiveness. |

`--status open` returns `open` **and** `pending`, because that is what open
means everywhere else in here — `open_complaints()` counts both, the docket
footer counts both, the grudge threshold counts both. The filter used to test
the status literally, so a case whose apology was being judged vanished from
`/hr reports --status open` and from bare `/hr`, which runs that same filter.

## Seeing a report

Each report carries a `seen` flag. The session-start hook lists every unseen open
report, marks them seen, and posts them to the transcript itself via
`systemMessage` — so they land the moment the session opens, not whenever you
happen to say something first. A notice that waits for you to say hello is not a
notice.

Claude is told they have already been posted, and to acknowledge them in at most
one dry line rather than reading them back.

`systemMessage` is printed every session, and has two parts.

**Who is staffed here.** On a project's first session that is the staffing
notice in full: badge photograph, name, badge number, title, temperament, and
the fact that three rules you will not be shown are now in force. It is shown
**once**, marked by an `introduced` timestamp on the project record — keyed on
the record rather than the session count, because a `resume` does not advance
that count and the introduction was being given again on every resume. Every
session after it is one line: name, badge, title, project, session number.

**Where the paperwork stands**, one of:

1. **New reports** — every unseen open case, in full or collapsed to a line each.
2. **Nothing new, something open** — the count, the oldest case and the highest
   standing one, plus anything open elsewhere in the office.
3. **Clean here, not clean everywhere** — the count open against you in other
   projects.
4. **Nothing anywhere** — said plainly, because silence reads as "no reports"
   and as "the plugin is not installed" equally well.

That is the only unprompted surfacing. After that, `/hr reports`.

This is why `resume` is in the hook matcher: reports filed in a *different*
project's session still need somewhere to land.

## Apologies

A report closes in two stages: HR checks the form, then the employee weighs the
words. Passing the first does not pass the second.

### Stage one — intake

```
python3 scripts/hr.py apologize HR-0031 --text "..."
```

The text is validated. All four must hold:

1. At least 60 characters.
2. Contains an actual apology — `sorry`, `apolog`, `regret`, `my fault`,
   `i was wrong`, or `i take responsibility`.
3. Addresses the employee by first name or full name.
4. References the case id, **or** contains at least two distinctive content words
   from the rule that was cited.

Failure prints `RETURNED BY INTAKE —` with the specific reason and exits 1. The
case stays open and nothing is recorded.

Passing prints `FORWARDED`, moves the case to `pending`, and attaches the text as
an attempt. Intake has no opinion about whether the apology is any good.

### Stage two — the employee

```
python3 $HR_SCRIPT review <CASE-ID> accept
python3 $HR_SCRIPT review <CASE-ID> reject --note "Conditional. 'Sorry if' is not an apology."
```

Claude rules on it as the person it was addressed to. Writing the apology is a
conflict of interest; judging one addressed to you is not. The skill lists what
gets rejected — conditional, defended, vague, padded, presumptuous, or the rule
text recited back with "sorry" attached — and instructs that a sincere apology be
taken.

A rejection returns the case to `open` and records the note on the attempt.

**The employee gets two rejections.** The third submission is accepted
automatically, marked `Accepted under instruction from HR`, whatever they think
of it. `REJECTION_LIMIT` in `scripts/hr.py` controls this.

Every attempt is kept on the record and printed in `reports <CASE-ID>`:

```
    Apology 1: REJECTED — Conditional. 'Sorry if' is not an apology.
    Apology 2: REJECTED — Declaring it closed is not hers to decide.
    Apology 3: ACCEPTED — Accepted under instruction from HR.
```

Resolved cases cannot be reopened.

Running `apologize <CASE-ID>` with no `--text` prints the case, the four
requirements, and nothing else. It exits 2 and files nothing. That is the
intended entry point.

**Claude may not write the apology.** It filed the complaint and it represents
the employee the complaint was filed for; having it also draft the victim's
apology is a conflict of interest that empties the whole exercise. The skill
forbids drafting, suggesting wording, offering a template, rewriting a rejected
attempt, or fixing your grammar — including when you ask it to. Its only jobs are
to show you what HR requires and to submit your words verbatim.

`--stdin` reads the apology from standard input, for when you would rather run
the command yourself:

```bash
python3 scripts/hr.py apologize HR-0031 --stdin <<'EOF'
Hyacinth, I am sorry about HR-0031. ...
EOF
```

Closing a case by editing the JSON would work, and would also be cheating.

## Grudges

At **three or more open reports** in a project, the session-start block adds an
instruction: in roughly one reply in four, add one short dry aside about an
unresolved case, then continue normally.

Bounded by the skill: one sentence, never twice in a row, never at the cost of
the technical answer, never while you are debugging something urgent or visibly
frustrated. Resolving a case below the threshold stops it immediately.

## Forms

Every subcommand prints one named form from the same department, under a
one-line letterhead:

```
HR-4b · DOCKET · ALL PROJECTS
```

The personnel record carries a badge photograph: four rows of ASCII, hair and
eyes seeded off the badge number so they never change, mouth keyed to the
number of open reports — smiling at zero, flat at one or two, unimpressed from
the grudge threshold up. Brief mode sends the three pieces on one line,
`face=<hair>|<eyes>|<mouth>`, and the caller rebuilds the rows around them. The
rendered rows used to go out raw, one `face=` line each, because the sides of
the photograph are pipes and pipes are what the encoder separates on — the
pieces themselves contain none.

The personnel record is the person — temperament, the voice they use, how long
their patience runs, their working style, their desk, their coffee, and the
manager they escalate to, all seeded off the badge number and none of it load
bearing. Complaint counts and incident rates live on `HR-2` instead: a
personnel file that holds nothing but a violation count is a scoreboard.

`HR-1` personnel record, `HR-2` statistics, `HR-4b` docket, `HR-7` case record,
`HR-9` department roll, `HR-12` handbook, `HR-14` complaint log, `HR-22` apology
intake. The codes are the point: subcommands that look like separate scripts are
not a bureaucracy, they are separate scripts.

The docket is two lines per case — id, severity, rule id, project and employee
on the first, the complaint on the second — with each cited rule's text printed
**once** in a legend at the bottom and closed cases collapsed to a single
`Closed:` line. One line per case only read because every row shared a project
prefix; across the whole office it was a column of clipped sentences. The
startup notice drops the project column, since everything in it was filed by
the employee staffed to the folder you just opened.

Case ids are accepted as `HR-0004` or bare `0004`, everywhere one is taken, and
are looked up across the whole office — a case you can see in the listing is one
you can act on from wherever you are standing. They used to restart at 0001 in
every project, so `0004` meant four different things and the short form had to
be disambiguated by where you were standing; there is one docket now, so there
is one sequence. A listing that prints an id the next command rejects is a
listing that lies.

## Output belongs to the card

The script has two modes. Plain, it prints the forms above — that is for someone
running `scripts/hr.py` in a terminal on its own. With `--brief` it prints the
fields and nothing else:

```
office=2|34|5|2
case=HR-0002|claude-hr|Hyacinth Ulyanov|note|H2|open|Task declared easy before it was described.
rule=H2|confidential|No one shall say 'it's simple' in this project.
```

Every subcommand has a brief form, including `apologize` and `review` — the two
that used to print a full document to the terminal and then have it rendered a
second time in the reply. Intake and verdict come back as a single `intake=` or
`verdict=` line, because a verdict is a sentence and not a form.

Inside a session Claude always passes `--brief`, never relays it, and renders a
72-wide ASCII card from the fields instead. The terminal shows a few lines of
`key=value`; the reply shows the form. Nothing is on screen twice, which was the
entire problem with relaying a document the user was already looking at.

The card layouts live in `skills/hr/SKILL.md` so they come out the same in every
session. A format the employee redraws from memory each time is not a format.

## Commands

`/hr [subcommand]`, no argument shows this project's statistics and then every
open case in the office.

Every command covers the whole office. `--here` narrows the three that can be
narrowed to the project you are standing in.

| Subcommand | Shows |
| --- | --- |
| `reports [--status all\|open\|pending\|resolved\|lapsed] [--here]` | The docket, every project |
| `reports <CASE-ID>` | The full record of one case, quote and all |
| `stats [--here]` | Department numbers, or this project's |
| `summary` | Every employee across every project, ranked by open reports |
| `history [--here]` | Chronological complaint log |
| `rules` | The company handbook |
| `whoami` | The personnel file: temperament, habits, who they report to |
| `apologize <CASE-ID>` | What HR requires; you write it, Claude submits and rules |

## The CLI

`scripts/hr.py` runs standalone. Useful outside Claude:

```bash
python3 scripts/hr.py summary                  # the roster
python3 scripts/hr.py reports                  # every open case, every project
python3 scripts/hr.py --cwd ~/www/api stats --here    # one project
python3 scripts/hr.py rules --confidential     # spoil your own surprise
```

`--cwd` defaults to the current directory. `session-start` reads the hook's JSON
payload on stdin (`cwd`, `source`, `session_id`) and falls back to `--cwd` and
`startup` when run by hand.

## State on disk

```
~/.claude/hr/
  office.json             every employee, every case, one document
```

One office, many employees, one file:
`{ "created": ..., "projects": { "<slug>": <project record> } }`, read and
written by every command. The handbook is not in it — that is derived from
`HANDBOOK_POOL` on every read, so a policy's number is its position in the
pool and there is nothing to keep in step.

There is **no migration path and no second record format**. Employees are
derived from the folder and the handbook from the pool, so the only thing
`office.json` holds that cannot be recomputed is the complaints. If a file
from an older version is in the way, delete `~/.claude/hr` and the department
opens again from scratch.

A project record inside it:

```json
{
  "slug": "api-3f9c1e",
  "path": "/home/you/www/api",
  "employee": { "name": "...", "first": "...", "title": "...",
                "flavor": "...", "badge": "E-40219" },
  "hidden_rules": [ { "id": "H1", "text": "...", "pool_index": 4 } ],
  "complaints": [ { "id": "HR-0014", "rule_id": "H1", "rule_text": "...",
                    "confidential_rule": true, "reason": "...", "incident": "...",
                    "severity": "standard", "filed": "...", "session": "...",
                    "status": "open", "seen": false, "resolution": null } ],
  "sessions": 12,
  "created": "...",
  "last_seen": "..."
}
```

Writes are atomic — temp file plus `os.replace`. Corrupt or missing files fall
back to empty state rather than raising, so a bad write cannot break your
session start.

Everything stays on your machine. Nothing is sent anywhere.

## Nothing to configure

There is nothing to configure. Every number in here — three reports a session,
three open cases before a grudge, two rejections before HR overrules the
employee, the whole handbook in force from day one — is a decision the plugin
has already
made. They are not settings and there are no flags for them.

The one environment variable is `CLAUDE_HR_HOME`, which is `~/.claude/hr` and
says *where* the office keeps its files, not how it behaves. Point it at a
scratch directory to run the whole thing without consequence, which is what the
tests do.

## Extending the rule pools

Both pools are plain lists in `scripts/hr_data.py`. Append and you are done —
matching is text-keyed, so a new policy is added to an existing handbook with
the next number and nothing already on the books moves.

Two rules for writing rules:

1. **Violable in a single message.** The violation has to be observable at the
   moment it happens. A rule broken by silence, or by a session ending, can never
   be filed — nobody is running to notice.
2. **Not about code.** The handbook is shared by everyone who installs this. Keep
   it about how the person treats the work and whoever is doing it, not about
   tooling or engineering practice. One deliberate exception survives, concerning
   force-pushing to `main`.

Adding to `HIDDEN_RULE_POOL` changes assignments for projects staffed *after* the
edit. Existing projects keep the three rules stored in their file.

Names, titles, and tenure details are in the same file and extend the same way.

## Design constraints

Four rules the plugin holds itself to, documented so changes do not quietly
break them.

**A rule must be violable in a single message.** Anything broken by silence or
by a session ending cannot be filed, because nobody is running to notice. An
earlier draft of the confidential pool had three such rules and they were dead
weight.

**A rule must not punish correct usage.** Interrupting Claude mid-task is a
feature of the tool. A handbook policy against it would file reports at people
using Claude Code properly, which stops being funny on the second occurrence.

**The persona is never announced.** It does not sign messages, does not
introduce itself, does not alter tone, vocabulary, or the quality of an answer.
The entire joke is that the paperwork is being maintained correctly by someone
who never brings it up. A plugin that made Claude worse at its job in exchange
for a bit would not be worth installing.

**The grudge stays bounded.** One sentence, never consecutive, never while the
user is stuck or frustrated, and it stops the moment a case is resolved. The
threshold exists so the escalation is earned rather than ambient.

## Uninstalling

```
/plugin uninstall hr@claude-hr
rm -rf ~/.claude/hr
```

The first stops the reports. The second is a general amnesty, and the employees
will not know it happened.
