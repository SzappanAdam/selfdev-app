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
            "id": self.id,
            "title": self.title,
            "category": self.category,
            "priority": self.priority,
            "due_date": self.due_date,
            "done": self.done,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            task_id=data.get("task_id") or data.get("id"),
            title=data.get("title"),
            category=data.get("category", "general"),
            priority=data.get("priority", "medium"),
            due_date=data.get("due_date"),
            done=data.get("done", False),
            created_at=data.get("created_at"),
        )