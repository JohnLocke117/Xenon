"""
FastAPI exception handlers for RFC 9457 error responses.

Define handler callables that convert raised exceptions into
`application/problem+json` responses. Wired into the FastAPI app
via app.add_exception_handler() in main.py.
"""

import logging

from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from .base import AppException
from .problem_detail import ProblemDetail

logger = logging.getLogger(__name__)


def problem_response(problem: ProblemDetail) -> JSONResponse:
    """
    Converts the defined Problem Detail model to JSON

    Args:
        problem: A validated Problem Detail object

    Returns:
        JSONResponse with matching status code and `Content-Type: application/problem+json`
    """

    return JSONResponse(
        status_code=problem.status,
        content=problem.model_dump(),
        media_type="application/problem+json",
    )


async def app_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """
    Handle AppException and all subclasses (e.g. NotFoundError)

    Logs server errors (5xx) at exception level and client errors (4xx)
    at warning level. Never expose internal details beyond `exc.detail`.
    Added a Bearer challenge for authentication failures on API routes

    Args:
        request: The incoming HTTP request (used for the instance field)
        exc: The raised exception (expected to be an ``AppException``).

    Returns:
        RFC 9457 problem detail response
    """

    if not isinstance(exc, AppException):
        raise exc

    if exc.status_code >= 500:
        logger.exception("AppException: %s", exc.detail, exc_info=exc)
    else:
        logger.warning("AppException [%s]: %s", exc.status_code, exc.detail)

    response = problem_response(exc.to_problem(instance=str(request.url)))

    if exc.status_code == 401 and request.url.path.startswith("/api/v1/"):
        response.headers["WWW-Authenticate"] = "Bearer"

    return response


async def validation_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """
    Handle Pydantic/FastAPI request validation failures.

    Returns HTTP 422 with structured validation errors in an extension
    member named ``errors``.

    Args:
        request: The incoming HTTP request.
        exc: The raised exception (expected to be ``RequestValidationError``).

    Returns:
        RFC 9457 problem detail response with status 422.
    """

    if not isinstance(exc, RequestValidationError):
        raise exc

    problem = ProblemDetail(
        type="about:blank",
        title="Validation Error",
        status=422,
        detail="Request Validation Failed",
        instance=str(request.url),
        errors=exc.errors(),
    )

    return problem_response(problem)


async def unhandled_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """
    Catch-all handler for unexpected exceptions.

    Logs the full traceback server-side but returns a generic HTTP 500
    problem response so internal implementation details are not leaked.

    Args:
        request: The incoming HTTP request.
        exc: The unhandled exception.

    Returns:
        Generic RFC 9457 500 problem detail response.
    """

    logger.exception("Unhandled Exception", exc_info=exc)

    # Never leak internal details to the client
    safe = AppException()
    return problem_response(safe.to_problem(instance=str(request.url)))
