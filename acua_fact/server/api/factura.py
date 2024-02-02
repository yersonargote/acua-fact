from typing import Annotated

from fastapi import APIRouter, Body, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio.session import AsyncSession

from acua_fact.server.db.session import get_session
from acua_fact.server.models.factura import Factura
from acua_fact.server.schemas.factura import FacturaCreate, FacturaRead

router = APIRouter(
    prefix="/facturas",
    tags=["facturas"],
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
async def create_factura(
    *,
    session: AsyncSession = Depends(get_session),
    factura: Annotated[FacturaCreate, Body(title="Factura a crear")],
) -> FacturaRead:
    db_factura = Factura.model_validate(factura)
    session.add(db_factura)
    await session.commit()
    await session.refresh(db_factura)
    return db_factura


@router.get(
    "/{id}",
    response_model=FacturaRead,
)
async def get_factura(
    id: int,
    session: AsyncSession = Depends(get_session),
) -> FacturaRead:
    db_factura = await session.get(Factura, id)
    if db_factura is None:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    return db_factura
