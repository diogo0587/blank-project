from functools import lru_cache
from pydantic import BaseSettings, AnyUrl


class Settings(BaseSettings):
    PROJECT_NAME: str = "CF Ops & Observability"
    API_V1_PREFIX: str = "/api"

    POSTGRES_DSN: AnyUrl = "postgresql+psycopg2://cfops:cfops@postgres:5432/cfops"
    CLICKHOUSE_DSN: str = "clickhouse://clickhouse:9000"

    JWT_SECRET_KEY: str = "CHANGE_ME"
    JWT_ALGORITHM: str = "HS256"

    CLOUDFLARE_API_BASE: str = "https://api.cloudflare.com/client/v4"

    LOGPUSH_SHARED_SECRET: str = "CHANGE_ME"

    REDIS_URL: str = "redis://redis:6379/0"

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    return Settings()