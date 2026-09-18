"""
Load Application Configuration from global config.yaml

Loads the config from the global yaml and validates
the loaded model defined in `config_models.py`
"""

from pathlib import Path

import yaml

from .config_models import Config

config_yaml_path = Path(__file__).resolve().parent.parent.parent / "config.yaml"

def load_config() -> Config:
    """
    Safe Load the config.yaml and return a validated object
    
    Returns:
        A validated Config Model Object
    """
    with Path(config_yaml_path).open() as file:
        raw = yaml.safe_load(file)

    return Config.model_validate(raw)
