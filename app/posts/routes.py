from flask import render_template
from app.posts import bp
from app.models import Post


@bp.route('/')
def index():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('posts/index.html', title='Blog Posts', posts=posts)
