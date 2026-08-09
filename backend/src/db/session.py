"""
Define PostgreSQL engine and request-scoped Sessions.
The Database URL is read from settings.secrets.DATABASE_URL
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config.settings import settings

# Import the DB URL from the global settings object
DATABASE_URL = settings.secrets.DATABASE_URL

# Create a SQLAlchemy Engine:
engine = create_engine(url=DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    Provide a request-scoped database session

    Yields:
        A SQLAlchemy `Session` bound to the application engine, closed when the caller finishes
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
