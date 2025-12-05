import pytest
from app import app as flask_app, db


@pytest.fixture(scope="module")
def setup_database():
    with flask_app.app_context():
        print("Creating DB...")
        db.create_all()
    yield
    with flask_app.app_context():
        print("Dropping DB...")
        db.drop_all()
        print("DB dropped")


@pytest.fixture(scope="module")
def client(setup_database):
    with flask_app.test_client() as testing_client:
        yield testing_client


def test_alphabet_home(client):
    response = client.get("/alphabet/")
    assert response.status_code == 200
    assert b"alphabet" in response.data.lower()


def test_hiragana_page(client):
    response = client.get("/alphabet/hiragana")
    assert response.status_code == 200
    assert b"hiragana" in response.data.lower()


def test_katakana_page(client):
    response = client.get("/alphabet/katakana")
    assert response.status_code == 200
    assert b"katakana" in response.data.lower()


def test_kanji_page(client):
    response = client.get("/alphabet/kanji")
    assert response.status_code == 200
    assert b"kanji" in response.data.lower()
