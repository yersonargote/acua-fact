from datetime import date
from uuid import UUID

from pydantic import BaseModel


class PagoBase(BaseModel):
    fecha: date
    total: float


class PagoCreate(PagoBase):
    pass


class PagoRead(PagoBase):
    id: UUID

    class Config:
        orm_mode = True
