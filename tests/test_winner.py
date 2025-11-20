from fastapi.testclient import TestClient
from src.app import api

client = TestClient(api)

def test_known_winner():
    response = client.get("/winner/Natalie Portman")
    assert response.status_code == 200
    assert response.json() == {
        "actress": "Natalie Portman",
        "movie": "Black Swan",
        "year": 2011
    }

def test_unknown_winner():
    response = client.get("/winner/NotAnActress")
    assert response.status_code == 404