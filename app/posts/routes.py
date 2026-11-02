import bleach
from flask import render_template, redirect, url_for, flash, request, abort
from flask_login import current_user, login_required
from app import db
from app.posts import bp
from app.posts.forms import PostForm
from app.models import Post, Tag

ALLOWED_TAGS = [
    'p', 'b', 'i', 'u', 'em', 'strong', 'a', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'ul', 'ol', 'li', 'blockquote', 'code', 'pre', 'hr', 'br', 'span', 's', 'sub', 'sup'
]
ALLOWED_ATTRIBUTES = {
    'a': ['href', 'title', 'target', 'rel'],
    '*': ['class']
}


def sanitize_html(raw_html: str) -> str:
    """Sanitize rich text HTML to allow safe formatting tags while preventing XSS."""
    return bleach.clean(raw_html, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES, strip=True)


def sync_post_tags(post: Post, tags_string: str) -> None:
    """Parse comma-separated tags string and associate with post."""
    post.tags.clear()
    if not tags_string:
        return

    tag_names = {t.strip().lower() for t in tags_string.split(',') if t.strip()}
    for name in tag_names:
        tag = Tag.query.filter_by(name=name).first()
        if not tag:
            tag = Tag(name=name)
            db.session.add(tag)
        post.tags.append(tag)


@bp.route('/')
def index():
    """List all blog posts ordered by creation date."""
    posts = Post.query.order_by(Post.created_at.desc()).all()
    all_tags = Tag.query.order_by(Tag.name.asc()).all()
    return render_template('posts/index.html', title='Blog Feed', posts=posts, tags=all_tags)


@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    """Create a new blog post."""
    form = PostForm()
    if form.validate_on_submit():
        clean_content = sanitize_html(form.content.data)
        post = Post(
            title=form.title.data.strip(),
            content=clean_content,
            author=current_user
        )
        db.session.add(post)
        sync_post_tags(post, form.tags.data)
        db.session.commit()

        flash('Your post has been published successfully!', 'success')
        return redirect(url_for('posts.detail', post_id=post.id))

    return render_template('posts/create_post.html', title='Create New Post', form=form)


@bp.route('/<int:post_id>')
def detail(post_id: int):
    """View a single blog post."""
    post = db.get_or_404(Post, post_id)
    return render_template('posts/detail.html', title=post.title, post=post)


@bp.route('/<int:post_id>/edit', methods=['GET', 'POST'])
@login_required
def edit(post_id: int):
    """Edit an existing blog post (restricted to author)."""
    post = db.get_or_404(Post, post_id)
    if post.author != current_user:
        abort(403)

    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data.strip()
        post.content = sanitize_html(form.content.data)
        sync_post_tags(post, form.tags.data)
        db.session.commit()

        flash('Your post has been updated successfully!', 'success')
        return redirect(url_for('posts.detail', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.tags.data = post.tags_as_string()

    return render_template('posts/edit_post.html', title=f'Edit: {post.title}', form=form, post=post)


@bp.route('/<int:post_id>/delete', methods=['POST'])
@login_required
def delete(post_id: int):
    """Delete a blog post (restricted to author)."""
    post = db.get_or_404(Post, post_id)
    if post.author != current_user:
        abort(403)

    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted successfully.', 'info')
    return redirect(url_for('posts.index'))


@bp.route('/tag/<string:tag_name>')
def tag_filter(tag_name: str):
    """Filter posts by tag/category."""
    tag = Tag.query.filter_by(name=tag_name.lower()).first_or_404()
    posts = tag.posts.order_by(Post.created_at.desc()).all()
    all_tags = Tag.query.order_by(Tag.name.asc()).all()
    return render_template(
        'posts/index.html',
        title=f'Posts tagged with #{tag.name}',
        posts=posts,
        selected_tag=tag,
        tags=all_tags
    )
