from sqlmodel import Session

from typing import List
from app.models.topic import Topic, TopicCreate


def create_topic(*, session: Session, topic_in: TopicCreate) -> Topic:
    db_obj = Topic.model_validate(topic_in)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj

def get_all_topics(*, session: Session) -> List[Topic]:
    db_obj = session.query(Topic).all()
    return db_obj


def get_topic_by_id(*, session: Session, topic_id: int) -> Topic|None:
    db_obj = session.query(Topic).get({"id": topic_id})
    return db_obj
