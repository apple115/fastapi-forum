from fastapi import APIRouter, HTTPException
from app.api.deps import SessionDep,CurrentUser
from app.models.post import Post, PostCreate, PostInput
from app.crud import post_crud
from app.crud.post_crud import get_topic_max_sequence

router = APIRouter()
"""
帖子:
 这个{post_id} 这个的是主题下第几个回答
- POST /topics/{topic_id}/posts: 在某个主题下创建帖子 (TODO)
- GET /topics/{topic_id}/posts: 在某个主题获得全部帖子 (TODO)(TODO 可能需要分页)
- GET /topics/{topic_id}/posts/{posts_id}:获取这个帖子在这个主题下(TODO)
- PUT /topics/{topic_id}/posts/{posts_id}:更新这个帖子,需要全部信息(TODO)
- PATCH /topics/{topic_id}/posts/{posts_id}:更新这个帖子，需要部分信息(TODO)
- PATCH /topics/{topic_id}/posts/{posts_id}/likes:更新这个点赞(TODO)
- GET /topics/{topic_id}/posts/{posts_id}/likes:查看这个点赞(TODO)

只有一级回应会放在这个帖子的下面
回应的回应不会放在这个帖子下
"""

@router.post("/topics/{topic_id}/posts")
def create_post(session: SessionDep, topic_id: int, post_input: PostInput,CurrentUser:CurrentUser):
    try:
        max_sequence = get_topic_max_sequence(session=session, topic_id=topic_id)
        new_sequence =( max_sequence+1) if max_sequence is not None else 1
        post = PostCreate(
            content=post_input.content,
            sequence=new_sequence,
            topic_id=topic_id,
            creator_id=CurrentUser.id
        )
        post_crud.create_post(session=session, post_in=post)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/topics/{topic_id}/posts",include_in_schema=False)
def get_posts(session: SessionDep, topic_id: int):
    try:
        pass
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/topics/{topic_id}/posts/{post_id}",include_in_schema=False)
def get_post(session: SessionDep, topic_id: int, post_id: int,include_in_schema=False):
    try:
        pass
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/topics/{topic_id}/posts/{post_id}",include_in_schema=False)
def patch_post(session: SessionDep, topic_id: int, post_id: int):
    try:
        pass
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/topics/{topic_id}/posts/{post_id}/likes",include_in_schema=False)
def get_post_likes(session: SessionDep, topic_id: int, post_id: int):
    try:
        pass
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
