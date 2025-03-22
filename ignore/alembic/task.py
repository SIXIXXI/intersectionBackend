from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime


class TaskBase(SQLModel):
  name: str = Field(index=True)
  completed: bool = False


class Task(TaskBase, table=True):
  id: int | None = Field(default=None, primary_key=True)
  created_at: datetime = Field(default_factory=datetime.utcnow)
  updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)


class UpdateTask(SQLModel):
  name: Optional[str] = None
  completed: Optional[bool] = None
