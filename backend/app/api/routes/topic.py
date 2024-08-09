from fastapi import APIRouter,HTTPException
from starlette.types import Message
from app.api.deps import SessionDep
from app.models.topic import TopicCreate, TopicInput,Topic
from app.models.user import UserPublic
from app.crud import topic_crud
from app.api.deps import CurrentUser,CurrentAdmin
from typing import Any

router = APIRouter()
'''
主题:
- POST /topics: 创建主题 (TODO)
- GET /topics: 获取所有主题 (TODO)
- GET /topics/{topic_id}: 获得某个主题(TODO)
- DELETE /topics/{topic_id}: 删除这个主题(TODO)
- PUT /topics/{topic_id}: 更新某个主题的信息,需要全部信息(TODO)
- PATCH /topics/{topic_id}: 更新某个主题的信息,需要部分信息(TODO)
'''

@router.get("/topics")
def  get_all_topic(session:SessionDep):
    try:
        topics=topic_crud.get_all_topics(session=session)
        if topics is None:
            return {"message":"no topics"}
        eniched_topics=[]
        for topic in topics:
            topic_links = [
                {"rel":"self","href":f"/topics/{topic.id}","methed":"GET"},
                {"rel":"delete","href":f"/topics/{topic.id}","methed":"DELETE"},
                {"rel":"put","href":f"/topics/{topic.id}","methed":"PUT"},
                {"rel":"patch","href":f"/topics/{topic.id}","methed":"PATCH"},
            ]
            enriched_topic={
                "id":topic.id,
                "title":topic.title,
                "description":topic.description,
                "creator":topic.id,
                "links":topic_links
            }
            eniched_topics.append(enriched_topic)
        return eniched_topics
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/topics")
def create_topic(
    session: SessionDep, topicData: TopicInput, current_user: CurrentUser
) -> Any:
    try:
        topic_in = TopicCreate(
            title=topicData.title,
            description=topicData.description,
            creator_id=current_user.id,
        )
        topic_crud.create_topic(
            session=session,
            topic_in=topic_in
        )
        return {"message": "Create a new topic"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/topics/{topic_id}")
def get_topic(session:SessionDep,topic_id:int):
    try:
        topic=topic_crud.get_topic_by_id(session=session,topic_id=topic_id)
        if topic is None:
            raise HTTPException(status_code=404,detail="topic not found")
        topic_links = [
            {"rel":"self","href":f"/topics/{topic.id}","methed":"GET"},
            {"rel":"delete","href":f"/topics/{topic.id}","methed":"DELETE"},
            {"rel":"put","href":f"/topics/{topic.id}","methed":"PUT"},
            {"rel":"patch","href":f"/topics/{topic.id}","methed":"PATCH"},
        ]
        enriched_topic={
            "id":topic.id,
            "title":topic.title,
            "description":topic.description,
            "creator":topic.id,
            "links":topic_links
        }
        return enriched_topic
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))

@router.delete("/topics/{topic_id}")
def delete_topic(session:SessionDep,topic_id:int,current_admin:CurrentAdmin):
    try:
        pass
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))

@router.put("/topics/{topic_id}")
def put_topic(session:SessionDep,topic_id:int,current_user: CurrentUser):
    try:
        pass
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))

@router.patch("topics/{topic_id}")
def patch_topic(session:SessionDep,topic_id:int,current_user: CurrentUser):
    try:
        pass
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
