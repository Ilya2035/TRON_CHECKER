from pydantic import BaseModel


class TronAddressRequest(BaseModel):
    address: str

class TronAddressResponse(TronAddressRequest):
    bandwidth: int
    energy: int
    balance_trx: float
