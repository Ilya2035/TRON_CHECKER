from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.models import Base

engine = create_async_engine("sqlite+aiosqlite:///tronchecker.db")

new_session = async_sessionmaker(engine, expire_on_commit=False)


async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_session():
    async with new_session() as session:
        yield session
