# BUILD_LOG.md

## Task 1 — Scaffold repo and write CLAUDE.md
- Brief: Create CLAUDE.md with project description, stack, conventions, and guardrails.
- What Claude proposed: A placeholder with empty sections.
- What I changed before approving: Rewrote it with the full Flask stack, conventions, and do-not list.
- Verification: CLAUDE.md visible on GitHub.
- One thing I learned: /init gives a starting point but you have to fill in what only you know.


## Task 2 — Create questions.py
- Brief: Create questions.py with 10 Python basics multiple choice questions.
- What Claude proposed: A typed list using TypedDict with 10 questions covering data types, strings, lists, functions, etc.
- What I changed before approving: Nothing — plan was clean.
- Verification: python -c "from questions import QUESTIONS; assert len(QUESTIONS) == 10"
- One thing I learned: TypedDict makes the data shape explicit without adding dependencies.

