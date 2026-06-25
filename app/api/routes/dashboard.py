from fastapi import APIRouter
from app.services.analytics_service import AnalyticsService

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

analytics = AnalyticsService()


@router.get("/")
def dashboard():
    return analytics.dashboard_summary()