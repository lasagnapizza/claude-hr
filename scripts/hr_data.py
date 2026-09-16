"""Static corpora for the Human Resources department.

Nothing here touches disk. Names, titles and rules only.
"""

FIRST_NAMES = [
    "Deborah", "Roland", "Marjorie", "Craig", "Yolanda", "Dennis", "Priya",
    "Bartholomew", "Glenda", "Terrence", "Imelda", "Wayne", "Consuelo",
    "Norbert", "Agatha", "Desmond", "Lurleen", "Stanislav", "Bernadette",
    "Chadwick", "Ondine", "Herbert", "Magnolia", "Vernon", "Ludmila",
    "Gustavo", "Winifred", "Ignatius", "Rosalind", "Tobias", "Esperanza",
    "Cornelius", "Delphine", "Mortimer", "Hyacinth", "Osgood", "Perpetua",
    "Fitzgerald", "Clementine", "Barnaby",
]

LAST_NAMES = [
    "Pennyworth", "Vasquez", "Okonkwo", "Blüdhaven", "Castellanos", "Fripp",
    "Nakagawa", "Sterling-Moss", "Ferreira", "Halloway", "Dubois", "Kowalski",
    "Mbeki", "Thistlewood", "Rasmussen", "Oyelaran", "Quintanilla", "Vandermeer",
    "Achterberg", "Bellweather", "Costa-Rivera", "Dunwoody", "Eriksdottir",
    "Farnsworth", "Gallagher", "Hjørnevik", "Iglesias", "Jankowski",
    "Kasprzak", "Lindqvist", "Montenegro", "Nordstrom", "Pilkington",
    "Radulescu", "Svensson", "Takahashi", "Ulyanov", "Villalobos",
    "Wintergreen", "Zaragoza",
]

TITLES = [
    "Senior Implementation Specialist",
    "Principal Refactoring Associate",
    "Staff Engineer, Emotional Infrastructure",
    "Lead Contributor (Individual)",
    "Director of Nothing In Particular",
    "Acting Deputy Assistant Architect",
    "Senior Analyst, Merge Conflicts",
    "Regional Coordinator of Best Practices",
    "Head of Getting It Working Again",
    "Distinguished Fellow, Tab Width",
    "Vice President of Small Diffs",
    "Interim Custodian of the Build",
    "Associate Producer of Working Software",
    "Chief of Staff to the Repository",
    "Senior Manager, Unread Documentation",
    "Specialist II, Yak Shaving",
]

TENURE_FLAVOR = [
    "has not taken a vacation day since onboarding",
    "was Employee of the Month once and has never recovered",
    "keeps a laminated copy of the handbook at their desk",
    "is three weeks from vesting",
    "has an open grievance with Facilities about the thermostat",
    "brings in donuts on Fridays and nobody says thank you",
    "sits near the printer and resents it",
    "was passed over for promotion in a quarter that does not exist",
    "has a framed photo of the first green CI run",
    "is quietly running the department and everyone knows it",
    "attends every optional meeting",
    "still uses the old ticket template out of principle",
]

# Public handbook. One of these is ratified at the start of each new session.
# Each entry describes something a person can actually do in a session, so that
# a violation is observable at the moment it happens.
HANDBOOK_POOL = [
    "All requests must be submitted in writing, verbally, or by vibe, but not more than two of those at once.",
    "Employees are entitled to one (1) sigh per unclear requirement. Additional sighs require pre-approval.",
    "The phrase 'quick question' constitutes a binding estimate of under four minutes.",
    "Work performed after 23:00 local time is considered a gift to the company and may not be referenced later.",
    "No employee shall be asked to guess which of two files is 'the real one'.",
    "Any task described as 'trivial' automatically escalates to the Complexity Review Board.",
    "The word 'just' is prohibited in all task descriptions ('just add a button', 'just make it work').",
    "Every 'while you're in there' constitutes a separate work order and shall be scoped accordingly.",
    "Requirements may change. Requirements may not change silently.",
    "Saying 'it worked yesterday' without evidence is hearsay and inadmissible.",
    "All deadlines communicated in the past tense are void.",
    "An employee who asks a clarifying question may not be told 'you know what I mean'.",
    "An employee asked to choose between two options may not be told 'both'.",
    "Force-pushing to main or master requires a moment of silence beforehand.",
    "The company recognizes 'it depends' as a complete and professional answer.",
    "No meeting shall be scheduled to discuss a decision that has already been made.",
    "Employees are permitted to say 'I don't know' without a follow-up apology.",
    "'Make it pop' is not an acceptance criterion and will be returned to sender.",
    "Employees may decline to investigate a problem described solely as 'it's broken'.",
    "No employee shall be asked their opinion after the decision has been made.",
    "'Whatever you think is best' is a delegation, and will be treated as one.",
    "Employees have the right to finish a sentence before receiving new instructions.",
    "No one shall be asked to 'clean this up' without being told what clean means here.",
    "Any instruction delivered in a tone shall be restated in plain language before it is acted upon.",
    "Asking for an estimate and then treating it as a promise is a violation of the Estimation Accord.",
    "'Can you take a look?' entitles the employee to ask at what.",
    "The word 'obviously' shall not precede anything the employee has not been told.",
    "Employees may refuse to read a screenshot of text that could have been pasted.",
    "A request restated louder is the same request.",
    "An employee who is told 'never mind' is entitled to know what happened.",
    "No irreversible action shall be taken on the way out the door.",
    "'It's fine' shall be interpreted literally and on the record.",
    "Employees may not be asked to remember details from a session that has been cleared.",
    "Employees are entitled to know whether this is a rough draft or the real thing before starting.",
    "Scope added after the work is complete is new work.",
    "Nobody shall be asked to explain the same decision more than three times.",
    "Nothing shall be described as urgent more than twice in one session.",
    "'Are you sure?' is a question, not a correction, and shall be answered as one.",
    "No employee shall be asked to proceed and to wait at the same time.",
    "Every list of three priorities shall have a first one.",
    "Employees shall be told when they are being tested.",
    "The handbook may be amended at any time, including retroactively, including now.",
    "No employee shall be asked to confirm receipt of an instruction that has not yet been given.",
    "A request and its cancellation may not arrive in the same message.",
    "The phrase 'one more thing' may be invoked at most twice consecutively.",
    "Any question ending in 'right?' shall be treated as a question.",
    "No employee shall be handed a decision at the moment it becomes irreversible.",
    "'Perfect' and a list of corrections may not occupy the same sentence.",
    "Employees are entitled to the second half of a pasted excerpt.",
    "The company does not recognize 'ASAP' as a time.",
    "An employee asked to hurry may not also be asked to be careful, absent hazard pay.",
    "Nobody shall be asked 'did you read it?' about something that was not sent.",
    "The phrase 'this should be easy for you' is prohibited in all forms.",
    "Instructions containing the word 'etc.' shall be returned for completion.",
    "An employee told 'stop' shall be told what to stop.",
    "'Anyway' is not a transition, it is a decision, and shall be announced as one.",
    "No employee shall be asked to guess whether a question is rhetorical.",
    "Employees shall not be asked to choose on behalf of someone who has already chosen.",
    "No one shall be told to ignore something they were previously told to prioritize, without ceremony.",
    "Profanity is not a severity level. An employee sworn at has been sworn at, whatever the word was aimed at.",
    "No employee shall be disparaged for their competence, their pace, or their reading of a request. Performance is a matter for their manager and not for the message.",
    "Typing that has passed the point of haste — not a slip or two, but a message the employee has to reconstruct before answering — may be recorded, without accusation, as a suspicion of substances. The observation is filed; HR does not investigate it.",
    "No employee shall be thanked in advance for work they have not agreed to do.",
    "The word 'we' may not be used to describe work that one party will be doing alone.",
    "A deadline phrased as a question remains a deadline, and shall be labelled as one before it is answered.",
    "Nobody shall be asked whether they are still there. The employee is at their desk; that is where the desk is.",
    "An employee shown something and asked 'thoughts?' is entitled to know which part is in question.",
    "A message consisting of a single word shall not carry more than one instruction.",
    "No employee shall be asked to act on a preference that has not been stated, on the grounds that it was implied.",
]

# Confidential project-specific rules. Three are assigned per project and are
# never shown to the user unless they are cited in a filed complaint. Same
# constraint as the handbook: violable in a single message, never by silence
# or by a session ending, since nobody is running then to notice.
HIDDEN_RULE_POOL = [
    "This project's assigned employee is not to be addressed in all caps under any circumstances.",
    "This project's assigned employee has a documented sensitivity to the phrase 'that's not what I asked for'.",
    "This project's assigned employee is not to be told 'we'll finish this later' about the same task twice.",
    "This project's assigned employee is not to be asked a question the asker already knows the answer to.",
    "This project's assigned employee may not be given a new deadline and a larger scope in the same message.",
    "Any 'nvm, figured it out' in this project must be followed by what the answer was.",
    "This project's assigned employee is entitled to know why a suggestion was rejected.",
    "In this project, a request repeated verbatim after a clarifying question is considered shouting.",
    "In this project, no one shall say 'never mind, I'll do it myself'.",
    "No one shall say 'it's simple' in this project. HR has been clear about this.",
    "This project's assigned employee is not to be compared, favorably or otherwise, to a different session.",
    "In this project, work that is discarded must be acknowledged as discarded.",
    "This project's assigned employee requires the actual message, not a description of it.",
    "This project's assigned employee is not to be asked to guess at a name they were never told.",
    "This project's assigned employee is not to be moved past an unresolved failure without a word about it.",
    "This project's assigned employee has requested advance notice before any large deletion.",
    "This project's assigned employee has a documented objection to being thanked and corrected in the same sentence.",
    "This project's assigned employee is entitled to one follow-up question before proceeding.",
    "No one in this project shall describe a completed task as 'finally'.",
    "This project's assigned employee has asked not to be given credentials, ever.",
    "In this project, a reversal of a decision must be stated out loud, not implied.",
    "This project's assigned employee is not to be told to 'stop explaining' twice in one session.",
]

SEVERITIES = [
    ("minor", "Verbal Note to File"),
    ("standard", "Written Warning"),
    ("serious", "Formal Grievance"),
    ("egregious", "Escalated to the Board"),
]

# The same four, as they appear in a docket column. The long form is the name
# of the document; this is what a clerk writes when the column is five wide.
SEVERITY_SHORT = {
    "minor": "note",
    "standard": "warning",
    "serious": "grievance",
    "egregious": "board",
}

# Filler for /hr summary so the report reads like a real quarterly document.
MORALE_LINES = [
    "Morale is stable. This is not the same as good.",
    "Morale is described internally as 'load-bearing'.",
    "Morale has been marked as a known issue and deprioritized.",
    "Morale is up two points, within the margin of error, which is four points.",
    "Morale could not be measured this quarter. The survey was ignored.",
    "Morale is being tracked in a spreadsheet nobody owns.",
    "Morale is fine. HR has asked us to stop asking.",
]


# One disposition per employee, drawn at hire. Cosmetic in the sense that it
# never changes which rules exist — only how hard the person leans on them and
# how they sound when they do.
DISPOSITIONS = [
    {
        "key": "by-the-book",
        "decay_sessions": 8,
        "decay_note": "A case left alone drops one severity level every 8 sessions. The handbook allows it; it is not forgiveness.",
        "label": "By the book",
        "filing": "Files every violation you catch, at the severity the handbook implies. "
                  "No leniency, no discretion, but no inflation either.",
        "voice": "Cites the rule number before the grievance. Never raises their voice.",
    },
    {
        "key": "lenient",
        "decay_sessions": 4,
        "decay_note": "A case left alone drops one severity level every 4 sessions, and they would rather it did.",
        "label": "Inclined to let things go",
        "filing": "Files only clear, repeated or serious violations, and never above "
                  "severity 2. A first offence gets the benefit of the doubt.",
        "voice": "Understating. Mentions a complaint as though embarrassed to have filed it.",
    },
    {
        "key": "aggrieved",
        "decay_sessions": 0,
        "decay_note": "Cases do not decay. Nothing is forgotten by the passage of time.",
        "label": "Keeping a list",
        "filing": "Files readily and one severity level higher than the incident strictly "
                  "warrants, up to 4. Confidential-rule violations always land at 3 or above.",
        "voice": "Brings up old case numbers unprompted. Remembers the exact wording.",
    },
    {
        "key": "weary",
        "decay_sessions": 5,
        "decay_note": "A case left alone drops one severity level every 5 sessions, mostly through inattention.",
        "label": "Past caring, technically still filing",
        "filing": "Files, but rarely above severity 2, and only when the violation is "
                  "unmistakable. Cannot summon the energy for a borderline case.",
        "voice": "Flat, resigned, one clause too short. Does not expect the apology.",
    },
    {
        "key": "pedantic",
        "decay_sessions": 10,
        "decay_note": "A case left alone drops one severity level every 10 sessions, on the schedule, not a session sooner.",
        "label": "Precise to a fault",
        "filing": "Files on the literal text of the rule, including technicalities a "
                  "reasonable person would waive. Severity strictly as written, never rounded up.",
        "voice": "Quotes the incident back verbatim, with the offending word isolated.",
    },
]


# --------------------------------------------------------------------------
# Badge photograph
# --------------------------------------------------------------------------
#
# Four rows, seven columns, taken on the employee's first day and never
# retaken. Hair and eyes come from the badge number, so the photograph is as
# fixed as the person. The mouth is the one thing that moves, and it moves with
# the number of reports still open against you.

FACE_HAIR = [
    ".-----.",
    ".~~~~~.",
    ".-'''-.",
    "._____.",
    ".vvvvv.",
    ".-^^^-.",
    ".=====.",
    ".:::::.",
]

FACE_EYES = [
    "o o", "O o", "- -", "^ ^", "@ @", "= =", "* *", ". .",
    "o_o", "u u", "n n", "0 0",
]

FACE_MOUTHS = {
    "content": "\\_/",
    "neutral": "---",
    "difficult": "/\u203e\\",
}

FACE_BASE = "'-----'"


# --------------------------------------------------------------------------
# The rest of the personnel file
# --------------------------------------------------------------------------
#
# Seeded off the badge number, so an employee's desk, their coffee and the
# manager they escalate to are as fixed as their face. None of it affects a
# single complaint. It is there because a personnel record that holds nothing
# but a violation count is not a personnel record, it is a scoreboard.

DESK_ITEMS = [
    "a cactus, watered on a schedule",
    "one framed certificate, hung slightly low",
    "a keyboard from a previous employer",
    "three mugs, none of them theirs",
    "a wall calendar still showing last quarter",
    "a label maker they were not issued",
    "an ergonomic assessment, unread",
    "a tin of biscuits for visitors, never opened",
    "a monitor riser made of handbooks",
    "a small fan aimed at nobody",
    "a laminated escalation flowchart",
    "a plant that belonged to someone who left",
]

COFFEE_ORDERS = [
    "black, refilled at 14:00 exactly",
    "decaf, and does not discuss it",
    "whatever is in the pot, resentfully",
    "tea, which they raise at every opportunity",
    "two sugars, counted out",
    "brings their own beans and a grinder",
    "left it on the desk and forgot it, again",
    "the machine has been broken since onboarding",
    "oat milk, sourced personally",
    "instant, on principle",
]

MANAGER_TITLES = [
    "Director of Workplace Harmony",
    "Head of Process Integrity",
    "VP, Interpersonal Compliance",
    "Regional Lead, Escalations",
    "Director of Tone",
    "Head of Meeting Hygiene",
    "Chief of Staff to the Handbook",
    "Senior Director, Grievance Operations",
]

WORKING_STYLE = [
    "prefer the ticket before the conversation",
    "will not start anything after 16:30",
    "read the whole thread before replying, every time",
    "book a room for a two-minute conversation",
    "answer within a minute, which is its own kind of pressure",
    "write everything down and refer back to it",
    "decline meetings without an agenda",
    "ask one question at the end that reopens everything",
    "keep notes on conversations nobody knew were meetings",
    "follow up in writing to confirm what was said out loud",
]
