from typing import Annotated
from datetime import timedelta

from fastapi import APIRouter,Depends,HTTPException
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordRequestForm

from app.models import Token
from app.core.config import settings
from app.api.deps import SessionDep
from app.crud import user_crud
from app.core import security

router = APIRouter()

@router.post("/login/access-token")
def login_access_token(
    session:SessionDep, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token:
    """
    使用OAuth2密码授权流程兼容的令牌登录，获取用于未来请求的访问令牌。

    参数:
    - session (AsyncSession): 数据库会话对象，用于执行数据库操作。
    - form_data (OAuth2PasswordRequestForm): 包含用户名和密码的表单数据。

    返回:
    - Token: 包含访问令牌和过期信息的响应模型。

    发生错误时:
    - 如果提供的用户名或密码不正确，将抛出一个状态码为401的Unauthorized HTTP异常。
    """
    user =user_crud.authenticate(
        session=session, name=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return Token(
        access_token=security.create_access_token(
            user.user_id, expires_delta=access_token_expires
        )
    )
