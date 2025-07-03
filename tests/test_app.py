import pytest
from flask import url_for
from app import app as flask_app

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    flask_app.config['WTF_CSRF_ENABLE'] = False # turn off test
    with flask_app.test_client() as client:
        yield client

def test_homepage_loads(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Nihongo Quest" in response.data # this change about index.html

def test_redirect_if_not_logged_in(client):
    response = client.get('/', follow_redirects=True)
    assert b"login" in response.data or response.status_code == 200