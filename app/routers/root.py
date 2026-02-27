from fastapi import APIRouter

from app.core.config import get_settings

router = APIRouter()


@router.get("/", summary="Health check")
def read_root() -> dict:
    """Simple health check endpoint to verify the API is running."""
    settings = get_settings()
    return {"status": "ok", "app": settings.app_name}

