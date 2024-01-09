from datetime import date
from uuid import UUID

from sqlmodel import Field, Relationship, SQLModel


class PagoBase(SQLModel):
    fecha: date
    total: float
    factura_id: UUID = Field(foreign_key="factura.id")


class Pago(PagoBase, table=True):
    id: UUID = Field(primary_key=True)
    factura: "Factura" = Relationship(back_populates="pagos")
