from app.repositories.task_repository import (
    TaskRepository
)

repo = TaskRepository()

repo.create_task(
    title="SQLAlchemy tanulás",
    category="study",
    priority="high",
    due_date="2026-06-30"
)

tasks = repo.get_all_tasks()

for task in tasks:
    print(task.id, task.title)