from sqlalchemy.orm import session
from sqlmodel import Session, create_engine, select
from app.core.config import settings
from app.crud import user_crud
from app.models.user import UserCreate
from app.models.user import User
from app.models.post import Post
from app.models.topic import Topic
from app.models.post import PostInfo
from sqlmodel import SQLModel

engine = create_engine(settings.SQLALCHEMY_DATABASE_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def init_db() -> None:
    session=Session(engine)
    user = session.exec(
        select(User).where(User.email == settings.ROOT_USEREMAIL)
    ).first()
    if not user:
        user_in = UserCreate(
            name="root",
            email=settings.ROOT_USEREMAIL,
            password=settings.ROOT_PASSWORD,
            level=0,
        )
        user = user_crud.create_user(session=session, user_create=user_in)
