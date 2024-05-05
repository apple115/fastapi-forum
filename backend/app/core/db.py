from sqlmodel import Session,create_engine
from app.core.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URL,echo=True)

def init_db(session:Session)->None:
    pass
