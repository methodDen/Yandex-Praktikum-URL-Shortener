import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from src.api.v1 import base
from src.core.config import app_settings
from src.middleware.blacklist import BlacklistMiddleware

app = FastAPI(
    title=app_settings.app_title,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
)

blacklist_middleware = BlacklistMiddleware(blacklist=app_settings.blacklist)

app.add_middleware(BaseHTTPMiddleware, dispatch=blacklist_middleware)
app.include_router(base.base_router, prefix="/api/v1")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=app_settings.project_host,
        port=app_settings.project_port,
        reload=True,
    )