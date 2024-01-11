import gradio as gr

from acua_fact.server.schemas.concepto import ConceptoRead
from acua_fact.server.schemas.persona import PersonaRead
from acua_fact.ui.services.concepto import get_all_conceptos
from acua_fact.ui.services.persona import get_all_personas


def get_personas(personas, nombres):
    if not personas and not nombres:
        personas: list[PersonaRead] = get_all_personas()
        nombres: list[str] = [persona.nombre for persona in personas]
    return gr.update(choices=nombres), personas, nombres


def get_persona(persona, personas):
    for i in personas:
        if i.nombre == persona:
            return i.id, i.nombre, i.direccion, i.telefono, i.estrato
    return "", "", "", "", ""


def get_conceptos(conceptos, c_nombres):
    if not conceptos and not c_nombres:
        conceptos: list[ConceptoRead] = get_all_conceptos()
        c_nombres: list[str] = [concepto.nombre for concepto in conceptos]
    return gr.update(choices=c_nombres), conceptos, c_nombres


def get_consumo(concepto, conceptos):
    if concepto:
        return f"{concepto}"
    return ""


def factura_tab() -> gr.Tab:
    personas = gr.State([])
    p_nombres = gr.State([])
    conceptos = gr.State([])
    c_nombres = gr.State([])
    with gr.Tab("Gestión Facturas") as tab:
        with gr.Row():
            with gr.Column():
                gr.Markdown(value="## Buscar Persona", show_label=False)
                personas_drop = gr.Dropdown(
                    show_label=False,
                    label="",
                    choices=[],
                    interactive=True,
                )
                id_l = gr.Label(label="Identificación", value="", scale=0)
                nombre_l = gr.Label(label="Nombre", value="")
                direccion_l = gr.Label(label="Dirección", value="")
                telefono_l = gr.Label(label="Teléfono", value="")
                estrato_l = gr.Label(label="Estrato", value="")

            with gr.Column():
                with gr.Row():
                    with gr.Column():
                        gr.Markdown(value="## Detalles Factura", show_label=False)
                        periodo_inicio = gr.Textbox(
                            placeholder="10/01/2021",
                            label="Fecha Inicio",
                        )
                        periodo_fin = gr.Textbox(
                            placeholder="10/02/2021",
                            label="Fecha Fin",
                        )
                        limite_pago = gr.Label(
                            value="10/03/2021", label="Fecha Límite Pago"
                        )
                with gr.Row():
                    with gr.Column():
                        conceptos_drop = gr.Dropdown(
                            label="Consumo",
                            choices=[],
                            multiselect=True,
                            interactive=True,
                        )
                        concepto_l = gr.Label(
                            value="",
                            label="Total",
                        )
                        gr.Button(value="Calcular")

        personas_drop.focus(
            fn=get_personas,
            inputs=[personas],
            outputs=[personas_drop, personas, p_nombres],
        )

        personas_drop.change(
            fn=get_persona,
            inputs=[personas_drop, personas],
            outputs=[id_l, nombre_l, direccion_l, telefono_l, estrato_l],
        )

        conceptos_drop.focus(
            fn=get_conceptos,
            inputs=[conceptos],
            outputs=[conceptos_drop, conceptos, c_nombres],
        )

        conceptos_drop.change(
            fn=get_consumo,
            inputs=[conceptos_drop, conceptos],
            outputs=[concepto_l],
        )

        gr.ClearButton([personas_drop, conceptos_drop])

    return tab
