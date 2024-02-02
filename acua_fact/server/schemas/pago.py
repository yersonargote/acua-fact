from datetime import date

from sqlmodel import SQLModel

from acua_fact.server.models.pago import PagoBase


class PagoCreate(PagoBase):
    pass


class PagoRead(PagoBase):
    id: int


class PagoUpdate(SQLModel):
    id: int | None = None
    fecha: date | None = None
    valor: float | None = None
