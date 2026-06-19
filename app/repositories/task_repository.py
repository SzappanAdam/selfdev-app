from app.database.database import SessionLocal
from app.database.models import TaskModel


class TaskRepository:

    def __init__(self):
        self.db = SessionLocal()

    def create_task(
        self,
        title,
        category,
        priority,
        due_date
    ):

        task = TaskModel(
            title=title,
            category=category,
            priority=priority,
            due_date=due_date
        )

        self.db.add(task)

        self.db.commit()

        self.db.refresh(task)

        return task

    def get_all_tasks(self):

        return self.db.query(
            TaskModel
        ).all()

    def get_task(self, task_id):

        return self.db.query(
            TaskModel
        ).filter(
            TaskModel.id == task_id
        ).first()

    def delete_task(self, task_id):

        task = self.get_task(task_id)

        if task:

            self.db.delete(task)

            self.db.commit()

            return True

        return False