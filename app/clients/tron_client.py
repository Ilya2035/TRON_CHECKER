from tronpy import AsyncTron
from tronpy.providers.async_http import AsyncHTTPProvider

from app.settings import settings


def get_tron_client() -> AsyncTron:
    return AsyncTron(provider=AsyncHTTPProvider(api_key=settings.API_KEY))
