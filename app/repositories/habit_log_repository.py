from app.database.models import HabitLogModel


class HabitLogRepository:

    def __init__(self, db):
        self.db = db

    def create_log(self, habit_id, log_date, completed=True):

        existing = (
            self.db.query(HabitLogModel)
            .filter(
                HabitLogModel.habit_id == habit_id,
                HabitLogModel.date == log_date
            )
            .first()
        )

        if existing:
            return existing

        log = HabitLogModel(
            habit_id=habit_id,
            date=log_date,
            completed=completed
        )

        try:
            self.db.add(log)
            self.db.commit()
            self.db.refresh(log)
            return log

        except Exception:
            self.db.rollback()
            raise

    def get_logs_for_habit(self, habit_id):

        return (
            self.db.query(HabitLogModel)
            .filter(HabitLogModel.habit_id == habit_id)
            .all()
        )

    def get_all_logs(self):

        return self.db.query(HabitLogModel).all()