from fastapi import APIRouter

from app.services.task_manager import TaskManager
from app.schemas.task_schema import TaskResponse
from app.schemas.task_schema import TaskCreate
from datetime import date

from app.services.habit_log_manager import (
    HabitLogManager
)

router = APIRouter()
manager = TaskManager()
habit_log_manager = HabitLogManager()

@router.get("/")
def root():
    return {
        "message": "SelfDev API működik!"
    }

@router.get(
    "/tasks",
    response_model=list[TaskResponse]
)
def get_tasks():
    return manager.list_tasks()

@router.get("/tasks")
def get_tasks():

    tasks = manager.list_tasks()

    return [
        {
            "id": task.id,
            "title": task.title,
            "category": task.category,
            "priority": task.priority,
            "done": task.done,
        }
        for task in tasks
    ]


@router.post("/tasks")
def create_task(task: TaskCreate):

    created_task = manager.add_task(
        title=task.title,
        category=task.category,
        priority=task.priority,
        due_date=task.due_date
    )

    return created_task

@router.get("/stats")
def get_stats():
    return manager.stats()

@router.get("/habits")
def get_habits():
    return habit_manager.list_habits()


@router.post("/habits")
def create_habit(
    name: str,
    category: str
):
    return habit_manager.create_habit(
        name,
        category
    )

@router.post("/habits/{habit_id}/complete")
def complete_habit(
    habit_id: int
):

    today = date.today().isoformat()

    return habit_log_manager.log_habit(
        habit_id,
        today
    )

@router.get(
    "/habits/{habit_id}/streak"
)
def get_streak(
    habit_id: int
):

    return {
        "habit_id": habit_id,
        "streak": habit_log_manager.calculate_streak(
            habit_id
        )
    }