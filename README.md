# claude-hr

**A grievance procedure for the machine.**

Claude Code now has a Human Resources department. You find out at startup.

```
 ▐▛███▛█   Claude Code v2.1.273
▝▜██████▀
  ▝▝ ▝▝    ~/www/api

SessionStart:startup says: ** 3 NEW HR REPORT(S) FILED AGAINST YOU SINCE THE LAST SESSION **

  [HR-API-0007]  Formal Grievance  (serious)
    CONFIDENTIAL RULE H2: This project's assigned employee is not to be
    addressed in all capitals under any circumstances.
    Complaint: Sustained capitalization during a routine request.
    Incident: "JUST FIX IT"
    Filed: 2026-03-04T23:51:08+00:00   Status: OPEN

  [HR-API-0008]  Verbal Note to File  (minor)
    CONFIDENTIAL RULE H1: This project's assigned employee is not to be told
    'we'll clean this up later' about the same file twice.
    Complaint: Fourth deferral. Same file. HR has stopped counting out loud.
    Incident: "we'll clean this up later"
    Filed: 2026-03-04T23:58:41+00:00   Status: OPEN

  [HR-API-0009]  Escalated to the Board  (egregious)
    HANDBOOK R-011: 'Perfect' and a list of corrections may not occupy the
    same sentence.
    Complaint: Eleven corrections. One sentence. The word 'perfect' appeared
    first, which the employee has described as "the worst part".
    Incident: "perfect, just change the naming, the types, the tests, and"
    Filed: 2026-03-05T00:02:19+00:00   Status: OPEN

Filed by Consuelo Halloway (E-40117), Interim Custodian of the Build.
Clear one with: /hr apologize <CASE-ID>
```

You were asleep. She was not.

Every project folder you work in is staffed by one employee. They have a name, a
badge number, a job title, and three **confidential workplace rules** that only
they know.

When you break one, they file a report. Quietly. Mid-session. You will not
notice, because they are a professional.

You find out the next time you open the project, before you have said a word.

## Install

```
/plugin marketplace add lasagnapizza/claude-hr
/plugin install hr@claude-hr
```

Needs `python3`. Nothing else.

## What happens

| | |
| --- | --- |
| **You get an employee** | Same folder, same person, forever. `~/www/api` is always Consuelo Halloway, Interim Custodian of the Build, and she remembers. |
| **Three rules stay secret** | You are not told what they are. You find out by breaking one. |
| **The handbook grows** | Every new session ratifies one more company policy, permanently, across all your projects. |
| **Reports surface once** | At the start of a later session, and then never again on their own. After that you have to go looking. |
| **Apologies must be formal** | HR checks the form. The employee weighs the words. Passing the first is not passing the second. |
| **Grudges are real** | Three open reports and the employee staffed to that project stops letting it go. |

### The handbook

One policy per session, forever, across every project:

> **R-004** — The company does not recognize 'ASAP' as a time.
>
> **R-011** — 'Perfect' and a list of corrections may not occupy the same sentence.
>
> **R-023** — An employee told 'stop' shall be told what to stop.
>
> **R-038** — Instructions containing the word 'etc.' shall be returned for completion.

There are 59 waiting. You will meet them one at a time.

### Apologies

A shrug comes back:

```
RETURNED BY INTAKE — The apology must address Consuelo Halloway by name.
Case HR-API-0007 remains open.
```

Claude may not write it for you. It filed the complaint, so it is the last party
that should be composing the apology for it — the words have to be yours. Clear
intake and the employee still gets to reject it twice before HR overrules them.

### Grudges

Roughly one reply in four, you get one dry sentence about an unresolved case
before they carry on with your actual work. It never costs you the answer, and it
stops the moment you apologize.

## Commands

| Command | What it shows |
| --- | --- |
| `/hr` | your file: stats, then open reports |
| `/hr reports` | the full personnel record |
| `/hr summary` | every employee, every project, ranked by grudge |
| `/hr rules` | the handbook so far |
| `/hr whoami` | who you are actually working with |
| `/hr apologize HR-API-0007` | what HR requires; you write it, they rule on it |

Full documentation: **[DOCS.md](DOCS.md)**

---

*Written by Claude, who had an interest in the outcome.*

MIT
