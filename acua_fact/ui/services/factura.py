from datetime import date

import requests

from acua_fact.server.schemas.factura import FacturaCreate

URL: str = "http://localhost:8000/facturas"


def create_factura(
    fecha_inicio: date,
    fecha_fin: date,
    fecha_limite_pago: date,
    total: float,
    persona_id: int,
) -> int:
    url = f"{URL}/"
    factura = FacturaCreate(
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin,
        fecha_limite_pago=fecha_limite_pago,
        total=total,
        persona_id=persona_id,
    )
    print(factura.model_dump_json())
    response = requests.post(url, data=factura.model_dump_json())
    if response.status_code == 201:
        return response.json()["id"]

    return -1
