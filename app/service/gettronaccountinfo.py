from tronpy import AsyncTron


async def get_tron_account_info(address: str) -> dict:
    async with AsyncTron() as client:
        account = await client.get_account(address)
        resources = await client.get_account_resource(address)

        bandwidth = resources.get('freeNetLimit', 0) - resources.get('freeNetUsed', 0)
        energy = resources.get('EnergyLimit', 0) - resources.get('EnergyUsed', 0)
        balance = account.get('balance', 0) / 1_000_000

        return {
            "address": address,
            "bandwidth": bandwidth,
            "energy": energy,
            "balance_trx": balance
        }
