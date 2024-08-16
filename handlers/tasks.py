from fastapi import APIRouter


router = APIRouter(prefix="/task", tags=["task"])  # Create a router


@router.get("/all")
async def get_tasks():
    return {"message": "OK"}


@router.post("/")
async def create_task():
    return {"message": "app is working"}
