# Blogging Platform with Flask

A production-ready blogging platform built using Flask, Flask-SQLAlchemy, Flask-Migrate, Flask-Login, and Flask-WTF, following the Application Factory pattern and modular Blueprints architecture.

---

## 📌 Milestones

### Week 1: Flask Setup and Basic Structure
- **Virtual Environment & Dependencies**: Initialized environment with `Flask`, `Flask-SQLAlchemy`, `Flask-Migrate`, and `python-dotenv`.
- **Application Factory Pattern**: Implemented `create_app()` in `app/__init__.py`.
- **Modular Blueprints**: Created `main` and `posts` blueprints.
- **Relational Models & Migrations**: Configured SQLAlchemy with `User` and `Post` models and initialized Alembic migrations.
- **Base UI**: Built responsive layout using Bootstrap 5.

### Week 2: User Authentication & Session Management
- **Flask-Login Integration**: Initialized `LoginManager`, custom user loader, and login views.
- **Security & Models**: Password hashing with Werkzeug (`generate_password_hash`, `check_password_hash`) and `UserMixin`.
- **Auth Blueprint**: User registration, login with remember-me, logout, and protected user profiles.

### Week 3: Blog Post CRUD Functionality & Tagging
- **Data Models for Tags & Posts**: `Tag` model, `post_tags` many-to-many relationship, and `updated_at` column.
- **Flask-WTF Forms**: `PostForm` with title validation, rich text content, and comma-separated tags.
- **Full CRUD Routes**: Create, Read, Edit, and Delete posts with strict author authorization rules (403 Forbidden).
- **Rich Text Editor**: Integrated CKEditor 5 Classic with server-side HTML sanitization via `bleach`.

### Week 4: Frontend: Displaying Posts and Navigation
- **Jinja2 Frontend Architecture**:
  - Reusable pagination macro (`app/templates/_macros.html`) supporting windowing, Previous/Next buttons, and parameter preservation.
  - Paginated home feed, post listing, and topic tags.
  - Detailed post reading view with reading time estimates, author info, and breadcrumbs.
  - Public author profile page (`/user/<username>`) with author stats and paginated articles.

### Week 5: Commenting System
- **Comment Data Model**: `Comment` model linked to `User` and `Post` with cascading deletes.
- **Comment Form & Views**: Authenticated comment submission (`/posts/<id>/comment`) and author deletion (`/posts/comment/<id>/delete`).
- **Interactive UI**: Real-time comment count headers, guest sign-in callout, and author badges.

### Week 6: Search and Filtering
- **SQLAlchemy ORM Search**:
  - Case-insensitive keyword search across `Post.title` and `Post.content` using `or_` and `ilike`.
  - Tag and category filtering using `Post.tags.any(Tag.name == selected_tag)`.
  - Global search bar embedded in navbar and dedicated search/filter page with active filter pills and query-preserving pagination.

### Week 7: Deployment Preparation and Testing
- **Unit Testing Suite (`tests/`)**:
  - Built comprehensive test suite using `pytest` with isolated in-memory SQLite fixtures (`TestingConfig`).
  - 18 automated unit tests covering authentication, post CRUD, authorization guards (403), HTML sanitization, comments, and search.
- **Production WSGI & Gunicorn**:
  - Configured `wsgi.py` production entry point.
  - Added `gunicorn` WSGI server configuration with multi-worker execution.
- **Containerization (Docker & Docker Compose)**:
  - Created production-ready `Dockerfile` with non-root security user (`appuser`), healthcheck, and Gunicorn command.
  - Configured `.dockerignore` to exclude temporary files and virtual environments.
  - Created `docker-compose.yml` with persistent volume mounting for SQLite database storage.

---

## 📂 Project Structure

```text
Blogging-Platform-with-Flask/
├── app/
│   ├── __init__.py           # Application Factory, Flask-Login & extensions
│   ├── models.py             # User, Post, Tag, Comment models & post_tags
│   ├── auth/                 # Authentication Blueprint
│   ├── main/                 # Main Blueprint (Home, Author profile, About)
│   ├── posts/                # Posts, Tags, Comments & Search Blueprint
│   ├── templates/            # Jinja2 templates (Navbar, Search, Posts, Auth, Profiles)
│   └── static/               # CSS and JS assets
├── tests/                    # Pytest Unit Test Suite
│   ├── conftest.py           # Fixtures: app, client, runner, auth helper
│   ├── test_auth.py          # Authentication & password hashing tests
│   ├── test_posts.py         # Post CRUD, authorization & sanitization tests
│   ├── test_comments.py      # Commenting system tests
│   └── test_search.py        # Search and tag filtering tests
├── migrations/               # Database migration scripts
├── instance/                 # SQLite database instance directory
├── .dockerignore             # Docker build exclusions
├── .env.example              # Environment variables template
├── .gitignore                # Git ignore configuration
├── config.py                 # Multi-environment configuration (Dev, Test, Prod)
├── Dockerfile                # Production Docker container definition
├── docker-compose.yml        # Docker Compose configuration
├── requirements.txt          # Python dependencies (includes gunicorn & pytest)
├── run.py                    # Development application entry point
├── wsgi.py                   # Production WSGI entry point
└── README.md                 # Project documentation
```

---

## 🧪 Running Unit Tests

Run the complete test suite using `pytest`:

```bash
# Run all tests
pytest -v

# Run with short test summary
pytest -q
```

All 18 unit tests execute against an isolated in-memory SQLite database.

---

## 🚀 Deployment

### Option A: Local / Virtual Environment
```bash
# Install dependencies
pip install -r requirements.txt

# Apply migrations
flask db upgrade

# Run with Gunicorn (Linux/macOS/Cloud)
gunicorn --bind 0.0.0.0:5000 --workers 4 wsgi:app

# Or development mode (Windows/All)
python run.py
```

### Option B: Docker Container
```bash
# Build the Docker image
docker build -t flask-blog .

# Run the container
docker run -d -p 5000:5000 -v $(pwd)/instance:/app/instance --name flask_blog flask-blog
```

### Option C: Docker Compose
```bash
# Start the container stack
docker compose up -d

# View logs
docker compose logs -f

# Stop the application
docker compose down
```
Access the application at: [http://localhost:5000](http://localhost:5000)

---

## 🛠️ Tech Stack
- **Backend**: Python 3, Flask
- **WSGI Production Server**: Gunicorn
- **Containerization**: Docker, Docker Compose
- **Testing**: Pytest (18 automated tests)
- **ORM & Migrations**: Flask-SQLAlchemy, Flask-Migrate (Alembic)
- **Frontend / Templating**: Jinja2, Bootstrap 5.3, Bootstrap Icons
- **Rich Text Editor**: CKEditor 5 Classic
- **Security & Sanitization**: Bleach, Werkzeug Security, Flask-WTF (CSRF)
- **Authentication**: Flask-Login
