import asyncio
from typing import Generator, AsyncGenerator

import pytest_asyncio
from httpx import AsyncClient

from src.core.config import app_settings
from src.main import app


app_settings.database_dsn = f'{app_settings.database_dsn}_test'


@pytest_asyncio.fixture(scope="session")
def event_loop(request) -> Generator:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture
async def async_client():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as client:
        yield client