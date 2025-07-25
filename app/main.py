from fastapi import FastAPI
from app.routers import todo, auth

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(todo.router, prefix="/todos", tags=["ToDos"])