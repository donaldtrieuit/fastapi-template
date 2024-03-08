from datetime import datetime

from sqlalchemy import Column, DateTime, Integer

from core.db import Base


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(
        DateTime(timezone=True), nullable=True, onupdate=datetime.utcnow
    )
