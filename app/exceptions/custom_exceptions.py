class AppException(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(message)


class TaskNotFoundError(AppException):
    def __init__(self):
        super().__init__("Task not found", 404)


class InvalidPriorityError(AppException):
    def __init__(self, value=None):
        msg = f"Invalid priority: {value}" if value else "Invalid priority"
        super().__init__(msg, 400)


class InvalidDateError(AppException):
    def __init__(self):
        super().__init__("Invalid date format (YYYY-MM-DD)", 400)