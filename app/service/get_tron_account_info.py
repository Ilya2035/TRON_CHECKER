from app.clients.tron_client import get_tron_client
from app.schemas import (
    TronAddressInfo,
    TronResourceInfoRaw
)


async def get_tron_account_info(address: str) -> TronAddressInfo:
    async with get_tron_client() as client:
        raw_balance = await client.get_account_balance(address)
        raw_resources = await client.get_account_resource(address)

        validated_resources = TronResourceInfoRaw(**raw_resources)

        balance = float(raw_balance) / 1_000_000
        bandwidth = validated_resources.freeNetLimit - validated_resources.freeNetUsed
        energy = validated_resources.EnergyLimit - validated_resources.EnergyUsed

        return TronAddressInfo(
            address=address,
            bandwidth=bandwidth,
            energy=energy,
            balance_trx=balance
        )
