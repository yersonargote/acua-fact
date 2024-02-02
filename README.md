## ACUA FACT

## Descripción

**ACUA FACT** es una aplicación web que permite a los usuarios realizar facturas de manera sencilla y rápida, además de poder llevar un control de las mismas.

## Instalación

```bash
poetry install
# o
make install
```

## Uso

Correr el servidor de **FastAPI** y **Gradio**.

```bash
poetry run uvicorn acua_fact.main:app --reload
# o
make run
```