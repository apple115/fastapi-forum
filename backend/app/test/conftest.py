from typing import Generator
from collections.abc import Generator
from sqlmodel import Session, delete
from app.core.db import engine, init_db
from app.models.user import User
from fastapi.testclient import TestClient
from app.test.utils.user import user_authentication_headers

from app.main import app
from app.core.security import settings
import pytest
import redis


redis_client = redis.Redis(
    host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB
)
@pytest.fixture(scope="session")
def redis_client_fixture():
    return redis_client


@pytest.fixture(scope="session", autouse=True)
def db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        init_db(session)
        yield session
        statement = delete(User)
        session.execute(statement)
        session.commit()


@pytest.fixture(scope="module")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as c:
        yield c


# @pytest.fixture(scope="module")
# def superuser_token_headers(client:TestClient)->dict[str,str]:
#     pass


# @pytest.fixture(scope="module")
# def normal_user_token_headers(client:TestClient)->dict[str,str]:
#     pass
