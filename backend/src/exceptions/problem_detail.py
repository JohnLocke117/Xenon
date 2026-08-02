"""
Defines the RFC 9457 problem detail format

Defines the Pydantic model used to serialize API error responses as
`application/problem+json`. Extension members (e.g. validation `errors`)
are supported via Pydantic's `extra="allow"` configuration.
"""

from typing import Any
from pydantic import BaseModel, ConfigDict, Field

class ProblemDetail(BaseModel):
    """
    RFC 9457 Problem Details JSON object
    
    Represents the standard error payload returned by all API exception
    handlers. Extension members may be supplied as additional keyword
    arguments and are serialized at the top level of the JSON object.

    Attributes:
        type: URI identifying the problem type (default `about:blank`)
        title: Short, human-readable summary of the problem category
        status: HTTP status code for this occurrence
        detail: Human-readable explanation specific to this occurrence
        instance: URI identifying this specific occurrence
    """

    model_config = ConfigDict(extra="allow")  # Allow extension members

    type: str = Field(default="about:blank")
    title: str
    status: int
    detail: str
    instance: str | None = None

    def model_dump(self, **kwargs: Any) -> dict[str, Any]:
        """
        Generate a dictionary representation of the problem detail model
        
        Returns:
            A dictionary of the RFC 9457 Problem Detail Model
        """
        return super().model_dump(by_alias=True, exclude_none=True, **kwargs)
