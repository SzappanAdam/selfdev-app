from app.database.models import GoalModel


class GoalRepository:

    def __init__(self, db):
        self.db = db

    def create_goal(self, title, description, target_date):

        goal = GoalModel(
            title=title,
            description=description,
            target_date=target_date
        )

        try:
            self.db.add(goal)
            self.db.commit()
            self.db.refresh(goal)
            return goal

        except Exception:
            self.db.rollback()
            raise

    def get_all_goals(self):

        return self.db.query(GoalModel).all()

    def get_goal_by_id(self, goal_id):

        return (
            self.db.query(GoalModel)
            .filter(GoalModel.id == goal_id)
            .first()
        )

    def delete_goal(self, goal_id):

        goal = self.get_goal_by_id(goal_id)

        if not goal:
            return False

        self.db.delete(goal)
        self.db.commit()

        return True