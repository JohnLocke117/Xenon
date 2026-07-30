from fastapi import FastAPI

from src.utils.logging import setup_logging
from src.api.routers.root import router as root_router

setup_logging("INFO")

app = FastAPI()

# Add the Router Instance
app.include_router(root_router, prefix="/api/v1")