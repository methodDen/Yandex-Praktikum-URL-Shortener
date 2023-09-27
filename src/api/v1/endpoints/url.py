from typing import List, Optional, Annotated

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
    status,
)
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request
from starlette.responses import Response

from src.crud.url import url
from src.crud.visit import visit

from src.db.db import get_session
from src.schemas.url import (
    UrlRequestCreateSchema,
    UrlResponseSchema,
    UrlFullStatsResponseSchema,
    UrlStatsResponseSchema,
)
from src.schemas.visit import (
    VisitDBSchema,
    VisitNestedSchema,
)

router = APIRouter(tags=["Url Shortener"])


@router.post("/", response_model=UrlResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_short_url(
    *,
    db: AsyncSession = Depends(get_session),
    url_in: UrlRequestCreateSchema,
):
    return await url.create(db, obj_in=url_in)


@router.post('/batch/', response_model=List[UrlResponseSchema], status_code=status.HTTP_201_CREATED)
async def create_short_url_batch(
    *,
    db: AsyncSession = Depends(get_session),
    url_list_in: List[UrlRequestCreateSchema],
):
    return await url.create_multi(db, obj_in=url_list_in)


@router.get('/{short_url_id}/', status_code=status.HTTP_307_TEMPORARY_REDIRECT)
async def redirect_by_short_url(
    *,
    db: AsyncSession = Depends(get_session),
    request: Request,
    short_url_id: int,
):
    result = await url.get(db, short_url_id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='URL not found')

    await visit.create(
        db=db,
        obj_in=VisitDBSchema(
            url_id=result.id,
            user_ip=str(request.client.host)
        )
    )

    return Response(status_code=status.HTTP_307_TEMPORARY_REDIRECT, headers={'Location': result.original_url})


@router.get(
    '/{short_url_id}/status/',
    response_model=UrlFullStatsResponseSchema | UrlStatsResponseSchema,
    response_model_exclude_none=True,
    status_code=status.HTTP_200_OK
)
async def get_short_url_status(
    *,
    db: AsyncSession = Depends(get_session),
    short_url_id: int,
    full_info: Optional[bool] = Query(default=False),
    max_results: Annotated[int, Query(description="Pagination page size", ge=1)] = 10,
    offset: Annotated[int, Query(description="Pagination page offset", ge=0)] = 0,
):
    result = await url.get(db, short_url_id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='URL not found')
    visits_count = await url.get_visits_count(db, short_url_id)
    if full_info:
        visit_history = await visit.get_visits_by_url_id(db, short_url_id, skip=offset, limit=max_results)
        return UrlFullStatsResponseSchema(
            original_url=result.original_url,
            short_url=result.short_url,
            visits_count=visits_count,
            visits=[VisitNestedSchema(**vis.__dict__) for vis in visit_history]
        )

    return UrlStatsResponseSchema(
        original_url=result.original_url,
        short_url=result.short_url,
        visits_count=visits_count,
    )


