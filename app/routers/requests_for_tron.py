"""API routes for Tron address requests."""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc
from fastapi_pagination import Page
from fastapi_pagination.ext.async_sqlalchemy import paginate

from app.service.get_tron_account_info import get_tron_account_info
from app.schemas import TronAddressRequest, TronAddressResponse, RequestsList
from app.database import get_session
from app.models import RequestsToTron
from app.crud.tron_requests import create_tron_request_record

router = APIRouter(prefix="/requests_for_tron", tags=["requests_for_tron"])


@router.post("/", response_model=TronAddressResponse)
async def create_request(
        address_data: TronAddressRequest,
        db: AsyncSession = Depends(get_session)
):
    """
    Handle a request for Tron account data and save the address to the database.

    Args:
        address_data (TronAddressRequest): Tron address payload.
        db (AsyncSession): Database session.

    Returns:
        TronAddressResponse: Account data.
    """
    data = await get_tron_account_info(address_data.address)
    await create_tron_request_record(data.address, db)
    return data


@router.get("/", response_model=Page[RequestsList])
async def get_requests(db: AsyncSession = Depends(get_session)):
    """
    Return a paginated list of all saved Tron address requests.

    Args:
        db (AsyncSession): Database session.

    Returns:
        Page[RequestsList]: Paginated request records.
    """
    query = select(RequestsToTron).order_by(desc(RequestsToTron.request_time))
    return await paginate(db, query)
