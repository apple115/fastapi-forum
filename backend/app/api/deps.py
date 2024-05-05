from typing import Annotated
from sqlmodel import Session
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from collections.abc import Generator
from app.core.db import engine
from app.core.config import settings

reusable_oauth2=OAuth2PasswordBearer(
    tokenUrl=f'{settings.API_V1_STR}/login/access-token'
)

def get_db()->Generator[Session,None,None]:
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_db)]
TokenDep = Annotated[str, Depends(reusable_oauth2)]
