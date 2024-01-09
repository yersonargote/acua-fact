from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

from acua_fact.server.models.persona import Persona
from acua_fact.server.models.factura import Factura
from acua_fact.server.models.pago import Pago
from acua_fact.server.models.concepto import Concepto
from acua_fact.server.models.concepto_factura import ConceptoFactura

# from acu_fact.server.db.sql_script import SQL_SCRITP

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/postgres"

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    future=True,
)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)
        # await conn.execute(SQL_SCRITP)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async_session = sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )
    async with async_session() as session:
        yield session
