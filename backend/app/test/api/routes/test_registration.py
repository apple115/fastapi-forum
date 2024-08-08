from fastapi.testclient import TestClient
from app.core.config import settings

#TODO fix 不知道这个test为什么会失败,但是我自己curl测试是成功的,这个之后再说
def test_register_user(client: TestClient):
    registry_data = {
        "name": "apple115",
        "email": "user@example.com",
        "password": "string",
        "check_password": "string",
    }
    r = client.post(f"{settings.API_V1_STR}/register", data=registry_data)
    assert r.status_code == 200
    assert "Please check your email to verify your account." in r.json()["message"]


def test_register_user_with_check_password(client: TestClient):
    registry_data = {
        "name": "apple115",
        "email": "test@example.com",
        "password": "123123",
        "check_password": "321321",
    }
    r = client.post(f"{settings.API_V1_STR}/register", data=registry_data)
    assert r.status_code == 401


# TODO
