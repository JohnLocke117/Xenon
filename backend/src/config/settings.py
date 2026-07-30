from functools import lru_cache
from dataclasses import dataclass

from .config_models import Config
from .secrets_models import Secrets

from .config_loader import load_config
from .secrets_loader import load_secrets

@dataclass(frozen=True)
class Settings:
    config: Config
    secrets: Secrets


@lru_cache
def get_settings() -> Settings:
    return Settings(
        config=load_config(),
        secrets=load_secrets()
    )

settings = get_settings()