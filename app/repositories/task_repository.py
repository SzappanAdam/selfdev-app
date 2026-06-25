from app.database.models import TaskModel


class TaskRepository:

    def __init__(self, db):
        self.db = db

    def create_task(self, title, category, priority, due_date):

        task = TaskModel(
            title=title,
            category=category,
            priority=priority,
            due_date=due_date
        )

        try:
            self.db.add(task)
            self.db.commit()
            self.db.refresh(task)
            return task

        except Exception:
            self.db.rollback()
            raise

    def get_all_tasks(self):

        return self.db.query(TaskModel).all()

    def get_task(self, task_id):

        return (
            self.db.query(TaskModel)
            .filter(TaskModel.id == task_id)
            .first()
        )

    def delete_task(self, task_id):

        task = self.get_task(task_id)

        if not task:
            return False

        self.db.delete(task)
        self.db.commit()

        return True

    def update_task(self, task_id, **kwargs):

        task = self.get_task(task_id)

        if not task:
            return None

        for key, value in kwargs.items():
            setattr(task, key, value)

        self.db.commit()
        self.db.refresh(task)

        return task