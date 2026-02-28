from fastapi import HTTPException
from app.services.file_handler import load_tasks, save_tasks, get_next_id

def get_all_tasks(completed: bool | None = None):
    """ Retrieve all tasks with optional filtering"""

    tasks = load_tasks()

    if completed is not None:
        tasks = [task for task in tasks if task["completed"] == completed]
    return tasks

def get_task_by_id(task_id: int):
    """Retrieve single task by ID."""
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            return task
        
    raise HTTPException(status_code=404, detail="Task not found")

def create_task(task_data):
    """ Create new task with sequential ID."""

    tasks = load_tasks()
    
    new_task = {
        "id": get_next_id(tasks),
        "title": task_data.title,
        "description": task_data.description,
        "completed": False
    }

    tasks.append(new_task)
    save_tasks(tasks)

    return new_task


def update_task(task_id: int, updated_task):
    """Replace full task object by ID."""
    tasks = load_tasks()
    
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks[index] = updated_task.model_dump()
            save_tasks(tasks)
            return updated_task
    
    raise HTTPException(status_code=404, detail="Task not found")

def delete_task(task_id: int):
    """Delete single task."""
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]

    if len(tasks) == len(new_tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    
    save_tasks(new_tasks)

def delete_all_tasks():
    """Remove all tasks for storage."""
    save_tasks([])

def get_task_stats():
    """ Return task statistics summary."""

    tasks = load_tasks()
    total = len(tasks)
    completed = len([t for t in tasks if t["completed"]])
    pending = total - completed
    percentage = (completed / total * 100) if total > 0 else 0
    
    return {
        "total_tasks": total,
        "completed_tasks": completed,
        "pending_tasks": pending,
        "completion_percentage": round(percentage, 2)
    }
