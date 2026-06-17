from app.services.task_manager import TaskManager


def test_add_task():

    manager = TaskManager(
        "test_tasks.json"
    )

    manager.add_task(
        "Python tanulás"
    )

    assert len(
        manager.tasks
    ) == 1