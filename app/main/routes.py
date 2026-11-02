from flask import render_template
from app.main import bp
from app.models import Post


@bp.route('/')
@bp.route('/index')
def index():
    recent_posts = Post.query.order_by(Post.created_at.desc()).limit(5).all()
    return render_template('main/index.html', title='Home', posts=recent_posts)


@bp.route('/about')
def about():
    return render_template('main/about.html', title='About')
