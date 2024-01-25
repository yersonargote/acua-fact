from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from sqlmodel import text

from acua_fact.server.core.config import settings
from acua_fact.server.models.concepto import Concepto
from acua_fact.server.models.concepto_factura import ConceptoFactura
from acua_fact.server.models.persona import Persona
from acua_fact.server.models.factura import Factura
from acua_fact.server.models.pago import Pago

DATABASE_URL = settings.db_url

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    future=True,
    connect_args={"check_same_thread": False},
)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)
        with open("acua_fact/server/db/insertion.sql") as file:
            lines: list[str] = file.readlines()
            for line in lines:
                await conn.execute(text(line))


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async_session = sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )
    async with async_session() as session:
        yield session
