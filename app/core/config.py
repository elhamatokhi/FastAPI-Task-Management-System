from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # App metadata
    APP_NAME: str = "Task Management API"
    VERSION: str = "1.0.0"

    # Database
    DATABASE_URL: str = "sqlite:///./tasks.db"

    # CORS
    BACKEND_CORS_ORIGINS: list[str] = ["http://localhost:3000"]

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache
def get_settings() -> Settings:
    return Settings()


# Optional: direct import shortcut
settings = get_settings()