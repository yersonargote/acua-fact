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

> [!WARNING]: Si desea usar **PostgreSQL** debe cambiar la `DATABASE_URL` en el archivo `.env`, ver el archivo `.env.example` para más información.

Correr el contenedor de docker de **PostgreSQL** esté corriendo.

```bash
docker-compose up -d
# o
make dup
```

## APP

Abre [**http://localhost:8000/**](http://localhost:8000/) para ver la aplicaión gradio en el **navegador**.

## STOP

Haz **Ctrl + C** para parar el servidor de **FastAPI** y **Gradio**.

> [!NOTE]
Para parar **PostgreSQL**.

```bash
docker-compose down
# o
make down
```
