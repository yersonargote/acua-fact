from sqlmodel import Field, SQLModel  # , Relationship


class PersonaBase(SQLModel):
    nombre: str
    direccion: str
    telefono: str


class Persona(PersonaBase, table=True):
    id: int = Field(primary_key=True)
    # facturas: list["Factura"] = Relationship(back_populates="persona")
