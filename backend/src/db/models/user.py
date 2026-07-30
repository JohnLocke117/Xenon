from src.db.base import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)