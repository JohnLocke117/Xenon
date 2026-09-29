"""
Pydantic Models for User endpoints
"""

from pydantic import BaseModel, ConfigDict

from src.db.models.user import UserRole


class SignupRequest(BaseModel):
    """
    Body for POST /api/v1/users
    """

    email: str
    password: str
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