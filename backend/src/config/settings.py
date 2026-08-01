"""
Central Access Point for App Configuration

Combines validated values from `config.yaml` and `backend/.env` into
a single Settings object. The module-level `settings` singleton
is created at import time
"""

from dataclasses import dataclass
from functools import lru_cache

from .config_loader import load_config
from .config_models import Config
from .secrets_loader import load_secrets
from .secrets_models import Secrets


@dataclass(frozen=True)
class Settings:
    """
    A dataclass holding the Validation Classes for config and secrets

    Attributes:
        config: Configuration values loaded from `config.yaml`
        secrets: Secrets and Credentials loaded from `backend/.env`
    """
    config: Config
    secrets: Secrets


@lru_cache
def get_settings() -> Settings:
    """
    Load config and secrets
    The result is memoised (cached) by @lru_cache so the configuration
    is read once per process

    Returns:
        A `Settings` instance containing validated configuration and secrets
    """
    return Settings(config=load_config(), secrets=load_secrets())


# Create the Settings Object
settings = get_settings()
