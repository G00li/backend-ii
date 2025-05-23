from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_safe_echo():
    resp = client.get("/safe-echo", params={"user_input": "<b>Oi!</b>"})
    assert resp.status_code == 200
    assert resp.json()["safe_message"] == "&lt;b&gt;Oi!&lt;/b&gt;"

def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"} 