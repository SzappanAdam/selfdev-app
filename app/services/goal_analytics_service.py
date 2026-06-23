from app.repositories.goal_repository import (
    GoalRepository
)

from app.repositories.habit_repository import (
    HabitRepository
)

from app.services.habit_log_manager import (
    HabitLogManager
)

class GoalAnalyticsService:

    def __init__(self):

        self.goal_repo = GoalRepository()

        self.habit_repo = HabitRepository()

        self.log_manager = (
            HabitLogManager()
        )

    def goal_progress(
        self,
        goal_id
    ):

        habits = (
            self.habit_repo
            .get_habits_by_goal(
                goal_id
            )
        )

        if not habits:
            return 0

        total = 0

        for habit in habits:

            streak = (
                self.log_manager
                .calculate_streak(
                    habit.id
                )
            )

            score = min(
                streak * 5,
                100
            )

            total += score

        return round(
            total / len(habits),
            2
        )
    
    def goal_status(
        self,
        goal_id
    ):

        progress = (
            self.goal_progress(
                goal_id
            )
        )

        if progress >= 80:

            return "on_track"

        if progress >= 50:

            return "needs_attention"

        return "at_risk"