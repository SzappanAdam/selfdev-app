from app.repositories.habit_repository import HabitRepository


class HabitManager:

    def __init__(self):
        self.repo = HabitRepository()

    def create_habit(self, name: str, category: str):

        if not name:
            raise ValueError("Habit name is required")

        if len(name.strip()) < 3:
            raise ValueError("Habit name too short")

        name = name.strip()

        return self.repo.create_habit(
            name,
            category
        )

    def list_habits(self):
        return self.repo.get_all_habits()