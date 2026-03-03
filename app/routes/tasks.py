from fastapi import APIRouter
from typing import List, Optional
from app.models import TaskCreate, TaskUpdate, TaskResponse
from app import crud

router = APIRouter()


@router.get("/", response_model=List[TaskResponse])
def list_tasks(status: Optional[str] = None):
    """
    Get all tasks.
    Optionally filter by status: pending | in_progress | completed
    Example: GET /tasks?status=pending
    """
    return crud.get_all_tasks(status=status)


@router.post("/", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate):
    """
    Create a new task.
    """
    return crud.create_task(task)


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    """
    Get a single task by its ID.
    """
    return crud.get_task_by_id(task_id)


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskUpdate):
    """
    Update an existing task.
    Only include the fields you want to change.
    """
    return crud.update_task(task_id, task)


@router.delete("/{task_id}")
def delete_task(task_id: int):
    """
    Delete a task by its ID.
    """
    return crud.delete_task(task_id)
