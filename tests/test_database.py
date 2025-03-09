from app.db.database import get_db
from app.db.models import Event
from datetime import datetime
from app.core import utilities

def test_get_db(db_session):
    db = next(get_db())  # Gets next item from iterator (get_db() has a yield)
    assert db is not None

def test_create_event(db_session):
    event_data = {
        "datetime": datetime(2023, 10, 1),
        "type": "Festival",
        "information": "Chocolat Moncton: Hot Chocolate Festival",
        "venue": "various",
        "cost": "$140",
        "link_type": "Website",
        "link": "https://chocolatmoncton.com/"
    }

    event_data['hash'] = utilities.calculate_row_hash(event_data)

    event = Event(**event_data)
    db_session.add(event)
    db_session.commit()

    stored_event = db_session.query(Event).filter(Event.information == event_data["information"]).first()
    assert stored_event is not None
    assert stored_event.type == event_data["type"]
    assert stored_event.datetime == event_data["datetime"]
    assert stored_event.venue == event_data["venue"]
    assert stored_event.cost == event_data["cost"]
    assert stored_event.link_type == event_data["link_type"]
    assert stored_event.link == event_data["link"]
    assert stored_event.hash == event_data['hash']
    assert stored_event.id is not None