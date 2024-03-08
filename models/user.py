from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, String

from models.base import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    username = Column(String(length=150), nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    first_name = Column(String(length=150), nullable=True)
    last_name = Column(String(length=150), nullable=True)
    is_active = Column(Boolean, nullable=False, default=False)
    is_superuser = Column(Boolean, nullable=False, default=False)
    date_joined = Column(DateTime, nullable=False, default=datetime.utcnow)
