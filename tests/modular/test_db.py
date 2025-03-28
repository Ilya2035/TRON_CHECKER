"""Tests for database interactions related to Tron address requests."""

import pytest
from sqlalchemy import select

from app.database import new_session, init_db
from app.crud.tron_requests import create_tron_request_record
from app.models import RequestsToTron


@pytest.mark.asyncio
async def test_create_tron_request_record():
    """
    Test creating a new record in the database using create_tron_request_record.

    Verifies the record is saved and can be queried from the database.
    """
    await init_db()
    async with new_session() as async_session:
        test_address = "TXYZ1234567890ABCDEF"

        created = await create_tron_request_record(test_address, async_session)

        result = await async_session.execute(
            select(RequestsToTron).where(RequestsToTron.id == created.id)
        )
        record = result.scalar_one_or_none()

        assert record is not None
        assert record.id == created.id
        assert record.tron_address == test_address
