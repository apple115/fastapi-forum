from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()

class SearchRequest(BaseModel):
    search: str
    type: str = ""


@router.post("/search")
def search(request: SearchRequest):
    # TODO 实现搜索功能
    result = {"search": "search"}
    return {"result": result, "total": len(result)}
