from datetime import datetime
from sqlmodel import Field, SQLModel

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

class UserPublic(SQLModel):
    user_id:int
    name:str
    email:str
