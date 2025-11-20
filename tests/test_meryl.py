from fastapi.testclient import TestClient
from src.app import api

client = TestClient(api)

def test_meryl_streep():
    response = client.get("/winner/Meryl Streep")
    assert response.status_code == 200
    assert response.json() == {
        "actress": "Meryl Streep",
        "movie": "The Iron Lady",
        "year": 2012
    }