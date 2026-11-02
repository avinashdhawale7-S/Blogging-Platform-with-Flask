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
- **Comment Data Model**: `Comment` model linked to `User` and `Post` with cascading deletes.
- **Comment Form & Views**: Authenticated comment submission (`/posts/<id>/comment`) and author deletion (`/posts/comment/<id>/delete`).
- **Interactive UI**: Real-time comment count headers, guest sign-in callout, and author badges.

### Week 6: Search and Filtering
- **SQLAlchemy ORM Search**:
  - Utilized `or_` and `ilike` in `app/posts/routes.py` to perform case-insensitive keyword searches across both `Post.title` and `Post.content`.
- **Category & Tag Filtering**:
  - Query filtering via `Post.tags.any(Tag.name == selected_tag)` allowing users to filter by specific topics or combine with text search.
- **Global & Dedicated Search UI**:
  - Embedded global search input directly into the top navigation bar (`app/templates/base.html`).
  - Created a dedicated search interface (`app/templates/posts/search.html`) featuring search keyword input, category dropdown, active filter pill badges, result count indicator, and an empty state.
  - Integrated smart pagination preserving `q` and `tag` query arguments across pages.

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
│   ├── posts/                # Posts, Tags, Comments & Search Blueprint
│   │   ├── __init__.py
│   │   ├── forms.py          # WTForms: PostForm, CommentForm
│   │   └── routes.py         # CRUD, Search, Filter, Comments
│   ├── templates/            # Jinja2 templates
│   │   ├── _macros.html      # Reusable pagination macro
│   │   ├── base.html         # Responsive layout with dynamic Auth navbar & global search
│   │   ├── auth/             # Login, Register, Account settings views
│   │   ├── main/             # Home (feed), Author profile, About views
│   │   └── posts/            # Feed, Detail, Create, Edit, and Search views
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
- **ORM & Querying**: SQLAlchemy (`or_`, `ilike`, `any`), Flask-SQLAlchemy, Flask-Migrate
- **Frontend / Templating**: Jinja2, Bootstrap 5.3, Bootstrap Icons
- **Rich Text Editor**: CKEditor 5 Classic
- **Security & Sanitization**: Bleach, Werkzeug Security, Flask-WTF (CSRF)
- **Authentication**: Flask-Login
