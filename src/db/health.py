"""
RDS (PostgreSQL) Readiness Probe

Provides a lightweight connection checks used by the system
readiness endpoint. Does not raise on failure, returns a status
dict instead
"""

import logging

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from src.db.session import engine

logger = logging.getLogger(__name__)


def check_postgres() -> dict[str, str | None]:
    """
    Runs a Simple query on DB and returns up/down status

    Executes `SELECT 1` using the application engine.

    Returns:
        A dict with `status` of `up` or `down`. When down,
        include a `detail` string suitable for API responses.
    """

    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {"status": "up"}

    except SQLAlchemyError:
        logger.exception("Readiness Check failed: Postgres Connection Failed")
        return {"status": "down", "detail": "Database Unreachable"}
