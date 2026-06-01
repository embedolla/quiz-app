from questions import QUESTIONS


def test_correct_answer_increments_score(client):
    client.get("/")
    correct = str(QUESTIONS[0]["answer"])
    client.post("/answer", data={"choice": correct})
    with client.session_transaction() as sess:
        assert sess["score"] == 1


def test_finish_redirects_to_results(client):
    client.get("/")
    for q in QUESTIONS[:-1]:
        client.post("/answer", data={"choice": str(q["answer"])})
    r = client.post("/answer", data={"choice": str(QUESTIONS[-1]["answer"])})
    assert r.status_code == 302
    assert r.headers["Location"] == "/results"
