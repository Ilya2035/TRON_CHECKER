from pydantic_settings import BaseSettings, SettingsConfigDict


class CustomBaseSettings(BaseSettings):
    """Application settings loaded from .env."""
    API_KEY: str

    model_config = SettingsConfigDict(
        case_sensitive=True, extra="ignore", env_file=".env"
    )


settings = CustomBaseSettings()
