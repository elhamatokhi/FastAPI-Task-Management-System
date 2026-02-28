import json
from datetime import datetime
import os 
from pathlib import Path
from app.core.config import settings
import datetime as dt

def load_tasks():
    """
    Load tasks from JSON Lines file.
    Returns list of dictionaries.
    """
    tasks_path = Path(settings.TASKS_FILE)
    if not os.path.exists(settings.TASKS_FILE):
        return []
    
    try:
        with tasks_path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        # File exists but is corrupted or empty
        return []


    return tasks
            
def save_tasks(tasks: list):
    """
    Save full task list to disk.
    Creates timestamped backup before overwrite.
    Uses atomic write to prevent data corruption.
    """
    tasks_path = Path(settings.TASKS_FILE)
    backup_dir = Path(settings.BACKUP_DIR)

    backup_dir.mkdir(parents=True, exist_ok=True)

    # Create backup
    if tasks_path.exists():
        timestamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d_%H%M%S")
        backup_path = backup_dir / f"tasks_backup_{timestamp}.json"

        with tasks_path.open("r", encoding="utf-8") as original, \
            backup_path.open("w", encoding="utf-8") as backup:
            backup.write(original.read())

    # Atomic write
    temp_path = tasks_path.with_suffix(".tmp")

    with temp_path.open("w", encoding="utf-8") as temp_file:
        json.dump(tasks, temp_file, indent=4)

    temp_path.replace(tasks_path)

def get_next_id(tasks: list):
    """Generate sequential ID starting from 1."""

    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1