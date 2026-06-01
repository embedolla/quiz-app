import random

from flask import Flask, Response, redirect, render_template, request, session, url_for

from questions import QUESTIONS


def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = "dev-secret-key"

    @app.route("/")
    def index() -> str:
        if session.get("question_index") is None or session.get("question_order") is None:
            session["question_index"] = 0
            session["score"] = 0
            session["question_order"] = random.sample(range(len(QUESTIONS)), len(QUESTIONS))
        idx = session["question_index"]
        q_idx = session["question_order"][idx]
        return render_template(
            "question.html",
            question=QUESTIONS[q_idx],
            index=idx,
            total=len(QUESTIONS),
            score=session["score"],
        )

    @app.route("/answer", methods=["POST"])
    def answer() -> Response:
        idx = session["question_index"]
        q_idx = session["question_order"][idx]
        choice = int(request.form["choice"])
        correct = choice == QUESTIONS[q_idx]["answer"]
        if correct:
            session["score"] += 1
        session["feedback_correct"] = correct
        session["feedback_answer"] = QUESTIONS[q_idx]["choices"][QUESTIONS[q_idx]["answer"]]
        session["question_index"] = idx + 1
        return redirect(url_for("feedback"))

    @app.route("/feedback")
    def feedback() -> str:
        correct = session.get("feedback_correct", False)
        correct_answer = session.get("feedback_answer", "")
        done = session.get("question_index", 0) >= len(QUESTIONS)
        return render_template(
            "feedback.html",
            correct=correct,
            correct_answer=correct_answer,
            done=done,
        )

    @app.route("/results")
    def results() -> str:
        score = session.get("score", 0)
        session.clear()
        return render_template("results.html", score=score, total=len(QUESTIONS))

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
