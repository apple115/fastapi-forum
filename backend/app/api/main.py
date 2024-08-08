from fastapi import APIRouter

from app.api.routes import login,users,register,topic

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(register.router,tags=["register"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(topic.router, prefix="/topics", tags=["topics"])
# api_router.include_router(items.router, prefix="/items", tags=["items"])
