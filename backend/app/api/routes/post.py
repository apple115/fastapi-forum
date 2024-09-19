from fastapi import APIRouter, HTTPException, status
from app.api.deps import (
    SessionDep,
    CurrentUser,
)  # pyright: ignore[reportMissingTypeStubs]
from app.models.post import (
    PostCreate,
    PostInput,
    PostUpdate,
    Post,
)  # pyright: ignore[reportMissingTypeStubs]
from app.crud import post_crud  # pyright: ignore[reportMissingTypeStubs]
from fastapi.responses import JSONResponse

router = APIRouter()
"""
帖子:
 这个{post_id} 这个的是主题下第几个回答
- POST /topic/{topic_id}/post: 在某个主题下创建帖子 (TODO)
- GET /topic/{topic_id}/post: 在某个主题获得全部帖子 (TODO)(TODO 可能需要分页)
- GET /topic/{topic_id}/post/{posts_id}:获取这个帖子在这个主题下(TODO)
- PUT /topic/{topic_id}/post/{posts_id}:更新这个帖子,需要全部信息(TODO)
- PATCH /topic/{topic_id}/post/{posts_id}:更新这个帖子，需要部分信息(TODO)
只有一级回应会放在这个帖子的下面
回应的回应不会放在这个帖子下
"""


@router.post("/topics/{topic_id}/posts")
def create_post(
    session: SessionDep,
    topic_id: int,
    post_in: PostInput,
    reply_to: int,
    CurrentUser: CurrentUser,
):
    post_Create = PostCreate(
        creator_id=CurrentUser.id, topic_id=topic_id, content=post_in.content
    )
    if reply_to != -1:
        post_Create.reply_id = reply_to
    _ = post_crud.create_post(session=session, post_in=post_Create)
    return {"message": "create post"}


@router.get("/topics/{topic_id}/posts", response_model=list[Post])
def get_posts(session: SessionDep, topic_id: int):
    posts = post_crud.get_posts_by_topic_id(session=session, topic_id=topic_id)
    if not posts:
        raise HTTPException(status_code=404, detail="posts not found")
    return posts


@router.get("/topics/{topic_id}/posts/{post_id}")
def get_post(session: SessionDep, _topic_id: int, post_id: int):
    post = post_crud.get_post_by_id(session=session, post_id=post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="post not found")
    return post


@router.patch("/topics/{topic_id}/posts/{post_id}")
def patch_post(
    session: SessionDep,
    _topic_id: int,
    post_id: int,
    post_update: PostUpdate,
    CurrentUser: CurrentUser,
):
    create_id = post_crud.get_create_id(session=session, post_id=post_id)
    if create_id != CurrentUser.id:
        raise HTTPException(
            status_code=403, detail="you are not the creator of this post"
        )
    rv = post_crud.update_post(session=session, post_id=post_id, post_in=post_update)
    if rv is False:
        raise HTTPException(status_code=404, detail="post not found")
    return {"message": "update post"}
