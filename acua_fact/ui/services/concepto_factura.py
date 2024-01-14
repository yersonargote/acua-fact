import requests

from acua_fact.server.schemas.concepto_factura import ConceptoFacturaCreate

URL: str = "http://localhost:8000/conceptos_factura"


def create_conceptos_factura(id_factura: int, ids: list[str]) -> bool:
    url = f"{URL}/"
    for id in ids:
        concepto = ConceptoFacturaCreate(factura_id=id_factura, concepto_id=id)
        response = requests.post(url, json=concepto.model_dump())
        if response.status_code != 201:
            return False
    return True
