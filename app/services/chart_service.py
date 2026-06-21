import io

import matplotlib.pyplot as plt

from app.services.analytics_service import (
    AnalyticsService
)


class ChartService:

    def __init__(self):
        self.analytics = AnalyticsService()

    def weekly_activity_chart(self):

        data = self.analytics.weekly_activity()

        weeks = list(data.keys())
        values = list(data.values())

        plt.figure(figsize=(8, 4))

        plt.bar(weeks, values)

        plt.title("Weekly Activity")
        plt.xlabel("Week")
        plt.ylabel("Completed Habits")

        buffer = io.BytesIO()

        plt.savefig(
            buffer,
            format="png",
            bbox_inches="tight"
        )

        plt.close()

        buffer.seek(0)

        return buffer
    
    def habit_ranking_chart(self):

        data = self.analytics.habit_counts()

        habits = list(data.keys())
        counts = list(data.values())

        plt.figure(figsize=(8, 4))

        plt.bar(
            habits,
            counts
        )

        plt.title(
            "Habit Completion Ranking"
        )

        plt.xlabel("Habit")
        plt.ylabel("Completions")

        buffer = io.BytesIO()

        plt.savefig(
            buffer,
            format="png",
            bbox_inches="tight"
        )

        plt.close()

        buffer.seek(0)

        return buffer