"""
The User Service that handles user CRUD and other logic.
Currently supports:
    - Get User (get_user)
    - Create New User (create_user)
"""

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.config.settings import settings
from src.db.models.user import User, UserRole
from src.exceptions.exceptions import ConflictError


def get_user(db: Session, *, keycloak_subject: str) -> User | None:
    """
    Find a User by its linked Keycloak subject field (sub)

    Args:
        db: Request-scoped DB Session
        keycloak_subject: Stable sub claim from a validated Keycloak Identity

    Returns:
        The matching user, or None if no Account is linked to this subject
    """

    subject = keycloak_subject.strip()

    if not subject:
        raise ValueError("Keycloak Subject cannot be empty")

    # Get the User
    user = db.scalar(select(User).where(User.keycloak_subject == subject))

    return user


def create_user(db: Session, *, keycloak_subject: str, email: str, name: str) -> User:
    """
    Create a User linked to a Keycloak Identity.
    The caller must commit to DB.

    Args:
        db: Request scoped database session
        keycloak_subject: Stable sub claim from a validated Keycloak Identity
        email: Email from the validated Keycloak Identity
        name: Display name from the validated Keycloak Identity

    Returns:
        The flushed User, including its generated User UUIDv7

    Raises:
        ValueError: If a required identity field is empty
        ConflictError: If the email or Keycloak subject is already in use
    """

    subject = keycloak_subject.strip()
    normalised_email = email.strip().lower()
    normalised_name = name.strip()

    if not subject:
        raise ValueError("Keycloak subject cannot be empty")
    if not normalised_email:
        raise ValueError("Email cannot be empty")
    if not normalised_name:
        raise ValueError("Name cannot be empty")

    # Define the User Role
    role = UserRole.ADMIN if normalised_email in settings.secrets.admin_emails else UserRole.BASIC

    user = User(keycloak_subject=subject, email=normalised_email, name=normalised_name, role=role)

    db.add(user)

    try:
        db.flush()
    except IntegrityError:
        db.rollback()
        raise ConflictError("The Email or Keycloak Identity is already linked to a User") from None

    return user
