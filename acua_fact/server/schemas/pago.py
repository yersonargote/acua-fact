from datetime import date
from uuid import UUID

from sqlmodel import SQLModel

from acua_fact.server.models.pago import PagoBase


class PagoCreate(PagoBase):
    id: UUID


class PagoRead(PagoBase):
    id: UUID


class PagoUpdate(SQLModel):
    id: UUID | None = None
    fecha: date | None = None
    total: float | None = None
