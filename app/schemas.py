from datetime import datetime

from pydantic import BaseModel


class TronAddressRequest(BaseModel):
    address: str


class TronAddressResponse(BaseModel):
    bandwidth: int
    energy: int
    balance_trx: float


class TronAddressInfo(TronAddressRequest, TronAddressResponse):
    pass


class TronResourceInfoRaw(BaseModel):
    freeNetLimit: int = 0
    freeNetUsed: int = 0
    EnergyLimit: int = 0
    EnergyUsed: int = 0


class RequestsList(BaseModel):
    id: int
    tron_address: str
    request_time: datetime

    class Config:
        orm_mode = True
