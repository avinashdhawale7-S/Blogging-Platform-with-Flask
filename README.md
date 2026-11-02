# Blogging Platform with Flask

A modern, scalable blogging platform built using Flask, Flask-SQLAlchemy, Flask-Migrate, Flask-Login, and Flask-WTF, following the Application Factory pattern and modular Blueprints architecture.

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
- **Comment Data Model (`app/models.py`)**:
  - Created `Comment` model with `body`, `created_at`, foreign key to `users.id`, and foreign key to `posts.id`.
  - Added cascading relationships so deleting a post or user automatically deletes associated comments.
- **Comment Form & Validation (`app/posts/forms.py`)**:
  - Implemented `CommentForm` with CSRF protection and character length validation (2–1000 characters).
- **Comment Views & Authorization (`app/posts/routes.py`)**:
  - `POST /posts/<id>/comment`: Restricted to authenticated users (`@login_required`), persists comments, flashes status, and redirects back to `#comments`.
  - `POST /posts/comment/<id>/delete`: Restricted to the comment author or the post author, preventing unauthorized comment deletions (403 Forbidden).
- **User Interface (`app/templates/posts/detail.html`)**:
  - Comment count header (`Comments (X)`).
  - Clean comment form for logged-in users; prominent sign-in callout for visitors.
  - Comment stream displaying author avatar, username linked to public profile, timestamp, comment body, and delete button for authors.
  - Dynamic comment counters displayed on article cards across home and feed pages.

---

## 📂 Project Structure

```text
Blogging-Platform-with-Flask/
├── app/
│   ├── __init__.py           # Application Factory, Flask-Login & extensions
│   ├── models.py             # User, Post, Tag, Comment models & post_tags
│   ├── auth/                 # Authentication Blueprint
│   │   ├── __init__.py
│   │   ├── forms.py          # WTForms: RegistrationForm, LoginForm
│   │   └── routes.py         # Login, Register, Logout, Profile
│   ├── main/                 # Main Blueprint
│   │   ├── __init__.py
│   │   └── routes.py         # Home (paginated), User Profile (paginated), About
│   ├── posts/                # Posts & Comments Blueprint
│   │   ├── __init__.py
│   │   ├── forms.py          # WTForms: PostForm, CommentForm
│   │   └── routes.py         # CRUD: Posts, Tags, and Comments
│   ├── templates/            # Jinja2 templates
│   │   ├── _macros.html      # Reusable pagination macro
│   │   ├── base.html         # Responsive layout with dynamic Auth navbar
│   │   ├── auth/             # Login, Register, Account settings views
│   │   ├── main/             # Home (feed), Author profile, About views
│   │   └── posts/            # Feed, Detail (with comments), Create, and Edit views
│   └── static/               # CSS and JS assets
├── migrations/               # Database migration scripts
├── instance/                 # SQLite database instance directory
├── .env.example              # Environment variables template
├── .gitignore                # Git ignore configuration
├── config.py                 # Configuration settings (pagination, db, keys)
├── requirements.txt          # Python dependencies
├── run.py                    # Application entry point
└── README.md                 # Project documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10+
- Git

### 2. Clone the Repository
```bash
git clone https://github.com/avinashdhawale7-S/Blogging-Platform-with-Flask.git
cd Blogging-Platform-with-Flask
```

### 3. Create and Activate Virtual Environment
```bash
# Windows
python -m venv .venv
.\.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Apply Database Migrations
```bash
flask db upgrade
```

### 6. Run the Application
```bash
python run.py
```
Open your browser and navigate to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🛠️ Tech Stack
- **Backend**: Python 3, Flask
- **Frontend / Templating**: Jinja2, Bootstrap 5.3, Bootstrap Icons
- **Rich Text Editor**: CKEditor 5 Classic
- **Security & Sanitization**: Bleach, Werkzeug Security, Flask-WTF (CSRF)
- **Authentication**: Flask-Login
- **Database ORM & Migrations**: Flask-SQLAlchemy, Flask-Migrate (Alembic)
