import logging
from fastapi import APIRouter

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/")
async def root():
    logger.info("This is a Sample Log")
    return {"message": "Hehe Bwoii"}

@router.get("/hehe/{name}")
async def say_my_name(name: str):
    logger.info("This is a Sample Log")
    return {"message": f"{name}. You're Goddamn Right."}

