"""FastAPI application entry point."""

from fastapi import FastAPI
from fastapi_pagination import add_pagination

from app.database import init_db
from app.routers.requests_for_tron import router as tron_router

app = FastAPI(title="Tron requests app")


@app.on_event("startup")
async def on_startup():
    """Initialize the database on application startup."""
    await init_db()

# Register router and enable pagination
app.include_router(tron_router)
add_pagination(app)  # library feature
