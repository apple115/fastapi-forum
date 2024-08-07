from typing import Any

from fastapi import APIRouter,Depends,HTTPException
from app.api.deps import CurrentUser
from app.models import UserPublic

router = APIRouter()
@router.get("/me", response_model=UserPublic)
def read_user_me(current_user: CurrentUser) -> Any:
    """
    Get current user.
    """
    return current_user


