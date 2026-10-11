"""
SQLAlchemy ORM models for application users
"""

import enum

from sqlalchemy import Enum, String
from sqlalchemy.orm import Mapped, mapped_column

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
        name: User display name,
        role: User Role. Defaults to basic
        keycloak_subject: The keycloak subject, unique identifier for a Keycloak User
    """

    __tablename__ = "users"

    # NOTE: We're not passing nullable=False in these columns as
    # mapped_column is nullable=False when we provide a proper type,
    # Mapped[str], rather than Mapped[str | None]

    user_id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: new_uuid("user"))
    email: Mapped[str] = mapped_column(String, unique=True)
    name: Mapped[str] = mapped_column(String)
    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole, name="user_role", values_callable=lambda roles: [r.value for r in roles]),
        default=UserRole.BASIC,
        server_default="basic",
    )
    keycloak_subject: Mapped[str] = mapped_column(String, unique=True, nullable=False)
