from fastapi import APIRouter, Query
from app.schemas.task import Task, TaskCreate
from fastapi.responses import JSONResponse
from app.services import task_service
from datetime import datetime
router = APIRouter()

# ---------------------------
# STATIC ROUTES
# ---------------------------

@router.get("/export")
def export_tasks():
    """Export all tasks as downloadable JSON file."""
    
    # Retrieve all tasks (no filter applied)
    tasks = task_service.get_all_tasks(completed=None)

    # Generate timestamped filename for safe versioning
    timestamp = datetime.now(datetime.timezone.utc()).strftime("%Y%m%d_%H%M%S")
    filename = f"tasks_backup_{timestamp}.json"

    # Return JSON with download headers
    return JSONResponse(
        content=tasks,
        headers={
            "Content-Disposition": f'attachment; filename="{filename}"'
        }
    )

@router.get('/stats')
def get_stats():
    """ Get task statistics."""
    return task_service.get_task_stats()

@router.get('/', response_model=list[Task])
def get_tasks(completed: bool | None = Query(None)):
    """ Get all tasks with optional filter. Example: /tasks?completed=true"""
    return task_service.get_all_tasks(completed)

@router.post('/', response_model=Task)
def create_task(task: TaskCreate):
    """Create new task."""
    return task_service.create_task(task)

@router.delete("/")
def delete_all_tasks():
    """ Delete all tasks."""
    task_service.delete_all_tasks()
    return {"message": "All tasks deleted successfully"}

# ---------------------------
# DYNAMIC ROUTES 
# ---------------------------

@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int):
    """ Get single task by ID."""
    return task_service.get_task_by_id(task_id)

@router.put('/{task_id}', response_model=Task)
def update_task(task_id: int, task: Task):
    """ Update existing task completely."""
    return task_service.update_task(task_id, task)

@router.delete("/{task_id}")
def delete_task(task_id: int):
    """ Delete single task."""

    task_service.delete_task(task_id)
    return {"message": "Task deleted successfully"}