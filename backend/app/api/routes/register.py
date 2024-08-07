import json
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from app.models import UserRegister, UserCreate
from app.core.security import get_password_hash
from app.email_util import send_verification_email
from app.crud.user_crud import create_user
from app.api.deps import SessionDep,RedisDep
import uuid


router = APIRouter()

@router.post("/register")
def register_user(userRegister: UserRegister, background_tasks: BackgroundTasks,redis_client:RedisDep):
    """
    验证两次密码是否一致

    生成唯一令牌：
    使用安全的随机生成器创建一个唯一的令牌，这个令牌将用于验证用户的邮箱。

    TODO 如果邮箱存在于这个redis中，那么就不发送邮件

    存储注册信息和令牌：
    将用户的注册信息和令牌存储在缓存系统（如 Redis）中，设置一个合理的过期时间。

    发送包含验证链接的邮件：
    向用户发送一封包含验证链接的邮件，链接中包含生成的令牌。

    """
    if userRegister.password != userRegister.check_password:
        raise HTTPException(status_code=401, detail="Passwords do not match.")
    verification_token = str(uuid.uuid4())
    registration_info = {
        "username": userRegister.name,
        "password": userRegister.password,
        "email": userRegister.email,
    }
    # TODO 如果邮箱存在于这个redis中，那么就不发送邮件

    redis_client.setex(
        name=f"register:{verification_token}",
        time=3600,
        value=json.dumps(registration_info),
    )
    # 发送包含验证链接的邮件（邮件发送逻辑略过）
    background_tasks.add_task(
        send_verification_email, email=userRegister.email, token=verification_token
    )
    return {"message": "Please check your email to verify your account."}


async def get_registration_info_from_cache(token: str,redis_client:RedisDep):
    registration_info_bytes = redis_client.get(f"register:{token}")
    if registration_info_bytes:
        # 将 bytes 类型解码为 utf-8 编码的字符串
        registration_info_str = registration_info_bytes.decode("utf-8") #type: ignore
        # 将字符串解析为 JSON 对象
        return json.loads(registration_info_str)
    return None


@router.get("/verify")
async def verify_email(token: str, session: SessionDep,redis_client:RedisDep):
    """
     1.    从缓存系统中获取注册信息和令牌：
      从缓存系统中获取用户的注册信息和令牌。

     2.   验证令牌：
      验证用户提供的令牌是否有效。

     3.  创建用户：
      如果令牌有效，创建用户。

     4. 删除redis中的令牌：
    """
    # 从缓存系统中获取注册信息和令牌
    registration_info = await get_registration_info_from_cache(token,redis_client)
    if not registration_info:
        raise HTTPException(status_code=404, detail="no token found")

    # 如果有效
    user_in = UserCreate(
        email=registration_info["email"],
        password=registration_info["password"],
        name=registration_info["username"],
    )
    create_user(session=session, user_create=user_in)
    # 删除这个令牌
    redis_client.delete(f'register:{token}')
    return {"message": "User created successfully."}
