import pytest
from app import create_app, db
from app.models import User, Post, Tag, Comment
from config import TestingConfig


@pytest.fixture
def app():
    """Create and configure a testing instance of the application."""
    test_app = create_app(TestingConfig)

    with test_app.app_context():
        db.create_all()
        yield test_app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    """Test client for simulating HTTP requests."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """Test CLI runner for Flask CLI commands."""
    return app.test_cli_runner()


class AuthActions:
    """Helper class for authenticating users inside unit tests."""
    def __init__(self, client):
        self._client = client

    def register(self, username='testuser', email='test@example.com', password='password123'):
        return self._client.post('/auth/register', data={
            'username': username,
            'email': email,
            'password': password,
            'password_confirm': password
        }, follow_redirects=True)

    def login(self, email='test@example.com', password='password123'):
        return self._client.post('/auth/login', data={
            'email': email,
            'password': password
        }, follow_redirects=True)

    def logout(self):
        return self._client.get('/auth/logout', follow_redirects=True)


@pytest.fixture
def auth(client):
    """Fixture providing authentication helpers."""
    return AuthActions(client)
