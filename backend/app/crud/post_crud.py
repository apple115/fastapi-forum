import uuid
from sqlmodel import Session, func, select
from app.models.post import Post, PostCreate, PostInput, PostUpdate
from app.models.topic import Topic


def create_post(*, session: Session, post_in: PostCreate) -> Post | None:
    db_obj = Post.model_validate(post_in)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj


def get_posts_by_topic_id(*, session: Session, topic_id: int) -> list[Post] | None:
    statement = select(Post).where(Post.topic_id == topic_id)
    posts = session.exec(statement)
    return posts


def get_post_by_id(*, session: Session, post_id: int) -> Post | None:
    statement = select(Post).where(Post.id == post_id)
    post = session.exec(statement).first()
    return post


def update_post(*, session: Session, post_id: int, post_in: PostUpdate) -> bool:
    post = session.get(Post, post_id)
    if not post:
        return False
    if post_in.content is not None:
        post.content = post_in.content
    if post_in.is_hidden is not None:
        post.is_hidden = post_in.is_hidden
    session.add(post)
    session.commit()
    session.refresh(post)
    return True


def get_create_id(*, session: Session, post_id: int) -> uuid.UUID | None:
    post = session.get(Post, post_id)
    return post.creator_id
