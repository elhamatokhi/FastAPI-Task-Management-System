from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # App metadata
    APP_NAME: str = "Task Management API"
    VERSION: str = "1.0.0"
    TASKS_FILE: str = "tasks.txt"
    BACKUP_FILE: str = "tasks_backup.txt"

    # CORS
    BACKEND_CORS_ORIGINS: list[str] = ["http://localhost:3000"]

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()