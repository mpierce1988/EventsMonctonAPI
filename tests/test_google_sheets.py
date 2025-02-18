from app.services.google_sheets import get_event_data
from datetime import datetime

def test_get_event_data():
    # Arrange
    current_date = datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)

    # Act
    events = get_event_data()

    # Assert
    assert events is not None
    assert len(events) > 0
    assert all(
        event["Date / Time"].replace(day=1) >= current_date.replace(day=1)
        for event in events
    )