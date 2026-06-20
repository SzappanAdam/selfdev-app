from app.repositories.habit_log_repository import (
    HabitLogRepository
)


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