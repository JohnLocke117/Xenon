"""
Pydantic Definitions of Valid Configurations loaded from
the global `config.yaml`

When adding a new field in `config.yaml`, add the type in
the corresponding class

To add a new section, define a new Config Class and add to
the final `Config` class
"""

from pydantic import BaseModel


class AppConfig(BaseModel):
    """
    General Application Configuration
    """

    name: str
    version: str


class ServerConfig(BaseModel):
    """
    Backend FastAPI Server Configuration
    """

    host: str
    port: int


class AuthConfig(BaseModel):
    """
    Trusted Keycloak Settings for API authentication

    Attributes:
        issuer: The exact issuer value accepted in access tokens
        audience: The audience that identifies the Xenon REST API
        jwks_url: The trusted endpoint used to fetch public signing keys
    """

    issuer: str
    audience: str
    jwks_url: str


class Config(BaseModel):
    """
    Collect the application settings loaded from config.yaml

    Attributes:
        app: The application specific (name, version) settings
        server: The backend server settings
        auth: The Keycloak token-validation settings
    """

    app: AppConfig
    server: ServerConfig
    auth: AuthConfig
