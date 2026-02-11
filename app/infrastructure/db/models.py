from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.infrastructure.db.session import Base


class CheckInModel(Base):
    __tablename__ = "checkins"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    document = Column(String)
    # Use application-level default for portability across DBs
    created_at = Column(DateTime, default=func.now(), nullable=True)