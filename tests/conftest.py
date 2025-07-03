import pytest
from app import app as flask_app
from extensions import db
from models.user import User

@pytest.fixture
def app():
    flask_app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "WTF_CSRF_ENABLED": False,
        "SECRET_KEY": "test",
    })

    with flask_app.app_context():
        db.create_all()
        yield flask_app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def create_user():
    def _create_user(username="testuser", email="test@example.com", password="1234"):
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user
    return _create_user

@pytest.fixture
def logged_in_user(client, create_user):
    user = create_user()
    with client:
        client.post('/login', data={'username': user.username, 'password': '1234'})
        yield user
