from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def root():
    """ Health check endpoint."""
    return {"message": "Task Management API is running."}