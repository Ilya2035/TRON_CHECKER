"""Tron client setup with API key provider."""

from tronpy import AsyncTron
from tronpy.providers.async_http import AsyncHTTPProvider

from app.settings import settings


def get_tron_client() -> AsyncTron:
    """
    Return an asynchronous Tron client configured with API key.

    Returns:
        AsyncTron: Configured Tron client instance.
    """
    return AsyncTron(provider=AsyncHTTPProvider(api_key=settings.API_KEY))
