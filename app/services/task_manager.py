from app.repositories.task_repository import TaskRepository


class TaskManager:

    def __init__(self):
        self.repo = TaskRepository()

    def add_task(
        self,
        title,
        category="general",
        priority="medium",
        due_date=None
    ):
        return self.repo.create_task(
            title=title,
            category=category,
            priority=priority,
            due_date=due_date
        )

    def list_tasks(self):
        return self.repo.get_all_tasks()

    def complete_task(self, task_id):
        task = self.repo.get_task(task_id)

        if not task:
            return False

        task.done = True
        self.repo.db.commit()
        return True

    def delete_task(self, task_id):
        return self.repo.delete_task(task_id)

    def search_tasks(self, keyword):
        tasks = self.repo.get_all_tasks()

        keyword = keyword.lower()

        return [
            task
            for task in tasks
            if keyword in task.title.lower()
        ]

    def pending_tasks(self):
        return [
            task
            for task in self.repo.get_all_tasks()
            if not task.done
        ]

    def completed_tasks(self):
        return [
            task
            for task in self.repo.get_all_tasks()
            if task.done
        ]

    def filter_by_priority(self, priority):
        return [
            task
            for task in self.repo.get_all_tasks()
            if task.priority == priority
        ]