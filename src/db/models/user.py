"""
SQLAlchemy ORM models for application users
"""

import enum

from sqlalchemy import Column, Enum, String

from src.db.base import Base
from src.db.generate_uuid import new_uuid


class UserRole(enum.Enum):
    """
    Class to define allowed User Roles
    """

    BASIC = "basic"
    ADMIN = "admin"


class User(Base):
    """
    Application User stored in Postgres

    Attributes:
        user_id: A unique user ID. Used as primary key
        email: User Email, unique and non-nullable
        password_hash: Hashed User Password
        name: User display name,
        role: User Role. Defaults to basic
    """

    __tablename__ = "users"

    user_id = Column(String, primary_key=True, nullable=False, default=lambda: new_uuid("user"))
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)
    name = Column(String, nullable=False)
    role = Column(
        Enum(UserRole, name="user_role"),
        nullable=False,
        default=UserRole.BASIC,
        server_default="basic",
    )
