from app.repositories.habit_repository import HabitRepository
from app.services.habit_log_manager import HabitLogManager


class GoalAnalyticsService:

    SCORE_MULTIPLIER = 5
    MAX_SCORE = 100

    def __init__(self, habit_repo=None, log_manager=None):

        self.habit_repo = habit_repo or HabitRepository()
        self.log_manager = log_manager or HabitLogManager()

    def goal_progress(self, goal_id: int) -> float:

        habits = self.habit_repo.get_habits_by_goal(goal_id)

        if not habits:
            return 0

        scores = []

        for habit in habits:

            streak = self.log_manager.calculate_streak(habit.id)

            score = min(
                streak * self.SCORE_MULTIPLIER,
                self.MAX_SCORE
            )

            scores.append(score)

        return round(sum(scores) / len(scores), 2)

    def goal_status(self, goal_id: int) -> str:

        progress = self.goal_progress(goal_id)

        if progress >= 80:
            return "on_track"

        if progress >= 50:
            return "needs_attention"

        return "at_risk"