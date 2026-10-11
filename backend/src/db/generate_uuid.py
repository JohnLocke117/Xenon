"""
Generate and return a prefixed UUIDv7 for resources generated
in the application.

Currently, IDs are generated for:
    - users
"""

import uuid


def new_uuid(prefix: str) -> str:
    """
    Generates and Returns a prefixed UUIDv7, e.g., user_0199fhsa...

    Args:
        - prefix (str): String prefix for the ID

    Returns:
        - A string UUIDv7
    """
    return f"{prefix}_{uuid.uuid7().hex}"
