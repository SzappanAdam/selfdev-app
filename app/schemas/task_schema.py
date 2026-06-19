from pydantic import BaseModel
from typing import Optional


class TaskCreate(BaseModel):
    title: str
    category: str = "general"
    priority: str = "medium"
    due_date: Optional[str] = None


class TaskResponse(BaseModel):
    id: int
    title: str
    category: str
    priority: str
    due_date: Optional[str]
    done: bool

    model_config = {
        "from_attributes": True
    }