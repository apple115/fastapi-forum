from typing import Any

from sqlmodel import Session, select
from app.models import User,UserPublic,UserCreate
from app.core.security import verifty_password
from app.core.security import get_password_hash


# def create_users()->User:
#     pass


def create_user(*, session: Session, user_create:UserCreate) -> User:
    """
    创建新用户并将其添加到数据库。

    参数:
        session (Session): SQLAlchemy 会话对象。
       user_in (UserCreate): 包含新用户信息的 UserCreate 模型。

    返回:
        User: 新创建的用户对象。
    """
    db_obj = User.model_validate(user_create,update={"password_hash":get_password_hash(user_create.password)})
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj


def get_user_by_name(*, session: Session, name: str) -> User | None:
    """
    通过用户名从数据库中检索用户。

    参数:
        session (Session): SQLAlchemy 会话对象。
        name (str): 要检索的用户名称。

    返回:
        User | None: 如果找到用户，则返回用户对象，否则返回 None。
    """
    statement = select(User).where(User.name == name)
    session_user = session.exec(statement).first()
    return session_user


# def update_user(*, session: Session, db_user: User, user_in: UserUpdate) -> Any:
#     pass


def authenticate(*, session: Session, name: str, password: str) -> User | None:
    """
    验证提供的用户名和密码。如果凭据有效，返回数据库中的用户对象；如果无效，返回None。

    参数:
        session (Session): SQLAlchemy数据库会话对象，用于执行数据库操作。
        name (str): 用户的用户名或电子邮件地址。
        password (str): 用户尝试登录时提供的明文密码。

    返回:
        User | None: 如果用户名存在且密码匹配，则返回User对象；否则返回None。

    发生错误时:
        如果找不到用户名，或密码不匹配，函数将静默地返回None，不抛出异常。
    """
    db_user = get_user_by_name(session=session, name=name)
    if not db_user:
        return None
    if not verifty_password(password, db_user.password_hash):
        return None
    return db_user
