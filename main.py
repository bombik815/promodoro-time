import uvicorn
from fastapi import FastAPI

from handlers import routers

app = FastAPI()  # create an instance of FastAPI

for router in routers:
    # include router in application
    app.include_router(router=router)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
