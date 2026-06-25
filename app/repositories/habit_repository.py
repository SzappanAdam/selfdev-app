from app.database.models import HabitModel


class HabitRepository:

    def __init__(self, db):
        self.db = db

    def create_habit(self, name, category):

        habit = HabitModel(
            name=name,
            category=category
        )

        try:
            self.db.add(habit)
            self.db.commit()
            self.db.refresh(habit)
            return habit

        except Exception:
            self.db.rollback()
            raise

    def get_all_habits(self):

        return self.db.query(HabitModel).all()

    def get_habits_by_goal(self, goal_id):

        return (
            self.db.query(HabitModel)
            .filter(HabitModel.goal_id == goal_id)
            .all()
        )

    def get_by_name(self, name):

        return (
            self.db.query(HabitModel)
            .filter(HabitModel.name == name)
            .first()
        )