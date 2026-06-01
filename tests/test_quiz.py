from questions import QUESTIONS


def test_correct_answer_increments_score(client):
    client.get("/")
    with client.session_transaction() as sess:
        q_idx = sess["question_order"][0]
    correct = str(QUESTIONS[q_idx]["answer"])
    client.post("/answer", data={"choice": correct})
    with client.session_transaction() as sess:
        assert sess["score"] == 1


def test_finish_links_to_results(client):
    client.get("/")
    for _ in range(len(QUESTIONS) - 1):
        client.post("/answer", data={"choice": "0"})
    r = client.post("/answer", data={"choice": "0"})
    assert r.status_code == 302
    assert r.headers["Location"] == "/feedback"
    r = client.get("/feedback")
    assert 'href="/results"' in r.data.decode()
