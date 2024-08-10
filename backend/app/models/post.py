from sqlmodel import Field, SQLModel
import uuid
from datetime import datetime

class PostBase(SQLModel):
    content: str
    sequence:int
    topic_id: int = Field(foreign_key="Topics.id")

class PostCreate(PostBase):
    creator_id: uuid.UUID = Field(foreign_key="Users.id")
    time: datetime = Field(default=datetime.now())

class PostInput(SQLModel):
    content:str

class PostCreateReply(PostBase):
    creator_id: uuid.UUID = Field(foreign_key="Users.id")
    time: datetime = Field(default=datetime.now())
    reply_id: int|None = Field(foreign_key="Posts.id", nullable=True)


class PostUpdate(PostBase):
    content:str|None

class Post(PostBase, table=True):
    """
    帖子表,作为一个论坛，我们需要有帖子，这个类表示数据库中

    """
    __tablename__: str = "Posts"
    __table_args__ = {'extend_existing':True}
    id: int|None = Field(default=None, primary_key=True)
    creator_id: uuid.UUID = Field(foreign_key="Users.id")
    time: datetime = Field(default=datetime.now())
    reply_id: int|None = Field(foreign_key="Posts.id", nullable=True,default=None)

# 帖子的额外信息
class PostInfo(SQLModel, table=True):
    """
    帖子信息表,作为一个论坛，我们需要有帖子，这个类表示数据库中
    """
    __tablename__: str = "PostInfo"
    __table_args__ = {'extend_existing':True}
    id: int = Field(primary_key=True)
    post_id: int = Field(foreign_key="Posts.id")
    like: int = 0
    dislike: int = 0
    reply: int = 0
