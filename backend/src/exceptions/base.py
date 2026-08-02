"""
Define the base exception class that inherits from Python's Exception class

All domain and infrastructure errors raised in application code should
extend AppException. Each exception carries HTTP semantics and can be
converted to an RFC 9457 ProblemDetail via to_problem().
"""

from typing import Optional, Any, Dict

from .problem_detail import ProblemDetail

class AppException(Exception):
    """
    Base Application Exception: 500 Internal Server Error

    Subclasses override class attributes (status_code, title, type_uri)
    to represent specific error categories. Instances carry an occurrence-
    specific detail message and optional extension members.

    Attributes:
        status_code: HTTP status code returned to the client
        title: Stable, human-readable title for this error category
        type_uri: URI identifying the problem type (RFC 9457 `type` field)
        detail: Occurrence-specific error message
        extensions: Additional top-level RFC extension members
    """

    status_code: int = 500
    title: str = "Internal Server Error"
    type_uri: str = "about:blank"

    def __init__(
        self,
        detail: str = "An unexpected error occurred",
        type_uri: Optional[str] = None,
        extensions: Optional[Dict[str, Any]] = None
    ) -> None:
        """
        Initialise an application exception

        Args:
            detail: Human readable explanation for this exception
            type_uri: Optional override of the problem type URI
            extensions: Optional RFC extension members merged into the response
        """

        super.__init__(detail)
        self.detail = detail

        if type_uri:
            self.type_uri = type_uri
        self.extensions = extensions or {}
    
    def to_problem(self, instance: str | None = None) -> ProblemDetail:
        """
        Build a validated RFC 9457 Problem Detail Payload

        Args:
            instance: URI identifying this occurrence (typically the request URL)
        
        Returns:
            ProblemDetail: A validated ProblemDetail model ready for JSON serialisation
        """
        
        base = {
            "type": self.type_uri,
            "title": self.title,
            "status": self.status_code,
            "detail": self.detail,
            "instance": instance
        }

        return ProblemDetail(**base, **self.extensions)