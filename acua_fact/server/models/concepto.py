from sqlmodel import Field, Relationship, SQLModel

from acua_fact.server.models.concepto_factura import ConceptoFactura


class ConceptoBase(SQLModel):
    nombre: str = Field(unique=True, index=True)
    valor: float
    subsidio: float


class Concepto(ConceptoBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    facturas: list["Factura"] = Relationship(
        back_populates="conceptos",
        link_model=ConceptoFactura,
    )
