from typing import Optional
from pydantic import BaseModel

class ToDoBase(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False

class ToDoCreate(ToDoBase):
    pass

class ToDoOut(ToDoBase):
    id: int

    model_config = {
        "from_attributes": True
    }

class ToDoUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    completed: Optional[bool]

    class Config:
        from_attributes = True
    