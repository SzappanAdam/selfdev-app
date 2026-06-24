from datetime import datetime

from app.exceptions.custom_exceptions import (
    InvalidDateError,
    InvalidPriorityError,
)

VALID_PRIORITIES = {
    "low",
    "medium",
    "high"
}


def validate_priority(priority):

    if not priority:
        raise InvalidPriorityError("Hiányzó prioritás")

    priority = priority.lower().strip()

    if priority not in VALID_PRIORITIES:

        raise InvalidPriorityError(
            f"Érvénytelen prioritás: {priority}"
        )

    return priority


def validate_date(date_string):

    if not date_string:
        return None

    try:
        parsed = datetime.strptime(
            date_string,
            "%Y-%m-%d"
        )
        return parsed.date()

    except ValueError:

        raise InvalidDateError(
            "A dátum formátuma: YYYY-MM-DD"
        )