from app.database.database import SessionLocal
from app.database.models import GoalModel


class GoalRepository:

    def __init__(self):
        self.db = SessionLocal()

    def create_goal(
        self,
        title,
        description,
        target_date
    ):

        goal = GoalModel(
            title=title,
            description=description,
            target_date=target_date
        )

        self.db.add(goal)

        self.db.commit()

        self.db.refresh(goal)

        return goal

    def get_all_goals(self):

        return (
            self.db.query(
                GoalModel
            ).all()
        )