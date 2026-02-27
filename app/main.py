from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import root, tasks
from app.core.config import settings

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.VERSION,
        description="Backend API for User Management"
    )

    # Register routers 
    app.include_router(root.router)
    app.include_router(tasks.router, prefix='/tasks', tags=["Tasks"])

    return app

app = create_app()