import httpx
import pytest
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_query_user():
    query = '{ user { id name } }'
    resp = client.post("/graphql", json={"query": query})
    assert resp.status_code == 200
    data = resp.json()["data"]["user"]
    assert data["id"] == 1
    assert isinstance(data["name"], str)

def test_update_name():
    mutation = 'mutation { updateName(name: "Maria") { id name } }'
    resp = client.post("/graphql", json={"query": mutation})
    assert resp.status_code == 200
    data = resp.json()["data"]["updateName"]
    assert data["name"] == "Maria" 