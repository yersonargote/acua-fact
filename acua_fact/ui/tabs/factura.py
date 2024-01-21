from datetime import date

import gradio as gr
from gradio_calendar import Calendar

from acua_fact.ui.services.concepto import get_all_conceptos
from acua_fact.ui.services.concepto_factura import create_conceptos_factura
from acua_fact.ui.services.factura import create_factura
from acua_fact.ui.services.pdf import generar_pdf
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
    personas_response = get_all_personas()
    if len(personas_response) != len(personas):
        personas = personas_response
        nombres = [persona.nombre for persona in personas]
        return gr.update(choices=nombres), personas, nombres
    return gr.update(), personas, nombres


def get_persona(persona, personas):
    for p in personas:
        if p.nombre == persona:
            return p.id, p.nombre, p.direccion, p.telefono, p.estrato
    return "", "", "", "", ""


def get_conceptos(conceptos, c_nombres):
    if not conceptos and not c_nombres:
        conceptos = get_all_conceptos()
        c_nombres = [concepto.nombre for concepto in conceptos]
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
    fecha_inicio = periodo_inicio.date()
    fecha_fin = periodo_fin.date()
    fecha_limite_pago = limite_pago.date()

    id_factura = create_factura(
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin,
        fecha_limite_pago=fecha_limite_pago,
        total=total,
        persona_id=id_l,
    )
    if id_factura == -1:
        return gr.update(), gr.update(), gr.update(), gr.update()
    ids_conceptos = [c.id for c in conceptos]
    created = create_conceptos_factura(id_factura, ids_conceptos)
    if not created:
        return gr.update(), gr.update(), gr.update(), gr.update()

    data_f = [
        [
            id_l,
            nombre_l,
            direccion_l,
            telefono_l,
            estrato_l,
            fecha_inicio,
            fecha_fin,
            fecha_limite_pago,
            total,
        ]
    ]
    data_c = []

    for nombre in conceptos_drop:
        for c in conceptos:
            if c.nombre == nombre:
                data_c.append([c.nombre, c.valor])

    factura_titulo = f"Factura {id_factura}"
    generar_pdf(
        title=factura_titulo,
        persona_id=id_l,
        nombre=nombre_l,
        direccion=direccion_l,
        telefono=telefono_l,
        estrato=estrato_l,
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin,
        fecha_limite_pago=fecha_limite_pago,
        factura_id=id_factura,
        conceptos=conceptos,
        total=total,
    )

    return (
        gr.update(value=data_f),
        gr.update(value=data_c),
        gr.update(value=factura_titulo),
        gr.update(value=f"Conceptos de la factura {id_factura}"),
    )


def validar_fechas(inicio: date, fin: date, limite: date):
    if inicio > fin:
        return "La fecha de inicio no puede ser mayor a la fecha fin"
    if inicio > limite:
        return "La fecha de inicio no puede ser mayor a la fecha límite de pago"
    if fin > limite:
        return "La fecha fin no puede ser mayor a la fecha límite de pago"
    return "Las fechas son válidas"


def factura_tab() -> gr.Tab:
    personas = gr.State([])
    p_nombres = gr.State([])
    conceptos = gr.State([])
    c_nombres = gr.State([])
    with gr.Tab("Gestión Facturas") as tab:
        with gr.Row(equal_height=True):
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
                        periodo_inicio = Calendar(
                            label="Fecha Inicio",
                            type="date",
                        )

                        periodo_fin = Calendar(
                            label="Fecha Fin",
                            type="date",
                        )
                        limite_pago = Calendar(
                            label="Fecha Límite Pago",
                            type="date",
                        )
                        validar_l = gr.Label(
                            value="",
                            label="",
                            show_label=False,
                        )
                    periodo_inicio.change(
                        fn=validar_fechas,
                        inputs=[periodo_inicio, periodo_fin, limite_pago],
                        outputs=[validar_l],
                    )
                    periodo_fin.change(
                        fn=validar_fechas,
                        inputs=[periodo_inicio, periodo_fin, limite_pago],
                        outputs=[validar_l],
                    )
                    limite_pago.change(
                        fn=validar_fechas,
                        inputs=[periodo_inicio, periodo_fin, limite_pago],
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
            gr.ClearButton(
                value="Limpiar",
                components=[
                    personas_drop,
                    periodo_inicio,
                    periodo_fin,
                    limite_pago,
                    validar_l,
                ],
            )

        with gr.Row():
            with gr.Column():
                factura_titulo = gr.Label(
                    value="Factura",
                    show_label=False,
                )
                factura_df = gr.DataFrame(headers=HEADERS_FACTURA)
        with gr.Row():
            with gr.Column():
                conceptos_factura_titulo = gr.Label(
                    value="Conceptos Factura",
                    show_label=False,
                )
                factura_consumos_df = gr.DataFrame(
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
            outputs=[
                factura_df,
                factura_consumos_df,
                factura_titulo,
                conceptos_factura_titulo,
            ],
        )

    return tab
