from datetime import datetime
from sqlmodel import Field, SQLModel, Relationship,create_engine,Session
from app.core.config import settings

class User(SQLModel, table=True):
    """
    使用SQLModel定义的用户表模型。这个类表示数据库中的一个用户表，
    继承自SQLModel，表明它是一个模型类，并且可以映射到数据库中的一个表。

    Attributes:
        __tablename__ (str): 指定数据库中的表名。如果不设置，默认为类名的小写形式。
        __table_args__ (dict): 特殊表参数，这里设置'extend_existing': True，表示允许模型扩展已存在的表。
        user_id (int | None): 用户的唯一标识符，设为主键（primary key），默认为None。
        created_at (datetime): 用户创建时间，使用Field指定默认值为当前时间。
        name (str): 用户的姓名。
        email (str): 用户的电子邮件地址，通过Field设置为唯一（unique=True），意味着在表中不能有重复的电子邮件。
        password_hash (str): 用户的密码哈希值，用于存储加密后的密码。
        level (int): 用户的权限等级，不同等级有不同权限：
            - level: 0 表示 root 权限。
            - level: 1 表示 管理员。
            - level: 2 表示 普通论坛人员。
    """
    __tablename__:str = "Users"  # 可以指定表名，如果不指定，默认为类名的小写形式
    __table_args__ = {'extend_existing': True}  # 允许扩展已存在的表，而不是每次重新创建
    user_id: int | None = Field(primary_key=True,default=None)
    created_at: datetime = Field(default=datetime.now())
    name: str
    email: str = Field(unique=True)
    password_hash: str
    level: int

class Topic(SQLModel, table=True):
    """
    主题表
    表名：Topics

    """
    __tablename__:str = "Topics"
    __table_args__ = {'extend_existing':True}
    id: int = Field(primary_key=True)
    time: datetime = Field(default=datetime.now)
    title: str
    creator_id: int = Field(foreign_key="Users.user_id")


class Post(SQLModel, table=True):
    """

    """
    __tablename__: str = "Posts"
    __table_args__ = {'extend_existing':True}
    id: int = Field(primary_key=True)
    user_id: int = Field(foreign_key="Users.user_id")
    content: str
    topic_id: int = Field(foreign_key="Topics.id")
    reply_id: int = Field(foreign_key="Posts.id", nullable=True)

class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"

engine = create_engine(settings.SQLALCHEMY_DATABASE_URL,echo=True)

# def create_user():
#     """
#     创造用户
#     """
#     user1=User(name='root',email='root@qq.com',password_hash='123456',level=0)
#     user2=User(name='apple',email='apple@qq.com',password_hash='123456',level=1)
#     with Session(engine) as session:
#         session.add(user1)
#         session.add(user2)
#         session.commit()


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def main():
    create_db_and_tables()
#    create_user()

if __name__ == '__main__':
    main()
