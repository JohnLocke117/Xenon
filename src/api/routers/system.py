"""
Defines health and system startup endpoints
"""

import logging

from fastapi import APIRouter

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/health")
async def health():
    """
    Default Health Check endpoint
    """

    return {"message": "Health OK"}

@router.get("/readiness")
async def readiness():
    """
    Readiness Check for all Services and Infrastructure
    """

    return {"backend": "FastAPI Backend is OK"}