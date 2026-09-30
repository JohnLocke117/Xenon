"""
Utility helper function to hash the passwords
before storing into the Database.
"""

import hashlib
import secrets


def hash_password(password: str) -> str:
    """
    Return a scrypt hash as scrypt$<salt hex>$<hash hex>

    Attributes:
        - password: A plain text password recived via /signup endpoint

    Returns:
        A hashed password that is stored into the DB as password_hash
    """

    salt = secrets.token_bytes(16)
    digest = hashlib.scrypt(password.encode(), salt=salt, n=2**14, r=8, p=1)

    return f"scrypt${salt.hex()}${digest.hex()}"
