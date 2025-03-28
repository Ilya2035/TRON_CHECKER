from fastapi import HTTPException
from app.clients.tron_client import get_tron_client
from app.schemas import (
    TronAddressInfo,
    TronResourceInfoRaw
)
from app.config import SUN_IN_TRX


async def get_tron_account_info(address: str) -> TronAddressInfo:
    async with get_tron_client() as client:
        try:
            raw_balance = await client.get_account_balance(address)
            raw_resources = await client.get_account_resource(address)
        except Exception as e:
            raise HTTPException(
                status_code=404,
                detail=f"Tron account '{address}' not found or invalid: {str(e)}"
            )

        try:
            validated_resources = TronResourceInfoRaw(**raw_resources)
        except Exception as e:
            raise HTTPException(
                status_code=422,
                detail=f"Failed to parse resource info for address '{address}': {str(e)}"
            )

        balance = float(raw_balance) / SUN_IN_TRX
        bandwidth = validated_resources.freeNetLimit - validated_resources.freeNetUsed
        energy = validated_resources.EnergyLimit - validated_resources.EnergyUsed

        return TronAddressInfo(
            address=address,
            bandwidth=bandwidth,
            energy=energy,
            balance_trx=balance
        )
