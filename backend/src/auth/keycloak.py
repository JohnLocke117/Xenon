"""
Validate Keycloak access tokens for the Xenon REST API

Fetch and cache Keycloak's public signing keys. Check each token before
returning the identity that Xenon uses to find its local user.
"""

from functools import lru_cache

import jwt
from jwt import PyJWKClient
from jwt.exceptions import InvalidTokenError, PyJWKClientConnectionError, PyJWKClientError

from src.config.settings import get_settings
from src.exceptions.exceptions import ServiceUnavailableError, UnauthorizedError


@lru_cache
def get_jwks_client() -> PyJWKClient:
    """
    Return the shared client used to fetch Keycloak's signing keys.

    Reuse a client with a cached Keycloak public-key set for five
    minutes to reduce requests to Keycloak.

    Returns:
        The client configured for the trusted Keycloak key endpoint
    """

    config = get_settings().config.auth
    return PyJWKClient(config.jwks_url, cache_jwk_set=True, lifespan=300, timeout=5)


def validate_access_token(token: str) -> str:
    """
    Validate a Keycloak access token and return its Keycloak User ID

    Check the signature, issuer, audience, token lifetime and required
    claims. Accept only tokens intended for the Xenon REST API.

    Args:
        token: The encoded access token from the Authorization header

    Returns:
        The validated subject claim, which identifies the Keycloak user

    Raises:
        UnauthorizedError: The token is invalid, expired or is not an accepted access token
        ServiceUnavailableError: Keycloak's signing keys cannot be fetched.
    """

    config = get_settings().config.auth

    try:
        signing_key = get_jwks_client().get_signing_key_from_jwt(token)

        claims = jwt.decode(
            token,
            signing_key.key,
            algorithms=["RS256"],
            issuer=config.issuer,
            audience=config.audience,
            options={"require": ["exp", "iat", "iss", "aud", "sub"]},
            leeway=5,
        )
    except PyJWKClientConnectionError as exc:
        raise ServiceUnavailableError(
            "Authentication verification is temporarily unavailable"
        ) from exc
    except (InvalidTokenError, PyJWKClientError) as exc:
        raise UnauthorizedError("Invalid or expired access token") from exc

    subject = claims.get("sub")

    if not isinstance(subject, str) or not subject.strip():
        raise UnauthorizedError("Invalid Access Token")

    # Keycloak's payload claim distinguishes its access token
    if claims.get("typ") != "Bearer":
        raise UnauthorizedError("An access token is required")

    return subject
