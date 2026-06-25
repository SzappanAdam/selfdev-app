from fastapi import APIRouter
from datetime import date

from app.services.habit_manager import HabitManager
from app.services.habit_log_manager import HabitLogManager

router = APIRouter(prefix="/habits", tags=["Habits"])

habit_manager = HabitManager()
log_manager = HabitLogManager()


@router.get("/")
def get_habits():
    return habit_manager.list_habits()


@router.post("/")
def create_habit(name: str, category: str = "general"):
    return habit_manager.create_habit(name, category)


@router.post("/{habit_id}/complete")
def complete_habit(habit_id: int):
    today = date.today().isoformat()
    return log_manager.log_habit(habit_id, today)


@router.get("/{habit_id}/streak")
def streak(habit_id: int):
    return {
        "habit_id": habit_id,
        "streak": log_manager.calculate_streak(habit_id)
    }