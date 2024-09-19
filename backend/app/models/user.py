from datetime import datetime
from sqlmodel import Field, SQLModel
from pydantic import EmailStr
import uuid


class UserBase(SQLModel):
    """
    name (str): 用户的姓名。
    email (str): 用户的电子邮件地址，通过Field设置为唯一（unique=True），意味着在表中不能有重复的电子邮件。
    level (int): 用户的权限等级，不同等级有不同权限：
        - level: 0 表示 root 权限。
        - level: 1 表示 管理员。
        - level: 2 表示 普通论坛人员。
    """

    email: EmailStr = Field(unique=True, index=True, max_length=255)
    name: str | None = Field(default=None, max_length=255)
    level: int = Field(default=2)
    is_active: bool = Field(default=True)


class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=255)


class UserRegister(SQLModel):
    email: EmailStr = Field(max_length=255)
    password: str = Field(max_length=255)
    check_password: str = Field(max_length=255)
    name: str | None = Field(default=None, max_length=255)


class UserUpdate(SQLModel):
    email: EmailStr | None = Field(default=None, max_length=255)
    password: str | None = Field(default=None, min_length=8, max_length=255)


class UserUpdateLevel(SQLModel):
    level: int | None = Field(default=2)


class UserData(UserBase):
    created_at: datetime
    id: uuid.UUID

class User(UserBase, table=True):
    """
    使用SQLModel定义的用户表模型。这个类表示数据库中的一个用户表，
    继承自SQLModel，表明它是一个模型类，并且可以映射到数据库中的一个表。
    """

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default=datetime.now())
    password_hash: str


class UserPublic(UserBase):
    id: uuid.UUID
    created_at: datetime
