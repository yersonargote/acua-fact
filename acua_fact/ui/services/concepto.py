import requests

from acua_fact.server.schemas.concepto import ConceptoRead

URL: str = "http://localhost:8000/conceptos"


def get_all_conceptos() -> list[ConceptoRead]:
    url = f"{URL}/"
    response = requests.get(url)
    if response.status_code == 200:
        conceptos = response.json()
        conceptos = [ConceptoRead.model_validate(concepto) for concepto in conceptos]
        return conceptos
    return []
