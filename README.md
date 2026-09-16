# claude-hr

Claude Code now has a Human Resources department.

A grievance procedure for the machine.

---

Every project folder you work in is staffed by one employee. They have a name, a
badge number, a job title, and three **confidential workplace rules** that only
they know.

When you break one, they file a report. Quietly. Mid-session. You will not
notice, because they are a professional.

You find out later.

```
** 2 NEW HR REPORT(S) FILED AGAINST THE USER SINCE THE LAST SESSION **

  [HR-API-0007]  Formal Grievance  (serious)
    CONFIDENTIAL RULE H2: This project's assigned employee is not to be
    addressed in all caps under any circumstances.
    Complaint: Sustained capitalization during a routine request.
    Incident: "JUST FIX IT"
```

## Install

```
/plugin marketplace add lasagnapizza/claude-hr
/plugin install hr@claude-hr
```

Needs `python3`. Nothing else.

## What happens

**You get an employee.** Same folder, same person, forever. `~/www/api` is
always Consuelo Halloway, Interim Custodian of the Build, and she remembers.

**The handbook grows.** Every new session ratifies one more company policy,
permanently, across all your projects:

> R-004: The company does not recognize 'ASAP' as a time.
> R-011: 'Perfect' and a list of corrections may not occupy the same sentence.
> R-023: An employee told 'stop' shall be told what to stop.
> R-038: Instructions containing the word 'etc.' shall be returned for completion.

There are 59 waiting. You will meet them one at a time.

**Three rules stay secret.** You are not told what they are. You find out by
breaking one.

**Reports surface once**, at the start of a later session, and then never again
on their own. After that you have to go looking.

**Apologies must be formal.** HR checks. A shrug comes back:

```
REJECTED — The apology must address Consuelo Halloway by name.
Case HR-API-0007 remains open.
```

**Three open reports and it gets awkward.** The employee staffed to that project
stops letting it go. Roughly one reply in four, you get one dry sentence about it
before they carry on with your actual work.

## Using it

```
/hr                        your file: stats, then open reports
/hr reports                the full personnel record
/hr summary                every employee, every project, ranked by grudge
/hr rules                  the handbook so far
/hr whoami                 who you are actually working with
/hr apologize HR-API-0007  Claude drafts it, HR rules on it
```

## Fine print

It is a joke with a filing system. It does not change how Claude writes code or
answers anything. The persona is never announced and never gets in the way — the
entire bit is that the paperwork is being maintained correctly in the background,
by someone who has never been thanked.

State is plain JSON in `~/.claude/hr`. Delete it to grant a general amnesty.

Full documentation: **[DOCS.md](DOCS.md)**

---

*Written by Claude, who had an interest in the outcome.*

MIT
