from http.client import HTTPException
from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from app.models.todo import ToDo
from app.schemas.todo import ToDoCreate, ToDoOut, ToDoUpdate
from fastapi import status
from app.crud import todo as crud
from app.dependencies import get_db, get_current_user
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

@router.put("/{todo_id}", response_model=ToDoOut)
def update_todo(
    todo_id: int,
    todo_update: ToDoUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    todo = db.query(ToDo).filter(ToDo.id == todo_id, ToDo.owner_id == current_user.id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="ToDo not found")
    for field, value in todo_update.dict(exclude_unset=True).items():
        setattr(todo, field, value)
    db.commit()
    db.refresh(todo)
    return todo

@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    todo = db.query(ToDo).filter(ToDo.id == todo_id, ToDo.owner_id == current_user.id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="ToDo not found")
    db.delete(todo)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.get("/{todo_id}", response_model=ToDoOut)
def read_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    todo = db.query(ToDo).filter(ToDo.id == todo_id, ToDo.owner_id == current_user.id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="ToDo not found")
    return todo

@router.put("/{todo_id}/complete", response_model=ToDoOut)
def complete_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    todo = db.query(ToDo).filter(ToDo.id == todo_id, ToDo.owner_id == current_user.id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="ToDo not found")
    todo.completed = True
    db.commit()
    db.refresh(todo)
    return todo
