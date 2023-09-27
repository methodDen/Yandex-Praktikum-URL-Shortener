import pytest
from httpx import AsyncClient
from fastapi import status


@pytest.mark.asyncio
async def test_ping_db(
    async_client: AsyncClient,
):
    response = await async_client.get("/api/v1/health-check/ping/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'message': 'Database is healthy'}


@pytest.mark.asyncio
async def test_create_short_url(
    async_client: AsyncClient,
):
    payload = {
        "original_url": "https://www.google.com/",
    }
    response = await async_client.post(
        "/api/v1/url/",
        json=payload,
    )
    assert response.status_code == status.HTTP_201_CREATED
    json = response.json()
    assert json['original_url'] == payload['original_url']


@pytest.mark.asyncio
async def test_create_short_url_batch(
    async_client: AsyncClient,
):
    payload = [
        {
            "original_url": "https://www.google.com/",
        },
        {
            "original_url": "https://www.ya.ru/",
        },
    ]
    response = await async_client.post(
        "/api/v1/url/batch/",
        json=payload,
    )
    assert response.status_code == status.HTTP_201_CREATED
    json = response.json()
    assert len(json) == len(payload)
    assert json[0]['original_url'] == payload[0]['original_url']
    assert json[1]['original_url'] == payload[1]['original_url']

