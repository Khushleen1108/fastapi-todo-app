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
│ ├── core/
│ ├── crud/
│ ├── database/
│ ├── models/
│ ├── schemas/
│ ├── routers/
│ ├── main.py│ 
├── alembic/
│ ├── versions/
│ └── env.py
├── .env
├── .gitignore
├── pyproject.toml
├── poetry.toml
└── README.md
```

---

## 🐘 PostgreSQL Setup (Local)

```bash
# Example using psql
createdb tododb
```
Or use GUI tools like pgAdmin, DBeaver, or TablePlus to create the database manually.
