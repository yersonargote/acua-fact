from typing import Annotated

from fastapi import APIRouter, Body, Depends, status
from sqlalchemy.ext.asyncio.session import AsyncSession

from acua_fact.server.db.session import get_session
from acua_fact.server.models.concepto_factura import ConceptoFactura
from acua_fact.server.schemas.concepto_factura import (
    ConceptoFacturaCreate,
    ConceptoFacturaRead,
)

router = APIRouter(
    prefix="/conceptos_factura",
    tags=["conceptos_factura"],
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
async def create_concepto_factura(
    *,
    session: AsyncSession = Depends(get_session),
    concepto_factura: Annotated[
        ConceptoFacturaCreate, Body(title="ConceptoFactura a crear")
    ],
) -> ConceptoFacturaRead:
    db_concepto_factura = ConceptoFactura.model_validate(concepto_factura)
    session.add(db_concepto_factura)
    await session.commit()
    await session.refresh(db_concepto_factura)
    return db_concepto_factura
