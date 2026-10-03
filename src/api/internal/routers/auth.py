"""
Internal User/Signup HTTP Endpoints
These are Internal Endpoints, not exposed to the user and used
only by Services like the UI-BFF

Contains:
    - User Provision: POST /provision
"""

from fastapi import APIRouter, Depends, status

from src.api.deps import DbSession
from src.api.internal.deps import require_bff_service
from src.api.models.user_model import ProvisionRequest, UserResponse
from src.services.user_service import create_user, get_user

router = APIRouter(dependencies=[Depends(require_bff_service)])


@router.post(
    "/provision",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    include_in_schema=False,
)
def provision(body: ProvisionRequest, db: DbSession) -> UserResponse:
    """
    Provision a User. Create if user doesn't exist.

    Returns:
        The created user

    Raises:
        ConflictError: This email is already registered
    """

    # Get the User
    user = get_user(db, keycloak_subject=body.keycloak_subject)

    # If User does not exist, create it:
    if user is None:
        user = create_user(
            db, keycloak_subject=body.keycloak_subject, email=body.email, name=body.name
        )

    db.commit()

    return UserResponse.model_validate(user)
