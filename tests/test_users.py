import pytest
from app import app as flask_app, db
from models.user import User
from werkzeug.security import generate_password_hash


def test_something(client):
    response = client.get('/')
    assert response.status_code == 200

def test_register_user(client):
    response = client.post("/register", data={
        "username": "newuser",
        "email": "new@example.com",
        "password": "1234"
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Account created!" in response.data

def test_login_valid_user(client, create_user):
    create_user()
    
    response = client.post("/login", data={
        "username": "testuser",
        "password": "1234"
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Login successful!" in response.data

def test_login_invalid_user(client):
    response = client.post("/login", data={
        "username": "wrong",
        "password": "wrong"
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Invalid username or password" in response.data

def test_logout(client, create_user):
    user = create_user()
    client.post("/login", data={
        "username": user.username,
        "password": "1234"
    }, follow_redirects=True)

    response = client.get("/logout", follow_redirects=True)
    assert response.status_code == 200
    assert b"Logged out!" in response.data
