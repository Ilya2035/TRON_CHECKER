from fastapi import FastAPI

from app.database import init_db

app = FastAPI(title="Tron requests app")


@app.on_event("startup")
async def on_startup():
    await init_db()

