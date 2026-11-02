from flask import render_template, request, current_app
from app import db
from app.main import bp
from app.models import Post, User, Tag


@bp.route('/')
@bp.route('/index')
def index():
    """Home page displaying paginated blog posts and platform highlights."""
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config.get('POSTS_PER_PAGE', 5)
    
    pagination = Post.query.order_by(Post.created_at.desc()).paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )
    posts = pagination.items
    popular_tags = Tag.query.order_by(Tag.name.asc()).limit(10).all()

    return render_template(
        'main/index.html',
        title='Home',
        posts=posts,
        pagination=pagination,
        tags=popular_tags
    )


@bp.route('/user/<string:username>')
def user_profile(username: str):
    """Public user profile page displaying author stats and their paginated posts."""
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config.get('POSTS_PER_PAGE', 5)

    pagination = user.posts.order_by(Post.created_at.desc()).paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )
    posts = pagination.items

    return render_template(
        'main/user_profile.html',
        title=f'{user.username} - Author Profile',
        user=user,
        posts=posts,
        pagination=pagination
    )


@bp.route('/about')
def about():
    """About page outlining the architecture and learning milestones."""
    return render_template('main/about.html', title='About')
