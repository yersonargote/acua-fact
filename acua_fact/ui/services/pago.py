from datetime import date

import requests

from acua_fact.server.schemas.pago import PagoCreate, PagoRead

URL: str = "http://localhost:8000/pagos"


def create_pago(
    id_factura: int,
    valor: int,
    fecha: date,
) -> int:
    url = f"{URL}/"
    pago = PagoCreate(
        id_factura=id_factura,
        valor=valor,
        fecha=fecha,
    )
    response = requests.post(url, data=pago.model_dump_json())
    return response.status_code == 201


def get_pagos(id_factura: int) -> list[PagoRead]:
    url = f"{URL}/factura/{id_factura}"
    response = requests.get(url)
    if response.status_code == 200:
        pagos = response.json()
        pagos = [PagoRead.model_validate(pago) for pago in pagos]
        print(pagos)
        return pagos
    return []
