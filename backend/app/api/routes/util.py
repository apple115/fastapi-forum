from fastapi import APIRouter
from pydantic import EmailStr

router = APIRouter()

@router.post("/email")
def send_email(email: EmailStr):
    pass
