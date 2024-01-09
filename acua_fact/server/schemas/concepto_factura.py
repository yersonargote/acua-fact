from uuid import UUID

from pydantic import BaseModel


class ConceptoFacturaBase(BaseModel):
    valor: float
    factura_id: int
    concepto_id: int


class ConceptoFacturaCreate(ConceptoFacturaBase):
    pass


class ConceptoFacturaRead(ConceptoFacturaBase):
    id: UUID

    class Config:
        orm_mode = True


class ConceptoFacturaUpdate(ConceptoFacturaBase):
    pass
