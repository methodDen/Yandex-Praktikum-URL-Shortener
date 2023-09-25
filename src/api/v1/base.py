from fastapi import APIRouter

from src.api.v1.endpoints import (
    health_check,
    url,
)

base_router = APIRouter()

base_router.include_router(health_check.router, prefix="/health-check")
base_router.include_router(url.router, prefix="/url")
