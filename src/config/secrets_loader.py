"""
Load Secrets from backend/.env

Loads the secrets and validates them against the Pydantic
model defined in `secrets_models.py`
"""

from pathlib import Path

from .secrets_models import Secrets

dotenv_path = Path(__file__).resolve().parent.parent.parent / ".env"


def load_secrets() -> Secrets:
    """
    Load and return a Secrets object

    Returns:
        A validated Secrets Model Object
    """
    return Secrets(_env_file=dotenv_path)
