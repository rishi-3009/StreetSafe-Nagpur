from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/api/reports", tags=["reports"])


@router.post("", response_model=schemas.ReportOut, status_code=201)
def create_report(report: schemas.ReportCreate, db: Session = Depends(get_db)):
    """
    Saves a new incident report. Always saved as 'pending' —
    it will not appear on the public map until an admin approves it.
    """
    db_report = models.Report(
        category=report.category,
        latitude=report.latitude,
        longitude=report.longitude,
        incident_time=report.incident_time,
        status="pending",
    )
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return db_report


@router.get("", response_model=list[schemas.ReportOut])
def list_approved_reports(db: Session = Depends(get_db)):
    """
    Public endpoint — only ever returns reports an admin has approved.
    This is what the live map will call to display markers.
    """
    return db.query(models.Report).filter(models.Report.status == "approved").all()
