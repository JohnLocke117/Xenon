"""
Internal User/Signup HTTP Endpoints
These are Internal Endpoints, not exposed to the user and used
only by Services like the UI-BFF

Contains:
    - User Signup: POST /signup
"""

from fastapi import APIRouter, status

from src.api.deps import DbSession
from src.api.models.user_model import SignupRequest, UserResponse
from src.services.user_service import create_user

router = APIRouter()


@router.post("/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def signup(body: SignupRequest, db: DbSession) -> UserResponse:
    """
    Create a basic user

    Returns:
        The created user without the password hash

    Raises:
        ConflictError: This email is already registered
    """

    user = create_user(db, email=body.email, password=body.password, name=body.name)
    db.commit()

    return UserResponse.model_validate(user)
