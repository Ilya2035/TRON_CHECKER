import asyncio
from tronpy import AsyncTron
from tronpy.providers.async_http import AsyncHTTPProvider

from app.settings import settings


async def get_tron_account_info(address: str) -> dict:
    async with AsyncTron(provider=AsyncHTTPProvider(api_key=settings.API_KEY)) as client:
        account_task = asyncio.create_task(client.get_account(address))
        resources_task = asyncio.create_task(client.get_account_resource(address))

        account = await account_task
        resources = await resources_task

        bandwidth = resources.get('freeNetLimit', 0) - resources.get('freeNetUsed', 0)
        energy = resources.get('EnergyLimit', 0) - resources.get('EnergyUsed', 0)

        balance = account.get('balance', 0) / 1_000_000

        return {
            "address": address,
            "bandwidth": bandwidth,
            "energy": energy,
            "balance_trx": balance
        }
