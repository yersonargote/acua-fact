from uuid import UUID

from sqlmodel import Field, SQLModel


class ConceptoFacturaBase(SQLModel):
    pass


class ConceptoFactura(ConceptoFacturaBase, table=True):
    id: UUID = Field(primary_key=True)
    factura_id: UUID = Field(foreign_key="factura.id")
    concepto_id: UUID = Field(foreign_key="concepto.id")
