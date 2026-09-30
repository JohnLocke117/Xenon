"""
Pydantic Definitions of Secrets being loaded from
`backend/.env`
Inherits validation logic from pydantic_settings.BaseSettings

When adding a new secret, add the corresponding field
type in the Secrets class
"""

from pydantic import computed_field
from pydantic_settings import BaseSettings


class Secrets(BaseSettings):
    """
    Defines the secrets loaded from backend/.env
    """

    ADMIN_EMAILS: str = ""
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    @computed_field  # type: ignore[prop-decorator]
    @property  # Allows us to access as .DATABASE_URL (attribute) instead of .DATABASE_URL()
    def DATABASE_URL(self) -> str:
        """
        Build a PostgreSQL connection URL from the DB_* fields
        """
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @computed_field  # type: ignore[prop-decorator]
    @property
    def admin_emails(self) -> set[str]:
        """Lowercased admin addresses from ADMIN_EMAILS"""
        return {email.strip().lower() for email in self.ADMIN_EMAILS.split(",") if email.strip()}
