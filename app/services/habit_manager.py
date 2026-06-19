from app.repositories.habit_repository import (
    HabitRepository
)


class HabitManager:

    def __init__(self):
        self.repo = HabitRepository()

    def create_habit(
        self,
        name,
        category
    ):
        return self.repo.create_habit(
            name,
            category
        )

    def list_habits(self):
        return self.repo.get_all_habits()