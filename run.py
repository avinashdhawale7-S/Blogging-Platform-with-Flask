import os
from app import create_app, db
from app.models import User, Post

app = create_app()


@app.shell_context_processor
def make_shell_context():
    """Provides automatic shell imports for `flask shell`."""
    return {'db': db, 'User': User, 'Post': Post}


if __name__ == '__main__':
    app.run(debug=True)
