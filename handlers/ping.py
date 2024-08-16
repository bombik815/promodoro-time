from fastapi import APIRouter


router = APIRouter(prefix="/ping", tags=["ping"])  # Create a router


@router.get("/db")
async def ping_db():
    return {"message": "OK"}


@router.get("/app")
async def ping_app():
    return {"message": "app is working"}
