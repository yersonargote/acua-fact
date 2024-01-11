from sqlmodel import SQLModel

from acua_fact.server.models.concepto import ConceptoBase


class ConceptoCreate(ConceptoBase):
    id: int


class ConceptoRead(ConceptoBase):
    id: int


class ConceptoUpdate(SQLModel):
    id: int | None = None
    nombre: str | None = None
    valor: float | None = None
    subsidio: float | None = None
