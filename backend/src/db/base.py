"""
Define the base class that inherits from SQLAlchemy DeclarativeBase

All ORM Models inherit from `Base`. Its metadata is used by Alembic
for schema autogeneration
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Declarative Base Class for all SQLAlchemy ORM models
    """
    pass
