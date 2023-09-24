from fastapi import APIRouter

from src.api.v1.endpoints import health_check

base_router = APIRouter()

base_router.include_router(health_check.router, prefix="/health-check")
