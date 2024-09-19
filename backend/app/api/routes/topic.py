from fastapi import APIRouter, HTTPException, Query
from sqlmodel import select
from app.api.deps import RedisDep, SessionDep
from app.models.topic import TopicCreate, TopicInput, Topic, TopicUpdate
from app.crud import topic_crud
from app.api.deps import CurrentUser, CurrentAdmin
from redis.commands.json.path import Path
from typing import Any
import uuid
import json
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
router = APIRouter()
"""
主题:
- POST /topic: 创建主题 (TODO)
- GET /topic: 获取所有主题 (TODO)
- GET /topic/{topic_id}: 获得某个主题(TODO)
- DELETE /topic/{topic_id}: 删除这个主题(TODO)
- PUT /topic/{topic_id}: 更新某个主题的信息,需要全部信息(TODO)
- PATCH /topic/{topic_id}: 更新某个主题的信息,需要部分信息(TODO)
"""


@router.get("/topic", response_model=list[Topic])
def get_all_topic(
    session: SessionDep, offset: int = 0, limit: int = Query(default=100, le=100)
):
    topics = session.exec(select(Topic).offset(offset).limit(limit)).all()
    if len(topics) == 0:
        raise HTTPException(status_code=404, detail="topics not found")
    return topics

@router.post("/topic")
def create_topic(session: SessionDep, topicData: TopicInput, current_user: CurrentUser):
    topic_in = TopicCreate(
        title=topicData.title,
        description=topicData.description,
        creator_id=current_user.id,
    )
    _ = topic_crud.create_topic(session=session, topic_in=topic_in)
    return {"message": "Create a new topic"}

@router.get("/topic/{topic_id}", response_model=Topic)
def get_topic(session: SessionDep, topic_id: int, redis_client: RedisDep):
    topic = redis_client.json().get(str(topic_id), Path.root_path())
    if topic:
        logger.info("get topic from redis")
        return topic
    else:
        topic = topic_crud.get_topic_by_id(session=session, topic_id=topic_id)
        _ = redis_client.json().set(
            str(topic_id), Path.root_path(), topic.model_json_schema()
        )
    if topic is None:
        raise HTTPException(status_code=404, detail="topic not found")
    return topic


@router.delete("/topic/{topic_id}")
def delete_topic(
    session: SessionDep,
    topic_id: int,
    _current_admin: CurrentAdmin,
    redis_client: RedisDep,
):
    rv = topic_crud.delete_topic_by_id(session=session, topic_id=topic_id)
    _ = redis_client.json().delete(str(topic_id), Path.root_path())
    if rv is False:
        raise HTTPException(status_code=404, detail="topic not found")
    return {"message": "Delete a topic"}


@router.put("/topic/{topic_id}", include_in_schema=False)
def put_topic(
    session: SessionDep,
    topic_id: int,
    topic_update: TopicUpdate,
    current_user: CurrentUser,
):
    create_id = topic_crud.get_create_id(session=session, topic_id=topic_id)
    if create_id != current_user.id:
        raise HTTPException(status_code=401, detail="topic not belong to you")
    rv = topic_crud.update_topic_by_id(
        session=session, topic_id=topic_id, topic_in=topic_update
    )
    if rv is False:
        raise HTTPException(status_code=404, detail="topic not found")
    return {"message": "Update a topic"}


# @router.patch("topics/{topic_id}", include_in_schema=False)
# def patch_topic(session: SessionDep, topic_id: int, current_user: CurrentUser):
#     try:
#         pass
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
