# Blogging Platform with Flask

A modern, scalable blogging platform built using Flask, Flask-SQLAlchemy, and Flask-Migrate, following the Application Factory pattern and modular Blueprints architecture.

---

## 📌 Week 1: Flask Setup and Basic Structure

### Objectives Completed:
1. **Flask Environment**: Set up virtual environment and core project dependencies (`Flask`, `Flask-SQLAlchemy`, `Flask-Migrate`, `python-dotenv`).
2. **Modular Architecture & Blueprints**:
   - Implemented the Application Factory pattern (`create_app()`) in `app/__init__.py`.
   - Structured routes using Blueprints:
     - `main`: Core pages (`/` home, `/about`).
     - `posts`: Blog post management and feeds (`/posts/`).
3. **Database Configuration**:
   - Configured SQLite database with SQLAlchemy ORM (`app/models.py`).
   - Defined `User` and `Post` relational models with one-to-many relationship and foreign key constraints.
   - Initialized database versioning with Flask-Migrate (`migrations/` directory).
   - Applied initial migration to create the `users` and `posts` tables.
4. **Templates & UI**:
   - Created base Jinja2 template (`app/templates/base.html`) styled with Bootstrap 5.
   - Built home, about, and post listing views.

---

## 📂 Project Structure

```text
Blogging-Platform-with-Flask/
├── app/
│   ├── __init__.py           # Application Factory (create_app), extension initialization
│   ├── models.py             # SQLAlchemy models (User, Post)
│   ├── main/                 # Main Blueprint
│   │   ├── __init__.py
│   │   └── routes.py         # Routes for Home and About
│   ├── posts/                # Posts Blueprint
│   │   ├── __init__.py
│   │   └── routes.py         # Routes for Blog Posts
│   ├── templates/            # Jinja2 templates
│   │   ├── base.html         # Base template with Bootstrap 5 navbar and footer
│   │   ├── main/
│   │   │   ├── index.html    # Home page
│   │   │   └── about.html    # Architecture overview
│   │   └── posts/
│   │       └── index.html    # Posts feed page
│   └── static/               # Static assets
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── main.js
├── migrations/               # Alembic / Flask-Migrate database migration scripts
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

### 5. Initialize & Apply Database Migrations
```bash
# If running for the first time on a fresh setup:
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
- `password_hash` (String(256))
- `created_at` (DateTime)
- `posts` (Relationship -> `Post`)

### `Post`
- `id` (Integer, Primary Key)
- `title` (String(140))
- `content` (Text)
- `created_at` (DateTime, Indexed)
- `user_id` (Integer, Foreign Key -> `users.id`)
- `author` (Backref -> `User`)

---

## 🛠️ Tech Stack
- **Backend**: Python, Flask
- **ORM & Migrations**: Flask-SQLAlchemy, Flask-Migrate (Alembic)
- **Frontend / Styling**: Jinja2, Bootstrap 5.3, Bootstrap Icons
