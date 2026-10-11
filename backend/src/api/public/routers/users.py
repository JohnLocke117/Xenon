"""
Expose REST API endpoints for the authenticated user's Xenon profile
"""

from fastapi import APIRouter

from src.api.deps import DbSession
from src.api.models.user_model import UserResponse
from src.api.public.deps import PrincipalDep
from src.db.models.user import User
from src.exceptions.exceptions import UnauthorizedError

router = APIRouter()


@router.get("/users/me", response_model=UserResponse)
def get_me(principal: PrincipalDep, db: DbSession) -> UserResponse:
    """
    Return the authenticated user's Xenon profile

    Args:
        principal: The Xenon identity resolved by the authentication dependency
        db: The database session for this request

    Returns:
        The user's ID, email, name, and role

    Raises:
        UnauthorizedError: The authenticated user's account no longer exists
    """

    user = db.get(User, principal.user_id)

    if user is None:
        raise UnauthorizedError("The Xenon account no longer exists")

    return UserResponse.model_validate(user)
