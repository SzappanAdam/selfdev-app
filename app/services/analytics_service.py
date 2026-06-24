import pandas as pd
from app.repositories.habit_log_repository import HabitLogRepository


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

        return round(df["completed"].mean() * 100, 2)

    def most_active_habit(self):

        df = self.get_dataframe()

        if df.empty:
            return None

        counts = (
            df.groupby("habit_id")
            .size()
            .sort_values(ascending=False)
        )

        return int(counts.index[0])

    def weekly_activity(self):

        df = self.get_dataframe()

        if df.empty:
            return {}

        df["date"] = pd.to_datetime(df["date"])

        df["week"] = df["date"].dt.isocalendar().week

        return df.groupby("week").size().to_dict()

    def habit_counts(self):

        df = self.get_dataframe()

        if df.empty:
            return {}

        return df.groupby("habit_id").size().to_dict()

    def dashboard_summary(self):

        df = self.get_dataframe()

        if df.empty:
            return {
                "total_logs": 0,
                "completion_rate": 0,
                "active_habits": 0
            }

        return {
            "total_logs": len(df),
            "completion_rate": round(df["completed"].mean() * 100, 2),
            "active_habits": df["habit_id"].nunique()
        }

    def last_7_days_logs(self):

        df = self.get_dataframe()

        if df.empty:
            return df

        df["date"] = pd.to_datetime(df["date"])

        seven_days_ago = pd.Timestamp.now() - pd.Timedelta(days=7)

        return df[df["date"] >= seven_days_ago]

    def weekly_completion_rate(self):

        df = self.last_7_days_logs()

        if df.empty:
            return 0

        return round(df["completed"].mean() * 100, 2)