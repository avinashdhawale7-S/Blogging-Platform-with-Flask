import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    """Base application configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default-dev-secret-key-98765'
    
    # SQLite database location in instance folder
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'instance', 'blog.db')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Pagination settings
    POSTS_PER_PAGE = int(os.environ.get('POSTS_PER_PAGE', 5))
