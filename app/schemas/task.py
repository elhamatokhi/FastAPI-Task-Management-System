from pydantic import BaseModel

class Task(BaseModel):
    """ Full Task model used in reponses."""

    id: int
    title: str
    description: str | None = None
    completed: bool = False

class TaskCreate(BaseModel):
    """ 
    Model used when creating a new task. 
    ID is auto-generated.
    """
    title: str
    description: str | None = None
    category: str | None = None
