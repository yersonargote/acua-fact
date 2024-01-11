from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlmodel import select

from acua_fact.server.db.session import get_session
from acua_fact.server.models.concepto import Concepto
from acua_fact.server.schemas.concepto import ConceptoRead

router = APIRouter(
    prefix="/conceptos",
    tags=["conceptos"],
)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
)
async def all_conceptos(
    *,
    session: AsyncSession = Depends(get_session),
) -> list[ConceptoRead]:
    """
    Retrieve all conceptos from the database.

    Parameters:
    - session: The database session to use (default: get_session())

    Returns:
    - A list of ConceptoRead objects representing the conceptos retrieved from the database.
    """
    result = await session.execute(select(Concepto))
    db_conceptos = result.scalars().all()
    return db_conceptos
