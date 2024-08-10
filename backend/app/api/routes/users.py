from typing import Any
import uuid

from fastapi import APIRouter, Depends, HTTPException
from app.api.deps import CurrentUser
from app.models.user import UserPublic, UserData
from app.api.deps import SessionDep
from app.crud import user_crud

router = APIRouter()


@router.get("/me", response_model=UserPublic)
def read_user_me(current_user: CurrentUser) -> Any:
    """
    Get current user.
    """
    return current_user


@router.get("/users/{user_id}", response_model=UserData)
def get_user_by_id(session: SessionDep, user_id: uuid.UUID) -> Any:
    """
    Get a specific user by id.
    """
    user =user_crud.get_user_by_id(session=session,id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
