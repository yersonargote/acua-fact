from typing import Annotated

from fastapi import APIRouter, Body, Depends, Path
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio.session import AsyncSession

from acua_fact.server.db.session import get_session
from acua_fact.server.models.persona import Persona
from acua_fact.server.schemas.persona import PersonaCreate, PersonaRead, PersonaUpdate

router = APIRouter(
    prefix="/personas",
    tags=["personas"],
)


@router.post("/")
async def check_problems(
    *,
    session: AsyncSession = Depends(get_session),
    persona: Annotated[PersonaCreate, Body(title="Persona a crear")],
) -> bool:
    db_persona = Persona.model_validate(persona)
    session.add(db_persona)
    try:
        await session.commit()
        await session.refresh(db_persona)
        return True
    except Exception:
        return False


@router.get("/{id}")
async def read_persona(
    *,
    id: Annotated[int, Path(title="ID de la persona a leer")],
    session: AsyncSession = Depends(get_session),
) -> PersonaRead:
    db_persona = await session.get(Persona, id)
    if not db_persona:
        return HTTPException(status_code=404, detail="Persona no encontrada")
    return db_persona


@router.patch("/{id}")
async def update_persona(
    *,
    id: Annotated[int, Path(title="ID de la persona a actualizar")],
    persona: Annotated[PersonaUpdate, Body(title="Persona a actualizar")],
    session: AsyncSession = Depends(get_session),
) -> PersonaRead:
    db_persona = await session.get(Persona, id)
    if not db_persona:
        return HTTPException(status_code=404, detail="Persona no encontrada")
    persona_data = persona.model_dump(exclude_unset=True)
    for key, value in persona_data.items():
        setattr(db_persona, key, value)
    await session.commit()
    await session.refresh(db_persona)
    return db_persona
