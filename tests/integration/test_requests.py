"""Tests for API endpoints related to Tron address requests."""

import pytest
from unittest.mock import AsyncMock, patch
from httpx import AsyncClient
from httpx._transports.asgi import ASGITransport

from app.main import app
from app.schemas import TronAddressInfo


@pytest.mark.asyncio
@patch("app.routers.requests_for_tron.get_tron_account_info", new_callable=AsyncMock)
async def test_create_tron_request(mock_get_info):
    """
    Test the POST /requests_for_tron/ endpoint.

    Verifies that a Tron address request is correctly handled and returns
    expected account data when get_tron_account_info is mocked.
    """
    mock_get_info.return_value = TronAddressInfo(
        address="TXYZopYRdj2D9XRtbG411XZZ3kM5VkAeBf",
        bandwidth=1000,
        energy=500,
        balance_trx=123.45
    )

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as ac:
        response = await ac.post("/requests_for_tron/", json={"address": "any_address"})
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["bandwidth"] == 1000
    assert response_data["energy"] == 500
    assert response_data["balance_trx"] == 123.45


@pytest.mark.asyncio
async def test_get_requests_list():
    """
    Test the GET /requests_for_tron/ endpoint.

    Verifies that a paginated list of Tron address requests is returned correctly.
    """
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as ac:
        response = await ac.get("/requests_for_tron/")

    assert response.status_code == 200
    assert "items" in response.json()
    assert isinstance(response.json()["items"], list)
