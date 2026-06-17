from datetime import datetime


class Task:
    def __init__(
        self,
        task_id,
        title,
        category="general",
        priority="medium",
        due_date=None,
        done=False,
        created_at=None,
    ):
        self.id = task_id
        self.title = title
        self.category = category
        self.priority = priority
        self.due_date = due_date
        self.done = done
        self.created_at = created_at or datetime.now().isoformat()

    def complete(self):
        self.done = True

    def to_dict(self):
        return {
            "task_id": self.id,
            "title": self.title,
            "category": self.category,
            "priority": self.priority,
            "due_date": self.due_date,
            "done": self.done,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)