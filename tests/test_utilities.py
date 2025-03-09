from datetime import datetime
from app.core import utilities

def test_get_hash():
    event_data = {
        "datetime": datetime(2023, 10, 1),
        "type": "Festival",
        "information": "Chocolat Moncton: Hot Chocolate Festival",
        "venue": "various",
        "cost": "$140",
        "link_type": "Website",
        "link": "https://chocolatmoncton.com/"
    }

    test_hash = utilities.calculate_row_hash(event_data)

    assert test_hash is not None

