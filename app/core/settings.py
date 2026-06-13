from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    DEBUG: bool

    DATABASE_URL: str
    REDIS_URL: str

    class Config:
        env_file=".env"
        extra="allow"


@lru_cache()
def get_settings()-> Settings:
    return Settings()

