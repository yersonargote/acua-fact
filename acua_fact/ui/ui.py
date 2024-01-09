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
    return "Error al crear persona"


def get_persona(id: int) -> dict:
    url = f"http://localhost:8000/personas/{id}"
    response = requests.get(url)
    yield response.json()


def build_ui_blocks() -> gr.Blocks:
    with gr.Blocks(title="ACUA Fact") as blocks:
        gr.Markdown("## ACUA Fact")
        with gr.Tab("Gestión Personas"):
            with gr.Row():
                with gr.Column():
                    id_s = gr.Number(label="Identificación")
                    result_s = gr.JSON(label="Persona")
                    search = gr.Button(value="Buscar")
                    search.click(
                        get_persona,
                        inputs=[id_s],
                        outputs=[result_s],
                    )
                with gr.Column():
                    id_c = gr.Textbox(label="Identificación")
                    nombre_c = gr.Textbox(label="Nombre Completo")
                    direccion_c = gr.Textbox(label="Dirección")
                    telefono_c = gr.Textbox(label="Teléfono")
                    result_c = gr.Label(label="Resultado")
                    crear = gr.Button(value="Crear")
                    crear.click(
                        create_persona,
                        inputs=[id_c, nombre_c, direccion_c, telefono_c],
                        outputs=[result_c],
                    )

    return blocks
