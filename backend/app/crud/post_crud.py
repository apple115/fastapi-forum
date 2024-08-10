from sqlmodel import Session, func
from app.models.post import Post, PostCreate


def create_post(*, session: Session, post_in: PostCreate) -> Post | None:
    db_obj = Post.model_validate(post_in)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj


def get_topic_max_sequence(*, session: Session, topic_id: int) -> int | None:
    max_sequence = (
        session.query(func.max(Post.sequence)).filter(Post.topic_id == topic_id).scalar()
    )
    return max_sequence
