from fastapi import FastAPI

from .api.v1 import root, healthcheck

app = FastAPI()

app.include_router(root.router)
app.include_router(healthcheck.router)