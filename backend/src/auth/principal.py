"""
Contains the application identity needed by REST Endpoints.
Independent of token claims and other Keycloak details.
"""

from dataclasses import dataclass

from src.db.models.user import UserRole


@dataclass(frozen=True)
class Principal:
    """
    The authenticated xenon identity for a request

    Attributes:
        user_id: The user's ID in the Xenon Database
        role: The user's current role in the DB
    """

    user_id: str
    role: UserRole
