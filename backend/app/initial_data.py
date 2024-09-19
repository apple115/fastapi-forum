import logging
from sqlmodel import SQLModel, Session, create_engine, select
from app.core.config import settings
from app.models.user import User, UserCreate
from app.models.post import Post
from app.models.topic import Topic
from app.crud import user_crud

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


engine = create_engine(settings.SQLALCHEMY_DATABASE_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def init_db() -> None:
    session = Session(engine)
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


def init() -> None:
    create_db_and_tables()
    init_db()


def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
