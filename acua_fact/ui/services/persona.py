import json

import requests

# TODO: Implementar la función de eliminar persona.


def create_persona(id: int, nombre: str, direccion: str, telefono: str) -> str:
    url = "http://localhost:8000/personas/"
    payload = {
        "id": id,
        "nombre": nombre,
        "direccion": direccion,
        "telefono": telefono,
    }
    response = requests.post(url, json=payload)
    if response.text == "true":
        return "Persona creada"
    return "No se pudo crear la persona"


def get_persona(id: int) -> set:
    url = f"http://localhost:8000/personas/{id}"
    response = requests.get(url)
    persona = json.loads(response.text)
    nombre, direccion, telefono, id = persona.values()
    return id, nombre, direccion, telefono


def update_persona(id: int, nombre: str, direccion: str, telefono: str) -> str:
    url = f"http://localhost:8000/personas/{id}"
    payload = {
        "nombre": nombre,
        "direccion": direccion,
        "telefono": telefono,
    }
    response = requests.patch(url, json=payload)
    if response.text == "true":
        return "Persona actualizada"
    return "No se pudo actualizar la persona"
