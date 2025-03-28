from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc

from fastapi_pagination import Page
from fastapi_pagination.ext.async_sqlalchemy import paginate

from app.service.gettronaccountinfo import get_tron_account_info
from app.schemas import TronAddressRequest, TronAddressResponse, RequestsList
from app.database import get_session
from app.models import RequestsToTron

router = APIRouter(prefix="/requestsfortron", tags=["requestsfortron"])


@router.post("/", response_model=TronAddressResponse)
async def create_request(
        addresdata: TronAddressRequest,
        db: AsyncSession = Depends(get_session)
):
    data = await get_tron_account_info(addresdata.address)
    upload = RequestsToTron(tron_address=data["address"])
    db.add(upload)
    await db.commit()
    await db.refresh(upload)
    return data


@router.get("/", response_model=Page[RequestsList])
async def get_requests(db: AsyncSession = Depends(get_session)):
    query = select(RequestsToTron).order_by(desc(RequestsToTron.request_time))
    return await paginate(db, query)
