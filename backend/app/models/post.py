from sqlmodel import Field, SQLModel

class Post(SQLModel, table=True):
    """
    帖子表,作为一个论坛，我们需要有帖子，这个类表示数据库中

    """
    __tablename__: str = "Posts"
    __table_args__ = {'extend_existing':True}
    id: int = Field(primary_key=True)
    user_id: int = Field(foreign_key="Users.user_id")
    content: str
    topic_id: int = Field(foreign_key="Topics.id")
    reply_id: int = Field(foreign_key="Posts.id", nullable=True)


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
