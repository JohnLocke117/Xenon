from pathlib import Path

from .secrets_models import Secrets

dotenv_path = Path(__file__).resolve().parent.parent.parent / ".env"

def load_secrets() -> Secrets:
    return Secrets(_env_file=dotenv_path)