"""Pytest fixtures for setting up the database session."""

import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import new_session, init_db


@pytest.fixture
async def async_session() -> AsyncSession:
    """
    Fixture that provides an initialized async database session
    for use in tests.
    """
    await init_db()
    async with new_session() as session:
        yield session
