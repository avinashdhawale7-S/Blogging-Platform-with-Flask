from app import db
from app.models import Post, Tag


def test_search_by_title_and_content(client, auth, app):
    """Test keyword searching across post title and body."""
    auth.register(username='searcher', email='searcher@test.com')
    auth.login(email='searcher@test.com')

    client.post('/posts/create', data={
        'title': 'Learn Python Data Structures',
        'content': '<p>Comprehensive guide to lists, sets, and dicts.</p>',
        'tags': 'python, programming'
    })
    client.post('/posts/create', data={
        'title': 'Flask Blueprint Architecture',
        'content': '<p>Structuring large-scale web applications.</p>',
        'tags': 'flask, webdev'
    })

    # Search title
    res_title = client.get('/posts/search?q=Structures')
    assert res_title.status_code == 200
    assert b'Learn Python Data Structures' in res_title.data
    assert b'Flask Blueprint Architecture' not in res_title.data

    # Search content
    res_body = client.get('/posts/search?q=large-scale')
    assert res_body.status_code == 200
    assert b'Flask Blueprint Architecture' in res_body.data
    assert b'Learn Python Data Structures' not in res_body.data


def test_filter_by_tag(client, auth, app):
    """Test filtering posts by specific category tag."""
    auth.register(username='tagger', email='tagger@test.com')
    auth.login(email='tagger@test.com')

    client.post('/posts/create', data={'title': 'Docker Guide', 'content': '<p>Containerization</p>', 'tags': 'devops, docker'})
    client.post('/posts/create', data={'title': 'CSS Grid', 'content': '<p>Styling</p>', 'tags': 'frontend, css'})

    res_tag = client.get('/posts/search?tag=devops')
    assert res_tag.status_code == 200
    assert b'Docker Guide' in res_tag.data
    assert b'CSS Grid' not in res_tag.data


def test_empty_search(client):
    """Test empty search result page."""
    res = client.get('/posts/search?q=NonExistentQueryXYZ')
    assert res.status_code == 200
    assert b'No matching articles found!' in res.data
