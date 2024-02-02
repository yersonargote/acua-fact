# Si desea utilizar PostgreSQL como base de datos, siga los siguientes pasos:

## Instalación

```bash
poetry add asyncpg
```

## Configuración

```python
from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql://user:xxxxxxxx@xxxxxxxxxxxxxxxx"
# o usar el archivo .env.backend
```

## Ejecución

1. **Correr PostgreSQL**

Correr el contenedor de docker de **PostgreSQL**.

```bash
docker-compose up -d
# o
make dup
```

2. **Correr el servidor de FastAPIy Gradio**

```bash
poetry run uvicorn acua_fact.main:app --reload
# o
make run
```

Abre [**http://localhost:8000/**](http://localhost:8000/) para ver la aplicaión gradio en el **navegador**.

3. **Parar el servidor de FastAPI y Gradio**

Haz `Ctrl + C` para parar el servidor de **FastAPI** y **Gradio**.


4. **Parar PostgreSQL**

```bash
docker-compose down
# o
make down
```