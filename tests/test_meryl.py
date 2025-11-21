from fastapi.testclient import TestClient
from src.app import api

client = TestClient(api)

def test_meryl_streep():
    response = client.get("/winner/Meryl Streep")
    assert response.status_code == 200
    assert "Meryl Streep" in response.text
    assert "The Iron Lady" in response.text
    assert "2012" in response.text