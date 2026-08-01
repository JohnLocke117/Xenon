from sqlalchemy import Column, Integer, String

from src.db.base import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
