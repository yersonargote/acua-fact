from uuid import UUID

from pydantic import BaseModel

from acua_fact.server.schemas.persona import PersonaRead


class FacturaBase(BaseModel):
    fecha: str
    total: float
    persona_id: str


class FacturaCreate(FacturaBase):
    pass


class FacturaUpdate(FacturaBase):
    id: UUID


class FacturaRead(FacturaBase):
    id: UUID

    class Config:
        orm_mode = True


class FacturaReadWithPersona(FacturaBase):
    id: UUID
    persona: PersonaRead

    class Config:
        orm_mode = True
