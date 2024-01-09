import json

import gradio as gr
import requests


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


def get_persona(id: int) -> dict:
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


def build_ui_blocks() -> gr.Blocks:
    with gr.Blocks(title="ACUA Fact") as blocks:
        gr.Markdown("## ACUA Fact")
        with gr.Tab("Gestión Personas"):
            with gr.Row():
                with gr.Column():
                    with gr.Row():
                        gr.Label(value="Buscar Persona")
                        id_s = gr.Number(label="Identificación")
                        search = gr.Button(value="Buscar")

            with gr.Row():
                with gr.Column():
                    gr.Label(value="Crear Persona")
                    id_c = gr.Textbox(label="Identificación")
                    nombre_c = gr.Textbox(label="Nombre Completo")
                    direccion_c = gr.Textbox(label="Dirección")
                    telefono_c = gr.Textbox(label="Teléfono")
                    result_c = gr.Label(label="Resultado")
                    crear = gr.Button(value="Crear")
                    actualizar = gr.Button(value="Actualizar")

        crear.click(
            create_persona,
            inputs=[id_c, nombre_c, direccion_c, telefono_c],
            outputs=[result_c],
        )
        actualizar.click(
            update_persona,
            inputs=[id_c, nombre_c, direccion_c, telefono_c],
            outputs=[result_c],
        )
        search.click(
            get_persona,
            inputs=[id_s],
            outputs=[id_c, nombre_c, direccion_c, telefono_c],
        )

    return blocks
