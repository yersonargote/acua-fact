from sqlmodel import Field, SQLModel


class ConceptoFacturaBase(SQLModel):
    pass


class ConceptoFactura(ConceptoFacturaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    factura_id: int = Field(foreign_key="factura.id")
    concepto_id: int = Field(foreign_key="concepto.id")
