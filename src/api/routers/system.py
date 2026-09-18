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

