"""
The User Service that handles user CRUD and other logic.
Currently supports:
    - Create New User (create_user)
    - Get User by UUID (get_user_by_uuid)
    - Get User by Email (get_user_by_email)
    - Update User (update_user)
    - Delete User (delete_user)
"""

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.config.settings import settings
from src.db.models.user import User, UserRole
from src.exceptions import NotFoundError
from src.exceptions.exceptions import ConflictError
from src.utils.hash_password import hash_password


def create_user(db: Session, email: str, password: str, name: str) -> User:
    """
    Insert a basic/admin user.

    Args:
        db: Request-scoped DB Session. The caller commits
        email: User email, stored lowercase
        password: Hashed before insertion into DB. Raw text value is not stored
        name: Display name

    Returns:
        The flushed User, including its generated user_id

    Raises:
        ConflictError: If a user with this email already exists
    """

    # Set role to admin if email is present in ADMIN_EMAILS
    normalised_email = email.strip().lower()

    role = (
        UserRole.ADMIN
        if normalised_email in settings.secrets.admin_emails
        else UserRole.BASIC
    )

    # NOTE: user_id is omitted as it is created by column default for each user
    user = User(
        email=email.strip().lower(),
        password_hash=hash_password(password),
        name=name,
        role=role,
    )

    db.add(user)

    try:
        db.flush()
    except IntegrityError:
        db.rollback()
        raise ConflictError("A User with this email already exists") from None

    return user


def get_user_by_uuid(db: Session, user_id: str) -> User:
    """
    Load one user by primary key

    Args:
        db: Request-scoped DB Session
        user_id: Prefixed UUIDv7

    Returns:
        The matching User

    Raises:
        NotFoundError: No row with the specified user_id found
    """

    user = db.get(User, user_id)

    if user is None:
        raise NotFoundError("User Not Found")

    return user


def get_user_by_email(db: Session, email: str) -> User | None:
    """
    Load one user by email

    Args:
        db: Request-scoped DB Session
        email: Compared after strip and lowercase, matching create_user

    Returns:
        The matching User, or None when no user has the specified Email
    """

    normalized_email = email.strip().lower()

    # db.scaler() Returns first matching User or None
    return db.scalar(select(User).where(User.email == normalized_email))


def update_user(db: Session, user_id: str, new_name: str) -> User:
    """
    Update a User's metadata

    Args:
        db: Request-Scoped DB Session. The caller commits
        user_id: Prefixed UUIDv7
        new_name: New name to be updated

    Raises:
        NotFoundError: from get_user_by_uuid(), if no user has this user_id
    """
    user = get_user_by_uuid(db, user_id)

    user.name = new_name
    db.flush()

    return user


def delete_user(db: Session, user_id: str) -> None:
    """
    Delete one user

    Args:
        db: Request scoped User Session
        user_id: Prefixed UUIDv7

    Raises:
        NotFoundError: No row has this user_id
    """

    user = get_user_by_uuid(db, user_id)

    db.delete(user)
    db.flush()
