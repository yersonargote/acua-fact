from sqlmodel import SQLModel

from acua_fact.server.models.persona import PersonaBase


class PersonaCreate(PersonaBase):
    id: int


class PersonaRead(PersonaCreate):
    pass


class PersonaUpdate(SQLModel):
    id: int | None = None
    nombre: str | None = None
    direccion: str | None = None
    telefono: str | None = None
