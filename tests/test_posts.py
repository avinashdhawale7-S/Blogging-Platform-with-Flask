from app import db
from app.models import Post, Tag, User


def test_create_post(client, auth, app):
    """Test creating a new post with tags as authenticated user."""
    auth.register(username='writer', email='writer@test.com')
    auth.login(email='writer@test.com')

    response = client.post('/posts/create', data={
        'title': 'Unit Testing Flask',
        'content': '<p>This is a <strong>rich</strong> post content.</p>',
        'tags': 'flask, testing, python'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'Your post has been published successfully!' in response.data
    assert b'Unit Testing Flask' in response.data

    with app.app_context():
        post = Post.query.filter_by(title='Unit Testing Flask').first()
        assert post is not None
        assert len(post.tags) == 3
        tag_names = [t.name for t in post.tags]
        assert 'flask' in tag_names
        assert 'testing' in tag_names


def test_post_html_sanitization(client, auth, app):
    """Test that malicious HTML/XSS script tags are sanitized."""
    auth.register(username='secuser', email='sec@test.com')
    auth.login(email='sec@test.com')

    client.post('/posts/create', data={
        'title': 'XSS Defense Post',
        'content': '<p>Safe paragraph</p><script>alert("Hacked")</script><img src="x" onerror="alert(1)">',
        'tags': 'security'
    }, follow_redirects=True)

    with app.app_context():
        post = Post.query.filter_by(title='XSS Defense Post').first()
        assert post is not None
        assert '<script>' not in post.content
        assert '</script>' not in post.content
        assert 'onerror' not in post.content
        assert '<p>Safe paragraph</p>' in post.content


def test_edit_post_author(client, auth, app):
    """Test that author can successfully edit their own post."""
    auth.register(username='editor', email='editor@test.com')
    auth.login(email='editor@test.com')

    client.post('/posts/create', data={
        'title': 'Original Title',
        'content': '<p>Original content</p>',
        'tags': 'original'
    })

    with app.app_context():
        post = Post.query.filter_by(title='Original Title').first()
        post_id = post.id

    edit_res = client.post(f'/posts/{post_id}/edit', data={
        'title': 'Updated Title',
        'content': '<p>Updated content</p>',
        'tags': 'updated'
    }, follow_redirects=True)

    assert edit_res.status_code == 200
    assert b'Your post has been updated successfully!' in edit_res.data
    assert b'Updated Title' in edit_res.data


def test_edit_post_unauthorized(client, auth, app):
    """Test that a non-author is blocked with 403 Forbidden from editing."""
    auth.register(username='owner', email='owner@test.com')
    auth.login(email='owner@test.com')
    client.post('/posts/create', data={'title': 'Owner Post', 'content': '<p>Text</p>', 'tags': ''})

    with app.app_context():
        post = Post.query.filter_by(title='Owner Post').first()
        post_id = post.id

    auth.logout()
    auth.register(username='hacker', email='hacker@test.com')
    auth.login(email='hacker@test.com')

    response = client.post(f'/posts/{post_id}/edit', data={'title': 'Hacked', 'content': 'Text', 'tags': ''})
    assert response.status_code == 403


def test_delete_post_author(client, auth, app):
    """Test that post author can delete their post."""
    auth.register(username='deleter', email='deleter@test.com')
    auth.login(email='deleter@test.com')
    client.post('/posts/create', data={'title': 'To Be Deleted', 'content': '<p>Text</p>', 'tags': ''})

    with app.app_context():
        post = Post.query.filter_by(title='To Be Deleted').first()
        post_id = post.id

    del_res = client.post(f'/posts/{post_id}/delete', follow_redirects=True)
    assert del_res.status_code == 200
    assert b'Your post has been deleted successfully.' in del_res.data

    with app.app_context():
        assert db.session.get(Post, post_id) is None


def test_delete_post_unauthorized(client, auth, app):
    """Test that a non-author cannot delete someone else's post."""
    auth.register(username='user1', email='user1@test.com')
    auth.login(email='user1@test.com')
    client.post('/posts/create', data={'title': 'Protected Post', 'content': '<p>Text</p>', 'tags': ''})

    with app.app_context():
        post_id = Post.query.filter_by(title='Protected Post').first().id

    auth.logout()
    auth.register(username='user2', email='user2@test.com')
    auth.login(email='user2@test.com')

    del_res = client.post(f'/posts/{post_id}/delete')
    assert del_res.status_code == 403
