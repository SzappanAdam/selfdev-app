import pytest

from app.validators.task_validator import (
    validate_priority
)

from app.exceptions.custom_exceptions import (
    InvalidPriorityError
)


def test_valid_priority():

    validate_priority("high")


def test_invalid_priority():

    with pytest.raises(
        InvalidPriorityError
    ):
        validate_priority("alma")