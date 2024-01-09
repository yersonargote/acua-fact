from uuid import UUID

from sqlmodel import Field, Relationship, SQLModel


class ConceptoFacturaBase(SQLModel):
    pass


class ConceptoFactura(ConceptoFacturaBase, table=True):
    id: UUID = Field(primary_key=True)
    factura_id: UUID = Field(foreign_key="factura.id")
    factura: "Factura" = Relationship(back_populates="conceptos")
    concepto_id: UUID = Field(foreign_key="concepto.id")
    concepto: "Concepto" = Relationship(back_populates="facturas")
