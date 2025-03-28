from pydantic import BaseModel


class TronAddressRequest(BaseModel):
    address: str


class TronAddressResponse(BaseModel):
    bandwidth: int
    energy: int
    balance_trx: float
