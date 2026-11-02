import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

# Initialize extensions outside create_app so they can be imported across modules
db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    """Application factory for the Flask Blogging Platform."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Ensure the instance directory exists
    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError:
        pass

    # Bind extensions to app
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models so Flask-Migrate / Alembic can discover metadata
    from app import models

    # Register Blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.posts import bp as posts_bp
    app.register_blueprint(posts_bp, url_prefix='/posts')

    return app
