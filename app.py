from flask import Flask, Response, redirect, render_template, request, session, url_for

from questions import QUESTIONS


def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = "dev-secret-key"

    @app.route("/")
    def index() -> str:
        if session.get("question_index") is None:
            session["question_index"] = 0
            session["score"] = 0
        idx = session["question_index"]
        return render_template(
            "question.html",
            question=QUESTIONS[idx],
            index=idx,
            total=len(QUESTIONS),
        )

    @app.route("/answer", methods=["POST"])
    def answer() -> Response:
        idx = session["question_index"]
        choice = int(request.form["choice"])
        if choice == QUESTIONS[idx]["answer"]:
            session["score"] += 1
        session["question_index"] = idx + 1
        if session["question_index"] >= len(QUESTIONS):
            return redirect(url_for("results"))
        return redirect(url_for("index"))

    @app.route("/results")
    def results() -> str:
        score = session.get("score", 0)
        session.clear()
        return render_template("results.html", score=score, total=len(QUESTIONS))

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
