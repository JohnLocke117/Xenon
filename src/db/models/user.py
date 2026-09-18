"""
SQLAlchemy ORM models for application users
"""

from sqlalchemy import Column, Integer, String

from src.db.base import Base


class User(Base):
    """
    Application User stored in Postgres

    Attributes:
        user_id: A unique user ID. Used as primary key
        name: User display name
    """
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
