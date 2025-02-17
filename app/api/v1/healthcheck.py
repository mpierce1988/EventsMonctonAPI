from fastapi import APIRouter

router = APIRouter(
    prefix="/healthcheck"
)

@router.get("/")
async def check_health():
    return {"status": "OK"}