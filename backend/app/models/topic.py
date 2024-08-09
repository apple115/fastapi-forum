from datetime import datetime
from sqlmodel import Field, SQLModel
import uuid

class TopicBase(SQLModel):
    title: str
    description: str

class TopicCreate(TopicBase):
    creator_id: uuid.UUID = Field(foreign_key="Users.id")

class TopicInput(SQLModel):
    title:str
    description: str

class TopicPublic(TopicBase):
    id: int
    time: datetime
    creator_id: uuid.UUID

class TopicUpdate(SQLModel):
    title:str|None = Field(default=None,max_length=100)
    description:str|None = Field(default=None,max_length=1000)

class Topic(TopicBase, table=True):
    """
    话题表,作为一个论坛，我们需要有话题，这个类表示数据库中
    比如：是
    表名：Topics
    """
    __tablename__:str = "Topics"
    __table_args__ = {'extend_existing':True}
    id: int|None = Field(default=None, primary_key=True)
    time: datetime = Field(default=datetime.now())
    creator_id: uuid.UUID = Field(foreign_key="Users.id")
