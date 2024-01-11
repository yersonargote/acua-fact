from typing import Annotated

from fastapi import APIRouter, Body, Depends, Path, status
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlmodel import select

from acua_fact.server.db.session import get_session
from acua_fact.server.models.persona import Persona
from acua_fact.server.schemas.persona import PersonaCreate, PersonaRead, PersonaUpdate
from acua_fact.server.schemas.response import OK

router = APIRouter(
    prefix="/personas",
    tags=["personas"],
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
async def create_persona(
    *,
    session: AsyncSession = Depends(get_session),
    persona: Annotated[PersonaCreate, Body(title="Persona a crear")],
) -> PersonaRead:
    db_persona = Persona.model_validate(persona)
    session.add(db_persona)
    await session.commit()
    return db_persona


@router.get("/")
async def all_personas(
    *,
    session: AsyncSession = Depends(get_session),
) -> list[PersonaRead]:
    """
    Retrieve all personas from the database.

    Parameters:
    - session: The database session to use (default: get_session())

    Returns:
    - A list of PersonaRead objects representing the personas retrieved from the database.
    """
    result = await session.execute(select(Persona))
    db_personas = result.scalars().all()
    return db_personas


@router.get("/{id}")
async def read_persona(
    *,
    id: Annotated[int, Path(title="ID de la persona a leer")],
    session: AsyncSession = Depends(get_session),
) -> PersonaRead:
    db_persona = await session.get(Persona, id)
    if db_persona is None:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return db_persona


@router.patch("/{id}")
async def update_persona(
    *,
    id: Annotated[int, Path(title="ID de la persona a actualizar")],
    persona: Annotated[PersonaUpdate, Body(title="Persona a actualizar")],
    session: AsyncSession = Depends(get_session),
) -> PersonaRead:
    db_persona = await session.get(Persona, id)
    if db_persona is None:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    persona_data = persona.model_dump(exclude_unset=True)
    for key, value in persona_data.items():
        setattr(db_persona, key, value)
    await session.commit()
    await session.refresh(db_persona)
    return db_persona


@router.delete("/{id}")
async def delete_persona(
    *,
    id: Annotated[int, Path(title="ID de la persona a eliminar")],
    session: AsyncSession = Depends(get_session),
) -> OK:
    db_persona = await session.get(Persona, id)
    if db_persona is None:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    await session.delete(db_persona)
    await session.commit()
    return OK(ok=True)
