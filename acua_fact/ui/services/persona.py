import requests

from acua_fact.server.schemas.persona import PersonaCreate, PersonaRead

# TODO: Implementar la función de eliminar persona.

URL: str = "http://localhost:8000/personas"


def create_persona(
    id: int,
    nombre: str,
    direccion: str,
    telefono: str,
    estrato: int,
) -> str:
    url = f"{URL}/"
    persona = PersonaCreate(
        id=id,
        nombre=nombre,
        direccion=direccion,
        telefono=telefono,
        estrato=estrato,
    )
    response = requests.post(url, json=persona.model_dump())
    if response.status_code == 201:
        return "Persona creada"
    return "No se pudo crear la persona"


def get_persona(id: int) -> tuple:
    url = f"{URL}/{id}"
    response = requests.get(url)
    if response.status_code == 200:
        persona = response.json()
        persona = PersonaRead.model_validate(persona)
        return (
            "Persona encontrada",
            persona.id,
            persona.nombre,
            persona.direccion,
            persona.telefono,
            persona.estrato,
        )
    return "Persona no encontrada", 0, "", "", "", 0


def update_persona(
    id: int,
    nombre: str,
    direccion: str,
    telefono: str,
    estrato: int,
) -> str:
    url = f"{URL}/{id}"
    persona = PersonaCreate(
        id=id,
        nombre=nombre,
        direccion=direccion,
        telefono=telefono,
        estrato=estrato,
    )
    persona = requests.patch(url, json=persona.model_dump())
    if persona.status_code == 200:
        return "Persona actualizada"
    return "No se pudo actualizar la persona"


def delete_persona(id: int) -> str:
    url = f"{URL}/{id}"
    persona = requests.delete(url)
    if persona.status_code == 200:
        return "Persona eliminada"
    return "No se pudo eliminar la persona"
