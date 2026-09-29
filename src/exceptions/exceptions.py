"""
Concrete application exception types.

Each class maps a domain error to a specific HTTP status and RFC 9457 title.
Raise these from routes and services instead of FastAPI's HTTPException.
"""

from typing import Any

from .base import AppException


class NotFoundError(AppException):
    """
    404 Not Found Exception
    """

    status_code = 404
    title = "Resource Not Found"

    def __init__(self, detail: str = "Resource Not Found", **kwargs: Any) -> None:
        """
        Initialise a not-found error

        Args:
            detail: Explanation of which resource was not found
            **kwargs: Forwarded to AppException (type_uri, extensions)
        """

        super().__init__(detail, **kwargs)


class ConflictError(AppException):
    """
    409 Conflict Error for alraedy existing resource
    """

    status_code = 409
    title = "Resource Conflict"

    def __init__(self, detail: str = "Resource Conflict", **kwargs: Any) -> None:
        super().__init__(detail, **kwargs)
