import pytest
from flask import url_for
from models.user import User
from models.word import Word
from app import app, db

@pytest.fixture
def new_word_data():
    return {
        "japanese": "テスト",
        "english": "test",
        "pronunciation": "tesuto",
    }

def test_words_access_protection(client):
    # GET /words without login should redirect to login #junior
    response = client.get("/words")
    assert response.status_code == 302
    assert "/login" in response.headers["Location"]

def test_add_word_get(client, logged_in_user):
    # GET add_word returns 200 #junior
    response = client.get("/add_word")
    assert response.status_code == 200

def test_add_word_post(client, logged_in_user, new_word_data):
    # POST add_word adds word #junior
    response = client.post("/add_word", data=new_word_data, follow_redirects=True)
    assert response.status_code == 200
    assert b"New word added successfully!" in response.data

    # Check word in DB #junior
    word = Word.query.filter_by(japanese=new_word_data["japanese"]).first()
    assert word is not None

def test_edit_word_get(client, logged_in_user, new_word_data):
    # Setup word to edit #junior
    word = Word(**new_word_data, user_id=logged_in_user.id)
    db.session.add(word)
    db.session.commit()

    response = client.get(f"/edit_word/{word.id}")
    assert response.status_code == 200
    assert b"form" in response.data

def test_edit_word_post(client, logged_in_user, new_word_data):
    # Setup word #junior
    word = Word(**new_word_data, user_id=logged_in_user.id)
    db.session.add(word)
    db.session.commit()

    data = {
        "japanese": "編集済み",
        "english": "edited",
        "pronunciation": "henshuu",
    }
    response = client.post(f"/edit_word/{word.id}", data=data, follow_redirects=True)
    assert response.status_code == 200
    assert b"Word updated successfully!" in response.data

    updated_word = Word.query.get(word.id)
    assert updated_word.japanese == "編集済み"

def test_delete_word_get(client, logged_in_user, new_word_data):
    word = Word(**new_word_data, user_id=logged_in_user.id)
    db.session.add(word)
    db.session.commit()

    response = client.get(f"/delete_word/{word.id}")
    assert response.status_code == 200
    assert b"Are you sure" in response.data or b"form" in response.data

def test_delete_word_post(client, logged_in_user, new_word_data):
    word = Word(**new_word_data, user_id=logged_in_user.id)
    db.session.add(word)
    db.session.commit()

    response = client.post(f"/delete_word/{word.id}", follow_redirects=True)
    assert response.status_code == 200
    assert b"Word deleted successfully!" in response.data

    deleted_word = Word.query.get(word.id)
    assert deleted_word is None
