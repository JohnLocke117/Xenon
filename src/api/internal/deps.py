"""
Defines the dependencies for authenticating
trusted internal service requests
"""

import secrets
from typing import Annotated

from fastapi import Header

from src.api.deps import SettingsDep
from src.exceptions.exceptions import UnauthorizedError


def require_bff_service(
    settings: SettingsDep,
    supplied_token: Annotated[str | None, Header(alias="X-BFF-Service-Token")] = None
) -> None:
    """
    Allow requests carrying the configured BFF Service Token

    The token authenticates the calling service. It does not prove that
    user identity fields in the request body came from Keycloak; the BFF
    must validate the Keycloak identity before calling this endpoint.
    """
    
    expected_token = settings.secrets.BFF_SERVICE_TOKEN

    if supplied_token is None or not secrets.compare_digest(supplied_token, expected_token):
        raise UnauthorizedError("Invalid Service Credentials")