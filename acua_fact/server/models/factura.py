from datetime import date

from sqlmodel import Field, Relationship, SQLModel

from acua_fact.server.models.concepto_factura import ConceptoFactura


class FacturaBase(SQLModel):
    fecha_inicio: date
    fecha_fin: date
    fecha_limite_pago: date
    total: float


class Factura(FacturaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    persona_id: int = Field(foreign_key="persona.id")
    persona: "Persona" = Relationship(back_populates="facturas")
    pagos: list["Pago"] = Relationship(back_populates="factura")
    conceptos: list["Concepto"] = Relationship(
        back_populates="facturas",
        link_model=ConceptoFactura,
    )
