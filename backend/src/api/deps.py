"""
Shared FastAPI dependency aliases

Routes import these aliases instead of repeating
`Annotated[..., Depends(...)]`

Override providers in tests via `app.dependency_overrides`
"""

from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from src.config.settings import Settings, get_settings
from src.db.session import get_db

DbSession = Annotated[Session, Depends(get_db)]
SettingsDep = Annotated[Settings, Depends(get_settings)]
