import io
import matplotlib.pyplot as plt
from app.services.analytics_service import AnalyticsService


class ChartService:

    def __init__(self):
        self.analytics = AnalyticsService()

    def _save_chart(self, fig):

        buffer = io.BytesIO()

        fig.savefig(
            buffer,
            format="png",
            bbox_inches="tight"
        )

        plt.close(fig)

        buffer.seek(0)

        return buffer

    def weekly_activity_chart(self):

        data = self.analytics.weekly_activity()

        if not data:
            return None

        weeks, values = zip(*sorted(data.items()))

        fig, ax = plt.subplots(figsize=(8, 4))

        ax.bar(weeks, values)
        ax.set_title("Weekly Activity")
        ax.set_xlabel("Week")
        ax.set_ylabel("Completed Habits")

        return self._save_chart(fig)

    def habit_ranking_chart(self):

        data = self.analytics.habit_counts()

        if not data:
            return None

        habits, counts = zip(*sorted(data.items()))

        fig, ax = plt.subplots(figsize=(8, 4))

        ax.bar(habits, counts)
        ax.set_title("Habit Completion Ranking")
        ax.set_xlabel("Habit")
        ax.set_ylabel("Completions")

        return self._save_chart(fig)