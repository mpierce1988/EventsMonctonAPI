import pandas as pd
from ..core.settings import settings
from datetime import datetime, date, time
from dateutil import parser

from ..db.models import Event

GOOGLE_SHEETS_URL = settings.google_sheets_url

def get_event_data():
    all_sheets = pd.read_excel(GOOGLE_SHEETS_URL, sheet_name=None)

    # List to store events
    events = []

    current_date = datetime.now()

    for sheet_name, df in all_sheets.items():
        try:
            sheet_date = parser.parse(sheet_name)

            if sheet_date.year >= current_date.year and sheet_date.month >= current_date.month:
                df['sheet_source'] = sheet_name
                sheet_events = df.to_dict(orient="records")
                events.extend(sheet_events)

        except (ValueError, TypeError):
            # Failed to parse date from sheet name
            continue

    return events

"""
def get_events():
    events = get_event_data()

    parsed_events = []

    datetime.now().

    for event in events:
        event_date: date = event['Date / Time']
        event_time: time = event[]
        parsed_event = Event(
            datetime = datetime(year=event["Date / Time"].year, month=event['Date / Time'])
            type = event['type'],
            venue = event['venue'],
            information = event['information']
        )

        parsed_events.append(parsed_event)

    return parsed_events
"""
