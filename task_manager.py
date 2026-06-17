import json
import os

from task import Task


class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.filename):
            self.tasks = []
            return

        with open(self.filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.tasks = [Task.from_dict(task) for task in data]

    def save_tasks(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(
                [task.to_dict() for task in self.tasks],
                f,
                indent=2,
                ensure_ascii=False,
            )

    def generate_id(self):
        if not self.tasks:
            return 1

        return max(task.id for task in self.tasks) + 1

    def add_task(
        self,
        title,
        category="general",
        priority="medium",
        due_date=None,
    ):
        task = Task(
            task_id=self.generate_id(),
            title=title,
            category=category,
            priority=priority,
            due_date=due_date,
        )

        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self):
        return self.tasks

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.complete()
                self.save_tasks()
                return True

        return False

    def delete_task(self, task_id):
        before = len(self.tasks)

        self.tasks = [
            task for task in self.tasks
            if task.id != task_id
        ]

        if len(self.tasks) != before:
            self.save_tasks()
            return True

        return False

    def search_tasks(self, keyword):
        keyword = keyword.lower()

        return [
            task
            for task in self.tasks
            if keyword in task.title.lower()
        ]

    def filter_by_priority(self, priority):
        return [
            task
            for task in self.tasks
            if task.priority == priority
        ]

    def pending_tasks(self):
        return [
            task
            for task in self.tasks
            if not task.done
        ]

    def completed_tasks(self):
        return [
            task
            for task in self.tasks
            if task.done
        ]