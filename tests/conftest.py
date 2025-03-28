import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import new_session, init_db


@pytest.fixture
async def async_session() -> AsyncSession:
    await init_db()
    async with new_session() as session:
        yield session
