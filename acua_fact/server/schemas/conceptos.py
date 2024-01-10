from uuid import UUID

from sqlmodel import SQLModel

from acua_fact.server.models.concepto import ConceptoBase


class ConceptoCreate(ConceptoBase):
    id: UUID


class ConceptoRead(ConceptoBase):
    id: UUID


class ConceptoUpdate(SQLModel):
    id: UUID | None = None
    nombre: str | None = None
    valor: float | None = None
    subsidio: float | None = None
