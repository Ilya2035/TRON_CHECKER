from fastapi import FastAPI
from fastapi_pagination import add_pagination

from app.database import init_db
from app.routers.requestsfortron import router as tron_router

app = FastAPI(title="Tron requests app")


@app.on_event("startup")
async def on_startup():
    await init_db()

app.include_router(tron_router)
add_pagination(app)