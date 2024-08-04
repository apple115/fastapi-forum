import secrets
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    PROJECT_NAME:str = 'forum'
    SQLALCHEMY_DATABASE_URL:str = 'mysql+pymysql://root:yyc13714729559@localhost/forum'
    SECRET_KEY: str =secrets.token_urlsafe(32)


settings = Settings()
