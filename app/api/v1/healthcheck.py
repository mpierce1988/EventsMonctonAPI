from fastapi import APIRouter

router = APIRouter(
    prefix="/v1/healthcheck"
)

@router.get("/")
async def check_health():
    return {"status": "OK"}