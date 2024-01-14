from pydantic import BaseModel

from acua_fact.server.models.concepto_factura import ConceptoFacturaBase


class ConceptoFacturaCreate(ConceptoFacturaBase):
    concepto_id: int
    factura_id: int


class ConceptoFacturaRead(ConceptoFacturaCreate):
    id: int


class ConceptoFacturaUpdate(BaseModel):
    id: int | None = None
    factura_id: int | None = None
    concepto_id: int | None = None
