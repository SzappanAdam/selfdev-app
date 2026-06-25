from fastapi import APIRouter
from app.services.analytics_service import AnalyticsService

router = APIRouter(prefix="/analytics", tags=["Analytics"])

analytics = AnalyticsService()


@router.get("/completion-rate")
def completion_rate():
    return {"completion_rate": analytics.completion_rate()}


@router.get("/top-habit")
def top_habit():
    return {"habit_id": analytics.most_active_habit()}


@router.get("/weekly")
def weekly():
    return analytics.weekly_activity()