from app.core.settings import settings

def test_read_google_sheets_url():
    url = settings.google_sheets_url
    assert url is not None
    assert url != ''