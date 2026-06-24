from app.services.analytics_service import AnalyticsService


class InsightService:

    def __init__(self, analytics=None):
        self.analytics = analytics or AnalyticsService()

    def generate_insights(self):

        insights = []

        completion = self.analytics.completion_rate()

        if completion < 50:
            insights.append("A teljesítési arányod 50% alatt van.")
            insights.append("Érdemes kisebb, könnyebb szokásokkal kezdeni.")

        elif completion < 75:
            insights.append("Jó úton haladsz, de van még tér a javulásra.")
            insights.append("Próbálj meg egy szokást fókuszálni egy hétig.")

        else:
            insights.append("Kiváló teljesítési arány!")
            insights.append("Tarthatod ezt a rendszert, jól működik nálad.")

        return insights