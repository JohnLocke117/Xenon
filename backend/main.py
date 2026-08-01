"""main.py file that serves as FastAPI App Entrypoint

This file initialises our global logging setup,
and our FastAPI app.
"""

from fastapi import FastAPI

from src.api.routers.root import router as root_router
from src.utils.logging import setup_logging

setup_logging("INFO")

app = FastAPI()

# Add the Router Instance
app.include_router(root_router, prefix="/api/v1")
