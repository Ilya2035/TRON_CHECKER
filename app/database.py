from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.models import Base

engine = create_async_engine("sqlite+aiosqlite///tronchecker.db")

new_session = async_sessionmaker(engine, expire_on_commit=False)


async def init_db() -> None:
    """
    Создание таблиц на основе ORM-моделей.
    Вызывается один раз при старте приложения.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_session():
    """
    Асинхронный генератор сессий для FastAPI-зависимостей.
    Используем в эндпоинтах через Depends.
    """
    async with new_session() as session:
        yield session
