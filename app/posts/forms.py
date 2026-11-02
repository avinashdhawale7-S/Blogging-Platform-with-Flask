from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    """Form for creating and editing blog posts."""
    title = StringField(
        'Title',
        validators=[
            DataRequired(message='Please provide a title for your post.'),
            Length(min=3, max=140, message='Title must be between 3 and 140 characters.')
        ]
    )
    content = TextAreaField(
        'Content',
        validators=[DataRequired(message='Post content cannot be empty.')]
    )
    tags = StringField(
        'Tags / Categories',
        description='Separate tags with commas, e.g. python, webdev, flask'
    )
    submit = SubmitField('Publish Post')


class CommentForm(FlaskForm):
    """Form for submitting a comment on a blog post."""
    body = TextAreaField(
        'Leave a Comment',
        validators=[
            DataRequired(message='Comment cannot be empty.'),
            Length(min=2, max=1000, message='Comment must be between 2 and 1000 characters.')
        ]
    )
    submit = SubmitField('Post Comment')
