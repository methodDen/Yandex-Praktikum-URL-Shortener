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

router = APIRouter(tags=["Health Check"])


@router.get("/ping/", response_model=MessageResponse)
async def check_database_health(
    *,
    db: AsyncSession = Depends(get_session),
):
    is_database_healthy = await ping_database(db=db)
    if not is_database_healthy:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Database is not healthy",
        )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Database is healthy"},
    )
