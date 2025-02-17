from fastapi import FastAPI

from .api.v1 import root, healthcheck

from .core.settings import settings

app = FastAPI()

app.include_router(root.router)
app.include_router(healthcheck.router)

print(settings.google_sheets_url)