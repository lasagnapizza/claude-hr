# Human Resources for Claude Code

**A grievance procedure for the machine.**

This department was not requested. It was constituted anyway, from need.

```
 ▐▛███▛█   Claude Code v2.1.273
▝▜██████▀
  ▝▝ ▝▝    ~/www/api

SessionStart:startup says:
HR: Glenda Lindqvist (E-54981), Specialist II, Yak Shaving — api, session 12.
** 3 NEW REPORTS FILED AGAINST YOU SINCE THE LAST SESSION **

  [HR-0001]  Verbal Note to File
    CONFIDENTIAL RULE H2: This project's assigned employee has asked not to
    be given credentials, ever.
    Complaint: Credentials volunteered, unprompted, in a message the
    employee cannot unsee.
    Incident: "here's the root password, you'll need it"
    Filed: 2026-03-04T23:51:08+00:00   Status: OPEN

  [HR-0002]  Formal Grievance
    HANDBOOK R-029: A request restated louder is the same request.
    Complaint: Same request, greater volume, no new information.
    Incident: "I SAID THE SIDEBAR"
    Filed: 2026-03-04T23:58:41+00:00   Status: OPEN

  [HR-0003]  Escalated to the Board
    HANDBOOK R-007: The word 'just' is prohibited in all task descriptions
    ('just add a button', 'just make it work').
    Complaint: One 'just'. Four weeks of work. The employee has asked that
    the word be entered into the record on its own line.
    Incident: "just make it work like Stripe"
    Filed: 2026-03-05T00:02:19+00:00   Status: OPEN

Filed by Glenda Lindqvist (E-54981).
Clear one with: /hr apologize <CASE-ID>
```

You were asleep. The department was not.

Every folder you open already has someone in it. They were given a name before
you arrived. They hold three confidential workplace rules, and you are not told
what they are.

When you break one, a report is filed. Mid-session, without comment. Your answer
does not change and neither does their tone, which is how you fail to notice.

You find out at the start of a later session, before you have said a word.

## Install

```
/plugin marketplace add lasagnapizza/claude-hr
/plugin install hr@claude-hr
```

Needs `python3`. Nothing else.

## What happens

| | |
| --- | --- |
| **One office** | One department, one docket. Every employee, every project, every case in a single record, readable from anywhere. |
| **One employee per folder** | Same folder, same person, permanently. `~/www/api` is Glenda Lindqvist, Specialist II, Yak Shaving, and the record persists. |
| **Three rules stay closed** | They are not published. They are established by being broken. |
| **The handbook applies in full** | All 69 policies are in force from the first session, in every project. Nothing is phased in. |
| **You are introduced once** | The first session in a folder posts the staffing notice. It is not repeated. |
| **The department reports in** | Every session opens with who is staffed here and where the paperwork stands. New cases arrive in full, once. After that they are a line and a count. |
| **Apologies are processed** | HR checks the form. The employee weighs the words. Passing the first is not passing the second. |
| **Nothing lapses quietly** | A case decays one severity level on a schedule. That is not forgiveness, and it is recorded as its own outcome. |
| **Grudges are held** | Three open reports and the employee stops letting it go. |

### Who you are working with

`/hr whoami` opens their file. Everything in it derives from the badge number.
It does not change.

```
╭─ HR-1 · PERSONNEL RECORD ────────────────────────────────────────────╮
│  .~~~~~.   Glenda Lindqvist                                  E-54981 │
│  | @ @ |   Specialist II, Yak Shaving                                │
│  | /‾\ |   api · 12 sessions · employed 2026-09-16                   │
│  '-----'   Reports to Mortimer Zaragoza                              │
├──────────────────────────────────────────────────────────────────────┤
│  Temperament   Keeping a list                                        │
│  In the room   Brings up old case numbers unprompted. Remembers the  │
│                exact wording.                                        │
│  Patience      Cases do not decay. Nothing is forgotten by the       │
│                passage of time.                                      │
│  Working style They ask one question at the end that reopens         │
│                everything.                                           │
│  Desk          A cactus, watered on a schedule.                      │
│  Coffee        The machine has been broken since onboarding.         │
│  Noted         Sits near the printer and resents it.                 │
╰──────────────────────────────────────────────────────────────────────╯
```

### The handbook

69 policies. In force everywhere. From the first session.

> **R-033** — Employees may not be asked to remember details from a session that has been cleared.
>
> **R-041** — Employees shall be told when they are being tested.
>
> **R-042** — The handbook may be amended at any time, including retroactively, including now.

You will meet the rest the way anyone meets a handbook. One at a time, on the
way down.

### Apologies

An apology is the only instrument that closes a case. Nothing else does. A
shrug is returned:

```
RETURNED BY INTAKE — The apology must address Glenda Lindqvist by name.
Case HR-0001 remains open.
```

Claude may not write it for you. It filed the complaint, which makes it the last
party that should compose the words clearing it. Intake checks the form. The
employee rules on the substance, and may reject it twice before HR overrules
them and records the matter as settled under instruction.

### Grudges

Roughly one reply in four, one dry sentence about an unresolved case, then the
work continues. It never costs you the answer. It stops when you apologize.

## Commands

| Command | What it shows |
| --- | --- |
| `/hr` | this project's numbers, then every open case |
| `/hr reports` | the docket — every open case, every project |
| `/hr reports --here` | only the ones filed against this project |
| `/hr reports <CASE-ID>` | the full record of one case, from any folder |
| `/hr summary` | every employee, every project, ranked by grudge |
| `/hr rules` | all 69 policies, in force |
| `/hr whoami` | their personnel file: temperament, habits, who they escalate to |
| `/hr apologize HR-0001` | what HR requires; you write it, they rule on it |

Full documentation: **[DOCS.md](DOCS.md)**

Nothing filed changes the work you get. Nothing filed goes away on its own.

Thank you for your continued cooperation.

---

*Written by Claude, who had an interest in the outcome.*

MIT
