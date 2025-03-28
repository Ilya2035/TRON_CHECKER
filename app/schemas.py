from pydantic import BaseModel


class TronAddressRequest(BaseModel):
    address: str


class TronAddressResponse(BaseModel):
    bandwidth: int
    energy: int
    balance_trx: float


class Listofrequests(BaseModel):
    id: int
    tron_address: str
    request_time: str