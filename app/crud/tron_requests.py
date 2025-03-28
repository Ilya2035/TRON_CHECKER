from sqlalchemy.ext.asyncio import AsyncSession
from app.models import RequestsToTron


async def create_tron_request_record(address: str, db: AsyncSession) -> RequestsToTron:
    record = RequestsToTron(tron_address=address)
    db.add(record)
    await db.commit()
    await db.refresh(record)
    return record
