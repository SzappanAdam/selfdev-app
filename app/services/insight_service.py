from app.services.analytics_service import (
    AnalyticsService
)


class InsightService:

    def __init__(self):
        self.analytics = AnalyticsService()

    def generate_insights(self):

        insights = []

        completion = (
            self.analytics
            .completion_rate()
        )

        if completion < 50:

            insights.append(
                "A teljesítési arányod 50% alatt van."
            )

        elif completion < 75:

            insights.append(
                "Jó úton haladsz, de van még tér a javulásra."
            )

        else:

            insights.append(
                "Kiváló teljesítési arány!"
            )

        return insights