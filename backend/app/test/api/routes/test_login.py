from fastapi.testclient import TestClient
from app.core.config import settings

def test_get_access_token(client:TestClient)->None:
    login_data  ={
        "username":"yyc13066828611@163.com",
        "password":"123456",
    }
    r = client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)
    tokens = r.json()
    assert r.status_code == 200
    assert "access_token" in tokens
    assert tokens["access_token"]

def test_get_access_token_incorrect_password(client:TestClient)->None:
    login_data = {
        "username":"yyc13714729559@163.com",
        "password":"incorrect"
    }
    r=client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)
    assert r.status_code == 401


