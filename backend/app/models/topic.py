from datetime import datetime
from sqlmodel import Field, SQLModel

class Topic(SQLModel, table=True):
    """
    话题表,作为一个论坛，我们需要有话题，这个类表示数据库中
    比如：是
    表名：Topics
    """
    __tablename__:str = "Topics"
    __table_args__ = {'extend_existing':True}
    topic_id: int = Field(primary_key=True)
    time: datetime = Field(default=datetime.now)
    title: str
    description: str
    creator_id: int = Field(foreign_key="Users.user_id")
