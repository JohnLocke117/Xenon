"""main.py file that serves as FastAPI App Entrypoint

This file initializes our global logging setup,
and our FastAPI app.
"""

from fastapi import APIRouter, Depends, FastAPI
from fastapi.exceptions import RequestValidationError

from src.api.internal.routers.auth import router as auth_router
from src.api.public.deps import get_principal
from src.api.public.routers.system import router as system_router
from src.api.public.routers.users import router as users_router
from src.exceptions.base import AppException
from src.exceptions.handlers import (
    app_exception_handler,
    unhandled_exception_handler,
    validation_exception_handler,
)
from src.utils.logging import setup_logging

setup_logging("INFO")

app = FastAPI()

# Add the Exception Handlers (in order)
app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)


# Add the Router Instances
# ---------- Internal Endpoints -----------
app.include_router(auth_router, prefix="/auth")

# ---------- Public Endpoints -----------
app.include_router(system_router, prefix="/api/v1")

# ---------- Business Endpoints ----------
business_router = APIRouter(prefix="/api/v1", dependencies=[Depends(get_principal)])

business_router.include_router(users_router)
app.include_router(business_router)
