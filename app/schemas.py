"""Pydantic schemas for data validation and serialization."""

from datetime import datetime
from pydantic import BaseModel


class TronAddressRequest(BaseModel):
    """Request schema containing a Tron address."""
    address: str


class TronAddressResponse(BaseModel):
    """Response schema with Tron account data."""
    bandwidth: int
    energy: int
    balance_trx: float


class TronAddressInfo(TronAddressRequest, TronAddressResponse):
    """Combined schema with both address and account data."""
    pass


class TronResourceInfoRaw(BaseModel):
    """Raw resource data from the Tron API (before transformation)."""
    freeNetLimit: int = 0
    freeNetUsed: int = 0
    EnergyLimit: int = 0
    EnergyUsed: int = 0


class RequestsList(BaseModel):
    """Schema for displaying a list of stored requests."""
    id: int
    tron_address: str
    request_time: datetime

    class Config:
        orm_mode = True
