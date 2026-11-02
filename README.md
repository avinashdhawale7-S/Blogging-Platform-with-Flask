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
  - **Reusable Pagination Macro (`app/templates/_macros.html`)**: Generic `render_pagination()` component supporting multi-page navigation, active states, ellipsis windowing, and URL parameter propagation.
  - **Home Page (`/`)**: Paginated feed with reading excerpts, author info, popular topics sidebar, and milestone tracking.
  - **Individual Post View (`/posts/<id>`)**: Comprehensive reading view with breadcrumbs, reading time calculation, author profile badge, safe rich HTML rendering, and author action buttons with delete modal.
  - **Public User Profile (`/user/<username>`)**: Author profile displaying avatar, join date, publication statistics, and a paginated list of all posts written by the user.
- **Full Pagination Integration**:
  - Configured `POSTS_PER_PAGE = 5` in `config.py`.
  - Added SQLAlchemy pagination across home feed (`/`), full post list (`/posts/`), tag-filtered views (`/posts/tag/<tag_name>`), and author profiles (`/user/<username>`).

---

## 📂 Project Structure

```text
Blogging-Platform-with-Flask/
├── app/
│   ├── __init__.py           # Application Factory, Flask-Login & extensions
│   ├── models.py             # User, Post, Tag models & post_tags association
│   ├── auth/                 # Authentication Blueprint
│   │   ├── __init__.py
│   │   ├── forms.py          # WTForms: RegistrationForm, LoginForm
│   │   └── routes.py         # Login, Register, Logout, Profile
│   ├── main/                 # Main Blueprint
│   │   ├── __init__.py
│   │   └── routes.py         # Home (paginated), User Profile (paginated), About
│   ├── posts/                # Posts Blueprint
│   │   ├── __init__.py
│   │   ├── forms.py          # WTForms: PostForm
│   │   └── routes.py         # CRUD: Create, Read, Edit, Delete, Tag filter (paginated)
│   ├── templates/            # Jinja2 templates
│   │   ├── _macros.html      # Reusable pagination macro
│   │   ├── base.html         # Responsive layout with dynamic Auth navbar
│   │   ├── auth/             # Login, Register, Account settings views
│   │   ├── main/             # Home (feed), Author profile, About views
│   │   └── posts/            # Feed, Detail, Create, and Edit views
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
