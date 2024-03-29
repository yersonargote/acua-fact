from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from acua_fact.server.api import (
    conceptos_factura_router,
    conceptos_router,
    facturas_router,
    pagos_router,
    personas_router,
)
from acua_fact.server.core.config import settings
from acua_fact.server.db.session import create_db_and_tables

origins = settings.origins


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(personas_router)
app.include_router(conceptos_router)
app.include_router(facturas_router)
app.include_router(conceptos_factura_router)
app.include_router(pagos_router)
