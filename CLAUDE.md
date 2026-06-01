# CLAUDE.md

## What this project is
A Python basics quiz web app built with Flask. It presents multiple-choice questions one at a time, tracks the user's score in a session, and shows a results page at the end. Built as a capstone for the Code2College Applied AI Cohort.

## Tech stack
- Python 3.10+, Flask 3.x, Jinja2 templates, vanilla HTML/CSS
- No database — questions live in a Python list in questions.py
- pytest for tests

## Conventions
- Use type hints on all functions
- Keep functions small and focused
- No global state — use Flask session for score tracking

## Do not
- Add new dependencies without asking
- Modify tests to make them pass
- Add a database or ORM
