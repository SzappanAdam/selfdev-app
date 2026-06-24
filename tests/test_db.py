from app.repositories.task_repository import TaskRepository

repo = TaskRepository()

task = repo.create_task(
    title="SQLAlchemy tanulás",
    category="study",
    priority="high",
    due_date="2026-06-30"
)

assert task.id is not None
assert task.title == "SQLAlchemy tanulás"

tasks = repo.get_all_tasks()

assert len(tasks) > 0

print("✔ DB test OK")