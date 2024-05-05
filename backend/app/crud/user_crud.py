from typing import Any

from sqlmodel import Session, select


from app.models import User
from app.core.security import verifty_password


# def create_users()->User:
#     pass


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
    db_user = get_user_by_name(session=session, name=name)
    if not db_user:
        return None
    if not verifty_password(password, db_user.password_hash):
        return None
    return db_user
