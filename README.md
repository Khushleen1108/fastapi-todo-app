# 📝 FastAPI Todo App

A full-featured Todo API built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **Alembic**, managed using **Poetry**. Includes user registration, authentication (JWT), and CRUD operations for todos.

---

## 🚀 Features

- 🔐 User registration & login (JWT-based)
- 🗂️ Create, Read, Update, Delete Todos
- 📦 Modular FastAPI project structure
- 🗃️ PostgreSQL with SQLAlchemy ORM
- 🔁 Alembic for schema migrations
- ⚙️ Poetry for dependency management
- 📄 Environment-based configuration

---

## 🛠️ Project Setup

### 1. 📦 Install Dependencies

```bash
poetry install
```

## ⚙️ Setup Environment Variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/tododb
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## 🔧 Run Migrations
```bash
poetry run alembic revision --autogenerate -m "message"
poetry run alembic upgrade head
```

🚀 Run the App
```bash
poetry run uvicorn app.main:app --reload
```

Visit: http://localhost:8000/docs for Swagger UI.

## 🧪 API Endpoints

| Method | Endpoint       | Description                |
|--------|----------------|----------------------------|
| POST   | `/register`    | Register a new user        |
| POST   | `/login`       | Authenticate and get token |
| GET    | `/todos/`      | Get user's todos           |
| POST   | `/todos/`      | Create a new todo          |
| PUT    | `/todos/{id}`  | Update a todo              |
| DELETE | `/todos/{id}`  | Delete a todo              |

---

## 📁 Project Structure

```yaml
todo-app/
├── app/
│   ├── core/                      # ⚙️ Core logic and settings
│   │   └── security.py
│
│   ├── crud/                      # 📦 Encapsulated DB logic (CRUD operations)
│   │   ├── user.py                # CRUD ops related to User (create_user, get_user_by_email, etc.)
│   │   └── todo.py                # CRUD ops related to ToDo items
│
│   ├── database/                  # 🗄️ DB connection and base metadata
│   │   └── db.py 
│
│   ├── models/                    # 🧱 SQLAlchemy ORM models
│   │   ├── user.py                # User model (id, username, email, password hash)
│   │   ├── todo.py                # ToDo model (id, title, description, etc.)
│   │   └── __init__.py            # Import all models for Alembic
│
│   ├── routers/                   # 🌐 API endpoints
│   │   ├── auth.py                # Endpoints for login and registration
│   │   ├── todo.py                # Endpoints for CRUD /todos and /todos/{id}/complete
│   │   └── user.py                # Get current user, change password, etc.
│
│   ├── schemas/                   # 🧾 Pydantic request/response models
│   │   ├── user.py                # UserCreate, UserOut, ChangePasswordRequest
│   │   ├── todo.py                # ToDoBase, ToDoCreate, ToDoUpdate, ToDoOut
│
│   └── main.py                    # 🚀 FastAPI app entry point (include routers, start app)
│
├── alembic/                       # 🧬 Alembic DB migrations
│   ├── versions/                  # 🔁 Auto-generated migration scripts
│   └── env.py                     # Alembic config that connects models to migrations
│
├── .env                           # 🔐 Environment variables (DB URL, JWT secret, etc.)
├── .gitignore                     # 🚫 Git ignore rules (e.g. __pycache__, .env)
├── pyproject.toml                 # 📦 Poetry project config (dependencies, scripts, etc.)
├── poetry.toml                    # ⚙️ Optional poetry settings (like virtualenv location)
└── README.md                      # 📘 Project documentation (setup, usage, etc.)
```

---

## 🐘 PostgreSQL Setup (Local)

```bash
# Example using psql
createdb tododb
```
Or use GUI tools like pgAdmin, DBeaver, or TablePlus to create the database manually.
