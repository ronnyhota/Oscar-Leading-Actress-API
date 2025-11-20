from fastapi.testclient import TestClient
from src.app import api

client = TestClient(api)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}