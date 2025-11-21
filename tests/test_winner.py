from fastapi.testclient import TestClient
from src.app import api

client = TestClient(api)

def test_known_winner():
    response = client.get("/winner/Natalie Portman")
    assert response.status_code == 200
    assert "Natalie Portman" in response.text
    assert "Black Swan" in response.text
    assert "2011" in response.text

def test_unknown_winner():
    response = client.get("/winner/NotAnActress")
    assert response.status_code == 404