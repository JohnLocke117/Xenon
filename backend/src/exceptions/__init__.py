"""
Global exception handling for the Xenon API.

Public exports for raising domain exceptions and referencing the
RFC 9457 problem detail model.
"""

from .base import AppException
from .exceptions import NotFoundError
from .problem_detail import ProblemDetail

__all__ = ["AppException", "NotFoundError", "ProblemDetail"]