from datetime import date
from app.repositories.goal_repository import GoalRepository


class GoalManager:

    def __init__(self):
        self.repo = GoalRepository()

    def create_goal(self, title: str, description: str, target_date: str):

        if not title:
            raise ValueError("Title is required")

        if not target_date:
            raise ValueError("Target date is required")

        return self.repo.create_goal(
            title,
            description,
            target_date
        )

    def list_goals(self):
        return self.repo.get_all_goals()