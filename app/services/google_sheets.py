import pandas as pd
from ..core.settings import settings
from datetime import datetime, date, time
from dateutil import parser
from app.core.utilities import calculate_row_hash

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

def get_events():
    events = get_event_data()

    parsed_events = []

    for event in events:
        try:
            event_date: date = event['Date / Time']
            event_time: time = event['test']
            event_datetime = datetime(year=event_date.year, month=event_date.month,
                                      day=event_date.day, hour=event_time.hour,
                                      minute=event_time.minute)
            event_hash = calculate_row_hash({
                'Information': event['Information'],
                'Cost': event['Cost'],
                'Link': event['Link'],
            })

            parsed_event = Event(
                datetime=event_datetime,
                type=event['type'],
                information=event['information'],
                venue=event['venue'],
                cost=event['cost'],
                link_type=event['link_type'],
                link=event['link'],
                hash=event_hash,
            )

            parsed_events.append(parsed_event)
        except Exception as e:
            print(f"The following exception occurred while parsing Event data into the Event model: {e}")
            continue

    return parsed_events

