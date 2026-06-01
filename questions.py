from typing import TypedDict


class Question(TypedDict):
    question: str
    choices: list[str]
    answer: int


QUESTIONS: list[Question] = [
    {
        "question": "What does type(3.14) return?",
        "choices": [
            "<class 'int'>",
            "<class 'str'>",
            "<class 'float'>",
            "<class 'double'>",
        ],
        "answer": 2,
    },
    {
        "question": "What does len(\"hello\") return?",
        "choices": ["4", "5", "6", "hello"],
        "answer": 1,
    },
    {
        "question": "Which syntax creates a list in Python?",
        "choices": ["(1, 2, 3)", "{1, 2, 3}", "[1, 2, 3]", "<1, 2, 3>"],
        "answer": 2,
    },
    {
        "question": "Which keyword is used to define a function?",
        "choices": ["function", "func", "define", "def"],
        "answer": 3,
    },
    {
        "question": "What does range(3) produce?",
        "choices": ["1, 2, 3", "0, 1, 2, 3", "0, 1, 2", "1, 2"],
        "answer": 2,
    },
    {
        "question": "What is the result of 10 // 3?",
        "choices": ["3.33", "3", "4", "1"],
        "answer": 1,
    },
    {
        "question": "How do you access the value for key \"name\" in a dict called person?",
        "choices": [
            "person.name",
            "person[name]",
            "person(\"name\")",
            "person[\"name\"]",
        ],
        "answer": 3,
    },
    {
        "question": "What does not True evaluate to?",
        "choices": ["True", "False", "None", "0"],
        "answer": 1,
    },
    {
        "question": "Which loop is best for iterating over each item in a list?",
        "choices": ["while", "for", "loop", "repeat"],
        "answer": 1,
    },
    {
        "question": "Which keyword is used to catch an exception?",
        "choices": ["catch", "handle", "except", "error"],
        "answer": 2,
    },
]
