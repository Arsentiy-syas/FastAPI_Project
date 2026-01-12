from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from typing import AsyncGenerator


DATABASE_URL_ASYNC = "postgresql+asyncpg://postgres:Ab362467@localhost/FirstFast"


async_engine = create_async_engine(
    url=DATABASE_URL_ASYNC,
    echo=False,
)


AsyncSessionLocal = async_sessionmaker(
    bind=async_engine, 
    class_=AsyncSession,
    expire_on_commit=False
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            session.close()


class Base(DeclarativeBase):
    pass