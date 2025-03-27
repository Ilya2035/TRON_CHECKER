from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.service.gettronaccountinfo import get_tron_account_info
from app.schemas import TronAddressRequest, TronAddressResponse
from app.database import get_session
from app.models import RequestsToTron

router = APIRouter(prefix="/requestsfortron", tags=["requestsfortron"])


@router.post("/", response_model=TronAddressResponse)
async def create_request(
        addresdata: TronAddressRequest,
        db: AsyncSession = Depends(get_session)
):
    data = await get_tron_account_info(addresdata.address)
    upload = RequestsToTron(tron_address=data.address)

