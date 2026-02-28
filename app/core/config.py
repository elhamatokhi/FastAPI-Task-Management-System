from pydantic_settings import BaseSettings
from pathlib import Path

# Define base paths OUTSIDE the Settings model
BASE_DIR = Path(__file__).resolve().parent.parent  # points to app/
DATA_DIR = BASE_DIR / "data"

class Settings(BaseSettings):
    # App metadata
    APP_NAME: str = "Task Management API"
    VERSION: str = "1.0.0"
    TASKS_FILE: Path = DATA_DIR / "tasks.json"
    BACKUP_DIR: Path = DATA_DIR / "backups"

    # CORS
    BACKEND_CORS_ORIGINS: list[str] = ["http://localhost:3000"]

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()