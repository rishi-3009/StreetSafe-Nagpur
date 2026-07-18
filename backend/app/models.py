from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func

from app.database import Base


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    incident_time = Column(DateTime, nullable=False)
    reported_at = Column(DateTime(timezone=True), server_default=func.now())

    # pending -> approved -> visible on the public map
    # pending -> rejected -> never shown publicly
    status = Column(String, nullable=False, default="pending")
