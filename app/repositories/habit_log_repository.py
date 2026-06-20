from app.database.database import SessionLocal
from app.database.models import HabitLogModel


class HabitLogRepository:

    def __init__(self):
        self.db = SessionLocal()

    def create_log(
        self,
        habit_id,
        date,
        completed=True
    ):

        existing = (
            self.db.query(HabitLogModel)
            .filter(
                HabitLogModel.habit_id == habit_id,
                HabitLogModel.date == date
            )
            .first()
        )

        if existing:
            return existing
        
        log = HabitLogModel(
            habit_id=habit_id,
            date=date,
            completed=completed
        )

        self.db.add(log)

        self.db.commit()

        self.db.refresh(log)

        return log

    def get_logs_for_habit(
        self,
        habit_id
    ):

        return (
            self.db.query(HabitLogModel)
            .filter(
                HabitLogModel.habit_id == habit_id
            )
            .all()
        )