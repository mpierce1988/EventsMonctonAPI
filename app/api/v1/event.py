from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ...db.database import get_db
from ...db.models import Event

router = APIRouter(
    prefix="/event"
)

@router.get("/")
def get_events(skip: int=0, limit: int=10, db: Session = Depends(get_db)):
    events = db.query(Event).offset(skip).limit(limit).all()
    return events