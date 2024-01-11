from datetime import date

from sqlmodel import Field, Relationship, SQLModel


class PagoBase(SQLModel):
    fecha: date
    total: float
    factura_id: int = Field(foreign_key="factura.id")


class Pago(PagoBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    factura: "Factura" = Relationship(back_populates="pagos")
