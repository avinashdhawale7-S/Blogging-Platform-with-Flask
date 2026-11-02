from app import db
from app.models import Post, Comment


def test_add_comment_authenticated(client, auth, app):
    """Test authenticated user adding a comment to a post."""
    auth.register(username='postauthor', email='author@test.com')
    auth.login(email='author@test.com')
    client.post('/posts/create', data={'title': 'Post for Comments', 'content': '<p>Body</p>', 'tags': ''})

    with app.app_context():
        post_id = Post.query.filter_by(title='Post for Comments').first().id

    auth.logout()
    auth.register(username='commenter', email='commenter@test.com')
    auth.login(email='commenter@test.com')

    res = client.post(f'/posts/{post_id}/comment', data={'body': 'Insightful article!'}, follow_redirects=True)
    assert res.status_code == 200
    assert b'Your comment has been posted successfully!' in res.data
    assert b'Insightful article!' in res.data
    assert b'commenter' in res.data


def test_add_comment_unauthenticated(client, auth, app):
    """Test unauthenticated comment attempt redirects to login."""
    auth.register(username='auth1', email='auth1@test.com')
    auth.login(email='auth1@test.com')
    client.post('/posts/create', data={'title': 'Post Test', 'content': '<p>Body</p>', 'tags': ''})

    with app.app_context():
        post_id = Post.query.filter_by(title='Post Test').first().id

    auth.logout()
    res = client.post(f'/posts/{post_id}/comment', data={'body': 'Anonymous comment'})
    assert res.status_code == 302
    assert '/auth/login' in res.headers['Location']


def test_delete_comment_permissions(client, auth, app):
    """Test comment deletion authorization."""
    auth.register(username='p_author', email='p@test.com')
    auth.login(email='p@test.com')
    client.post('/posts/create', data={'title': 'Discussion Post', 'content': '<p>Body</p>', 'tags': ''})

    with app.app_context():
        post_id = Post.query.filter_by(title='Discussion Post').first().id

    auth.logout()
    auth.register(username='c_author', email='c@test.com')
    auth.login(email='c@test.com')
    client.post(f'/posts/{post_id}/comment', data={'body': 'My Comment'})

    with app.app_context():
        comment_id = Comment.query.filter_by(body='My Comment').first().id

    # Stranger cannot delete
    auth.logout()
    auth.register(username='stranger', email='s@test.com')
    auth.login(email='s@test.com')
    unauth_del = client.post(f'/posts/comment/{comment_id}/delete')
    assert unauth_del.status_code == 403

    # Comment author can delete
    auth.logout()
    auth.login(email='c@test.com')
    del_res = client.post(f'/posts/comment/{comment_id}/delete', follow_redirects=True)
    assert del_res.status_code == 200
    assert b'Comment has been deleted.' in del_res.data
