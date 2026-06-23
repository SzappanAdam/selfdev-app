from fastapi import APIRouter

from app.services.task_manager import TaskManager
from app.schemas.task_schema import TaskResponse
from app.schemas.task_schema import TaskCreate
from datetime import date

from app.services.habit_log_manager import (
    HabitLogManager
)
from app.services.analytics_service import (
    AnalyticsService
)
from fastapi.responses import StreamingResponse

from app.services.chart_service import (
    ChartService
)

chart_service = ChartService()

analytics = AnalyticsService()
router = APIRouter()
manager = TaskManager()
habit_log_manager = HabitLogManager()

@router.get("/")
def root():
    return {
        "message": "SelfDev API működik!"
    }

@router.get(
    "/tasks",
    response_model=list[TaskResponse]
)
def get_tasks():
    return manager.list_tasks()

@router.get("/tasks")
def get_tasks():

    tasks = manager.list_tasks()

    return [
        {
            "id": task.id,
            "title": task.title,
            "category": task.category,
            "priority": task.priority,
            "done": task.done,
        }
        for task in tasks
    ]


@router.post("/tasks")
def create_task(task: TaskCreate):

    created_task = manager.add_task(
        title=task.title,
        category=task.category,
        priority=task.priority,
        due_date=task.due_date
    )

    return created_task

@router.get("/stats")
def get_stats():
    return manager.stats()

@router.get("/habits")
def get_habits():
    return habit_manager.list_habits()


@router.post("/habits")
def create_habit(
    name: str,
    category: str
):
    return habit_manager.create_habit(
        name,
        category
    )

@router.post("/habits/{habit_id}/complete")
def complete_habit(
    habit_id: int
):

    today = date.today().isoformat()

    return habit_log_manager.log_habit(
        habit_id,
        today
    )

@router.get(
    "/habits/{habit_id}/streak"
)
def get_streak(
    habit_id: int
):

    return {
        "habit_id": habit_id,
        "streak": habit_log_manager.calculate_streak(
            habit_id
        )
    }

@router.get("/analytics/completion-rate")
def completion_rate():

    return {
        "completion_rate":
        analytics.completion_rate()
    }

@router.get("/analytics/top-habit")
def top_habit():

    return {
        "habit_id":
        analytics.most_active_habit()
    }

@router.get("/analytics/weekly")
def weekly():

    return analytics.weekly_activity()

@router.get("/charts/weekly")
def weekly_chart():

    image = (
        chart_service
        .weekly_activity_chart()
    )

    return StreamingResponse(
        image,
        media_type="image/png"
    )

@router.get("/charts/ranking")
def ranking_chart():

    image = (
        chart_service
        .habit_ranking_chart()
    )

    return StreamingResponse(
        image,
        media_type="image/png"
    )

@router.get("/dashboard")
def dashboard():

    return analytics.dashboard_summary()

from app.services.insight_service import (
    InsightService
)

insights = InsightService()

@router.get("/insights")
def get_insights():

    return {
        "insights":
        insights.generate_insights()
    }

from app.services.review_service import (
    ReviewService
)

reviews = ReviewService()

@router.get("/review/weekly")
def weekly_review():

    return {
        "summary":
        reviews.weekly_review()
    }

from app.services.goal_manager import (
    GoalManager
)

goal_manager = GoalManager()

@router.post("/goals")
def create_goal(
    title: str,
    description: str = "",
    target_date: str | None = None
):

    return goal_manager.create_goal(
        title,
        description,
        target_date
    )

@router.get("/goals")
def get_goals():

    return goal_manager.list_goals()

from app.services.goal_analytics_service import (
    GoalAnalyticsService
)

goal_analytics = (
    GoalAnalyticsService()
)

@router.get(
    "/goals/{goal_id}/progress"
)
def goal_progress(
    goal_id: int
):

    return {
        "goal_id": goal_id,
        "progress":
            goal_analytics
            .goal_progress(
                goal_id
            ),
        "status":
            goal_analytics
            .goal_status(
                goal_id
            )
    }

@router.post("/register")
def register(
    username: str,
    email: str,
    password: str
):  hashed = hash_password(
    password
)

user_repo.create_user(
    username,
    email,
    hashed
)

return {
    "message":
    "User created"
}

@router.post("/login")
def login(
    username: str,
    password: str
): token = create_access_token(
    username
)