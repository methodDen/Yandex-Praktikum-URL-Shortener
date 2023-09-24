from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from src.db.db import get_session
from src.services.health_check import ping_database
from src.schemas.base import MessageResponse

router = APIRouter(tags=["Url Shortener"])


@router.post("/", response_model=None)
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
