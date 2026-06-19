from app.database.database import SessionLocal
from app.database.models import HabitModel


class HabitRepository:

    def __init__(self):
        self.db = SessionLocal()

    def create_habit(
        self,
        name,
        category
    ):

        habit = HabitModel(
            name=name,
            category=category
        )

        self.db.add(habit)

        self.db.commit()

        self.db.refresh(habit)

        return habit

    def get_all_habits(self):

        return self.db.query(
            HabitModel
        ).all()