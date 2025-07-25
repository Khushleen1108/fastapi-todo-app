from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.todo import ToDo
from app.schemas.todo import ToDoCreate, ToDoOut
from app.crud import todo as crud
from app.database.db import get_db
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter()

@router.get("/", response_model=list[ToDoOut])
def read_todos(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(ToDo).filter(ToDo.owner_id == current_user.id).all()

@router.post("/", response_model=ToDoOut)
def create_new_todo(todo: ToDoCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_todo = ToDo(**todo.dict(), owner_id=current_user.id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo