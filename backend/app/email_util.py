from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from app.core.config import settings

#fastapi的地址如http://127.0.0.1:8000/ 发送验证地址
conf = settings.get_fastapi_mail_config()

# 发送验证邮件的异步函数
#http://127.0.0.1:8000/verify?token=7d763643-4ed2-44b4-b821-53e57d936ba8
async def send_verification_email(email: str, token: str):
    # 邮件内容，这里简单地使用 HTML 格式
    html = f"""<p>请点击以下链接验证您的邮箱</p><a href="http://127.0.0.1:8000/api/v1/verify?token={token}">验证链接</a>"""
    message = MessageSchema(
        subject="邮箱验证",
        recipients=[email],
        body=html,
        subtype=MessageType.html,
    )
    fast_mail = FastMail(conf)
    # 发送邮件
    await fast_mail.send_message(message)
