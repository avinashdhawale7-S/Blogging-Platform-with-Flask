from app import db
from app.models import User


def test_password_hashing():
    """Test user model password hashing and verification."""
    user = User(username='hashuser', email='hash@test.com')
    user.set_password('SecretPassword')

    assert user.password_hash != 'SecretPassword'
    assert user.check_password('SecretPassword') is True
    assert user.check_password('WrongPassword') is False


def test_registration(client, app):
    """Test user registration flow."""
    response = client.post('/auth/register', data={
        'username': 'newuser',
        'email': 'newuser@test.com',
        'password': 'password123',
        'password_confirm': 'password123'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'Your account has been created successfully!' in response.data

    with app.app_context():
        user = User.query.filter_by(username='newuser').first()
        assert user is not None
        assert user.email == 'newuser@test.com'


def test_registration_duplicate_username(client, auth):
    """Test rejection of duplicate username during registration."""
    auth.register(username='dupuser', email='first@test.com')
    response = auth.register(username='dupuser', email='second@test.com')

    assert b'Username already taken.' in response.data


def test_login_and_logout(client, auth):
    """Test successful user login, session access, and logout."""
    auth.register(username='logintest', email='login@test.com', password='password123')
    
    # Login with valid credentials
    response = auth.login(email='login@test.com', password='password123')
    assert response.status_code == 200
    assert b'Welcome back, logintest!' in response.data

    # Access protected profile
    profile_res = client.get('/auth/profile')
    assert profile_res.status_code == 200
    assert b'logintest' in profile_res.data

    # Logout
    logout_res = auth.logout()
    assert logout_res.status_code == 200
    assert b'You have been logged out successfully.' in logout_res.data


def test_invalid_login(client, auth):
    """Test rejection of invalid credentials."""
    auth.register(username='badlogin', email='bad@test.com', password='password123')
    response = auth.login(email='bad@test.com', password='wrongpassword')

    assert b'Invalid email or password.' in response.data


def test_protected_route_requires_login(client):
    """Test that anonymous users are redirected from protected routes."""
    response = client.get('/auth/profile', follow_redirects=False)
    assert response.status_code == 302
    assert '/auth/login' in response.headers['Location']
