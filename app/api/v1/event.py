from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ...db.database import get_db
from ...db.models import Event

router = APIRouter(
    prefix="/event"
)

@router.get("/")
def get_events(skip: int=0, limit: int=10, db: Session = Depends(get_db)):
    """
    Fetches a list of events from the database with optional pagination.

    This function retrieves a list of events from the database by applying
    pagination through the `skip` and `limit` parameters. It uses SQLAlchemy
    to query the database session. The retrieved events are returned as a list.

    :param skip: The number of records to skip from the start of the query result.
                 Default value is 0.
    :type skip: int
    :param limit: The maximum number of records to retrieve. Default value is 10.
    :type limit: int
    :param db: The database session dependency for querying the database.
    :type db: Session
    :return: A list of events fetched from the database.
    :rtype: list
    """
    events = db.query(Event).offset(skip).limit(limit).all()
    return events