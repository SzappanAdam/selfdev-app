from fastapi import APIRouter
from app.services.goal_manager import GoalManager
from app.services.goal_analytics_service import GoalAnalyticsService

router = APIRouter(prefix="/goals", tags=["Goals"])

goal_manager = GoalManager()
goal_analytics = GoalAnalyticsService()


@router.post("/")
def create_goal(title: str, description: str = "", target_date: str | None = None):
    return goal_manager.create_goal(title, description, target_date)


@router.get("/")
def get_goals():
    return goal_manager.list_goals()


@router.get("/{goal_id}/progress")
def progress(goal_id: int):
    return {
        "goal_id": goal_id,
        "progress": goal_analytics.goal_progress(goal_id),
        "status": goal_analytics.goal_status(goal_id)
    }