from fastapi import APIRouter, Query
from app.schemas.task import Task, TaskCreate
from app.services import task_service

router = APIRouter()

@router.get('/', response_model=list[Task])
def get_tasks(completed: bool | None = Query(None)):
    """ Get all tasks with optional filter. Example: /tasks?completed=true"""

    return task_service.get_all_tasks(completed)

@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int):
    """ Get single task by ID."""
    return task_service.get_task_by_id(task_id)

@router.post('/', response_model=Task)
def create_task(task: TaskCreate):
    """Create new task."""
    return task_service.create_task(task)

@router.put('/{task_id}', response_model=Task)
def update_task(task_id: int, task: Task):
    """ Update existing task completely."""
    return task_service.update_task(task_id, task)

@router.delete("/{task_id}")
def delete_task(task_id: int):
    """ Delete single task."""

    task_service.delete_task(task_id)
    return {"message": "Task deleted successfully"}

@router.delete("/")
def delete_all_tasks():
    """ Delete all tasks."""
    task_service.delete_all_tasks()
    return {"message": "All tasks deleted successfully"}

@router.get('/stats')
def get_stats():
    """ Get task statistics."""
    return task_service.get_task_stats()