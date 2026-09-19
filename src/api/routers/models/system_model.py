"""
Defines the Pydantic Models for System-Level Endpoints
"""

from typing import Literal
from pydantic import BaseModel


class HealthCheckResponse(BaseModel):
    """
    Health-Check Endpoint.
    GET /health
    
    Attributes:
        - status: Process liveness indicator
    """
    status: Literal["OK"]


class CheckResult(BaseModel):
    """
    Readiness Check Endpoint per-service Schema

    Attributes:
        - status: Whether the dependency is reachable (up, or down)
        - detail: Optional human-readable detail when service is down
    """
    status: Literal["up", "down"]
    detail: str | None = None


class ReadinessResponse(BaseModel):
    """
    Readiness Check Endpoint
    GET /readiness

    Attributes:
        - status: `ready` when all services are up, else `not_ready`
        - checks: Mapping of service name to its `CheckResult`
    """
    status: Literal["ready", "not_ready"]
    checks: dict[str, CheckResult]
