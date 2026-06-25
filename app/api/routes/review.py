from fastapi import APIRouter
from app.services.review_service import ReviewService

router = APIRouter(prefix="/review", tags=["Review"])

review_service = ReviewService()


@router.get("/weekly")
def weekly_review():
    return {"summary": review_service.weekly_review()}