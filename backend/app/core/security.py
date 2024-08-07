from typing import Any
from datetime import timedelta,datetime
from jose import jwt
from passlib.context import CryptContext
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
ALGORITHM = "HS256"

def verifty_password(plain_password:str,hashed_password:str)->bool:
    return pwd_context.verify(plain_password,hashed_password)

# def verifty_password(plain_password:str,hashed_password:str)->bool:
#     return plain_password==hashed_password

def get_password_hash(password:str)->str:
    return pwd_context.hash(password)

def create_access_token(subject: str | Any, expires_delta: timedelta) -> str:
    """
    创建一个带有过期时间的访问令牌（JWT）。

    参数:
    - subject (str | Any): 令牌的主题，通常是用户的唯一标识符。
    - expires_delta (timedelta): 一个timedelta对象，表示令牌的有效期。

    返回:
    - str: 编码后的JWT令牌。
    """
    # 计算令牌的过期时间，即当前时间加上有效期
    expire = datetime.utcnow() + expires_delta

    to_encode = {
        "exp": expire,
        "sub": str(subject),
    }

    # 使用jwt库的encode方法编码JWT
    # to_encode 是一个字典，包含要编码的信息
    # settings.SECRET_KEY 是用于编码的密钥
    # algorithm 是指定的散列算法
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
