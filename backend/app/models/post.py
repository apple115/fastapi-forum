from sqlmodel import Field, SQLModel  # pyright: ignore
import uuid
from datetime import datetime


class PostBase(SQLModel):
    topic_id: int
    content: str = Field(max_length=255)
    is_hidden: bool = Field(default=False)


class PostCreate(PostBase):
    creator_id: uuid.UUID
    time: datetime = Field(default=datetime.now())
    reply_id: int | None = Field(nullable=True, default=None)


class PostInput(SQLModel):
    content: str


class PostUpdate(SQLModel):
    content: str | None
    is_hidden: bool | None


class Post(PostBase, table=True):
    """
    帖子表,作为一个论坛，我们需要有帖子，这个类表示数据库中
    """

    id: int | None = Field(default=None, primary_key=True)  # 自动id
    creator_id: uuid.UUID
    time: datetime = Field(default=datetime.now())
    reply_id: int | None = Field(nullable=True, default=None)
