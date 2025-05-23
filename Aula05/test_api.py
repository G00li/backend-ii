from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_get_data():
    response = client.get("/data")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "results" in data
    assert len(data["results"]) == 2
    assert all("source" in result for result in data["results"])
    assert all("data" in result for result in data["results"]) 