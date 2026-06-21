import pandas as pd

from app.repositories.habit_log_repository import (
    HabitLogRepository
)


class AnalyticsService:

    def __init__(self):
        self.repo = HabitLogRepository()

    def get_dataframe(self):

        logs = self.repo.get_all_logs()

        data = [
            {
                "habit_id": log.habit_id,
                "date": log.date,
                "completed": log.completed
            }
            for log in logs
        ]

        return pd.DataFrame(data)
    
    def completion_rate(self):

        df = self.get_dataframe()

        if df.empty:
            return 0

        return round(
            df["completed"].mean() * 100,
            2
        )
    
    def most_active_habit(self):

        df = self.get_dataframe()

        if df.empty:
            return None

        counts = (
            df.groupby("habit_id")
            .size()
            .sort_values(
                ascending=False
            )
        )

        return int(counts.index[0])
    
    def weekly_activity(self):

        df = self.get_dataframe()

        if df.empty:
            return {}

        df["date"] = pd.to_datetime(
            df["date"]
        )

        df["week"] = (
            df["date"]
            .dt.isocalendar()
            .week
        )

        result = (
            df.groupby("week")
            .size()
            .to_dict()
        )

        return result
    
    def habit_counts(self):

        df = self.get_dataframe()

        if df.empty:
            return {}

        return (
            df.groupby("habit_id")
            .size()
            .to_dict()
        )