from app.services.task_manager import TaskManager


def test_add_task():

    manager = TaskManager()

    manager.add_task(
        "Test",
        "study",
        "high",
        "2026-06-30"
    )

    tasks = manager.list_tasks()

    assert len(tasks) > 0