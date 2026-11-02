"""Production WSGI entrypoint for Gunicorn or other WSGI servers."""
import os
from app import create_app
from config import config_by_name

env = os.environ.get('FLASK_ENV', 'production')
app = create_app(config_by_name.get(env, config_by_name['production']))

if __name__ == '__main__':
    app.run()
