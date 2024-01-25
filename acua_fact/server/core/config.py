from pydantic import AnyHttpUrl, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_url: str = Field(validation_alias="DATABASE_URL")
    origins: list[AnyHttpUrl] = Field(validation_alias="ORIGINS")
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()
print(settings.model_dump())
