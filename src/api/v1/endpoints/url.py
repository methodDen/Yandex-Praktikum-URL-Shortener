from typing import List

from fastapi import (
    APIRouter,
    Depends,
    status,
)
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request

from src.db.db import get_session
from src.schemas.url import UrlRequestCreateSchema, UrlResponseSchema
from src.crud.url import url


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


@router.get('/{short_url_id}', status_code=status.HTTP_307_TEMPORARY_REDIRECT)
async def redirect_by_short_url(
    short_url: str,
    request: Request,
    short_url_id: int,
):
    pass
