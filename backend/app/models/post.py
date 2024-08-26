from sqlmodel import Field, SQLModel # pyright: ignore
import uuid
from datetime import datetime

USERFOREIGNKEY = "user.id"
POSTFOREIGNKEY = "post.id"
TOPICFOREIGNKEY = "topic.id"

class PostBase(SQLModel):
    content: str
    sequence: int
    topic_id: int = Field(foreign_key=TOPICFOREIGNKEY)


class PostCreate(PostBase):
    creator_id: uuid.UUID = Field(foreign_key=USERFOREIGNKEY)
    time: datetime = Field(default=datetime.now())


class PostInput(SQLModel):
    content: str


class PostCreateReply(PostBase):
    creator_id: uuid.UUID = Field(foreign_key=USERFOREIGNKEY)
    time: datetime = Field(default=datetime.now())
    reply_id: int | None = Field(foreign_key=USERFOREIGNKEY, nullable=True)


class PostUpdate(PostBase):
    content: str


class Post(PostBase, table=True):
    """
    帖子表,作为一个论坛，我们需要有帖子，这个类表示数据库中

    """
    __table_args__ = {"extend_existing": True}
    id: int | None = Field(default=None, primary_key=True)
    creator_id: uuid.UUID = Field(foreign_key=USERFOREIGNKEY)
    time: datetime = Field(default=datetime.now())
    reply_id: int | None = Field(foreign_key=POSTFOREIGNKEY, nullable=True, default=None)


# 帖子的额外信息
class PostInfo(SQLModel, table=True):
    """
    帖子信息表,作为一个论坛，我们需要有帖子，这个类表示数据库中
    """
    __table_args__ = {"extend_existing": True}
    id: int = Field(primary_key=True)
    post_id: int = Field(foreign_key=POSTFOREIGNKEY)
    like: int = 0
    dislike: int = 0
    reply: int = 0
