from sqlalchemy.orm import Session
from app.models.todo import ToDo
from app.schemas.todo import ToDoCreate

def get_all_todos(db: Session):
    return db.query(ToDo).all()

def create_todo(db: Session, todo: ToDoCreate):
    db_todo = ToDo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo