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
- **Data Models for Tags & Posts**:
  - Implemented `Tag` model (`tags` table) with unique names.
  - Implemented `post_tags` many-to-many association table.
  - Extended `Post` model with `updated_at` timestamp and many-to-many relationship to `Tag`.
- **Flask-WTF Forms**:
  - `PostForm`: Title, rich HTML content, and comma-separated tags field.
- **Full CRUD Routes (`app/posts`)**:
  - **Create (`/posts/create`)**: Authenticated creation of posts with tag assignment and rich text sanitization (`bleach`).
  - **Read (`/posts/`, `/posts/<id>`, `/posts/tag/<tag_name>`)**: Feed browsing, article detail reading, and tag filtering.
  - **Update (`/posts/<id>/edit`)**: Pre-populated edit form restricted to the post's author (403 Forbidden for unauthorized users).
  - **Delete (`/posts/<id>/delete`)**: Safe deletion with modal confirmation, author check, and automatic cascade tag disassociation.
- **Rich Text Editor Integration**:
  - Integrated **CKEditor 5 Classic** for rich formatting (headings, lists, blockquotes, bold/italic, links).
  - Configured server-side HTML sanitization with `bleach` to prevent Cross-Site Scripting (XSS).

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
│   ├── main/                 # Main Blueprint (Home, About)
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── posts/                # Posts Blueprint
│   │   ├── __init__.py
│   │   ├── forms.py          # WTForms: PostForm
│   │   └── routes.py         # CRUD: Create, Read, Edit, Delete, Tag filtering
│   ├── templates/            # Jinja2 templates
│   │   ├── base.html         # Responsive layout with dynamic Auth navbar
│   │   ├── auth/             # Login, Register, Profile views
│   │   ├── main/             # Home and About views
│   │   └── posts/            # Feed, Detail, Create, and Edit views
│   └── static/               # CSS and JS assets
├── migrations/               # Database migration scripts
├── instance/                 # SQLite database instance directory
├── .env.example              # Environment variables template
├── .gitignore                # Git ignore configuration
├── config.py                 # Configuration settings
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

## 🗄️ Database Schema & Relationships

- **User**: (1-to-many with `Post`)
- **Post**: (many-to-many with `Tag` via `post_tags`, foreign key to `User`)
- **Tag**: (many-to-many with `Post` via `post_tags`)
- **post_tags**: (`post_id`, `tag_id`)

---

## 🛠️ Tech Stack
- **Backend**: Python 3, Flask
- **Rich Text Editor**: CKEditor 5 Classic
- **HTML Sanitization**: Bleach
- **Forms & Validation**: Flask-WTF, WTForms, email-validator
- **Authentication**: Flask-Login, Werkzeug Security
- **Database ORM & Migrations**: Flask-SQLAlchemy, Flask-Migrate (Alembic)
- **Frontend / Styling**: Jinja2, Bootstrap 5.3, Bootstrap Icons
