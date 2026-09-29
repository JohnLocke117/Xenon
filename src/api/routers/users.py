"""
User HTTP Endpoints.
Contains:
    - User Signup: POST /users
"""

from fastapi import APIRouter, status

from src.services.user_service import create_user
from src.api.deps import DbSession
from src.api.routers.models.user_model import SignupRequest, UserResponse

router = APIRouter()


@router.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
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