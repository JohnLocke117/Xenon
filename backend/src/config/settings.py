from dataclasses import dataclass
from functools import lru_cache

from .config_loader import load_config
from .config_models import Config
from .secrets_loader import load_secrets
from .secrets_models import Secrets


@dataclass(frozen=True)
class Settings:
    config: Config
    secrets: Secrets


@lru_cache
def get_settings() -> Settings:
    return Settings(config=load_config(), secrets=load_secrets())


settings = get_settings()
