from app.services.analytics_service import AnalyticsService


class ReviewService:

    def __init__(self, analytics=None):
        self.analytics = analytics or AnalyticsService()

    def weekly_review(self):

        review = []

        rate = self.analytics.weekly_completion_rate()

        review.append(f"A heti teljesítési arányod {rate}%.")

        if rate >= 80:
            review.append("Kiváló hét volt!")
            review.append("Tartsd fenn a jelenlegi ritmust.")

        elif rate >= 60:
            review.append("Jó haladás.")
            review.append("Egy kis fókusz növelheti az eredményeid.")

        else:
            review.append("Érdemes egyszerűbb napi célokat kitűzni.")
            review.append("Kezdj 1-2 szokással, ne túl sokkal egyszerre.")

        return review