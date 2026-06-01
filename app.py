from flask import Flask, render_template, session

from questions import QUESTIONS


def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = "dev-secret-key"

    @app.route("/")
    def index() -> str:
        session["question_index"] = 0
        session["score"] = 0
        return render_template(
            "question.html",
            question=QUESTIONS[0],
            index=0,
            total=len(QUESTIONS),
        )

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
