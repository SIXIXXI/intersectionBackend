from typing import Generator, Annotated
from app.db.session import engine
from sqlmodel import Session
from fastapi import Depends


def get_db() -> Generator:
  with Session(engine) as session:
    yield session


db_dep = Annotated[Session, Depends(get_db)]
