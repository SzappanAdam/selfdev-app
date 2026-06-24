from app.repositories.task_repository import TaskRepository


def test_create_task():

    repo = TaskRepository()

    task = repo.create_task(
        title="Test task",
        category="study",
        priority="high",
        due_date="2026-06-30"
    )

    assert task.id is not None
    assert task.title == "Test task"