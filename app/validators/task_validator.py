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

    if priority not in VALID_PRIORITIES:

        raise InvalidPriorityError(
            f"Érvénytelen prioritás: {priority}"
        )


def validate_date(date_string):

    if not date_string:
        return

    try:

        datetime.strptime(
            date_string,
            "%Y-%m-%d"
        )

    except ValueError:

        raise InvalidDateError(
            "A dátum formátuma: YYYY-MM-DD"
        )