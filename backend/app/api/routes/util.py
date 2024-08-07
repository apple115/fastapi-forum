from fastapi import APIRouter
from pydantic import EmailStr




router = APIRouter()

@router.post("/email")
def
