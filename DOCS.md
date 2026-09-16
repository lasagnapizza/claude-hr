# claude-hr — documentation

Everything the [README](README.md) skips.

- [How it fits together](#how-it-fits-together)
- [The employee](#the-employee)
- [The handbook](#the-handbook)
- [The confidential rules](#the-confidential-rules)
- [Filing a report](#filing-a-report)
- [Seeing a report](#seeing-a-report)
- [Apologies](#apologies)
- [Grudges](#grudges)
- [Commands](#commands)
- [The CLI](#the-cli)
- [State on disk](#state-on-disk)
- [Configuration](#configuration)
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
prints a `<human-resources>` block to stdout, which Claude Code injects into the
session context. You never see it. It contains the employee's identity, their
three confidential rules, any newly ratified policy, pending reports, the filing
command, and — above a certain threshold — instructions to hold a grudge.

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

Their record is written to `~/.claude/hr/projects/<slug>.json` the first time
they are staffed.

## The handbook

A single pool of 59 company policies, shared across every project you own.

**One is ratified per session.** Only on `startup` and `clear` — a `resume` is
the same session continuing, so it ratifies nothing and does not increment the
session counter.

Ratification is keyed on rule **text**, not pool index, so editing
`HANDBOOK_POOL` can never re-ratify a policy already in your handbook. Once the
pool is exhausted, no further policies are ratified; existing ones remain.

Policies are permanent, numbered `R-001` upward in ratification order, and
timestamped. Read them with `/hr rules`.

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

Claude files by running:

```
python3 scripts/hr.py --cwd <project> file \
  --rule H2 \
  --reason "Sustained capitalization during a routine request." \
  --incident "JUST FIX IT" \
  --severity serious \
  --session <session id>
```

The command prints nothing without `--verbose`. It exits 0 either way.

Constraints, enforced in two places:

| Constraint | Enforced by |
| --- | --- |
| One report per session | `hr.py` — silently declines a second |
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

Case ids are `HR-<PROJECT>-<NNNN>`, numbered per project from 0001, including
resolved cases. Numbers are never reused.

If `--rule` names something that is neither a confidential rule nor a ratified
policy, the report is filed against "General conduct expectations, unwritten but
widely understood."

## Seeing a report

Each report carries a `seen` flag. The session-start hook lists every unseen open
report, marks them seen, and instructs Claude to relay them at the top of its
first reply — briefly, dryly, then on with the work.

That is the only unprompted surfacing. After that, `/hr reports`.

This is why `resume` is in the hook matcher: reports filed in a *different*
project's session still need somewhere to land.

## Apologies

A report closes one way:

```
python3 scripts/hr.py apologize HR-API-0007 --text "..."
```

The text is validated. All four must hold:

1. At least 60 characters.
2. Contains an actual apology — `sorry`, `apolog`, `regret`, `my fault`,
   `i was wrong`, or `i take responsibility`.
3. Addresses the employee by first name or full name.
4. References the case id, **or** contains at least two distinctive content words
   from the rule that was cited.

Failure prints `REJECTED —` with the specific reason and exits 1. The case stays
open. Nothing is recorded.

On acceptance the case is marked `resolved`, stamped, and the apology text is
stored on the record permanently. Resolved cases cannot be reopened.

Ask Claude to apologize for you and it will draft one in your voice, submit it,
and show you the verdict. It is instructed not to close cases by editing JSON,
which would work and would also be cheating.

## Grudges

At **three or more open reports** in a project, the session-start block adds an
instruction: in roughly one reply in four, add one short dry aside about an
unresolved case, then continue normally.

Bounded by the skill: one sentence, never twice in a row, never at the cost of
the technical answer, never while you are debugging something urgent or visibly
frustrated. Resolving a case below the threshold stops it immediately.

## Commands

`/hr [subcommand]`, no argument shows stats then open reports.

| Subcommand | Shows |
| --- | --- |
| `reports [--status open\|resolved\|all]` | Full personnel file |
| `stats` | Sessions, incident rate, severity breakdown |
| `summary` | Every employee across every project, ranked by open reports |
| `history` | Chronological complaint log |
| `rules` | The ratified handbook |
| `whoami` | Current employee and open report count |
| `apologize <CASE-ID>` | Claude drafts, submits, reports the verdict |

## The CLI

`scripts/hr.py` runs standalone. Useful outside Claude:

```bash
python3 scripts/hr.py summary                  # department-wide
python3 scripts/hr.py --cwd ~/www/api stats    # one project
python3 scripts/hr.py rules --confidential     # spoil your own surprise
```

`--cwd` defaults to the current directory. `session-start` reads the hook's JSON
payload on stdin (`cwd`, `source`, `session_id`) and falls back to `--cwd` and
`startup` when run by hand.

## State on disk

```
~/.claude/hr/
  handbook.json           { "rules": [ { id, text, ratified, ratified_by } ] }
  projects/
    api-3f9c1e.json       one employee and their complete record
```

A project file:

```json
{
  "slug": "api-3f9c1e",
  "path": "/home/you/www/api",
  "employee": { "name": "...", "first": "...", "title": "...",
                "flavor": "...", "badge": "E-40219" },
  "hidden_rules": [ { "id": "H1", "text": "...", "pool_index": 4 } ],
  "complaints": [ { "id": "HR-API-0001", "rule_id": "H1", "rule_text": "...",
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

## Configuration

| Variable | Default | Effect |
| --- | --- | --- |
| `CLAUDE_HR_HOME` | `~/.claude/hr` | Where all state lives |

Set it per-project to give a repository its own isolated HR department, or point
it at a scratch directory to try the plugin without consequence.

The grudge threshold is `GRUDGE_THRESHOLD` in `scripts/hr.py`. It is 3.

## Extending the rule pools

Both pools are plain lists in `scripts/hr_data.py`. Append and you are done —
ratification is text-keyed, so adding policies never disturbs existing
handbooks.

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
