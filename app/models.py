from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum


class TaskStatus(str, Enum):
    pending     = "pending"
    in_progress = "in_progress"
    completed   = "completed"


class TaskCreate(BaseModel):
    """Schema for creating a new task."""
    title:       str            = Field(..., min_length=1, max_length=255, example="Buy groceries")
    description: Optional[str] = Field(None, example="Milk, eggs, bread")
    status:      TaskStatus     = Field(TaskStatus.pending, example="pending")
    due_date:    Optional[datetime] = Field(None, example="2024-12-31T18:00:00")


class TaskUpdate(BaseModel):
    """Schema for updating an existing task. All fields are optional."""
    title:       Optional[str]      = Field(None, min_length=1, max_length=255)
    description: Optional[str]      = None
    status:      Optional[TaskStatus] = None
    due_date:    Optional[datetime]  = None


class TaskResponse(BaseModel):
    """Schema for returning a task in API responses."""
    id:          int
    title:       str
    description: Optional[str]
    status:      str
    due_date:    Optional[datetime]
    created_at:  datetime
    updated_at:  datetime
