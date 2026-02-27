import json 
import os 
from app.core.config import settings

def load_tasks():
    """
    Load tasks from JSON Lines file.
    Returns list of dictionaries.
    """
    if not os.path.exists(settings.TASKS_FILE):
        return []
    
    tasks = []
    with open(settings.TASKS_FILE, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                tasks.append(json.loads(line))
            
    return tasks

def save_tasks(tasks: list):
    """
    Save full task list to file.
    Creates automatic backup before overwrite.
    """

    # Create backup
    if os.path.exists(settings.TASKS_FILE):
        with open(settings.TASKS_FILE, 'r') as original, open(settings.BACKUP_FILE, 'w') as backup:
            backup.write(original.read())

    # Rewrite entire file (data integrity requirement)
    with open(settings.TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(json.dumps(task) + "\n")


def get_next_id(tasks: list):
    """Generate sequential ID starting from 1."""

    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1