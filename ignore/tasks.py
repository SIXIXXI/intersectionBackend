from typing import List, final
from fastapi import APIRouter, Depends, HTTPException
from app.api.deps import db_dep
from app.models.task import TaskBase, Task, UpdateTask
from sqlmodel import select

router = APIRouter()


@router.get("")
def read_tasks(db: db_dep) -> List[Task]:
  return list(db.exec(select(Task)).all())


@router.post("")
def create_task(task: TaskBase, db: db_dep) -> Task:
  db_task = Task.model_validate(task)
  db.add(db_task)
  db.commit()
  db.refresh(db_task)
  return db_task


@router.get("/{task_id}")
def read_task(task_id: int, db: db_dep) -> Task:
  task = db.get(Task, task_id)
  if task is None:
    raise HTTPException(status_code=404, detail="Task not found")
  return task


@router.put("/{task_id}")
def update_task(task_id: int, task: UpdateTask, db: db_dep) -> Task:
  db_task = db.get(Task, task_id)
  if db_task is None:
    raise HTTPException(status_code=404, detail="Task not found")
  new_task = task.model_dump(exclude_unset=True)
  for key, value in new_task.items():
    setattr(db_task, key, value)
  db.add(db_task)
  db.commit()
  db.refresh(db_task)
  return db_task
