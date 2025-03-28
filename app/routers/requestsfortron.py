from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.service.gettronaccountinfo import get_tron_account_info
from app.schemas import TronAddressRequest, TronAddressResponse, Listofrequests
from app.database import get_session
from app.models import RequestsToTron
from app.config import PAGES_SIZE

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


@router.get("/", response_model=Listofrequests)
async def get_requests_list(
        page: int = Query(1, ge=1, description="Номер страницы (начиная с 1)"),

        db: AsyncSession = Depends(get_session)
):
    pass
