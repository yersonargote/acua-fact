from sqlmodel import Field, Relationship, SQLModel


class PersonaBase(SQLModel):
    nombre: str = Field(index=True)
    direccion: str
    telefono: str
    estrato: int


class Persona(PersonaBase, table=True):
    id: int = Field(primary_key=True)
    facturas: list["Factura"] = Relationship(back_populates="persona")
