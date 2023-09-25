from fastapi import (
    APIRouter,
    Depends,
    status,
)
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.db import get_session

router = APIRouter(tags=["Url Shortener"])


@router.post("/", response_model=None, status_code=status.HTTP_201_CREATED)
async def create_short_url(
    *,
    db: AsyncSession = Depends(get_session),
    url_in: None,
):
    pass


@router.post('/batch/', response_model=None)
async def create_short_url_batch(
    *,
    db: AsyncSession = Depends(get_session),
    url_list_in: None,
):
    pass
