"""
System health and readiness HTTP Endpoints

Endpoints Included:
    - /health: Health Check
    - /readiness: Services Readiness Check
"""

import asyncio

from fastapi import APIRouter, Response, status

from src.api.routers.models.system_model import CheckResult, HealthCheckResponse, ReadinessResponse
from src.db.health import check_postgres

router = APIRouter()


# ----- GET /health: Health Check -----
@router.get("/health", response_model=HealthCheckResponse)
async def health() -> HealthCheckResponse:
    """
    Default Health Check endpoint

    Returns:
        HealthCheckResponse with `status` set to `OK`
    """

    return HealthCheckResponse(status="OK")


# ----- GET /readiness: All Services Readiness Check -----
CHECKS = [("postgres", check_postgres)]


@router.get("/readiness", response_model=ReadinessResponse)
async def readiness(response: Response) -> ReadinessResponse:
    """
    Readiness Endpoint, returns current status of all Services

    Each check is run in a worker thread. Sets HTTP 200 when every
    check is `up`, otherwise HTTP 503.

    Returns:
        ReadinessResponse with overall `status` and per-service
        `checks`
    """

    checks: dict[str, CheckResult] = {}

    for name, fn in CHECKS:
        result = await asyncio.to_thread(fn)
        checks[name] = CheckResult(**result)

    all_up = all(c.status == "up" for c in checks.values())
    response.status_code = status.HTTP_200_OK if all_up else status.HTTP_503_SERVICE_UNAVAILABLE

    return ReadinessResponse(status="ready" if all_up else "not_ready", checks=checks)
