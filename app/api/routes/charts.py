from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.services.chart_service import ChartService

router = APIRouter(prefix="/charts", tags=["Charts"])

chart_service = ChartService()


@router.get("/weekly")
def weekly_chart():
    image = chart_service.weekly_activity_chart()
    return StreamingResponse(image, media_type="image/png")


@router.get("/ranking")
def ranking_chart():
    image = chart_service.habit_ranking_chart()
    return StreamingResponse(image, media_type="image/png")