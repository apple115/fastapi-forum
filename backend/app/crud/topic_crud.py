from sqlmodel import Session

from app.models.topic import Topic, TopicCreate


def create_topic(*,session:Session,topic_in:TopicCreate)->Topic:
    db_obj = Topic.model_validate(topic_in)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj
