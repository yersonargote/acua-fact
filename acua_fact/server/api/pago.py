from typing import Annotated

from fastapi import APIRouter, Body, Depends, Path, status
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlmodel import col, select

from acua_fact.server.db.session import get_session
from acua_fact.server.models.pago import Pago
from acua_fact.server.schemas.pago import PagoCreate, PagoRead

router = APIRouter(
    prefix="/pagos",
    tags=["pagos"],
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
async def create_pago(
    *,
    session: AsyncSession = Depends(get_session),
    pago: Annotated[PagoCreate, Body(title="Pago a crear")],
) -> PagoRead:
    db_pago = Pago.model_validate(pago)
    session.add(db_pago)
    await session.commit()
    await session.refresh(db_pago)
    return db_pago


@router.get("/factura/{id}")
async def get_pago_by_factura(
    *,
    id: Annotated[int, Path(title="ID de la factura")],
    session: AsyncSession = Depends(get_session),
) -> list[PagoRead]:
    result = await session.execute(select(Pago).where(col(Pago.id_factura) == id))
    db_pagos = result.scalars().all()
    return db_pagos
