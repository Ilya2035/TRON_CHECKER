"""Application settings loaded from .env."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class CustomBaseSettings(BaseSettings):
    """Environment-based configuration settings."""
    API_KEY: str

    model_config = SettingsConfigDict(
        case_sensitive=True, extra="ignore", env_file=".env"
    )


settings = CustomBaseSettings()
