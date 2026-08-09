"""main.py file that serves as FastAPI App Entrypoint

This file initialises our global logging setup,
and our FastAPI app.
"""

from .src.exceptions.base import AppException
from .src.exceptions.handlers import (
    app_exception_handler,
    unhandled_exception_handler,
    validation_exception_handler,
)
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from src.api.routers.system import router as system_router
from src.utils.logging import setup_logging

setup_logging("INFO")

app = FastAPI()

# Add the Exception Handlers (in order)
app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)


# Add the Router Instance
app.include_router(system_router, prefix="/api/v1")
