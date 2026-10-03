"""
Pydantic Models for User endpoints
"""

from pydantic import BaseModel, ConfigDict

from src.db.models.user import UserRole


class ProvisionRequest(BaseModel):
    """
    Body for POST /auth/provision
    """
    keycloak_subject: str
    email: str
    name: str


class UserResponse(BaseModel):
    """
    Public User fields. The hashed password is never included
    """

    model_config = ConfigDict(from_attributes=True)

    user_id: str
    email: str
    name: str
    role: UserRole
