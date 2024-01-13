from datetime import datetime

import gradio as gr

from acua_fact.server.schemas.concepto import ConceptoRead
from acua_fact.server.schemas.persona import PersonaRead
from acua_fact.ui.services.concepto import get_all_conceptos
from acua_fact.ui.services.persona import get_all_personas

HEADERS_FACTURA = [
    "Identificación",
    "Nombre",
    "Dirección",
    "Teléfono",
    "Estrato",
    "Fecha Inicio",
    "Fecha Fin",
    "Fecha Límite Pago",
    "Total",
]


def get_personas(personas, nombres):
    if not personas and not nombres:
        personas: list[PersonaRead] = get_all_personas()
        nombres: list[str] = [persona.nombre for persona in personas]
    return gr.update(choices=nombres), personas, nombres


def get_persona(persona, personas):
    for p in personas:
        if p.nombre == persona:
            return p.id, p.nombre, p.direccion, p.telefono, p.estrato
    return "", "", "", "", ""


def get_conceptos(conceptos, c_nombres):
    if not conceptos and not c_nombres:
        conceptos: list[ConceptoRead] = get_all_conceptos()
        c_nombres: list[str] = [concepto.nombre for concepto in conceptos]
    return gr.update(choices=c_nombres), conceptos, c_nombres


def get_consumo(concepto, conceptos):
    total: float = 0
    for nombre in concepto:
        for c in conceptos:
            if c.nombre == nombre:
                total += c.valor
    return total


def generar_factura(
    id_l,
    nombre_l,
    direccion_l,
    telefono_l,
    estrato_l,
    periodo_inicio,
    periodo_fin,
    limite_pago,
    total,
    conceptos,
    conceptos_drop,
):
    data_f = [
        [
            id_l,
            nombre_l,
            direccion_l,
            telefono_l,
            estrato_l,
            periodo_inicio,
            periodo_fin,
            limite_pago,
            total,
        ]
    ]
    data_c = []

    for nombre in conceptos_drop:
        for c in conceptos:
            if c.nombre == nombre:
                data_c.append([c.nombre, c.valor])
    return gr.update(value=data_f), gr.update(value=data_c)


def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, "%d/%m/%Y")
        return gr.update(value="Formato de fecha válido")
    except ValueError:
        return gr.update(value="Formato de fecha inválido")


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
                        limite_pago = gr.Textbox(
                            placeholder="10/03/2021",
                            label="Fecha Límite Pago",
                        )
                        validar_l = gr.Label(
                            value="",
                            label="",
                            show_label=False,
                        )

                    periodo_inicio.input(
                        fn=validar_fecha,
                        inputs=[periodo_inicio],
                        outputs=[validar_l],
                    )
                    periodo_fin.input(
                        fn=validar_fecha,
                        inputs=[periodo_fin],
                        outputs=[validar_l],
                    )
                    limite_pago.input(
                        fn=validar_fecha,
                        inputs=[limite_pago],
                        outputs=[validar_l],
                    )

                with gr.Row():
                    with gr.Column():
                        conceptos_drop = gr.Dropdown(
                            label="Consumo",
                            choices=[],
                            multiselect=True,
                        )
                        total = gr.Label(
                            value="",
                            label="Total",
                        )
        with gr.Row():
            generar = gr.Button(value="Generar Factura", variant="primary")
            gr.ClearButton(value="Limpiar", components=[personas_drop, conceptos_drop])

        with gr.Row():
            with gr.Column():
                gr.Markdown(
                    value="## Factura",
                    show_label=False,
                )
                factura = gr.DataFrame(headers=HEADERS_FACTURA)
        with gr.Row():
            with gr.Column():
                gr.Markdown(
                    value="## Conceptos Factura",
                    show_label=False,
                )
                factura_consumos = gr.DataFrame(
                    headers=[
                        "Concepto",
                        "Valor",
                    ]
                )

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
            outputs=[total],
        )

        generar.click(
            generar_factura,
            inputs=[
                id_l,
                nombre_l,
                direccion_l,
                telefono_l,
                estrato_l,
                periodo_inicio,
                periodo_fin,
                limite_pago,
                total,
                conceptos,
                conceptos_drop,
            ],
            outputs=[factura, factura_consumos],
        )

    return tab
