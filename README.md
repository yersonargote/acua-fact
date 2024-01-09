## ACUA FACT

## Descripción

ACUA FACT es una aplicación web que permite a los usuarios realizar facturas de manera sencilla y rápida, además de poder llevar un control de las mismas.

## Instalación

```bash
poetry install
# o
make install
```

## Uso

Primero se debe asegurar que el contenedor de docker de **PostgreSQL** esté corriendo.

```bash
docker-compose up -d
```

Luego se debe correr el servidor de **FastAPI** y **Gradio**.

```bash
poetry run uvicorn acua_fact.main:app --reload
# o
make run
```

## APP

Abre [**http://localhost:8000/**](http://localhost:8000/) para ver la aplicaión gradio en el **navegador**.