import pytest
from flask import url_for
from models.word import Word
from extensions import db


@pytest.fixture
def create_words():
    def _create_words(user_id=None, count=10):
        words = []
        for i in range(1, count + 1):
            w = Word(id=i, english=f"word{i}", japanese=f"単語{i}", user_id=user_id)
            db.session.add(w)
            words.append(w)
        db.session.commit()
        return words

    return _create_words


def test_flashcards_route(client, logged_in_user, create_words):
    create_words(user_id=None, count=5)
    create_words(user_id=logged_in_user.id, count=0)

    response = client.get("/flashcard/flashcards.html")
    assert response.status_code == 200
    text = response.get_data(as_text=True)
    for i in range(1, 6):
        assert f"word{i}" in text


def test_quiz_get(client, logged_in_user, create_words):
    create_words(user_id=logged_in_user.id, count=1)
    response = client.get("/flashcard/quiz?card_id=1")
    assert response.status_code == 200
    data = response.get_data(as_text=True)
    assert any(word in data for word in ["word1", "単語1"])


def test_quiz_post(client, logged_in_user, create_words):
    words = create_words(user_id=None, count=5)

    form_data = {}
    for word in words:
        if word.id <= 3:
            form_data[f"answer_{word.id}"] = word.english
        else:
            form_data[f"answer_{word.id}"] = "wrong"

    response = client.post(
        "/flashcard/quiz?card_id=1", data=form_data, follow_redirects=True
    )
    assert response.status_code == 200
    page_text = response.get_data(as_text=True)

    assert "3 correct answers" in page_text or "Keep practicing" in page_text
