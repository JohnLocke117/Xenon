"""
Provide authentication dependencies for business REST API routes.

Read the bearer token, validate it, and resolve its Keycloak identity
to a local Xenon user.
"""

from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.api.deps import DbSession
from src.auth.keycloak import validate_access_token
from src.auth.principal import Principal
from src.exceptions.exceptions import UnauthorizedError
from src.services.user_service import get_user

bearer = HTTPBearer(auto_error=False)

# Credentials extracted from the request's Authorization header
BearerCredentials = Annotated[HTTPAuthorizationCredentials | None, Depends(bearer)]


def get_principal(credentials: BearerCredentials, db: DbSession) -> Principal:
    """
    Authenticate the request and resolve its xenon identity

    Args:
        credentials: Bearer credentials read from the request, or None when
            a Bearer credential is not provided
        db: The database session for this request

    Returns:
        The authenticated user's Xenon ID and current role

    Raises:
        UnauthorizedError: The credential is missing or invalid, or no
            Xenon user is linked to the validated Keycloak identity
        ServiceUnavailableError: Keycloak's signing keys cannot be fetched
    """

    if credentials is None:
        raise UnauthorizedError("Bearer authentication is required")

    subject = validate_access_token(credentials.credentials)
    user = get_user(db, keycloak_subject=subject)

    if user is None:
        raise UnauthorizedError("No Xenon account linked to this identity")

    return Principal(user_id=user.user_id, role=user.role)


# The authenticated Xenon identity injected into an endpoint
PrincipalDep = Annotated[Principal, Depends(get_principal)]
