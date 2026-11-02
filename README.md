# Blogging Platform with Flask

A modern, scalable blogging platform built using Flask, Flask-SQLAlchemy, Flask-Migrate, and Flask-Login, following the Application Factory pattern and modular Blueprints architecture.

---

## 📌 Milestones

### Week 1: Flask Setup and Basic Structure
- **Virtual Environment & Dependencies**: Initialized environment with `Flask`, `Flask-SQLAlchemy`, `Flask-Migrate`, and `python-dotenv`.
- **Application Factory Pattern**: Implemented `create_app()` in `app/__init__.py`.
- **Modular Blueprints**: Created `main` and `posts` blueprints.
- **Relational Models & Migrations**: Configured SQLAlchemy with `User` and `Post` models and initialized Alembic migrations.
- **Base UI**: Built responsive layout using Bootstrap 5.

### Week 2: User Authentication & Session Management
- **Flask-Login Integration**:
  - Initialized `LoginManager` in `app/__init__.py` with custom login views and flash messages.
  - Implemented `@login_manager.user_loader` callback.
  - Extended `User` model with `UserMixin` and secure password hashing using Werkzeug (`generate_password_hash`, `check_password_hash`).
- **Auth Blueprint (`app/auth`)**:
  - Built secure forms with Flask-WTF and WTForms (`RegistrationForm`, `LoginForm`).
  - Added duplicate username and email validation rules.
  - Implemented `/auth/register`: User creation and password hashing.
  - Implemented `/auth/login`: Credential verification, session creation via `login_user()`, and safe `next` parameter redirects.
  - Implemented `/auth/logout`: Safe session termination via `logout_user()`.
  - Implemented `/auth/profile`: Protected route guarded by `@login_required`.
- **Dynamic Navigation & Templates**:
  - Built modern authentication views: `login.html`, `register.html`, and `profile.html`.
  - Updated navbar to reflect real-time authentication states (logged in dropdown vs. guest buttons).

---

## 📂 Project Structure

```text
Blogging-Platform-with-Flask/
├── app/
│   ├── __init__.py           # Application Factory, Flask-Login and extension setup
│   ├── models.py             # User (UserMixin) and Post SQLAlchemy models
│   ├── auth/                 # Authentication Blueprint
│   │   ├── __init__.py
│   │   ├── forms.py          # WTForms (RegistrationForm, LoginForm)
│   │   └── routes.py         # Login, Register, Logout, Profile routes
│   ├── main/                 # Main Blueprint (Home, About)
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── posts/                # Posts Blueprint
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── templates/            # Jinja2 templates
│   │   ├── base.html         # Responsive layout with dynamic Auth navbar
│   │   ├── auth/             # Login, Register, Profile views
│   │   ├── main/             # Home and About views
│   │   └── posts/            # Posts feed view
│   └── static/               # CSS and JS assets
├── migrations/               # Database migration versions
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

## 🗄️ Database Models

### `User`
- `id` (Integer, Primary Key)
- `username` (String(64), Unique, Indexed)
- `email` (String(120), Unique, Indexed)
- `password_hash` (String(256), Not Null)
- `created_at` (DateTime)
- `posts` (Relationship -> `Post`)
- Methods: `set_password()`, `check_password()`

### `Post`
- `id` (Integer, Primary Key)
- `title` (String(140))
- `content` (Text)
- `created_at` (DateTime, Indexed)
- `user_id` (Integer, Foreign Key -> `users.id`)
- `author` (Backref -> `User`)

---

## 🛠️ Tech Stack
- **Backend**: Python 3, Flask
- **Authentication & Sessions**: Flask-Login, Werkzeug Security
- **Forms & Validation**: Flask-WTF, WTForms, email-validator
- **ORM & Migrations**: Flask-SQLAlchemy, Flask-Migrate (Alembic)
- **Frontend / Styling**: Jinja2, Bootstrap 5.3, Bootstrap Icons
