from sqlmodel import SQLModel,create_engine
from core.config import settings
from models import User,Post,PostInfo,Topic


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
