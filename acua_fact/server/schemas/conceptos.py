from uuid import UUID

from pydantic import BaseModel


class ConceptoBase(BaseModel):
    nombre: str
    descripcion: str


class ConceptoCreate(ConceptoBase):
    pass


class ConceptoRead(ConceptoBase):
    id: UUID

    class Config:
        orm_mode = True
