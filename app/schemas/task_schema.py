from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class PriorityEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class TaskCreate(BaseModel):
    title: str
    category: str = "general"
    priority: PriorityEnum = PriorityEnum.medium
    due_date: Optional[date] = None


class TaskResponse(BaseModel):
    id: int
    title: str
    category: str
    priority: PriorityEnum
    due_date: Optional[date]
    done: bool

    model_config = {
        "from_attributes": True
    }