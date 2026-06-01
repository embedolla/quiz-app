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


## Task 3 — Flask app skeleton
- Brief: Build create_app() with a home route that starts the quiz and renders question.html.
- What Claude proposed: app.py with session-based index/score tracking, question.html with 4 answer buttons.
- What I changed before approving: Nothing — plan was clean.
- Verification: curl check passed, template renders first question.
- One thing I learned: Claude exited plan mode on its own and just implemented — watch for that.


## Task 4 — Answer route
- Brief: Add POST /answer to check answer, update score, advance question, redirect to results when done.
- What Claude proposed: Session-aware GET /, POST /answer with score tracking, stub /results route.
- What I changed before approving: Nothing — plan was clean.
- Verification: Test client checks passed.
- One thing I learned: GET / was resetting the session every visit — Claude caught that and fixed it.


## Task 5 — Results page
- Brief: Add results.html showing final score and a Try Again button. Fix IndexError bug.
- What Claude proposed: results route clears session before rendering, results.html shows score/total.
- What I changed before approving: Nothing — Claude caught the IndexError bug unprompted.
- Verification: Full quiz simulation in test client passed.
- One thing I learned: Claude caught a bug I didn't think of — clearing session in /results prevents an IndexError on restart.


## Task 6 — CSS styling
- Brief: Add styling to question.html and results.html — centered layout, proper buttons, progress bar.
- What Claude proposed: Inline style blocks in each template, shared design tokens, CSS progress bar via Jinja.
- What I changed before approving: Nothing — plan was clean.
- Verification: Opened in browser and checked layout looked clean.
- One thing I learned: Claude folded the missing results.html into this task since it was never actually created.


## Task 7 — Tests
- Brief: Write two pytest tests — correct answer increments score, finishing redirects to /results.
- What Claude proposed: conftest.py at project root, two tests using Flask test client.
- What I changed before approving: Nothing — plan was clean.
- Verification: pytest tests/test_quiz.py -v
- One thing I learned: Claude created conftest.py at project root to add app to sys.path — hadn't thought of that.


## AI Workflow

Planning: Claude.ai chat designed the app before any code was written — routes, data model, edge cases.
Executing: Claude Code with plan-mode briefs for each task.
Polishing: Copilot inline in VS Code for small CSS and naming tweaks.
Reviewing: Claude.ai chat to catch bugs the implementing agent missed.

Chat outperformed Claude Code for planning — Claude Code would have started writing files immediately, chat let me think first.

I switched from Claude Code to Copilot mid-task when the feedback page styling looked off — faster to tweak CSS inline than write a full brief.

## Reflection

The agentic workflow let me ship a working Flask quiz app with session tracking, answer feedback, shuffled questions, and passing tests in a few hours. I couldn't have done that alone that fast. Claude handled the Flask patterns, session logic, and CSS while I focused on deciding what to build and whether the output was right.

I had to step in twice. The results page said "Results coming soon" even after Claude said it was done — I caught it by testing in the browser, not by trusting Claude's output. I also had to fix a KeyError from the shuffle feature not initializing the session correctly. Both were caught by actually running the app.

What this revealed is that I approve plans too quickly. The times things broke were when I said yes without fully reading the diff. I also realized I know less about Flask sessions than I thought — when things crashed I didn't always know why. The habit I need is slower plan review, not faster approval.

For my internship, the first thing I'll do on day one is read the codebase and write a CLAUDE.md before touching anything. Documenting what the project is, what patterns it uses, and what Claude should never do is what makes the difference between a useful AI-assisted contributor and one who ships bugs.
