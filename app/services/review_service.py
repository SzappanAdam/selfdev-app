from app.services.analytics_service import (
    AnalyticsService
)


class ReviewService:

    def __init__(self):

        self.analytics = (
            AnalyticsService()
        )

    def weekly_review(self):

        review = []

        rate = (
            self.analytics
            .weekly_completion_rate()
        )

        review.append(
            f"A heti teljesítési arányod {rate}%."
        )

        if rate >= 80:

            review.append(
                "Kiváló hét volt!"
            )

        elif rate >= 60:

            review.append(
                "Jó haladás."
            )

        else:

            review.append(
                "Érdemes egyszerűbb napi célokat kitűzni."
            )

        return review