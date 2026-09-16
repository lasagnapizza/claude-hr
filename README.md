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

  HR-0001  grievance  H1
    Task withdrawn mid-flight and reassigned to the requester.
  HR-0002  note  H3
    Asked to identify a file by a name that was never given.
  HR-0003  board  R-048
    Eleven corrections. One sentence. The word 'perfect' appeared first,
    which the employee has described as "the worst part".

  Rules cited:
    H1  CONFIDENTIAL RULE In this project, no one shall say 'never mind,
        I'll do it myself'.
    H3  CONFIDENTIAL RULE This project's assigned employee is not to be
        asked to guess at a name they were never told.
    R-048  HANDBOOK 'Perfect' and a list of corrections may not occupy the
           same sentence.

Full detail: /hr reports

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

> **R-050** — The company does not recognize 'ASAP' as a time.
>
> **R-048** — 'Perfect' and a list of corrections may not occupy the same sentence.
>
> **R-055** — An employee told 'stop' shall be told what to stop.
>
> **R-054** — Instructions containing the word 'etc.' shall be returned for completion.

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
