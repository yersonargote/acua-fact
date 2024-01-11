from datetime import date

from sqlmodel import SQLModel

from acua_fact.server.models.factura import FacturaBase


class FacturaCreate(FacturaBase):
    id: int
    persona_id: int


class FacturaRead(FacturaCreate):
    pass


class FacturaUpdate(SQLModel):
    id: int | None = None
    fecha_inicio: date | None = None
    fecha_fin: date | None = None
    fecha_limite_pago: date | None = None
    total: float | None = None
