import gradio as gr

from acua_fact.ui.services.persona import get_all_personas


def filter_personas():
    personas = get_all_personas()
    nombres = [persona.nombre for persona in personas]
    return gr.update(choices=nombres)


def get_persona(persona):
    return persona


def factura_tab() -> gr.Tab:
    with gr.Tab("Gestión Facturas") as tab:
        gr.Markdown(value="## Personas", show_label=False)
        personas_drop = gr.Dropdown(
            label="Personas",
            choices=[],
            interactive=True,
        )
        personas_drop.focus(
            fn=filter_personas,
            inputs=None,
            outputs=[personas_drop],
        )
        nombre_l = gr.Label(value="")

        personas_drop.change(
            fn=get_persona,
            inputs=[personas_drop],
            outputs=[nombre_l],
        )

        gr.ClearButton(personas_drop)

    return tab
