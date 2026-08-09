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


class Config(BaseModel):
    """
    Final `Config` class that contains the whole configuration
    """
    app: AppConfig
    server: ServerConfig
