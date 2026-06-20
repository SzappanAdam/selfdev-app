from app.repositories.habit_log_repository import (
    HabitLogRepository
)
from datetime import date, timedelta

class HabitLogManager:

    def __init__(self):
        self.repo = HabitLogRepository()

    def log_habit(
        self,
        habit_id,
        date
    ):
        return self.repo.create_log(
            habit_id,
            date
        )

    def get_logs(
        self,
        habit_id
    ):
        return self.repo.get_logs_for_habit(
            habit_id
        )
    
    def calculate_streak(
        self,
        habit_id
    ):

        logs = self.repo.get_logs_for_habit(
            habit_id
        )

        completed_dates = {
            log.date
            for log in logs
            if log.completed
        }

        streak = 0

        current_day = date.today()

        while current_day in completed_dates:

            streak += 1

            current_day -= timedelta(days=1)

        return streak