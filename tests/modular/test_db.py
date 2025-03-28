import pytest


@pytest.mark.asyncio
async def test_create_tron_request_record():
    from app.database import new_session, init_db

    await init_db()
    async with new_session() as async_session:
        test_address = "TXYZ1234567890ABCDEF"

        from app.crud.tron_requests import create_tron_request_record
        record = await create_tron_request_record(test_address, async_session)

        assert record.tron_address == test_address
