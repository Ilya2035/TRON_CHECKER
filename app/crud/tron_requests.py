"""CRUD operations for Tron request records."""

from sqlalchemy.ext.asyncio import AsyncSession

from app.models import RequestsToTron


async def create_tron_request_record(address: str, db: AsyncSession) -> RequestsToTron:
    """
    Create and save a new record of a Tron address request.

    Args:
        address (str): Tron address.
        db (AsyncSession): Database session.

    Returns:
        RequestsToTron: The created database record.
    """
    record = RequestsToTron(tron_address=address)
    db.add(record)
    await db.commit()
    await db.refresh(record)
    return record
