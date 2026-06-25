from fastapi import APIRouter
from app.services.task_manager import TaskManager
from app.schemas.task_schema import TaskCreate, TaskResponse

router = APIRouter(prefix="/tasks", tags=["Tasks"])

manager = TaskManager()


@router.get("/", response_model=list[TaskResponse])
def get_tasks():
    return manager.list_tasks()


@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate):
    return manager.add_task(
        title=task.title,
        category=task.category,
        priority=task.priority,
        due_date=task.due_date
    )


@router.delete("/{task_id}")
def delete_task(task_id: int):
    return manager.delete_task(task_id)


@router.get("/stats")
def stats():
    return manager.stats()