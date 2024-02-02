from datetime import datetime

import gradio as gr

from acua_fact.server.schemas.factura import FacturaRead
from acua_fact.server.schemas.pago import PagoRead
from acua_fact.ui.services.factura import get_factura
from acua_fact.ui.services.pago import create_pago, get_pagos

HEADERS_PAGOS = [
    "Numero de pago",
    "Valor",
    "Fecha",
]


def limpiar_components():
    return (
        gr.update(value=0),
        gr.update(value=0),
        gr.update(value="Esperando pago..."),
        gr.update(value=0),
        gr.update(),
        gr.update(value="Total"),
    )


def pagos_factura(id: int):
    factura = FacturaRead.model_validate(get_factura(id))
    total_fact = factura.total
    pagos: list[PagoRead] = get_pagos(id)
    pagos_df = []
    total = 0
    for pago in pagos:
        pagos_df.append(
            [
                pago.id,
                pago.valor,
                datetime.strftime(pago.fecha, "%Y-%m-%d"),
            ]
        )
        total += pago.valor
    return (
        gr.update(value=pagos_df),
        gr.update(value=total_fact),
        gr.update(value=total),
    )


def hacer_pago(id: int, valor: float):
    if valor < 0:
        return (
            gr.update(),
            gr.update(),
            gr.update(),
            gr.update(value="El valor no puede ser negativo"),
        )

    hoy = datetime.now().date()
    creado = create_pago(id, valor, hoy)
    if not creado:
        return (
            gr.update(),
            gr.update(),
            gr.update(),
            gr.update(value="No se pudo realizar el pago"),
        )
    pagos_df, total_fact, total = pagos_factura(id)
    return pagos_df, total_fact, total, gr.update(value="Pago realizado con éxito")


def pago_tab() -> gr.Tab:
    with gr.Tab("Gestión de Pagos") as tab:
        gr.Markdown(value="## Buscar Información de Pagos", show_label=False)
        with gr.Row():
            id = gr.Number(label="Ingrese el id de la factura")
            search = gr.Button(value="Buscar")
        with gr.Row():
            with gr.Column():
                gr.Markdown(value="## Factura")
                total_fact = gr.Label(label="Total")
                gr.Markdown(value="### Pagos realizados")
                pagos_df = gr.DataFrame(headers=HEADERS_PAGOS)
                total = gr.Label(label="Total pagado")

            with gr.Column():
                gr.Markdown(value="## Ralizar Pago")
                valor = gr.Number(
                    label="Valor a pagar",
                )
                pagar = gr.Button(value="Pagar")
                informacion = gr.Label(value="Esperando pago...", show_label=False)
                limpiar = gr.Button(
                    value="Limpiar",
                )

    search.click(
        pagos_factura,
        inputs=[id],
        outputs=[pagos_df, total_fact, total],
    )
    pagar.click(
        hacer_pago,
        inputs=[id, valor],
        outputs=[pagos_df, total_fact, total, informacion],
    )
    limpiar.click(
        limpiar_components,
        inputs=[],
        outputs=[id, valor, informacion, total, pagos_df, total_fact],
    )

    return tab
