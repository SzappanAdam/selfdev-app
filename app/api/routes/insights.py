from fastapi import APIRouter
from app.services.insight_service import InsightService

router = APIRouter(prefix="/insights", tags=["Insights"])

insights = InsightService()


@router.get("/")
def get_insights():
    return {"insights": insights.generate_insights()}