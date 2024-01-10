from uuid import UUID

from pydantic import BaseModel

from acua_fact.server.models.concepto_factura import ConceptoFacturaBase


class ConceptoFacturaCreate(ConceptoFacturaBase):
    id: UUID
    concepto_id: UUID
    factura_id: UUID


class ConceptoFacturaRead(ConceptoFacturaCreate):
    pass


class ConceptoFacturaUpdate(BaseModel):
    id: UUID | None = None
    factura_id: UUID | None = None
    concepto_id: UUID | None = None
