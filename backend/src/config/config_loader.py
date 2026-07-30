import yaml
from pathlib import Path

from .config_models import Config

config_yaml_path = Path(__file__).resolve().parent.parent.parent / "config.yaml"

def load_config() -> Config:
    with Path(config_yaml_path).open() as file:
        raw = yaml.safe_load(file)

    return Config.model_validate(raw)