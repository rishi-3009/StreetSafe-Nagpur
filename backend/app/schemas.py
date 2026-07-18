from datetime import datetime
from pydantic import BaseModel, field_validator

from app.config import NAGPUR_BOUNDS

VALID_CATEGORIES = {"Harassment", "Poor Lighting", "Accident", "Crime"}


class ReportCreate(BaseModel):
    """Shape of data the frontend sends when submitting a new report."""
    category: str
    latitude: float
    longitude: float
    incident_time: datetime

    @field_validator("category")
    @classmethod
    def category_must_be_valid(cls, v):
        if v not in VALID_CATEGORIES:
            raise ValueError(f"category must be one of {VALID_CATEGORIES}")
        return v

    @field_validator("latitude")
    @classmethod
    def latitude_in_bounds(cls, v):
        if not (NAGPUR_BOUNDS["min_lat"] <= v <= NAGPUR_BOUNDS["max_lat"]):
            raise ValueError("latitude is outside the Nagpur area")
        return v

    @field_validator("longitude")
    @classmethod
    def longitude_in_bounds(cls, v):
        if not (NAGPUR_BOUNDS["min_lng"] <= v <= NAGPUR_BOUNDS["max_lng"]):
            raise ValueError("longitude is outside the Nagpur area")
        return v


class ReportOut(BaseModel):
    """Shape of data the API sends back — includes fields the DB generates."""
    id: int
    category: str
    latitude: float
    longitude: float
    incident_time: datetime
    status: str

    class Config:
        from_attributes = True
