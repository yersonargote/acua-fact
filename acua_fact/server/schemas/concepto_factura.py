from pydantic import BaseModel

from acua_fact.server.models.concepto_factura import ConceptoFacturaBase


class ConceptoFacturaCreate(ConceptoFacturaBase):
    id: int
    concepto_id: int
    factura_id: int


class ConceptoFacturaRead(ConceptoFacturaCreate):
    pass


class ConceptoFacturaUpdate(BaseModel):
    id: int | None = None
    factura_id: int | None = None
    concepto_id: int | None = None
