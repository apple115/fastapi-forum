from fastapi import APIRouter

from app.api.routes import login, users, register, topic, post

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(register.router, tags=["register"])
api_router.include_router(users.router, tags=["users"])
api_router.include_router(topic.router, tags=["topics"])
api_router.include_router(post.router, tags=["posts"])
# api_router.include_router(items.router, prefix="/items", tags=["items"])
