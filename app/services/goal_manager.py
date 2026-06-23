from app.repositories.goal_repository import (
    GoalRepository
)


class GoalManager:

    def __init__(self):

        self.repo = GoalRepository()

    def create_goal(
        self,
        title,
        description,
        target_date
    ):

        return self.repo.create_goal(
            title,
            description,
            target_date
        )

    def list_goals(self):

        return self.repo.get_all_goals()