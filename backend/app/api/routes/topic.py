from fastapi import APIRouter,HTTPException
from app.api.deps import SessionDep
from app.models.topic import TopicCreate, TopicInput
from app.models.user import UserPublic
from app.crud import topic_crud
from app.api.deps import CurrentUser
from typing import Any

router = APIRouter()


@router.post("/topic_create")
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



@router.get("/{topic_id}")
def get_topic():
    return {"message": ""}
