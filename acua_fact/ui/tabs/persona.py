import gradio as gr

from acua_fact.ui.services.persona import (
    create_persona,
    delete_persona,
    get_persona,
    update_persona,
)


def persona_tab():
    with gr.Tab("Gestión Personas") as tab:
        gr.Markdown(value="## Buscar Persona", show_label=False)
        with gr.Row():
            id_s = gr.Number(label="Identificación")
            search = gr.Button(value="Buscar")
            with gr.Accordion(label="Eliminar persona", open=False):
                delete = gr.Button(value="Eliminar", variant="stop")

        gr.Markdown(value="## Crear/Actualizar Persona")
        with gr.Row():
            with gr.Column():
                id_c = gr.Number(label="Identificación")
                nombre_c = gr.Textbox(
                    label="Nombre Completo",
                    placeholder="Hugo Perez",
                )
                direccion_c = gr.Textbox(
                    label="Dirección",
                    placeholder="Poblaseña",
                )
                telefono_c = gr.Textbox(
                    label="Teléfono",
                    placeholder="312-123-4567",
                )
                estrato_c = gr.Number(label="Estrato")
            with gr.Column():
                result_c = gr.Label(label="Resultado")
                crear = gr.Button(value="Crear")
                actualizar = gr.Button(value="Actualizar")

        crear.click(
            create_persona,
            inputs=[id_c, nombre_c, direccion_c, telefono_c, estrato_c],
            outputs=[result_c],
        )
        actualizar.click(
            update_persona,
            inputs=[id_c, nombre_c, direccion_c, telefono_c, estrato_c],
            outputs=[result_c],
        )
        search.click(
            get_persona,
            inputs=[id_s],
            outputs=[id_c, nombre_c, direccion_c, telefono_c, estrato_c],
            # outputs=[result_c],
        )
        delete.click(
            delete_persona,
            inputs=[id_s],
            outputs=[result_c],
        )

    return tab
