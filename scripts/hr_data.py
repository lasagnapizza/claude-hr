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
