from sqlmodel import Session, select
from collections.abc import Sequence
from app.models.topic import Topic, TopicBase, TopicCreate, TopicUpdate
import uuid


def create_topic(*, session: Session, topic_in: TopicCreate) -> bool:
    db_obj = Topic.model_validate(topic_in)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return True


def get_all_topics(*, session: Session) -> Sequence[Topic] | None:
    db_obj = session.exec(select(Topic)).all()
    return db_obj


def get_topic_by_id(*, session: Session, topic_id: int) -> Topic | None:
    db_obj = session.exec(select(Topic).where(Topic.id == topic_id)).first()
    return db_obj


def get_create_id(*, session: Session, topic_id: int) -> uuid.UUID | None:
    db_obj = session.exec(select(Topic).where(Topic.id == topic_id)).first()
    return db_obj.creator_id


def delete_topic_by_id(*, session: Session, topic_id: int) -> bool:
    db_obj = session.exec(select(Topic).where(Topic.id == topic_id)).first()
    if db_obj is None:
        return False
    session.delete(db_obj)
    session.commit()
    return True


def update_topic_by_id(
    *, session: Session, topic_id: int, topic_in: TopicUpdate
) -> bool:
    db_obj = session.exec(select(Topic).where(Topic.id == topic_id)).first()
    if db_obj is None:
        return False
    if topic_in.title is not None:
        db_obj.title = topic_in.title
    if topic_in.description is not None:
        db_obj.description = topic_in.description
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return True
